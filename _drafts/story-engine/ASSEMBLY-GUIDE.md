# Assembly Guide

**Purpose**: Combine atomic scene files into complete, publication-ready manuscripts.

---

## When to Assemble

- All scenes drafted and revised
- Ready to read as complete work
- Preparing for publication
- Need to check flow across scenes
- Creating submission manuscript
- Publishing to blog/website

---

## Assembly Methods

### Method 1: Manual Assembly Session (Recommended)

**Best for**: Final polish, ensuring smooth transitions

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/ASSEMBLY-GUIDE.md

# Assemble: [Project Name]

Project folder: _drafts/[project-name]/

Load scenes in order:
- scenes/ch01-sc01-draft.md
- scenes/ch01-sc02-draft.md
- scenes/ch01-sc03-draft.md
[etc]

Assemble into single manuscript with:
- Smooth transitions between scenes
- Remove scene headers/metadata
- Add chapter breaks where appropriate
- Clean formatting
- Verify continuity

Output to: final/[project-name]-manuscript.md
```

**What LLM Does**:
1. Loads each scene in order
2. Strips metadata/headers
3. Adds transitions between scenes
4. Inserts chapter breaks (if novel/novella)
5. Ensures flow and continuity
6. Outputs single clean file

---

### Method 2: Script-Based Assembly

**Best for**: Quick drafts, intermediate checks

**Simple Concatenation Script** (bash):
```bash
#!/bin/bash
# assemble.sh - Concatenate scene files

PROJECT=$1
OUTPUT="_drafts/${PROJECT}/assembled-draft.md"

# Clear output file
> "${OUTPUT}"

# Add frontmatter/header
cat "_drafts/${PROJECT}/frontmatter.md" >> "${OUTPUT}"

# Concatenate all scene files in order
for scene in _drafts/${PROJECT}/scenes/*.md; do
    # Skip metadata lines (lines starting with **)
    grep -v '^\*\*' "${scene}" >> "${OUTPUT}"
    echo "" >> "${OUTPUT}"  # Add blank line between scenes
done

echo "Assembled: ${OUTPUT}"
```

**Usage**:
```bash
./assemble.sh my-story
```

**Python Version** (more control):
```python
#!/usr/bin/env python3
# assemble.py - Smart scene assembly

import sys
import re
from pathlib import Path

def assemble_scenes(project_name):
    project_dir = Path(f"_drafts/{project_name}")
    scenes_dir = project_dir / "scenes"
    output_file = project_dir / "assembled-draft.md"
    
    # Get all scene files sorted
    scene_files = sorted(scenes_dir.glob("ch*-sc*-draft.md"))
    
    with output_file.open('w') as out:
        # Add frontmatter if exists
        frontmatter = project_dir / "frontmatter.md"
        if frontmatter.exists():
            out.write(frontmatter.read_text())
            out.write("\n\n")
        
        current_chapter = None
        
        for scene_file in scene_files:
            # Extract chapter number from filename
            match = re.match(r'ch(\d+)-sc(\d+)', scene_file.name)
            if match:
                chapter_num = int(match.group(1))
                
                # Add chapter break if new chapter
                if chapter_num != current_chapter:
                    if current_chapter is not None:
                        out.write("\n\n---\n\n")  # Chapter separator
                    out.write(f"## Chapter {chapter_num}\n\n")
                    current_chapter = chapter_num
            
            # Read scene content
            content = scene_file.read_text()
            
            # Remove metadata section (everything before first ---)
            parts = content.split('---', 2)
            if len(parts) >= 3:
                scene_text = parts[2].strip()
            else:
                scene_text = content.strip()
            
            # Remove revision notes section at end
            if '## Revision Notes' in scene_text:
                scene_text = scene_text.split('## Revision Notes')[0].strip()
            
            # Write scene
            out.write(scene_text)
            out.write("\n\n")  # Scene separator
    
    print(f"Assembled {len(scene_files)} scenes to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python assemble.py <project-name>")
        sys.exit(1)
    
    assemble_scenes(sys.argv[1])
```

**Usage**:
```bash
python assemble.py my-story
```

---

### Method 3: LLM Assembly with Polish

**Best for**: Final publication, adding transitions, smoothing

**Session Template**:
```
Connect to my Workbench repo on GitHub.

# Assemble and Polish: [Project Name]

Project folder: _drafts/[project-name]/

Load all scene files in order.

Assemble into single manuscript:
1. Remove scene metadata
2. Add smooth transitions between scenes
3. Insert chapter breaks at logical points
4. Ensure continuity (character knowledge, time flow, etc.)
5. Polish opening/closing of each chapter
6. Add scene breaks (### or * * *) where appropriate
7. Format for publication platform

Create two versions:
- final/[project-name]-manuscript.md (clean text)
- final/[project-name]-formatted.md (with publication frontmatter)

Commit both files.
```

---

## File Structure for Assembly

### Before Assembly
```
project-name/
├── scenes/
│   ├── ch01-sc01-draft.md
│   ├── ch01-sc02-draft.md
│   ├── ch01-sc03-draft.md
│   ├── ch02-sc01-draft.md
│   ├── ch02-sc02-draft.md
│   └── ...
├── frontmatter.md (optional)
└── README.md
```

### After Assembly
```
project-name/
├── scenes/ (individual files preserved)
├── assembled-draft.md (quick assembly)
└── final/
    ├── [project-name]-manuscript.md (clean)
    └── [project-name]-formatted.md (publication-ready)
```

---

## Frontmatter Template

Create `frontmatter.md` in project root:

**For Jekyll/Blog**:
```markdown
---
layout: post
title: [Story Title]
date: [YYYY-MM-DD]
categories: [Fiction]
tags: [shortstory, fantasy, etc]
author: Douglas Langille
readtime: true
comments: true
---

[Optional author's note or summary]
```

**For Manuscript Submission**:
```markdown
[Your Name]
[Address]
[Email]
[Phone]

[Word Count] words

# [STORY TITLE]
## by [Your Name]
```

---

## Scene File Format

**During Drafting** - Scene files have metadata:
```markdown
# Chapter 3, Scene 2: The Revelation

**Brief**: scene-briefs/ch03-sc02-brief.md
**Status**: Revised
**Word Count**: 1,847

---

[Scene prose starts here]

Mitzy stood at the edge of the clearing...

[Scene prose continues]

---

## Revision Notes
- Changed opening to strengthen hook
- Added sensory detail in middle section
```

**After Assembly** - Metadata stripped:
```markdown
Mitzy stood at the edge of the clearing...

[Scene prose continues]
```

---

## Transition Strategies

### Scene-to-Scene (Same Chapter)

**No transition needed** if:
- Time is continuous
- Location is same
- POV is same

**Add space break** (\* \* \*) if:
- Time jump within chapter
- Location change
- POV shift

**Add transition sentence** if:
- Need to orient reader
- Significant time/place change
- Emotional shift needs bridge

### Chapter-to-Chapter

**Chapter breaks** naturally provide transition. Consider:
- Ending chapter on hook/cliffhanger
- Opening next chapter with time/place establishment
- Using chapter headers if helpful ("Chapter 3: The Maze")

---

## Assembly Checklist

### Before Assembly
- [ ] All scenes drafted
- [ ] All scenes revised
- [ ] Scene order finalized
- [ ] Continuity verified
- [ ] Frontmatter prepared (if needed)

### During Assembly
- [ ] Load scenes in correct order
- [ ] Remove metadata/headers
- [ ] Add transitions where needed
- [ ] Insert scene/chapter breaks
- [ ] Check flow between scenes
- [ ] Verify character consistency
- [ ] Verify timeline consistency

### After Assembly
- [ ] Read complete manuscript
- [ ] Check for formatting issues
- [ ] Verify word count
- [ ] Add publication metadata
- [ ] Spell check / grammar check
- [ ] Export to required format
- [ ] Commit final files

---

## Output Formats

### Markdown (Default)
- Clean, portable
- Version control friendly
- Easy to convert to other formats

### Export to Other Formats

**Using Pandoc**:
```bash
# To Word (.docx)
pandoc manuscript.md -o manuscript.docx

# To PDF
pandoc manuscript.md -o manuscript.pdf

# To HTML
pandoc manuscript.md -o manuscript.html

# To ePub
pandoc manuscript.md -o manuscript.epub --metadata title="Story Title"
```

**Using Jekyll** (for blog):
- Place in `_posts/` with date prefix
- Jekyll auto-converts markdown to HTML
- Frontmatter controls layout/metadata

---

## Special Cases

### Flash Fiction / Short Stories

**No chapter breaks**:
- Use scene breaks (\* \* \*) for time/place jumps
- Smooth prose flow throughout
- Single continuous read

### Novellas / Novels

**Add chapter structure**:
- Group scenes into chapters
- Add chapter headers
- Consider part/section divisions for longer works

### Serials / Episodes

**Assemble per episode**:
- Each episode = separate assembly
- Keep episode boundaries clear
- Include episode number/title

---

## Assembly Session Example

```
Connect to my Workbench repo on GitHub.

# Assemble: The Memory Thief

Project folder: _drafts/memory-thief/

Load scenes in order:
- scenes/ch01-sc01-draft.md (Awakening)
- scenes/ch01-sc02-draft.md (The Offer)
- scenes/ch01-sc03-draft.md (First Theft)
- scenes/ch02-sc01-draft.md (Consequences)
- scenes/ch02-sc02-draft.md (The Hunt)
- scenes/ch03-sc01-draft.md (Revelation)
- scenes/ch03-sc02-draft.md (Climax)
- scenes/ch03-sc03-draft.md (Resolution)

Assemble into complete manuscript:
1. Strip metadata from each scene
2. Add smooth transitions between scenes
3. Insert chapter breaks between chapters
4. Add scene breaks (***) for time/place jumps within chapters
5. Ensure continuity of character knowledge and timeline
6. Polish chapter openings and endings
7. Format for blog publication (Jekyll frontmatter)

Output to:
- final/memory-thief-manuscript.md (clean text)
- final/memory-thief-post.md (with Jekyll frontmatter)

Commit with message: "Assemble The Memory Thief - complete manuscript"
```

---

## Post-Assembly

### Read Complete Draft
- Read assembled manuscript start to finish
- Note any issues:
  - Awkward transitions
  - Continuity errors
  - Pacing problems
  - Missing scenes

### Create Issues List
If problems found:
```
Create: final/assembly-issues.md

List:
- Transition between Ch2-Sc2 and Ch3-Sc1 needs work
- Character name inconsistency (Ch1: "Mitsy" vs Ch3: "Mitzy")
- Timeline gap: Ch2 is Tuesday, Ch3 jumps to Thursday
- Missing scene: Need bridge between escape and confrontation
```

### Fix at Source
- Go back to individual scene files
- Fix issues there
- Re-assemble

**Why**: Keeps atomic files as source of truth

---

## Preserving Scene Files

**Important**: Never delete scene files after assembly!

**They are**:
- Source of truth
- Granular version history
- Revisable units
- Reorderable
- Modular

**Assembled manuscript is**:
- Output product
- Derived from scene files
- Regenerable at any time

**Think of it like**:
- Scene files = source code
- Assembled manuscript = compiled binary
- Always keep source!

---

## Version Control

### Tag Assembled Versions
```bash
git tag v1.0-assembled "Complete first assembly"
git tag v1.1-revised "Post-assembly revisions"
git tag v1.2-final "Publication-ready"
```

### Commit Messages
```bash
git commit -m "Assemble complete manuscript from 23 scene files"
git commit -m "Add transitions between chapters 2 and 3"
git commit -m "Final polish on assembled manuscript"
```

---

## Quick Reference

**Quick assembly** → Use script (bash/python)
**Final polish** → Use LLM session with explicit instructions
**Publication** → Add frontmatter, format for platform
**Preserve scenes** → Never delete atomic files
**Fix issues** → Edit source scene files, reassemble

---

**Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
