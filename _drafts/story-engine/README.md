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
Load _drafts/mitzy-revision/ and report status.
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
Develop into story premise.
```

---

### UNIVERSE-BOOTSTRAP.md
**When to use**: Building story bible, world-building docs, series continuity

**Output**: Comprehensive universe documentation

**Example**:
```
Load story-engine/bootstraps/UNIVERSE-BOOTSTRAP.md

# Universe: The Maze Stories
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
Manage episodic releases and continuity.
```

---

### NOVEL-BOOTSTRAP.md
**When to use**: Long-form work management (50,000+ words)

**Output**: Chapter-by-chapter management with act structure tracking

**Example**:
```
Load story-engine/bootstraps/NOVEL-BOOTSTRAP.md

# Novel: [Working Title]
Begin long-form project management.
```

---

## File Structure

```
_drafts/
├── story-engine/
│   ├── README.md (this file)
│   └── bootstraps/
│       ├── ASSESSMENT-BOOTSTRAP.md
│       ├── REVISION-BOOTSTRAP.md
│       ├── EXPANSION-BOOTSTRAP.md
│       ├── DRAFTING-BOOTSTRAP.md
│       ├── IDEATION-BOOTSTRAP.md
│       ├── UNIVERSE-BOOTSTRAP.md
│       ├── SERIAL-BOOTSTRAP.md
│       └── NOVEL-BOOTSTRAP.md
│
├── [story-name]-revision/      # Revision projects
├── [story-name]-expansion/     # Expansion projects
├── [story-name]-draft/         # Active drafts
├── [universe-name]/            # Universe documentation
└── [series-name]/              # Serial/series work
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
- Plot structure and pacing
- Scene construction and dialogue
- Revision planning and execution
- Expansion and development
- Series/universe continuity management
- Documentation and project tracking

WORKFLOW:
Each session begins by loading the appropriate bootstrap for the work type
from _drafts/story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md

Then load relevant project artifacts and report status before proceeding.
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
```

**Session 2: Drafting**
```
Connect to Workbench.
Load story-engine/bootstraps/DRAFTING-BOOTSTRAP.md
# Draft: [Title]
Load concept from ideation session
```

**Session 3+: Polish**
Once draft complete, potentially use REVISION-BOOTSTRAP for final polish

---

## Version History

**v1.0** - December 23, 2025  
Initial Story Engine structure with modular bootstrap system

---

**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
