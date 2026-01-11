---
title: "Writing Workflow: Markdown, Obsidian & VS Code"
date: 2024
categories: [tech, writing, workflow]
tags: [markdown, obsidian, vscode, chatgpt, workflow, plain-text, writing-tools, portability]
context: Deep exploration of portable writing workflow for long-form fiction
status: reference
---

# Writing Workflow Options: Markdown, Obsidian & VS Code

*A comprehensive exploration of building a portable, AI-integrated writing workflow for long-form fiction using plain-text tools.*

## Core Requirements

### Non-Negotiables
- **Markdown-native files** for 20+ year portability
- No proprietary format lock-in
- ChatGPT Plus integration (no API keys)
- Mac-primary workflow with iOS viewing capability
- Minimal friction for long-form fiction management

### Current State
- Writing blog posts and essays successfully in ChatGPT + Canvas
- Friction managing multiple artifacts for long-form fiction
- Obsidian installed but not actively using it
- Prefer filesystem-level organization over elaborate PKM systems

---

## File Structure Decision

### Single-Folder Approach (Selected)

No subfolders; everything in one directory:

```
/ProjectName/
  _bible.md              # Story bible (underscore = admin file)
  _characters.md         # Optional: split bible
  _settings.md           # Optional: split bible  
  _scenelist.md          # Optional: scene tracker
  S010 The Broken Regulator.md
  S020 Next Scene.md
  ...
```

**Benefits:**
- Underscore-prefixed admin files group at top
- Easy to exclude from compilation
- Natural sorting by scene numbers
- No nested folder navigation
- Tool-agnostic portability

### Scene File Template

YAML front matter for metadata + scene briefs; prose in body:

```markdown
---
id: S010
title: The Broken Regulator
order: 10         # Increment by 10s for easy insertion
pov: Maggie
when: 2032-05-12 evening
location: Lunenburg workshop
status: drafting

brief: |
  Goal: Maggie tests the repaired clock; Richard arrives early.
  Conflict: The regulator drifts; trust wobbles.
  Outcome: Maggie hides protest hardware; Richard senses it.

bible_snippets: |
  - Maggie: watchmaker; "time drift" activism; cautious trust.
  - Workshop: oil/metal smell; hidden compartment under bench.
  - Richard: RCMP consultant; pattern-spotter; wary empathy.
---

[Prose only. No headings.]
```

**Why This Works:**
- YAML keeps metadata separate from prose
- Obsidian reads YAML as "Properties" natively
- Pandoc treats YAML as metadata (not printed)
- Easy to copy entire file into ChatGPT (brief provides context)
- Body-only compilation possible by stripping YAML

---

## Compilation Strategy

### Build Script

Simple bash script to compile scenes in order:

```bash
#!/usr/bin/env bash
# build.sh — stitch Markdown scenes into _manuscript.md

set -euo pipefail

MANUSCRIPT="_manuscript.md"
TMP_INDEX="$(mktemp)"
trap 'rm -f "$TMP_INDEX"' EXIT

# Collect non-underscore .md files
found_any=false
find . -maxdepth 1 -type f -name "*.md" ! -name "_*" -print0 |
while IFS= read -r -d '' f; do
  found_any=true
  # Extract 'order' from YAML
  ord="$(
    awk '
      NR==1 && $0 ~ /^---[[:space:]]*$/ {in=1; next}
      in && $0 ~ /^---[[:space:]]*$/ {exit}
      in && $1=="order:" {print $2; exit}
    ' "$f" | tr -cd "0-9"
  )"
  : "${ord:=99999999}"
  printf "%08d\t%s\n" "$ord" "${f#./}" >> "$TMP_INDEX"
done

# Concatenate in order, stripping YAML
sort -n "$TMP_INDEX" | cut -f2- | while IFS= read -r f; do
  awk '
    NR==1 && $0 ~ /^---[[:space:]]*$/ {in=1; next}
    in && $0 ~ /^---[[:space:]]*$/ {in=0; next}
    in {next}
    {print}
  ' "$f"
  printf "\n\n"
done > "$MANUSCRIPT"

echo "Wrote $MANUSCRIPT"

# Optional Pandoc export
if [ $# -ge 1 ]; then
  out="$1"
  if command -v pandoc >/dev/null 2>&1; then
    pandoc "$MANUSCRIPT" -o "$out"
    echo "Wrote $out (via pandoc)"
  else
    echo "pandoc not found"
    exit 1
  fi
fi
```

**Usage:**
```bash
chmod +x build.sh
./build.sh                 # Creates _manuscript.md
./build.sh Draft.docx      # Creates manuscript + exports to DOCX
./build.sh Draft.epub      # Creates manuscript + exports to EPUB
```

---

## Version Control Strategy

### Non-Git Approach (Selected)

**Components:**
1. **iCloud Drive** - Primary storage for cross-device access
2. **Time Machine** - External SSD for hourly/daily/weekly backups
3. **VS Code Timeline** - Per-file local history (non-Git)
4. **Obsidian File Recovery** - Short-term rollback capability

**Why No Git:**
- Don't want to commit creative writing to GitHub
- iCloud provides cross-device sync
- Time Machine + Timeline provide adequate version safety
- No ceremony or background automation needed
- Can always add Git later if collaboration needed

**Important Notes:**
- iCloud ≠ version history (only 30-day deleted file recovery)
- Time Machine must be on external disk (not same-disk snapshots)
- VS Code Timeline works without Git configuration
- Obsidian File Recovery is a "seatbelt," not full backup

---

## Tool Integration

### VS Code Setup

**Extensions:**
- **Markdown All in One** - TOCs, shortcuts, preview, word count
- **Timeline** (built-in) - Local file history per save

**Benefits:**
- Low friction drafting environment
- No plugin ceremony
- Timeline provides version rollback
- Zero lock-in

### Obsidian Setup

**Usage Pattern:**
- Treat as viewer/organizer over filesystem
- Vault = plain folder of Markdown files
- No complex plugins required
- Better for mobile viewing (iOS)

**Core Plugins to Enable:**
- **File Recovery** - Short-term rollback
- **Note Composer** - Merge/split notes without breaking links
- **Templates** (optional) - Stamp scene skeletons

**Key Insight:**
Obsidian "Properties" = YAML front matter. No special format needed.

---

## ChatGPT Integration

### Plus-Only Workflow (No API)

**Available Options:**

1. **ChatGPT Mac App Overlay**
   - Install official macOS app
   - Use ⌥-Space to summon over any window
   - Accepts file/snippet pasting
   - Stays within Plus account

2. **Projects for Context**
   - Attach `_bible.md` to ChatGPT Project
   - Context travels across all chats in project
   - "Attach once, reuse many times" pattern

3. **Safari Integration**
   - ChatGPT Mac app works over Safari
   - Apple Intelligence → ChatGPT (Sequoia)
   - Shortcuts + Advanced URI for Obsidian capture

**Workflow:**
1. Copy entire scene file (YAML brief + prose) into ChatGPT
2. YAML brief at top provides context automatically
3. Work with AI on revisions
4. Paste result back to scene file
5. Or use Shortcuts to append to vault

**What Doesn't Work Without API:**
- Most Obsidian AI plugins (Text Generator, Copilot, ChatGPT-MD)
- VS Code AI extensions (Genie, etc.)
- Unofficial web session extensions (break frequently)

### Safari → Obsidian Capture

**Tools:**
- **Actions for Obsidian** - 40+ Shortcuts actions
- **Obsidian Web Clipper** - Bookmarklet for full-page capture
- **Advanced URI** - Create/append notes via URL
- **Hookmark** - Deep linking between apps

**Setup:**
1. Install Actions for Obsidian (Mac App Store)
2. Create Shortcut: "Send to Obsidian" (appends selection)
3. Add to Safari Share menu
4. Optional: Add Web Clipper bookmarklet

---

## Export Strategy

### Output Formats

**Philosophy:**
- Export/compile is "nice to have," not core workflow
- Copy/paste into specialized tools works fine:
  - **Reedsy** for EPUB formatting
  - **Word** for transportable format

**Pandoc as Escape Hatch:**
- Install but don't wire into daily workflow
- Use only when direct export needed
- Supports: DOCX, EPUB, PDF, HTML

**Build Script Integration:**
```bash
./build.sh Draft.docx    # One-step compile + export
```

---

## Mobile Considerations

### Drafting Environment
- Physical keyboard only (MacBook)
- iPhone/iPad soft keyboards not viable for long sessions
- If using keyboard with iPad, might as well use MacBook

### Ideation & Planning
- Heavy use on both iPad and iPhone
- Almost entirely within ChatGPT
- Obsidian good for mobile viewing/light edits

### Storage Location
- Keep project in iCloud Drive for cross-device access
- Create Obsidian vault on iOS first, then move Mac files in
- Ensures smooth iOS sync

---

## Decision Rationale

### Why Single Files (Not Twin Files)

Considered:
- **Option A**: Single file (YAML + prose)
- **Option B**: Twin files (scene.brief.md + scene.md)

Selected **Option A** because:
- YAML cleanly separates metadata from prose
- Easier to manage single artifact per scene
- Copy entire file to ChatGPT = instant context
- Compilation can strip YAML for body-only output
- More tool-agnostic (YAML widely supported)

### Why Obsidian + VS Code (Not Just One)

**VS Code for:**
- Active drafting on Mac
- Timeline version history
- Fast, distraction-free writing
- Markdown All in One conveniences

**Obsidian for:**
- Mobile viewing/light edits (iOS)
- Graph view when needed
- Properties UI for YAML
- File Recovery plugin
- Note linking when useful

**Key Insight:**
Both tools read same files. No lock-in. Use whichever fits the moment.

### Why Not Other Options

**Scrivener:**
- Proprietary project format
- Would need "compile to Markdown" workflow
- Adds complexity without clear benefit

**novelWriter:**
- Purpose-built but less familiar
- No mobile component
- VS Code + Obsidian more flexible

**Apple Notes:**
- Fine for ephemeral Forever Notes planning
- Not for long-tail creative writing
- Limited export to Markdown

---
## Scene Order Management

### Order Property Strategy

**Pattern:**
- Increment scene `order` by 10s: 10, 20, 30, 40...
- Easy to insert scenes between existing ones
- Example: Insert between 30 and 40 → use order: 35

**Benefits:**
- No file renaming needed
- Natural sort in build script
- Can reorder without touching filenames
- Compilation always correct regardless of filename

---

## Story Bible Approach

### One File vs. Multiple

**Decision:** It depends on the project

**Single Bible (`_bible.md`):**
- Simpler to attach to ChatGPT
- Easier to search
- Good for shorter works

**Split Bibles:**
- `_characters.md`
- `_settings.md`
- `_timeline.md`
- Better for complex worlds
- Easier to navigate

**Either Way:**
- Use underscore prefix for grouping
- Include in ChatGPT Project as needed
- YAML `bible_snippets` pulls relevant excerpts into scenes

---

## Future-Proofing

### Portability Guarantees

**What's Durable:**
- Plain text Markdown (Library of Congress standard)
- YAML front matter (widely adopted standard)
- Filesystem organization (tool-agnostic)
- Pandoc for format conversion (stable, open source)

**What's Ephemeral:**
- Specific editor (VS Code, Obsidian)
- Plugin ecosystem
- ChatGPT integrations

**Escape Hatches:**
- Files are just Markdown - open anywhere
- Pandoc converts to any format
- YAML can be stripped with simple script
- TextBundle for Markdown + assets packaging

### Optional Future Additions

**If Needs Change:**
- **Git** - Add later if collaboration needed
- **Obsidian Sync** - Paid, E2E encrypted, version history
- **API Integration** - If workflow demands it
- **Obsidian Git** - Background auto-commit
- **gitwatch** - Filesystem-level auto-commit

**None Required Now:**
- Start simple
- Add complexity only when friction appears
- Maintain portability throughout

---

## Key Insights

### From Exploration Process

1. **PKM is mostly a lie** - Most notes created once, never opened again. Accept this.

2. **Creative writing has a long tail** - Only thing worth keeping truly portable (20+ years).

3. **ChatGPT is the planning tool** - Not Obsidian. Use what actually works.

4. **Multiple artifacts = friction** - Hence single-file approach with YAML.

5. **Obsidian not being used = signal** - Don't force it. Use when it fits.

6. **Filesystem-native wins** - Folders and files beat elaborate systems.

7. **Export is nice-to-have** - Paste into specialized tools works fine.

8. **Plus-only viable** - No API needed for this workflow.

9. **Version safety ≠ Git** - Time Machine + Timeline sufficient for solo work.

10. **Tool-agnostic = sustainable** - Can change editors, keep files forever.

---

## Implementation Checklist

### Setup (30 minutes)

- [ ] Create project folder in iCloud Drive
- [ ] Install ChatGPT Mac app (⌥-Space overlay)
- [ ] Set up Time Machine to external SSD
- [ ] Install VS Code + Markdown All in One extension
- [ ] Configure Obsidian vault pointing to project folder
- [ ] Enable File Recovery in Obsidian
- [ ] Save `build.sh` script in project folder
- [ ] Make build.sh executable: `chmod +x build.sh`
- [ ] Create `_bible.md` template
- [ ] Create scene file template
- [ ] Optional: Install Pandoc via Homebrew
- [ ] Optional: Set up Actions for Obsidian + Shortcuts

### First Scene Workflow

1. Create scene file: `S010 Scene Title.md`
2. Fill in YAML front matter (brief, bible_snippets, order)
3. Draft prose in body
4. Copy entire file into ChatGPT for iteration
5. Paste back revised prose
6. Repeat as needed

### Compilation Test

1. Create 2-3 test scenes with different `order` values
2. Run `./build.sh` to generate `_manuscript.md`
3. Verify scenes compile in correct order
4. Verify YAML stripped from output
5. Optional: Test `./build.sh Draft.docx`

---

## Resources

### Documentation
- [Pandoc Manual](https://pandoc.org/MANUAL.html)
- [Obsidian Properties](https://help.obsidian.md/properties)
- [YAML Spec](https://yaml.org/spec/1.2.2/)
- [VS Code Markdown](https://code.visualstudio.com/docs/languages/markdown)
- [ChatGPT Projects](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)
- [Obsidian Advanced URI](https://vinzent03.github.io/obsidian-advanced-uri/)

### Tools
- [ChatGPT Mac App](https://chatgpt.com/features/desktop/)
- [VS Code](https://code.visualstudio.com/)
- [Obsidian](https://obsidian.md/)
- [Pandoc](https://pandoc.org/)
- [Actions for Obsidian](https://actions.work/actions-for-obsidian)
- [Obsidian Web Clipper](https://gist.github.com/kepano/90c05f162c37cf730abb8ff027987ca3)

---

## Conclusion

This workflow provides:
- **20+ year portability** via plain text Markdown
- **Zero lock-in** to any specific tool
- **ChatGPT Plus integration** without API costs
- **Cross-device access** via iCloud + Obsidian mobile
- **Version safety** via Time Machine + Timeline
- **Compilation flexibility** via Pandoc
- **Low friction** via single-folder, YAML-in-front pattern
- **Tool choice** between VS Code and Obsidian as mood suits

Start simple. Add complexity only when friction appears. Keep files portable always.
