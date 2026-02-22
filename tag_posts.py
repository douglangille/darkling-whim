#!/usr/bin/env python3
"""
Tag posts in ./_posts/ using GitHub Copilot CLI.

Reads each .md file, calls Copilot to categorize the story by format and genre,
then updates the front-matter tags accordingly.

Usage:
    python tag_posts.py                             # process all posts
    python tag_posts.py --test 5                    # process only first 5 posts
    python tag_posts.py --start 1 --count 10        # process files 1-10 (batch 1)
    python tag_posts.py --start 11 --count 10       # process files 11-20 (batch 2)
    python tag_posts.py --start 21 --count 10       # process files 21-30 (batch 3)
    python tag_posts.py --file FILENAME             # process single file
    python tag_posts.py --logonly                   # print tags without writing files
    python tag_posts.py --logonly --test 5          # combine test with logonly
"""

import argparse
import json
import os
import subprocess
import sys
import time
import glob
from typing import Optional
try:
    import requests
except Exception:
    requests = None
import urllib.request
import urllib.error
try:
    import yaml
except Exception:
    yaml = None


class _FallbackResponse:
    def __init__(self, status: int, body: bytes):
        self.status_code = status
        self._body = body

    @property
    def text(self) -> str:
        return self._body.decode("utf-8", errors="replace")

    def json(self):
        return json.loads(self.text)

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise urllib.error.HTTPError("", self.status_code, "HTTP error", None, None)


def _http_post_fallback(url: str, headers: dict, payload: dict, timeout: int = 30):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            return _FallbackResponse(resp.getcode(), body)
    except urllib.error.HTTPError as e:
        body = e.read() if hasattr(e, "read") else b""
        return _FallbackResponse(getattr(e, "code", 500), body)


POSTS_DIR = os.path.join(os.path.dirname(__file__), "_posts")

SYSTEM_PROMPT = (
        "You are a fiction categorizer.\n"
        "\n"
        "FORMAT is about STRUCTURE:\n"
        "\n"
        "FLASH = Single location/scene, single POV, one core conflict. TIME CAN PASS (Monday→Friday) but NO DISTINCT SCENE BREAKS.\n"
        "  - CRITICAL: All action happens in one place (office cubicle, kitchen, car) EVEN IF DAYS/WEEKS PASS\n"
        "  - NO scene breaks (---) or transitions to DIFFERENT persistent locations\n"
        "  - Named days passing (Monday...Tuesday...Wednesday) while staying in one location = FLASH not SHORT-STORY\n"
        "  - Brief mentions of going home or other places don't matter if main action stays in one location\n"
        "  - EXAMPLE: A character sits at their office desk over a week (Mon-Fri), events happen at desk = FLASH despite time passing\n"
        "  - Usually under 2000 words, tight pacing\n"
        "\n"
        "SHORT-STORY = REQUIRES at least ONE of: DISTINCT SCENE BREAKS or LOCATION CHANGES or MULTIPLE POVs.\n"
        "  - Shows different major locations (office → home → office again, with distinct scenes in each) or scene breaks (---)\n"
        "  - Multiple POV sections (different character perspectives)\n"
        "  - Time jumps that SHOW different scenes/locations, not just narrator mentioning time passed\n"
        "  - Character arc or multiple character introductions across different settings\n"
        "\n"
        "POETRY = Verse form. Any length.\n"
        "\n"
        "GENRE is about TONE and CONTENT (what it's about emotionally):\n"
        "  - drama: Relational/intimate stakes. Character connection, grief, revelation, betrayal. Focus on how people relate.\n"
        "  - fantasy: Magic, impossible elements, alternate worlds.\n"
        "  - scifi: Technology, science-based speculation, futures.\n"
        "  - horror: Dread, fear, unsettling, disturbing.\n"
        "  - thriller: Plot-driven tension, suspense, power games, psychological games, deception.\n"
        "  - humour: Darkly comic, absurdist, playful, funny.\n"
        "\n"
        "Assign exactly ONE format tag and ONE or TWO genre tags.\n"
)

USER_PROMPT_TEMPLATE = """\
Story title: "{title}"
Content preview (word count and pacing will help determine FORMAT):
{content}

This preview is truncated. Estimate the full story word count and pacing from what's shown.

Respond ONLY with valid JSON (no markdown, no preamble):
{{
    "format": "flash|poetry|short-story",
    "genres": ["genre1"] or ["genre1", "genre2"]
}}
"""


class CopilotCLIClient:
    """Wrapper for calling the GitHub Copilot CLI via subprocess.
    
    Requires the Copilot CLI to be installed and authenticated.
    Calls `gh copilot explain` or similar to get model responses.
    """

    def __init__(self, model: str = "gpt-4"):
        self.model = model

    def create(self, prompt: str, max_tokens: int = 512, timeout: int = 60) -> dict:
        """Call the standalone Copilot CLI and return a response-like object."""
        try:
            # Use the standalone copilot CLI with -p (prompt) flag
            result = subprocess.run(
                ["copilot", "-p", prompt],
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            if result.returncode == 0 and result.stdout.strip():
                return _CLIResponse(result.stdout)
            
            # Fallback: raise helpful error
            if result.stderr:
                error_msg = result.stderr
            else:
                error_msg = "No output received"
            
            raise RuntimeError(
                f"GitHub Copilot CLI failed: {error_msg}\n"
                "Ensure the standalone Copilot CLI is installed from: https://github.com/github/copilot-cli"
            )
        except FileNotFoundError:
            raise RuntimeError(
                "Copilot CLI not found. Install from: https://github.com/github/copilot-cli"
            )
        except subprocess.TimeoutExpired:
            raise RuntimeError(f"Copilot CLI timed out after {timeout}s")


class _CLIResponse:
    """Minimal response wrapper for Copilot CLI output."""

    def __init__(self, text: str):
        self._text = text

    @property
    def text(self) -> str:
        return self._text

    def json(self):
        return json.loads(self._text)

    def raise_for_status(self):
        pass  # CLI doesn't have HTTP status codes


class CopilotHTTPClient:
    """HTTP client wrapper for calling a Copilot-style endpoint.

    This class is intentionally generic: set `COPILOT_API_URL` to the HTTP
    endpoint that proxies or exposes the GitHub Copilot `sonnet-4.6` model.
    The `token` is optional; if provided it's sent as a Bearer token.
    """

    def __init__(self, api_url: str, token: Optional[str], model: str = "sonnet-4.6"):
        self.api_url = api_url
        self.token = token
        self.model = model

    def create(self, prompt: str, max_tokens: int = 512, timeout: int = 30):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        payload = {"model": self.model, "prompt": prompt, "max_tokens": max_tokens}
        if requests is not None:
            resp = requests.post(self.api_url, headers=headers, json=payload, timeout=timeout)
            resp.raise_for_status()
            return resp
        else:
            return _http_post_fallback(self.api_url, headers, payload, timeout=timeout)


def parse_post(filepath: str) -> tuple[dict, str, str]:
    """Parse a Jekyll post file into (front_matter, content, raw_front_matter_text)."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    if not raw.startswith("---"):
        return {}, raw, ""

    # Find the closing ---
    end = raw.find("\n---", 3)
    if end == -1:
        return {}, raw, ""

    front_matter_text = raw[3:end].strip()
    content = raw[end + 4:].lstrip("\n")

    front_matter = yaml.safe_load(front_matter_text) or {}
    return front_matter, content, front_matter_text


def write_post(filepath: str, front_matter: dict, content: str) -> None:
    """Write a Jekyll post file back with updated front-matter."""
    fm_yaml = yaml.dump(
        front_matter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )
    new_text = f"---\n{fm_yaml}---\n\n{content}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_text)


def categorize(client: "CopilotCLIClient | CopilotHTTPClient | None", title: str, content: str) -> dict:
    """Call a Copilot endpoint (CLI or HTTP) to get format + genre tags for a story.

    If `client` is None the function returns an empty dict.
    """
    # Detect structural markers that indicate multiple POVs or scene breaks
    pov_markers = []
    if '**' in content:  # Bold headers like **PRIM**, **DANA**
        import re
        bold_headers = re.findall(r'\*\*([^*]+)\*\*', content[:4500])
        # Filter out common formatting (like emphasis in text) - POV headers are typically short (1-3 words)
        pov_markers = [h for h in bold_headers if len(h.split()) <= 3 and h.isupper()]
    
    has_scene_breaks = '***' in content or '\n---\n' in content
    unique_povs = len(set(pov_markers))
    
    # Build analysis hint for the AI - strongest signals first
    structure_hint = ""
    if unique_povs > 1:
        structure_hint = f"\n[CRITICAL: {unique_povs} distinct POV sections detected: {', '.join(set(pov_markers))}. This is SHORT-STORY structure.]"
    elif has_scene_breaks:
        structure_hint = "\n[CRITICAL: Explicit scene breaks (--- or ***) detected. This is SHORT-STORY structure.]"
    elif _is_single_location_story(content):
        structure_hint = "\n[CRITICAL: Single-location story with time passing (days/weeks mentioned but no location changes). This is FLASH structure.]"
    
    preview_content = content[:4500]
    if structure_hint:
        preview_content += structure_hint
    
    user_prompt = USER_PROMPT_TEMPLATE.format(title=title, content=preview_content)

    if client is None:
        return {}

    # Try up to 3 times for transient errors
    last_exc = None
    for attempt in range(1, 4):
        try:
            resp = client.create(prompt=SYSTEM_PROMPT + "\n\n" + user_prompt, max_tokens=256)
            # Try to parse common response shapes
            try:
                data = resp.json()
            except Exception:
                response_text = resp.text
            else:
                # OpenAI-like: choices -> text/message
                if isinstance(data, dict) and "choices" in data:
                    choices = data["choices"]
                    if choices and isinstance(choices, list):
                        first = choices[0]
                        response_text = first.get("text") or first.get("message") or json.dumps(first)
                    else:
                        response_text = json.dumps(data)
                # simple key names
                elif isinstance(data, dict) and "completion" in data:
                    response_text = data["completion"]
                elif isinstance(data, dict) and "output" in data:
                    response_text = data["output"]
                else:
                    # Fallback to stringifying the whole body
                    response_text = json.dumps(data)

            response_text = response_text.strip()
            try:
                return json.loads(response_text)
            except json.JSONDecodeError:
                # Try to extract JSON object inside the text
                start = response_text.find("{")
                end = response_text.rfind("}")
                if start != -1 and end != -1 and end > start:
                    snippet = response_text[start : end + 1]
                    try:
                        return json.loads(snippet)
                    except json.JSONDecodeError:
                        pass
                raise ValueError(f"Copilot returned invalid JSON. Raw response: {response_text!r}")
        except Exception as exc:
            last_exc = exc
            time.sleep(0.5 * attempt)
            continue
    # All retries failed
    raise last_exc


def _is_poetry(content: str) -> bool:
    """Detect if content is verse/poetry based on structure."""
    import re
    
    # Strip HTML tags first
    content_clean = re.sub(r'<[^>]+>', '', content)
    lines = content_clean.split('\n')
    
    # Look for haiku: 3 consecutive lines with 5-7-5 syllable pattern
    # (rough check: line lengths correlating to syllable count)
    haiku_pattern = 0
    for i in range(len(lines) - 2):
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i+2].strip()
        
        # Haiku lines have no quotation marks and specific lengths
        # Avoid dialogue (quoted lines)
        if (not line1.startswith('"') and not line1.startswith("'") and
            not line2.startswith('"') and not line2.startswith("'") and
            not line3.startswith('"') and not line3.startswith("'") and
            8 <= len(line1) <= 30 and 
            12 <= len(line2) <= 35 and 
            8 <= len(line3) <= 25):
            haiku_pattern += 1
    
    if haiku_pattern >= 1:
        return True
    
    # General poetry: >60% short lines (no dialogue) + 25+ lines
    non_dialogue_lines = [l for l in lines if l.strip() and not l.strip().startswith(('"', "'"))]
    short_lines = sum(1 for line in non_dialogue_lines if len(line.strip()) < 80)
    
    if len(non_dialogue_lines) >= 25 and short_lines / len(non_dialogue_lines) > 0.6:
        return True
    
    return False


def _is_single_location_story(content: str) -> bool:
    """Detect if story is single-location despite multiple location mentions."""
    import re
    content_lower = content.lower()
    
    # Check for explicit scene breaks or POV shifts
    if '***' in content or '\n---\n' in content:
        return False
    
    # Check for location transitions - more specific phrases only
    # Avoid false positives like "inside the barn" being counted as two transitions
    location_transitions = re.findall(
        r'\b(went to|moved to|traveled to|arrived at|headed to|drove to|walked to|returned to|pulled in|came to|entered|exited|came into|walked into|drove into)\b',
        content_lower
    )
    
    # If word count is short (under 1000) and few location transitions, it's flash
    word_count = len(content.split())
    if word_count < 1000 and len(location_transitions) <= 2:
        return True
    
    return False


def process_post(client: "CopilotCLIClient | CopilotHTTPClient | None", filepath: str, log_only: bool = False) -> None:
    """Process a single post: categorize and optionally update tags."""
    import re
    
    front_matter, content, _ = parse_post(filepath)

    title = front_matter.get("title", os.path.basename(filepath))

    # Always call categorize to get genres
    result = categorize(client, title, content)
    genres = result.get("genres", []) if isinstance(result, dict) else []
    
    # Override format if poetry detected
    if _is_poetry(content):
        fmt = "poetry"
    else:
        fmt = result.get("format", "") if isinstance(result, dict) else ""

    # Word count is context, not a rule
    word_count = len(content.split())
    
    # CRITICAL OVERRIDES - Applied in priority order (strongest signals first)
    
    # 1. Multiple distinct POV sections = SHORT-STORY, period
    pov_markers = []
    if '**' in content:
        bold_headers = re.findall(r'\*\*([^*]+)\*\*', content[:4500])
        pov_markers = [h for h in bold_headers if len(h.split()) <= 3 and h.isupper()]
    unique_povs = len(set(pov_markers))
    
    if unique_povs > 1:
        fmt = "short-story"
    # 2. Poetry structure detected = POETRY (takes priority over scene breaks and single-location)
    elif fmt == "poetry":
        # Keep as poetry unless it's >5000 words (then it's a poetry collection = short-story)
        if word_count > 5000:
            fmt = "short-story"
        # else: fmt stays as "poetry"
    # 3. Explicit scene breaks (proper dividers, not notes) = SHORT-STORY
    elif re.search(r'^\*{3,}\s*$', content, re.MULTILINE) or '\n---\n' in content:
        fmt = "short-story"
    # 4. Single location + time passing = FLASH (override AI if needed)
    elif _is_single_location_story(content):
        fmt = "flash"


    # Build new tags list: format first (if non-empty), then genres
    new_tags = [t for t in ([fmt] + (genres if isinstance(genres, list) else [])) if t]

    genre_str = " + ".join(genres) if genres else "(no genres)"
    print(f"✓ {title} | {fmt or '(no format)'} + {genre_str} ({word_count} words)")

    if not log_only and new_tags:
        # Preserve 'haley' tag if it exists, replace format/genre tags
        existing_tags = front_matter.get("tags", [])
        if not isinstance(existing_tags, list):
            existing_tags = []
        
        # Keep only the 'haley' tag from existing tags
        preserved_tags = [t for t in existing_tags if t == "haley"]
        
        # Combine preserved tags with new format and genre tags
        front_matter["tags"] = preserved_tags + new_tags
        write_post(filepath, front_matter, content)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tag blog posts using GitHub Copilot CLI or HTTP endpoint."
    )
    parser.add_argument(
        "--file",
        metavar="FILENAME",
        help="Process a single post by filename (e.g. 2013-03-14-stormy-night.md).",
    )
    parser.add_argument(
        "--test",
        type=int,
        metavar="N",
        help="Only process the first N files (for validation).",
    )
    parser.add_argument(
        "--start",
        type=int,
        metavar="N",
        help="Start processing from file N (1-indexed). Use with --count for batch processing.",
    )
    parser.add_argument(
        "--count",
        type=int,
        metavar="N",
        help="Process N files. Use with --start for batch processing.",
    )
    parser.add_argument(
        "--logonly",
        action="store_true",
        help="Print suggested tags without writing changes to files.",
    )
    args = parser.parse_args()

    # Copilot configuration
    github_token = os.environ.get("GITHUB_TOKEN")
    copilot_url = os.environ.get("COPILOT_API_URL")

    # Use Copilot CLI for all runs (no API keys required)
    client = CopilotCLIClient()

    # Ensure YAML is available before attempting file parsing/writing
    if yaml is None:
        print(
            "Error: PyYAML is not installed. Install dependencies: pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    # Get the list of files to process
    if args.file:
        filepath = os.path.join(POSTS_DIR, args.file)
        if not os.path.exists(filepath):
            print(f"Error: File not found: {filepath}", file=sys.stderr)
            sys.exit(1)
        md_files = [filepath]
    else:
        md_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
        if not md_files:
            print(f"No .md files found in {POSTS_DIR}", file=sys.stderr)
            sys.exit(1)

        # Handle batch processing (--start and --count)
        if args.start is not None or args.count is not None:
            start_idx = max(0, (args.start or 1) - 1)  # Convert 1-indexed to 0-indexed
            count = args.count or (len(md_files) - start_idx)  # Default: process rest of files
            md_files = md_files[start_idx : start_idx + count]
            print(f"--batch mode: processing files {start_idx + 1} to {start_idx + len(md_files)} ({len(md_files)} file(s))\n")
        elif args.test is not None:
            md_files = md_files[: args.test]
            print(f"--test mode: processing {len(md_files)} file(s)\n")
    if args.logonly:
        print("--logonly mode: files will NOT be modified\n")

    total_files = len(md_files)
    for idx, filepath in enumerate(md_files, start=1):
        print(f"Processing {idx}/{total_files}: {os.path.basename(filepath)}")
        process_post(client, filepath, log_only=args.logonly)
        # Rate-limit: 1 request per second (skip sleep after last file)
        if idx < total_files:
            time.sleep(1)


if __name__ == "__main__":
    main()
