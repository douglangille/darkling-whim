# Story Engine

**A systematic approach to all phases of creative writing - from ideation through publication.**

---

## What Is Story Engine?

Story Engine is a modular workflow system for managing creative writing projects of any scope. It provides:

- **Structured workflows** for different types of creative work
- **GitHub-backed persistence** - never lose your place
- **Consistent editorial approach** across all projects
- **Flexible bootstraps** for different scopes and phases
- **Clear documentation** of all creative decisions

## How It Works

### 1. Create a Story Engine Space in Perplexity
- Name: "Story Engine" (or your preference)
- Load custom instructions from: `story-engine/CUSTOM-INSTRUCTIONS.txt`
- This gives you a dedicated creative workspace with consistent behavior

### 2. Start Any Session
```
Connect to Workbench.

Load story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md

[Follow bootstrap-specific startup instructions]
```

### 3. The AI Handles the Rest
- Loads appropriate artifacts
- Reports current status
- Guides you through the workflow
- Saves progress to GitHub

## Available Workflows

### ASSESSMENT-BOOTSTRAP.md
**For**: Analyzing existing published work to determine best path forward

**Use when**: You want to revisit a published story and need to decide whether to polish it, expand it, reboot it, or leave it alone.

**Outputs**: Comprehensive assessment with scope analysis and path recommendations

---

### REVISION-BOOTSTRAP.md
**For**: Polishing and refining existing work within its current scope

**Use when**: Story is complete but needs technical refinement, clarity improvements, or minor restructuring.

**Outputs**: Revised story with documented changes

---

### EXPANSION-BOOTSTRAP.md
**For**: Growing existing flash/short stories into larger works

**Use when**: Assessment shows the story has "more to say" and would benefit from deeper exploration.

**Outputs**: Expanded story preserving original core with added depth

---

### DRAFTING-BOOTSTRAP.md
**For**: Building complete stories from brain dumps, fragments, or partial drafts

**Use when**: You have raw material (notes, scenes, ideas) that needs structure and completion.

**Outputs**: Complete draft ready for revision

---

### IDEATION-BOOTSTRAP.md
**For**: Developing story concepts from initial sparks to workable outlines

**Use when**: You have a premise, character, or "what if" that needs to become a full story concept.

**Outputs**: Story concept with character, conflict, structure, and target scope

---

### UNIVERSE-BOOTSTRAP.md
**For**: Building story bibles, world-building documents, and cross-story continuity

**Use when**: Creating a shared universe for multiple stories or managing complex world-building.

**Outputs**: Story bible with characters, settings, rules, timelines, continuity tracking

---

### SERIAL-BOOTSTRAP.md
**For**: Managing multi-part stories, series, or episodic fiction

**Use when**: Writing connected stories, novel chapters, or serialized fiction.

**Outputs**: Series tracking with episode/chapter management and continuity tools

---

### NOVEL-BOOTSTRAP.md
**For**: Managing long-form work (50,000+ words)

**Use when**: Writing a novel with multiple acts, subplots, and complex character arcs.

**Outputs**: Novel management system with act/chapter tracking, subplot coordination, pacing tools

---

## Project Structure

All Story Engine work lives in `Workbench` repository:

```
Workbench/
├── story-engine/
│   ├── README.md (this file)
│   ├── CUSTOM-INSTRUCTIONS.txt (Space configuration)
│   └── bootstraps/
│       ├── ASSESSMENT-BOOTSTRAP.md
│       ├── REVISION-BOOTSTRAP.md
│       ├── EXPANSION-BOOTSTRAP.md
│       ├── DRAFTING-BOOTSTRAP.md
│       ├── IDEATION-BOOTSTRAP.md
│       ├── UNIVERSE-BOOTSTRAP.md
│       ├── SERIAL-BOOTSTRAP.md
│       └── NOVEL-BOOTSTRAP.md
├── _posts/                      # Published stories
└── _drafts/
    ├── [story-name]-revision/   # Revision projects
    ├── [story-name]-expansion/  # Expansion projects
    ├── [story-name]-draft/      # Active drafts
    ├── [universe-name]/         # Universe building
    └── [series-name]/           # Serial/series work
```

## Typical Workflows

### Revisiting Published Work
1. **ASSESSMENT** → Analyze and recommend path
2. Choose:
   - **REVISION** → Polish at current scope
   - **EXPANSION** → Grow to larger scope
   - **REBOOT** → Use as seed for fresh approach (DRAFTING)
   - Leave as-is

### Creating New Work
1. **IDEATION** → Develop concept
2. **DRAFTING** → Build complete draft
3. **REVISION** → Polish to publication quality

### Building a Universe
1. **UNIVERSE** → Establish world, rules, continuity
2. **IDEATION** → Develop stories within universe
3. **SERIAL** (optional) → Manage connected stories

### Writing a Novel
1. **IDEATION** or **UNIVERSE** → Foundation
2. **NOVEL** → Structure and chapter management
3. **DRAFTING** → Write individual chapters
4. **REVISION** → Polish complete manuscript

## Quick Reference

**Space Name**: Story Engine  
**Custom Instructions**: `story-engine/CUSTOM-INSTRUCTIONS.txt`  
**Bootstrap Location**: `story-engine/bootstraps/`  
**Published Stories**: `_posts/`  
**Active Work**: `_drafts/`  

**Session Startup Pattern**:
```
Connect to Workbench.
Load story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md
[Workflow-specific command]
```

---

**Story Engine Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
