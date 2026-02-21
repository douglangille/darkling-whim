#!/usr/bin/env python3
"""
Tag posts in ./_posts/ using Claude Haiku API.

Reads each .md file, calls Claude to categorize the story by format and genre,
then updates the front-matter tags accordingly.

Usage:
    python tag_posts.py                # process all posts
    python tag_posts.py --test 5       # process only first 5 posts
    python tag_posts.py --logonly      # print tags without writing files
    python tag_posts.py --test 5 --logonly  # combine both
"""

import argparse
import json
import os
import sys
import time
import glob

import anthropic
import yaml


POSTS_DIR = os.path.join(os.path.dirname(__file__), "_posts")

SYSTEM_PROMPT = (
    "You are a fiction categorizer for a short story blog. Read this story and assign "
    "exactly ONE format tag and ONE or TWO genre tags.\n"
    "Available formats: flash, poetry, short-story, vignette\n"
    "Available genres: fantasy, scifi, horror, thriller, drama, humour\n"
)

USER_PROMPT_TEMPLATE = """\
Story title: "{title}"
Content preview (first 1500 chars):
{content}
Respond ONLY with valid JSON (no markdown, no preamble):
{{
  "format": "format-name",
  "genres": ["genre1"] or ["genre1", "genre2"]
}}
"""


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


def categorize(client: anthropic.Anthropic, title: str, content: str) -> dict:
    """Call Claude Haiku to get format + genre tags for a story."""
    user_prompt = USER_PROMPT_TEMPLATE.format(
        title=title,
        content=content[:1500],
    )
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_prompt}
        ],
    )
    response_text = message.content[0].text.strip()
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Claude returned invalid JSON: {exc}\nRaw response: {response_text!r}"
        ) from exc


def process_post(client: anthropic.Anthropic, filepath: str, log_only: bool = False) -> None:
    """Process a single post: categorize and optionally update tags."""
    front_matter, content, _ = parse_post(filepath)

    title = front_matter.get("title", os.path.basename(filepath))

    result = categorize(client, title, content)

    fmt = result.get("format", "")
    genres = result.get("genres", [])

    # Build new tags list: format first (if non-empty), then genres
    new_tags = [t for t in ([fmt] + genres) if t]

    genre_str = " + ".join(genres) if genres else "(no genres)"
    print(f"✓ {title} | {fmt or '(no format)'} + {genre_str}")

    if not log_only:
        # Replace tags entirely (removing "literary" and old tags)
        front_matter["tags"] = new_tags
        write_post(filepath, front_matter, content)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tag blog posts using Claude Haiku API."
    )
    parser.add_argument(
        "--test",
        type=int,
        metavar="N",
        help="Only process the first N files (for validation).",
    )
    parser.add_argument(
        "--logonly",
        action="store_true",
        help="Print suggested tags without writing changes to files.",
    )
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    md_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    if not md_files:
        print(f"No .md files found in {POSTS_DIR}", file=sys.stderr)
        sys.exit(1)

    if args.test is not None:
        md_files = md_files[: args.test]
        print(f"--test mode: processing {len(md_files)} file(s)\n")

    if args.logonly:
        print("--logonly mode: files will NOT be modified\n")

    for i, filepath in enumerate(md_files):
        process_post(client, filepath, log_only=args.logonly)
        # Rate-limit: 1 request per second (skip sleep after last file)
        if i < len(md_files) - 1:
            time.sleep(1)


if __name__ == "__main__":
    main()
