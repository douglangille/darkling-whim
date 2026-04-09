#!/usr/bin/env python3
"""
Fix existing excerpts in Jekyll posts.
For poetry: replace with first line only.
For prose: replace with first complete sentence.
"""

import re
import sys
from pathlib import Path

def extract_first_line(text):
    """
    Extract just the first line of text (for poetry).
    Strips trailing commas, colons, semicolons (but keeps . ! ?)
    """
    clean_text = text.strip()

    # Remove leading HTML tags
    clean_text = re.sub(r'^<[^>]+>\s*', '', clean_text)

    # Remove leading markdown images ![...](...)
    clean_text = re.sub(r'^!\[[^\]]*\]\([^\)]+\)\s*', '', clean_text)

    # Get first line (everything before first newline)
    first_line = clean_text.split('\n')[0].strip()

    # Clean up HTML/markdown remnants and normalize whitespace
    first_line = re.sub(r'<[^>]+>', '', first_line)
    first_line = re.sub(r'!\[[^\]]*\]\([^\)]+\)', '', first_line)
    first_line = re.sub(r'\s+', ' ', first_line).strip()

    # Strip trailing commas, colons, semicolons (but keep . ! ?)
    first_line = re.sub(r'[,;:]+$', '', first_line).strip()

    return first_line if first_line else None


def extract_first_sentence(text):
    """
    Extract first sentence from prose (for articles/stories).
    First line, but if no punctuation, grab up to first . ! or ?
    """
    clean_text = text.strip()

    # Remove leading HTML tags
    clean_text = re.sub(r'^<[^>]+>\s*', '', clean_text)

    # Remove leading markdown images ![...](...)
    clean_text = re.sub(r'^!\[[^\]]*\]\([^\)]+\)\s*', '', clean_text)

    # Get first line
    first_line = clean_text.split('\n')[0].strip()

    # If first line ends with punctuation, use it
    if re.search(r'[.!?]$', first_line):
        first_line = re.sub(r'<[^>]+>', '', first_line)
        first_line = re.sub(r'!\[[^\]]*\]\([^\)]+\)', '', first_line)
        first_line = re.sub(r'\s+', ' ', first_line).strip()
        return first_line

    # Otherwise, try to grab up to first sentence terminator
    match = re.match(r'([^.!?]*[.!?])', clean_text)
    if match:
        sentence = match.group(1).strip()
        sentence = re.sub(r'<[^>]+>', '', sentence)
        sentence = re.sub(r'!\[[^\]]*\]\([^\)]+\)', '', sentence)
        sentence = re.sub(r'\s+', ' ', sentence).strip()
        return sentence if sentence else first_line

    # Fallback to first line
    return first_line if first_line else None


def fix_excerpt(filepath, dry_run=True, poetry_only=False):
    """
    Replace existing excerpt with correct one.
    Returns (changed, details)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse front matter
    if not content.startswith('---'):
        return False, "No front matter found"

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, "Malformed front matter"

    front_matter = parts[1]
    body = parts[2]

    # Check if excerpt exists
    excerpt_match = re.search(r'^excerpt:\s*"([^"]*)"', front_matter, re.MULTILINE)
    if not excerpt_match:
        return False, "No excerpt found"

    old_excerpt = excerpt_match.group(1)

    # Check if this is poetry
    is_poetry = re.search(r'^\s*-\s*poetry', front_matter, re.MULTILINE)

    # Skip non-poetry if poetry_only flag set
    if poetry_only and not is_poetry:
        return False, "Not poetry (skipped)"

    # Extract new excerpt based on type
    if is_poetry:
        new_excerpt = extract_first_line(body)
    else:
        new_excerpt = extract_first_sentence(body)

    if not new_excerpt:
        return False, "Could not extract text from body"

    # Escape quotes
    new_excerpt = new_excerpt.replace('"', '\\"')

    # Only replace if different
    if old_excerpt == new_excerpt:
        return False, "Excerpt already correct"

    # Replace in front matter
    new_front_matter = re.sub(
        r'^excerpt:\s*"[^"]*"',
        f'excerpt: "{new_excerpt}"',
        front_matter,
        flags=re.MULTILINE
    )

    new_content = f"---{new_front_matter}---{body}"

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    # Show diff
    old_preview = old_excerpt[:50] + "..." if len(old_excerpt) > 50 else old_excerpt
    new_preview = new_excerpt[:50] + "..." if len(new_excerpt) > 50 else new_excerpt
    return True, f"Old: {old_preview}\n   New: {new_preview}"


def main():
    posts_dir = Path('./_posts')
    if not posts_dir.exists():
        print("❌ Error: _posts directory not found.")
        print("   Run this script from your blog root directory (where _posts/ is located)")
        sys.exit(1)

    dry_run = '--fix' not in sys.argv
    poetry_only = '--poetry' in sys.argv

    if dry_run:
        print("🔍 DRY RUN: showing what would change")
        print("   Run with --fix to apply changes\n")
    else:
        print("⚙️  FIXING EXCERPTS\n")

    if poetry_only:
        print("(Poetry posts only)\n")

    posts = sorted(posts_dir.glob('*.md'))
    changed_count = 0

    for post in posts:
        changed, detail = fix_excerpt(post, dry_run=dry_run, poetry_only=poetry_only)
        if changed:
            changed_count += 1
            status = "✓" if not dry_run else "→"
            print(f"{status} {post.name}")
            print(f"   {detail}\n")

    print(f"{'='*60}")
    print(f"Posts to fix: {changed_count} / {len(posts)}")

    if dry_run and changed_count > 0:
        print("\nRun with --fix flag to apply these changes:")
        if poetry_only:
            print(f"  python3 fix-excerpts.py --fix --poetry")
        else:
            print(f"  python3 fix-excerpts.py --fix")


if __name__ == '__main__':
    main()
