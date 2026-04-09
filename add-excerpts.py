#!/usr/bin/env python3
"""
Add missing excerpts to Jekyll post front matter.
Extracts the first sentence from post body if excerpt doesn't exist.
"""

import re
import sys
from pathlib import Path

def extract_first_sentence(text):
    """
    Extract the first complete sentence from text.
    Skips HTML tags and returns first sentence ending with . ! or ?
    """
    # Remove leading HTML tags
    clean_text = re.sub(r'^<[^>]+>\s*', '', text.strip())

    # Find first sentence (ending with . ! or ?)
    # Match text up to first sentence terminator
    match = re.match(r'([^.!?]*[.!?])', clean_text, re.DOTALL)

    if match:
        sentence = match.group(1).strip()
        # Clean up any remaining HTML or extra whitespace
        sentence = re.sub(r'<[^>]+>', '', sentence)
        sentence = re.sub(r'\s+', ' ', sentence).strip()
        return sentence

    # Fallback: return first ~80 chars if no sentence found
    fallback = re.sub(r'<[^>]+>', '', clean_text)
    fallback = re.sub(r'\s+', ' ', fallback).strip()
    if len(fallback) > 80:
        return fallback[:77] + "..."
    return fallback if fallback else None


def add_excerpt(filepath, dry_run=True):
    """
    Add excerpt to post front matter if missing.
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

    # Check if excerpt already exists
    if re.search(r'^excerpt:', front_matter, re.MULTILINE):
        return False, "Excerpt already defined"

    # Extract first sentence from body
    first_sentence = extract_first_sentence(body)
    if not first_sentence:
        return False, "Could not extract text from body"

    # Escape quotes in the sentence
    first_sentence = first_sentence.replace('"', '\\"')

    # Find where to insert excerpt (after date line, before other fields)
    # Look for the date line and insert after it
    date_match = re.search(r'^date:.*$', front_matter, re.MULTILINE)
    if date_match:
        insert_point = date_match.end()
        new_line = f'\nexcerpt: "{first_sentence}"'
        new_front_matter = front_matter[:insert_point] + new_line + front_matter[insert_point:]
    else:
        # Fallback: insert before tags or at end
        new_line = f'excerpt: "{first_sentence}"\n'
        new_front_matter = new_line + front_matter

    new_content = f"---{new_front_matter}---{body}"

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    # Show preview of extracted excerpt (truncated)
    preview = first_sentence[:60] + "..." if len(first_sentence) > 60 else first_sentence
    return True, f'Added excerpt: "{preview}"'


def main():
    posts_dir = Path('./_posts')
    if not posts_dir.exists():
        print("❌ Error: _posts directory not found.")
        print("   Run this script from your blog root directory (where _posts/ is located)")
        sys.exit(1)

    dry_run = '--fix' not in sys.argv

    if dry_run:
        print("🔍 DRY RUN: showing posts needing excerpts")
        print("   Run with --fix to apply changes\n")
    else:
        print("⚙️  ADDING EXCERPTS\n")

    posts = sorted(posts_dir.glob('*.md'))
    changed_count = 0

    for post in posts:
        changed, detail = add_excerpt(post, dry_run=dry_run)
        if changed:
            changed_count += 1
            status = "✓" if not dry_run else "→"
            print(f"{status} {post.name}")
            print(f"   {detail}\n")

    print(f"{'='*60}")
    print(f"Posts to update: {changed_count} / {len(posts)}")

    if dry_run and changed_count > 0:
        print("\nRun with --fix flag to apply these changes:")
        print(f"  python3 add-excerpts.py --fix")


if __name__ == '__main__':
    main()
