# Story Engine

**Purpose**: A systematic workspace for all phases of storytelling - from initial ideation through publication.

---

## Overview

The Story Engine is a modular system for managing creative writing projects of any scope. It uses workflow-specific bootstraps to guide different types of work while maintaining consistent editorial principles.

---

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

**Type**: [Short story / Novel / Serial / Universe / Blog Post]
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

## Available Workflows (10 Total)

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

**Phases**: Analysis → Planning → Execution → Integration → Finalization

**Output**: Revised story with author's note, preserved at original scope

**Size**: 20,995 bytes (comprehensive workflow)

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

**Phases**: Foundation Review → Structure Planning → Incremental Building → Integration & Polish

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

### BETA-REVIEW-BOOTSTRAP.md
**When to use**: Simulating beta reader feedback for outlines or drafts before major revision

**Phases**: Setup & Intent → Audience Simulation → Feedback Synthesis → Revision Plan

**Output**: Beta review report with prioritized feedback and revision plan

**Size**: 10,084 bytes (complete workflow)

**Use for**: Blog post outlines, fiction drafts, essay structures

**Example**:
```
Load story-engine/bootstraps/BETA-REVIEW-BOOTSTRAP.md

# Beta Review: How to Build a Story Engine
Artifact: _drafts/story-engine-post/outline.md
Target audience: Fiction writers, productivity enthusiasts
Review for: Structure, clarity, actionability
Run beta review with 4 personas.
```

---

### BLOG-POST-BOOTSTRAP.md
**When to use**: Planning, drafting, revising, and publishing non-fiction blog posts

**Phases**: Setup → Concept & Angle → Outline & Research → Beta Review (optional) → Drafting → Revision → Publication

**Output**: Published blog post with complete project archive

**Size**: 12,985 bytes (comprehensive workflow)

**Use for**: Substack essays, how-to posts, opinion pieces, case studies, personal reflections

**Example**:
```
Load story-engine/bootstraps/BLOG-POST-BOOTSTRAP.md

# New Post: How to Build a Personal Story Engine
Target: Substack (weekly essay)
Audience: Fiction writers, productivity enthusiasts
Purpose: Teach systematic approach to story development
Scope: 1,500 words
Begin setup and concept development.
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

### Need feedback on outline or draft?
→ **BETA-REVIEW-BOOTSTRAP**

### Starting from scratch?
- Have a concept? → **IDEATION-BOOTSTRAP**
- Have notes/partial draft? → **DRAFTING-BOOTSTRAP**
- Building a world/series? → **UNIVERSE-BOOTSTRAP**

### Working on non-fiction?
→ **BLOG-POST-BOOTSTRAP** (blog posts, essays, tutorials)

### Working on long-form?
- Single novel? → **NOVEL-BOOTSTRAP**
- Series/episodes? → **SERIAL-BOOTSTRAP**

---

## Bootstrap Relationships

### Common Workflow Chains

**Fiction Revision Path**:
```
ASSESSMENT → REVISION → (optional) BETA-REVIEW → Final REVISION
```

**Fiction Expansion Path**:
```
ASSESSMENT → EXPANSION → (optional) BETA-REVIEW → REVISION
```

**New Fiction from Scratch**:
```
IDEATION → DRAFTING → (optional) BETA-REVIEW → REVISION
```

**Blog Post Standard**:
```
BLOG-POST (includes optional BETA-REVIEW at Phase 4)
```

**Long-form Fiction**:
```
IDEATION → NOVEL (self-contained Snowflake workflow)
```

**Series Development**:
```
UNIVERSE → SERIAL → (multiple DRAFTING/REVISION cycles)
```

**Quick Fiction**:
```
DRAFTING → REVISION (skip IDEATION if concept is clear)
```

### Bootstrap Dependencies

| Bootstrap | Can Lead To | Can Follow |
|-----------|-------------|------------|
| ASSESSMENT | REVISION, EXPANSION | (entry point) |
| IDEATION | DRAFTING, NOVEL | (entry point) |
| DRAFTING | REVISION, BETA-REVIEW | IDEATION |
| EXPANSION | REVISION, BETA-REVIEW | ASSESSMENT |
| BETA-REVIEW | REVISION | DRAFTING, EXPANSION, BLOG-POST |
| REVISION | (publication) | ASSESSMENT, EXPANSION, DRAFTING, BETA-REVIEW |
| BLOG-POST | (publication) | (self-contained) |
| NOVEL | (publication) | IDEATION |
| SERIAL | (publication) | UNIVERSE, DRAFTING |
| UNIVERSE | SERIAL, DRAFTING | (entry point) |

---

## Bootstrap Sizes

| Bootstrap | Size (bytes) | Completeness |
|-----------|--------------|-------------|
| ASSESSMENT | 8,274 | Complete |
| BETA-REVIEW | 10,084 | Complete (4 phases) |
| BLOG-POST | 12,985 | Comprehensive (7 phases) |
| DRAFTING | 10,750 | Complete (5 phases) |
| EXPANSION | 9,685 | Complete (4 phases) |
| IDEATION | 9,432 | Complete (5 phases) |
| NOVEL | 14,142 | Comprehensive |
| REVISION | 20,995 | Comprehensive (5 phases) |
| SERIAL | 13,041 | Complete |
| UNIVERSE | 12,889 | Complete |

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
- Beta reader simulation with persona-based feedback
- Scope assessment (flash → novel)
- World-building and character development
- Plot structure and pacing (multiple frameworks)
- Scene construction (Goal→Conflict→Disaster, Reaction→Dilemma→Decision)
- Revision planning and execution
- Expansion and development
- Blog post development and publication workflow
- Snowflake Method for novels
- Fractal scene-building
- Series/universe continuity management
- Documentation and project tracking

WORKFLOW:
Each session begins by loading the appropriate bootstrap for the work type
from story-engine/bootstraps/[WORKFLOW]-BOOTSTRAP.md

Available workflows (10 total):
- ASSESSMENT: Analyze existing work to determine optimal path
- REVISION: Polish and refine within current scope (5 phases)
- EXPANSION: Grow stories to larger scope
- DRAFTING: Build complete stories from fragments
- IDEATION: Develop concepts into workable outlines
- BETA-REVIEW: Simulate reader feedback for outlines/drafts
- BLOG-POST: Complete blog post workflow from concept to publication
- UNIVERSE: Build story bibles and world continuity
- SERIAL: Manage multi-part stories and series
- NOVEL: Coordinate long-form work with Snowflake Method

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

### Writing Weekly Blog Post

**Session 1: Setup and Outline**
```
Connect to Workbench.
Load story-engine/bootstraps/BLOG-POST-BOOTSTRAP.md
# New Post: [Working Title]
Target: Substack
Audience: [Description]
Scope: 1,500 words
Begin setup through outline.
```

**Session 2 (Optional): Beta Review Outline**
```
Connect to Workbench.
Load story-engine/bootstraps/BETA-REVIEW-BOOTSTRAP.md
# Beta Review: [Title]
Artifact: _drafts/[post-slug]/outline.md
Run beta review before drafting.
```

**Session 3: Draft and Publish**
```
Connect to Workbench.
Load story-engine/bootstraps/BLOG-POST-BOOTSTRAP.md
# Post: [Title]
Load artifacts: _drafts/[post-slug]/
Complete drafting, revision, and publication.
```

---

### Testing Fiction Draft Before Revision

**Session 1: Beta Review**
```
Connect to Workbench.
Load story-engine/bootstraps/BETA-REVIEW-BOOTSTRAP.md
# Beta Review: [Title]
Artifact: _drafts/[story-name]/assembled-draft.md
Target audience: [Genre] readers
Simulate reader panel and synthesize feedback.
```

**Session 2: Revision from Feedback**
```
Connect to Workbench.
Load story-engine/bootstraps/REVISION-BOOTSTRAP.md
# Revising: [Title]
Project folder: _drafts/[story-name]/
Use beta-review.md to guide revision planning.
```

---

## FAQ / Troubleshooting

### Q: Which bootstrap should I use for an existing story?
**A**: Always start with ASSESSMENT-BOOTSTRAP for existing published work. It will analyze the story and recommend whether to use REVISION (polish at current scope) or EXPANSION (grow to larger scope).

### Q: Can I switch bootstraps mid-project?
**A**: Yes! Document the switch in your project README.md under "Workflow History". Common switches: DRAFTING → BETA-REVIEW → REVISION, or ASSESSMENT → EXPANSION → REVISION.

### Q: What if I'm between two scopes (e.g., long flash vs. short story)?
**A**: Use ASSESSMENT-BOOTSTRAP to analyze the work. It includes scope analysis that will help you decide. When in doubt, start with the smaller scope and expand if needed.

### Q: Should I use BETA-REVIEW before or after drafting?
**A**: Either works:
- **Before drafting**: Review outline to test structure (faster, catches big issues early)
- **After drafting**: Review complete draft for full reader experience (more realistic feedback)

### Q: Can BLOG-POST be used for fiction?
**A**: No. BLOG-POST is specifically for non-fiction (essays, tutorials, opinion pieces). For fiction, use the appropriate fiction bootstrap (IDEATION → DRAFTING → REVISION).

### Q: How do I handle a project that uses multiple bootstraps?
**A**: Track the workflow history in your project README.md. Example:
```markdown
## Workflow History

### Phase 1: Assessment (Dec 2025)
**Bootstrap**: ASSESSMENT-BOOTSTRAP
**Outcome**: Recommended expansion

### Phase 2: Expansion (Jan 2026)
**Bootstrap**: EXPANSION-BOOTSTRAP
**Status**: Complete

### Phase 3: Beta Review (Jan 2026)
**Bootstrap**: BETA-REVIEW-BOOTSTRAP
**Status**: In progress
```

### Q: What if I don't have a published original for ASSESSMENT?
**A**: ASSESSMENT requires existing published work. For new projects, use:
- IDEATION (just an idea)
- DRAFTING (partial draft or notes)
- NOVEL (long-form from scratch)

### Q: Can I create my own bootstrap?
**A**: Yes! See the BOOTSTRAP-TEMPLATE.md for guidance on creating custom workflows. Follow the standard structure: Purpose → Phases → Deliverables → Status Checks.

### Q: How do I know when to move to the next phase?
**A**: Each phase ends with a "Status Check" section. Complete when that checklist is satisfied. Don't rush—quality over speed.

### Q: What if the AI suggests changes I don't like?
**A**: The core principle is "Author approval required". Always push back, ask for alternatives, or specify exactly what you want. You're the author; the AI is the collaborator.

### Q: Should I commit after every phase?
**A**: Yes, commit at phase completion at minimum. More frequent commits are fine for large phases. Use clear commit messages that reference the phase and deliverable.

---

## Migrating Existing Projects

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

**v1.3** - December 23, 2025  
Added improvements:
- Fixed bootstrap sizes table with actual file sizes
- Added Bootstrap Relationships section with workflow chains
- Added Bootstrap Dependencies table
- Added FAQ/Troubleshooting section
- Alphabetized bootstrap sizes table

**v1.2** - December 23, 2025  
Completed all 10 bootstraps:
- Expanded REVISION-BOOTSTRAP.md (5,319 → 20,995 bytes)
- Completed BETA-REVIEW-BOOTSTRAP.md (3,361 → 10,084 bytes)
- Completed BLOG-POST-BOOTSTRAP.md (2,470 → 12,985 bytes)
- Updated folder naming across all bootstraps

**v1.1** - December 23, 2025  
Updated folder naming convention - removed workflow suffix

**v1.0** - December 23, 2025  
Initial Story Engine structure with modular bootstrap system

---

**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
