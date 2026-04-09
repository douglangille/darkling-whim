#!/usr/bin/env python3
"""
Fix Jekyll post headers: add overlay_image where missing.
Standardizes to Minimal Mistakes theme format.
"""

import re
import sys
from pathlib import Path

def fix_post(filepath, dry_run=True):
    """
    Fix a single post file.
    - Add overlay_image to header if teaser exists but overlay_image doesn't
    - Optionally remove inline <img> tag that matches the teaser
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

    # Check if overlay_image already exists
    if 'overlay_image:' in front_matter:
        return False, "Already has overlay_image"

    # Extract teaser value and its indentation
    teaser_match = re.search(r'([ ]*)(teaser):\s*["\']?([^\n"\']+)["\']?', front_matter)
    if not teaser_match:
        return False, "No teaser found"

    indent = teaser_match.group(1)  # Capture the actual indentation
    teaser_path = teaser_match.group(3).strip()

    # Find where to insert overlay_image (right after teaser)
    insert_point = teaser_match.end()

    # Build overlay_image line with matching indentation
    new_overlay = f"\n{indent}overlay_image: \"{teaser_path}\""

    # Prepare new front matter
    new_front_matter = front_matter[:insert_point] + new_overlay + front_matter[insert_point:]

    # Try to remove inline <img> tag if it matches the teaser
    new_body = body
    img_pattern = rf'<img[^>]*src="?{re.escape(teaser_path)}"?[^>]*>\s*'
    if re.search(img_pattern, new_body):
        new_body = re.sub(img_pattern, '', new_body, count=1)
        img_removed = True
    else:
        img_removed = False

    new_content = f"---{new_front_matter}---{new_body}"

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    details = f"Added overlay_image: {teaser_path}"
    if img_removed:
        details += " + removed inline <img>"

    return True, details


def main():
    posts_dir = Path('./_posts')
    if not posts_dir.exists():
        print("❌ Error: _posts directory not found.")
        print("   Run this script from your blog root directory (where _posts/ is located)")
        sys.exit(1)

    dry_run = '--fix' not in sys.argv  # Default to dry-run unless --fix passed

    if dry_run:
        print("🔍 DRY RUN: showing what would change")
        print("   Run with --fix to apply changes\n")
    else:
        print("⚙️  APPLYING FIXES\n")

    posts = sorted(posts_dir.glob('*.md'))
    changed_count = 0

    for post in posts:
        changed, detail = fix_post(post, dry_run=dry_run)
        if changed:
            changed_count += 1
            status = "✓" if not dry_run else "→"
            print(f"{status} {post.name}: {detail}")

    print(f"\n{'='*60}")
    print(f"Posts to fix: {changed_count} / {len(posts)}")

    if dry_run and changed_count > 0:
        print("\nRun with --fix flag to apply these changes:")
        print(f"  python3 /sessions/wonderful-amazing-davinci/fix-post-headers.py --fix")


if __name__ == '__main__':
    main()
