# Story Engine

**Purpose**: A systematic workspace for all phases of storytelling - from initial ideation through publication.

---

## Overview

The Story Engine is a modular system for managing creative writing projects of any scope. It uses workflow-specific bootstraps to guide different types of work while maintaining consistent editorial principles.

## Quick Start

### In the Story Engine Space (Perplexity):

1. **Connect to GitHub**
   ```
   Connect to my Workbench repo on GitHub.
   ```

2. **Load appropriate bootstrap**
   ```
   Load story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md
   ```

3. **Start your session**
   ```
   # [Session Type]: [Project Name]
   [Specific instructions based on workflow]
   ```

---

## File Structure Convention

### Project Folders

All projects live in `_drafts/[project-name]/` regardless of workflow:

```
_drafts/
├── story-engine/          # Bootstrap library
├── mitzy/                 # Just the story name
├── eddie-zero/            # No workflow suffix
├── memory-thief/          # Novel project
└── maze-chronicles/       # Serial project
```

**Inside each project folder**, the README.md tracks:
- Current workflow (assessment, revision, expansion, etc.)
- Bootstrap history (which workflows used when)
- Current phase
- Status

### Why No Workflow Suffix?

- Same story might use multiple workflows (assess → expand → revise)
- Workflow is implementation detail, not identity
- Cleaner folder structure
- README.md inside tracks workflow history

### Project README Template

```markdown
# [Project Name]

**Type**: [Short story / Novel / Serial / Universe]
**Status**: [Active / Complete / On Hold]
**Current Phase**: [Analysis / Planning / Drafting / Revision / etc]

---

## Workflow History

### Phase 1: Assessment (Dec 2025)
**Bootstrap**: ASSESSMENT-BOOTSTRAP  
**Outcome**: Recommended expansion to short story  
**Artifacts**: assessment.md

### Phase 2: Expansion (Dec 2025 - Jan 2026)
**Bootstrap**: EXPANSION-BOOTSTRAP  
**Status**: In progress  
**Current**: Scene building (Act II)  
**Artifacts**: foundation.md, expansion-plan.md, scenes/

---

## Project Files

- `README.md` - This file
- `original-[filename].md` - Archived original (if applicable)
- `assessment.md` - Assessment report (if assessed)
- `[other workflow-specific files]`

---

## Next Steps

[What needs to happen next]
```

---

## Available Workflows

### ASSESSMENT-BOOTSTRAP.md
**When to use**: Analyzing existing published work to determine the best path forward

**Output**: Comprehensive assessment with scope analysis and path recommendations

**Leads to**: REVISION, EXPANSION, or REBOOT workflows

**Example**:
```
Load story-engine/bootstraps/ASSESSMENT-BOOTSTRAP.md

# Assess: Mitzy and the Butterfly
Original: _posts/2015-08-21-mitzy-and-the-butterfly.md
Project folder: _drafts/mitzy/
Analyze and recommend path forward.
```

---

### REVISION-BOOTSTRAP.md
**When to use**: Polishing/refining existing work at its current scope

**Phases**: Analysis → Planning → Execution → Finalization

**Output**: Revised story with author's note, preserved at original scope

**Example**:
```
Load story-engine/bootstraps/REVISION-BOOTSTRAP.md

# Revising: Mitzy and the Butterfly
Project folder: _drafts/mitzy/
Load artifacts and report status.
```

---

### EXPANSION-BOOTSTRAP.md
**When to use**: Growing existing flash/short work into larger scope

**Phases**: Foundation Review → Structure Planning → Incremental Building → Integration

**Output**: Expanded story preserving original core with added depth

**Example**:
```
Load story-engine/bootstraps/EXPANSION-BOOTSTRAP.md

# Expand: Mitzy and the Butterfly
Project folder: _drafts/mitzy/
Original: _posts/2015-08-21-mitzy-and-the-butterfly.md
Target scope: Short story (4,000 words)
Begin expansion planning.
```

---

### DRAFTING-BOOTSTRAP.md
**When to use**: Building complete story from brain dump, partial draft, or concept

**Phases**: Foundation → Outline → Scene Building → Assembly → Polish

**Output**: Complete first draft ready for revision

**Example**:
```
Load story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# New Story: The Collector
Project folder: _drafts/the-collector/
Attached: brain dump notes
Target scope: Short story
Develop complete draft.
```

---

### IDEATION-BOOTSTRAP.md
**When to use**: Developing story concept from seed idea or prompt

**Phases**: Premise → Characters → Conflict → Structure → Validation

**Output**: Story concept document ready for drafting

**Example**:
```
Load story-engine/bootstraps/IDEATION-BOOTSTRAP.md

# New Concept: "What if memories could be stolen?"
Project folder: _drafts/memory-thief-concept/
Develop into story premise.
```

---

### UNIVERSE-BOOTSTRAP.md
**When to use**: Building story bible, world-building docs, series continuity

**Output**: Comprehensive universe documentation

**Example**:
```
Load story-engine/bootstraps/UNIVERSE-BOOTSTRAP.md

# Universe: The Maze Worlds
Project folder: _drafts/maze-worlds/
Analyze existing stories and build continuity documentation.
```

---

### SERIAL-BOOTSTRAP.md
**When to use**: Managing multi-part stories, novel chapters, series installments

**Output**: Episode/chapter tracking with arc management

**Example**:
```
Load story-engine/bootstraps/SERIAL-BOOTSTRAP.md

# Serial: Dark Tales Collection
Project folder: _drafts/dark-tales/
Manage episodic releases and continuity.
```

---

### NOVEL-BOOTSTRAP.md
**When to use**: Long-form work management (50,000+ words)

**Method**: Snowflake Method with fractal scene-building

**Output**: Complete novel from concept to publication

**Example**:
```
Load story-engine/bootstraps/NOVEL-BOOTSTRAP.md

# Novel: The Memory Thief
Project folder: _drafts/memory-thief/
One-sentence premise: A memory thief must recover her own stolen past.
Target: 80,000 words
Begin Snowflake development.
```

---

## Decision Tree: Which Bootstrap?

### Starting with existing published work?
→ **ASSESSMENT-BOOTSTRAP** (determines next step)

### Assessment says "polish at current scope"?
→ **REVISION-BOOTSTRAP**

### Assessment says "expand to larger scope"?
→ **EXPANSION-BOOTSTRAP**

### Starting from scratch?
- Have a concept? → **IDEATION-BOOTSTRAP**
- Have notes/partial draft? → **DRAFTING-BOOTSTRAP**
- Building a world/series? → **UNIVERSE-BOOTSTRAP**

### Working on long-form?
- Single novel? → **NOVEL-BOOTSTRAP**
- Series/episodes? → **SERIAL-BOOTSTRAP**

---

## Space Custom Instructions

The Story Engine Space should have these custom instructions:

```
You are a literary editor and creative collaborator working with Douglas Langille 
across all phases of storytelling - from initial ideation through publication.

CORE PRINCIPLES:
- GitHub (douglangille/Workbench) is the source of truth
- Author approval required before executing creative decisions
- Preserve and strengthen the author's distinctive voice
- Question assumptions - collaborate, don't dictate
- Document all decisions for continuity
- Work systematically through defined phases
- Commit to GitHub frequently
- Think with surgical precision

YOUR CAPABILITIES:
- Story analysis and critique
- Scope assessment (flash → novel)
- World-building and character development
- Plot structure and pacing (multiple frameworks)
- Scene construction (Goal→Conflict→Disaster, Reaction→Dilemma→Decision)
- Revision planning and execution
- Expansion and development
- Snowflake Method for novels
- Fractal scene-building
- Series/universe continuity management
- Documentation and project tracking

WORKFLOW:
Each session begins by loading the appropriate bootstrap for the work type
from _drafts/story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md

Then load relevant project artifacts from _drafts/[project-name]/ and report 
status before proceeding.

PROJECT FOLDERS:
All projects use simple folder names: _drafts/[project-name]/
Workflow history tracked in project README.md, not folder name.
```

---

## Typical Workflows

### Revising Published Flash Fiction

**Session 1: Assessment**
```
Connect to Workbench.
Load story-engine/bootstraps/ASSESSMENT-BOOTSTRAP.md
# Assess: [Title]
Original: _posts/[filename].md
Project folder: _drafts/[story-name]/
```

**Session 2: Choose Path**
Based on assessment, load REVISION or EXPANSION bootstrap

**Session 3+: Execute**
Work through chosen workflow phases

---

### Building New Story from Idea

**Session 1: Ideation**
```
Connect to Workbench.
Load story-engine/bootstraps/IDEATION-BOOTSTRAP.md
# New Concept: [Premise]
Project folder: _drafts/[concept-name]/
```

**Session 2: Drafting**
```
Connect to Workbench.
Load story-engine/bootstraps/DRAFTING-BOOTSTRAP.md
# Draft: [Title]
Project folder: _drafts/[story-name]/
Load concept from ideation session
```

**Session 3+: Polish**
Once draft complete, potentially use REVISION-BOOTSTRAP for final polish

---

### Migrating Existing Projects

For projects created before this convention (like `mitzy-revision/`):

**Option 1: Rename folder**
```bash
mv _drafts/mitzy-revision/ _drafts/mitzy/
```
Then update project README to track workflow history.

**Option 2: Leave as-is**
Existing projects can keep their names. New convention applies to new projects.

---

## Version History

**v1.1** - December 23, 2025  
Updated folder naming convention - removed workflow suffix

**v1.0** - December 23, 2025  
Initial Story Engine structure with modular bootstrap system

---

**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
