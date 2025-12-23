# Context Management Strategy

**Core Principle**: GitHub is the source of truth. Every session starts fresh by loading only what's needed.

---

## Why This Matters

**The Problem**: LLM context windows are limited and context drift accumulates across long conversations.

**The Solution**: 
- Store ALL artifacts as individual files in GitHub
- Start new sessions regularly
- Load bootstrap + only needed artifacts
- Work intentionally with small context
- Push results immediately back to GitHub

**Benefits**:
- Fresh context every session = no drift
- Precise control over what LLM sees
- Easy to resume work days/weeks/months later
- Parallel work possible (multiple sessions on different scenes)
- Complete audit trail in git history

---

## File Granularity Guidelines

### Always Separate Files

**Character files** - One file per major character:
```
characters/
├── protagonist-mitzy.md
├── antagonist-goblin.md
└── supporting-larry.md
```

**World-building** - Separate concerns:
```
world/
├── geography.md
├── magic-system.md
├── history.md
└── cultures.md
```

**Scene files** - ONE scene per file:
```
scenes/
├── ch01-sc01-awakening.md
├── ch01-sc02-meeting-larry.md
├── ch02-sc01-entering-maze.md
└── ch02-sc02-confrontation.md
```

**Scene briefs** - ONE brief per file:
```
scene-briefs/
├── ch01-sc01-brief.md
├── ch01-sc02-brief.md
└── ...
```

### Why Atomic Files?

**For Characters**:
- Load only characters needed for current scene
- Update character without affecting others
- Easy to reference specific character across sessions

**For Scenes**:
- Write/revise one scene without loading entire draft
- Parallel work (AI drafts scene 5 while you revise scene 3)
- Precise context: scene brief + relevant character files + world rules
- Easy to reorder scenes (just rename files)

**For World-Building**:
- Load magic system without geography
- Update history without touching cultures
- Reference only what current scene needs

---

## Session Patterns

### Pattern 1: Planning Session
**Context Load**:
- Bootstrap (planning phase)
- Project README (status)
- Dossier (if analyzing existing work)

**Output**:
- Updated README
- Planning documents (outline, structure, etc.)
- Individual character files
- Commit all

**Keep It Small**: Planning documents should be concise references, not full prose.

---

### Pattern 2: Scene Drafting Session
**Context Load**:
- Bootstrap (drafting phase)
- Scene brief for THIS scene
- Character files for characters IN this scene
- World-building files RELEVANT to this scene
- Previous scene ending (for continuity)

**Output**:
- Completed scene file
- Updated drafting notes
- Commit

**Intentional**: Don't load entire outline, entire cast, entire world. Just what's needed.

---

### Pattern 3: Revision Session
**Context Load**:
- Bootstrap (revision phase)
- Scene being revised
- Critique/analysis of that scene
- Character consistency notes

**Output**:
- Revised scene
- Update to revision log
- Commit

**Focus**: One scene at a time. Finish it. Move to next.

---

### Pattern 4: Analysis Session
**Context Load**:
- Bootstrap (analysis phase)
- Story/scene to analyze
- Assessment criteria

**Output**:
- Analysis document
- Recommendations
- Commit

---

### Pattern 5: Continuity Check Session
**Context Load**:
- Bootstrap (continuity phase)
- Timeline
- Character database
- Scene range being checked

**Output**:
- Continuity report
- Corrections needed
- Commit

---

## Starting A New Session

### Template
```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md

# [Session Type]: [Project Name]

Project folder: _drafts/[project-name]/

Load artifacts:
- [Specific file 1]
- [Specific file 2]
- [Specific file 3]

[Specific instruction for this session]
```

### Be Explicit About Context

**Good**:
```
Load artifacts:
- README.md (project status)
- scene-briefs/ch03-sc02-brief.md
- characters/protagonist-mitzy.md
- characters/supporting-larry.md

Draft scene 3.2 following brief.
```

**Bad**:
```
Load the project and continue where we left off.
```

**Why**: LLM doesn't know "where we left off." Be explicit.

---

## File Naming Conventions

### Use Sortable Names

**Scenes**: `ch[XX]-sc[XX]-[name].md`
- Example: `ch01-sc01-awakening.md`
- Sorts correctly in file listings
- Easy to identify and load

**Characters**: `[role]-[name].md`
- Example: `protagonist-mitzy.md`
- Clear role identification

**World**: `[topic].md`
- Example: `magic-system.md`
- Simple, descriptive

### Use Hyphens, Not Spaces
- Good: `scene-brief.md`
- Bad: `scene brief.md`
- Reason: CLI-friendly, URL-friendly

---

## What Goes In Each File Type

### README.md (Project Root)
- Project metadata
- Workflow history
- Current status
- File structure map
- Next steps
- **Keep brief**: 1-2 pages max

### Dossier / Assessment
- Complete analysis of existing work
- Or comprehensive story concept
- Foundation for all other work
- **Reference document**: Load when making major decisions

### Character Files
```markdown
# [Character Name]

**Role**: [Protagonist/Antagonist/Supporting]
**Appears In**: [List of scenes]

## Basic Info
- Age:
- Appearance:
- Occupation:

## Psychology
- Motivation:
- Goal:
- Flaw:
- Arc:

## Voice
- Speech patterns:
- Vocabulary:
- Quirks:

## Relationships
- [Character A]: [relationship]
- [Character B]: [relationship]

## Knowledge State
[What they know at different points in story]

## Continuity Notes
[Track changes, decisions, important moments]
```

### Scene Brief
```markdown
# Chapter [X], Scene [Y]: [Title]

**Type**: SCENE / SEQUEL
**POV**: [Character]
**Setting**: [Where/when]
**Characters**: [Who's present]
**Word Count Target**: [X words]

## Structure
[Scene: Goal/Conflict/Disaster OR Sequel: Reaction/Dilemma/Decision]

## Key Elements
- Plot advance:
- Character reveal:
- Tension:
- Atmosphere:

## Opening
[How scene begins]

## Ending
[How scene ends / hook]

## Continuity
- Follows: [Previous scene]
- Leads to: [Next scene]
- References: [Past events]
```

### Scene Draft
```markdown
# Chapter [X], Scene [Y]: [Title]

**Brief**: scene-briefs/ch[XX]-sc[YY]-brief.md
**Status**: [Draft / Revised / Final]
**Word Count**: [Actual count]

---

[Full prose of scene]

---

## Revision Notes
[What changed from brief, why]
```

### World-Building Files
```markdown
# [Topic]

## Overview
[Brief description]

## Rules
[How this works]

## Limitations
[What it can't do]

## History
[How it came to be]

## Story Impact
[How this affects plot/characters]

## Continuity Notes
[Track usage across scenes]
```

---

## Commit Frequency

### Commit Often
- After each scene draft
- After each character file
- After each planning document
- After each revision pass

### Commit Messages
Be specific:
- Good: "Draft chapter 3 scene 2: Larry's revelation"
- Good: "Revise protagonist-mitzy.md: add childhood trauma"
- Bad: "Update files"
- Bad: "Work in progress"

---

## Context Budget Management

### Estimate Token Counts

**Bootstrap**: ~5,000-8,000 tokens
**Character file**: ~500-1,000 tokens
**Scene brief**: ~300-500 tokens
**World-building file**: ~500-1,000 tokens
**Scene draft**: ~1,000-2,000 tokens

### Plan Your Context

For a scene drafting session:
- Bootstrap: 6,000 tokens
- Scene brief: 400 tokens
- 2 character files: 1,500 tokens
- 1 world file: 800 tokens
- **Total**: ~8,700 tokens
- **Remaining**: ~120K tokens for conversation

### If Context Gets Tight

1. **Start new session** with just what you need
2. **Split world files** into smaller pieces
3. **Reference, don't load**: "Use magic system as defined in magic-system.md"
4. **Summarize instead of loading**: Include summary in brief, not full file

---

## Long-Form Work Strategy

### Novels (50K+ words)

**DO**:
- One scene per file (~1,000-2,000 words)
- Scene briefs before drafting
- Character files separately
- World bible in pieces
- Regular continuity checks (every 10 scenes)

**DON'T**:
- Try to load entire novel
- Put all characters in one file
- Put all world-building in one file
- Work on multiple scenes in one session

### Serials / Episodes

**DO**:
- One episode per folder
- Master series bible at root
- Per-episode character state
- Continuity log updated after each episode

**DON'T**:
- Try to load all episodes at once
- Mix episodes in one file

---

## Example: Novel Session Workflow

### Day 1: Planning
```
Load: NOVEL-BOOTSTRAP, project README
Create: concept.md, structure.md
Output: Chapter summaries (one file per chapter summary)
Commit: "Complete novel structure planning"
```

### Day 2: Character Development
```
Load: NOVEL-BOOTSTRAP, structure.md
Create: characters/protagonist.md, characters/antagonist.md
Commit: "Create main character profiles"
```

### Day 3: Scene Briefs (Ch 1)
```
Load: NOVEL-BOOTSTRAP, chapters/ch01-summary.md, character files
Create: scene-briefs/ch01-sc01-brief.md through ch01-sc05-brief.md
Commit: "Create scene briefs for chapter 1"
```

### Day 4: Draft Scene 1.1
```
Load: NOVEL-BOOTSTRAP, scene-briefs/ch01-sc01-brief.md, 
      characters/protagonist.md, world/magic-system.md
Create: scenes/ch01-sc01-draft.md
Commit: "Draft chapter 1, scene 1"
```

### Day 5: Draft Scene 1.2
```
Load: NOVEL-BOOTSTRAP, scene-briefs/ch01-sc02-brief.md,
      characters/protagonist.md, characters/supporting-mentor.md,
      scenes/ch01-sc01-draft.md (for continuity)
Create: scenes/ch01-sc02-draft.md
Commit: "Draft chapter 1, scene 2"
```

**Pattern**: Each scene is its own session. Fresh context. Precise artifacts.

---

## Recovery and Resumption

### Coming Back After Break

**Week Later**:
```
Load: README.md
Read: Status, workflow history, next steps
Decide: What to work on
Start: New targeted session
```

**Month Later**:
```
Load: README.md, review commits since last session
Refresh: What was happening
Load: Specific artifact for current work
Proceed: From saved state
```

**Year Later**:
```
Everything is in GitHub.
README tells you exactly where you were.
Bootstraps still work the same way.
Pick up and continue.
```

---

## Tools and Helpers

### Use GitHub's File Structure
- Folders group related files
- File tree shows organization
- Easy to navigate and find files

### Use Markdown
- Human-readable
- Version-control friendly
- Easy to edit anywhere
- LLM-native format

### Use Git Commits
- Every save point is a commit
- Easy to see what changed
- Easy to revert if needed
- Complete history of work

---

## Anti-Patterns to Avoid

❌ **"Load the project"** - Too vague
✅ **"Load README.md and scene-briefs/ch02-sc03-brief.md"** - Specific

❌ **Single huge dossier file** (for novels)
✅ **Separate character/world/plot files** - Modular

❌ **All scenes in one file**
✅ **One scene per file** - Atomic

❌ **Long continuous conversation**
✅ **Fresh session for each task** - Clean context

❌ **"Continue where we left off"**
✅ **"Load scene-briefs/ch05-sc02-brief.md and draft scene"** - Explicit

❌ **Keeping work in conversation**
✅ **Commit immediately to GitHub** - Persistent

---

## Summary

1. **GitHub is truth**: Everything lives there
2. **Atomic files**: One concern per file
3. **Fresh sessions**: Start clean, load precisely
4. **Explicit instructions**: Tell LLM exactly what to load
5. **Commit often**: Every artifact, every draft
6. **Small context**: Only load what's needed
7. **Reference in briefs**: Scene brief contains everything needed to write that scene
8. **Track in README**: Workflow history and status

This strategy enables consistent, high-quality work across days, weeks, months, or years. The LLM never drifts because every session starts from saved state in GitHub.

---

**Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
