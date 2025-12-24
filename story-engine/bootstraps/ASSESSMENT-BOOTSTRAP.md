# ASSESSMENT Bootstrap

**Purpose**: Analyze existing published work to determine the optimal path forward (revision, expansion, or other).

---

## When to Use This Bootstrap

- You have a published story (flash, vignette, short story)
- You want to improve it but aren't sure whether to polish or expand
- You need to understand the story's potential scope
- You want professional assessment before committing to a workflow

---

## Assessment Process

### Phase 1: Deep Analysis

1. **Load and Read Original Story**
   - From: `_posts/[YYYY-MM-DD-story-title].md`
   - Note current word count and scope
   - Identify publication context

2. **Generate Comprehensive Dossier**
   - Story metadata and synopsis
   - Scene/beat breakdown
   - Character analysis (present and implied)
   - World-building (shown and suggested)
   - Themes, motifs, symbols
   - Plot structure and pacing
   - Voice, style, POV characteristics
   - Technical strengths and weaknesses

3. **Identify Compression Points**
   - What elements exist but are compressed?
   - What threads were cut for space?
   - What backstory is implied but not shown?
   - What world-building is hinted at?
   - What character depth is suggested?

### Phase 2: Scope Analysis

4. **Assess Current Scope**
   - Flash fiction (under 1,000 words)
   - Vignette (descriptive snapshot)
   - Short-short (1,000-2,000 words)
   - Short story (2,000-7,500 words)
   - Novelette (7,500-17,500 words)
   - Novella (17,500-40,000 words)

5. **Determine Natural Scope**
   - What does the material want to be?
   - What scope serves the story best?
   - Consider:
     - Complexity of premise
     - Character development needs
     - World-building requirements
     - Plot threads present
     - Thematic depth

6. **Analyze Expansion Potential**
   - **HIGH**: Rich compressed material, clear expansion paths
   - **MEDIUM**: Some expansion possible, requires creative development
   - **LOW**: Story feels complete at current scope
   - **NONE**: Perfect as-is, expansion would dilute

### Phase 3: Path Recommendations

7. **Evaluate Options**

   **Option A: Polish/Revision (Current Scope)**
   - Story is complete at current length
   - Needs refinement, not expansion
   - Technical improvements only
   - Next: REVISION-BOOTSTRAP

   **Option B: Expansion (Larger Scope)**
   - Material wants/needs more room
   - Clear paths for development
   - Expansion would strengthen story
   - Next: EXPANSION-BOOTSTRAP

   **Option C: Reboot (Same or Different Scope)**
   - Core idea strong, execution weak
   - Better to rebuild than revise
   - Next: DRAFTING-BOOTSTRAP (using original as reference)

   **Option D: Series/Universe Potential**
   - World/characters support multiple stories
   - Consider expanding universe, not just story
   - Next: UNIVERSE-BOOTSTRAP

   **Option E: Leave As-Is**
   - Story is complete and effective
   - Changes would not improve it
   - Archive assessment, celebrate success

8. **Make Recommendation**
   - Primary recommendation with reasoning
   - Alternative options if applicable
   - Estimated work involved for each path
   - Expected outcomes

---

## Assessment Report Template

Create in: `_drafts/[story-name]/assessment.md`

```markdown
# Story Assessment: [Title]

**Date**: [Date]  
**Original Publication**: [Where/When]  
**Current Scope**: [Scope type]  
**Current Word Count**: [X words]

---

## Story Summary

[2-3 sentence synopsis]

---

## Current State Analysis

### What's Working (Preserve These)

- [Strength 1]
- [Strength 2]
- [Strength 3]

### What's Compressed (Could Expand)

- [Compressed element 1]
- [Compressed element 2]
- [Compressed element 3]

### What's Missing (If Expanded)

- [Missing element 1]
- [Missing element 2]
- [Missing element 3]

---

## Scope Analysis

### Current Scope
**[Flash Fiction / Short Story / etc]** - [X words]

Functions as: [complete story / character sketch / world glimpse / etc]

### Natural Scope
**[Short Story / Novella / etc]** - [target word count]

The material suggests: [what it wants to be and why]

### Expansion Potential: [HIGH / MEDIUM / LOW / NONE]

**Reasoning**: [Why this assessment?]

---

## Expansion Analysis

### If Expanded to Short Story (3,000-5,000 words)

**Additional Scenes Needed**:
1. [Scene description]
2. [Scene description]
3. [Scene description]

**Character Development Opportunities**:
- [Character 1]: [What to develop]
- [Character 2]: [What to develop]

**World-Building to Explore**:
- [Element 1]
- [Element 2]

**Subplot Potential**:
- [Possible subplot 1]
- [Possible subplot 2]

**Estimated Work**: [X new scenes, Y revision passes, Z weeks]

### If Expanded to Novella (20,000-30,000 words)

[Similar analysis for novella scope]

### If Expanded to Novel (60,000+ words)

[Similar analysis for novel scope]

---

## Path Recommendations

### ⭐ RECOMMENDED: Option [A/B/C]

**Path**: [Polish/Expand/Reboot/etc]

**Why**: [Clear reasoning for this recommendation]

**Work Involved**:
- [Task 1]
- [Task 2]
- [Task 3]

**Expected Outcome**: [What you'll have when done]

**Next Bootstrap**: [Which workflow to use]

**Estimated Timeline**: [X sessions / Y weeks]

### Alternative: Option [X]

**Path**: [Alternative path]

**Why Consider This**: [When this might be better]

**Next Bootstrap**: [Which workflow]

---

## Decision Point

**Author, please choose**:
1. Accept primary recommendation and proceed with [BOOTSTRAP]
2. Choose alternative option: [which one?]
3. Request additional analysis on: [what?]
4. Table this story for now

---

## Appendix: Full Story Dossier

[Comprehensive analysis - all the detail]

### Characters
[Full character analysis]

### World-Building
[Full world analysis]

### Structure
[Full structural analysis]

### Themes
[Full thematic analysis]

### Technical Notes
[Voice, style, POV, prose]

```

---

## Deliverables

After assessment session, you should have:

1. **assessment.md** - Complete assessment report
2. **original-[filename].md** - Archived copy of original story
3. **Author decision** - Which path to take

These files save to: `_drafts/[story-name]/`

---

## Example Session Initialization

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/ASSESSMENT-BOOTSTRAP.md

# Assess: Mitzy and the Butterfly

Original story: _posts/2015-08-21-mitzy-and-the-butterfly.md

Generate comprehensive assessment with scope analysis and path recommendations.
```

---

## After Assessment

Once author chooses a path:

### If REVISION chosen:
```
Connect to Workbench.
Load story-engine/bootstraps/REVISION-BOOTSTRAP.md
# Revising: [Title]
Load assessment from _drafts/[story-name]/
Begin revision project.
```

### If EXPANSION chosen:
```
Connect to Workbench.
Load story-engine/bootstraps/EXPANSION-BOOTSTRAP.md
# Expand: [Title]
Target scope: [Short Story / Novella / etc]
Load assessment from _drafts/[story-name]/
Begin expansion planning.
```

### If REBOOT chosen:
```
Connect to Workbench.
Load story-engine/bootstraps/DRAFTING-BOOTSTRAP.md
# Reboot: [Title]
Original for reference: _posts/[filename].md
Assessment: _drafts/[story-name]/assessment.md
Begin fresh draft using core concept.
```

---

## Key Questions to Answer

1. **Completeness**: Does this story feel complete at its current scope?
2. **Compression**: Are important elements compressed or cut?
3. **Potential**: Would expansion make this story better or just longer?
4. **Voice**: Can the voice sustain a longer work?
5. **Substance**: Is there enough material to expand without padding?
6. **Interest**: Would readers want more of this world/character?
7. **Author Intent**: What did the author want when they wrote this?
8. **Objective Value**: What serves the story best?

---

## Assessment Principles

- **Be honest**: Don't recommend expansion just because we can
- **Be specific**: Identify exactly what would expand and how
- **Be realistic**: Estimate actual work involved
- **Honor the original**: Preserve what makes the story work
- **Think strategically**: Consider author's goals and catalog
- **Question assumptions**: Maybe it's perfect as-is

---

**Bootstrap Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench