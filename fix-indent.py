#!/usr/bin/env python3
"""
Fix overlay_image indentation in Jekyll post headers.
Aligns overlay_image to match teaser indentation level.
"""

import re
import sys
from pathlib import Path

def fix_indent(filepath, dry_run=True):
    """
    Fix overlay_image indentation in a single post.
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

    # Find teaser line and extract indentation
    teaser_match = re.search(r'^([ ]*)teaser:', front_matter, re.MULTILINE)
    if not teaser_match:
        return False, "No teaser found"

    correct_indent = teaser_match.group(1)

    # Find overlay_image line and check its indentation
    overlay_match = re.search(r'^([ ]*)overlay_image:', front_matter, re.MULTILINE)
    if not overlay_match:
        return False, "No overlay_image found"

    current_indent = overlay_match.group(1)

    # If indentation already matches, nothing to fix
    if current_indent == correct_indent:
        return False, "Indentation already correct"

    # Fix the indentation
    new_front_matter = re.sub(
        rf'^{re.escape(current_indent)}(overlay_image:)',
        f'{correct_indent}\g<1>',
        front_matter,
        flags=re.MULTILINE
    )

    new_content = f"---{new_front_matter}---{body}"

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True, f"Fixed indent: '{current_indent}' → '{correct_indent}'"


def main():
    posts_dir = Path('./_posts')
    if not posts_dir.exists():
        print("❌ Error: _posts directory not found.")
        print("   Run this script from your blog root directory (where _posts/ is located)")
        sys.exit(1)

    dry_run = '--fix' not in sys.argv

    if dry_run:
        print("🔍 DRY RUN: checking indentation")
        print("   Run with --fix to apply changes\n")
    else:
        print("⚙️  FIXING INDENTATION\n")

    posts = sorted(posts_dir.glob('*.md'))
    fixed_count = 0

    for post in posts:
        changed, detail = fix_indent(post, dry_run=dry_run)
        if changed:
            fixed_count += 1
            status = "✓" if not dry_run else "→"
            print(f"{status} {post.name}: {detail}")

    print(f"\n{'='*60}")
    print(f"Posts to fix: {fixed_count} / {len(posts)}")

    if dry_run and fixed_count > 0:
        print("\nRun with --fix flag to apply these corrections:")
        print(f"  python3 fix-indent.py --fix")


if __name__ == '__main__':
    main()
