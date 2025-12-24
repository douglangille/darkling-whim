# BETA-REVIEW Bootstrap

**Purpose**: Run a single, focused "beta reader" pass on an outline or draft, simulate target audience feedback, and convert it into a surgical revision plan.

**Use this for**:
- Blog post outlines before drafting
- Fiction or essay drafts before heavy revision
- Sanity checks on structure and clarity (not line editing)

**Constraints**:
- **Single pass only** (avoid endless tweaking)
- Focus on **patterns and priorities**, not granular line edits

---

## When to Use This Bootstrap

- You have a completed draft or detailed outline
- You want fresh perspective before major revision
- You need to validate structure, clarity, and impact
- You want to identify patterns (not line edits)
- You're close to publication and need final sanity check

---

## Beta Review Workflow

### Phase 1: SETUP & INTENT
**Goal**: Clarify what you want from the beta review so feedback stays focused

**Tasks**:
1. **Choose artifact**:
   - Blog outline: `outline.md`
   - Draft: `draft.md` or `working-draft.md`
   - Fiction: `assembled-draft.md`
2. **Define target audience**:
   - Age range, typical knowledge level
   - Genre or topic preferences
   - What they value (clarity, craft, novelty, emotional hit, etc.)
3. **Define review questions**:
   - "What hits?" (engaging, clear, compelling)
   - "What misses?" (confusing, boring, repetitive, off-tone)
   - "What's missing?" (gaps in logic, stakes, context, payoff)
4. **Set constraints**:
   - What you're NOT asking for (e.g., no copy-edits, no style changes)
   - Specific concerns (pacing, clarity, emotional impact)
   - Time investment (single pass, focused feedback)

**Deliverables**:
- `beta-brief.md` (purpose, audience, review questions, constraints)

**Status Check**: ✅ Complete when intent is documented

---

### Phase 2: AUDIENCE SIMULATION
**Goal**: Simulate a small panel of target readers with different perspectives

**Tasks**:
1. **Define 3-5 reader personas**:
   
   **For blog posts**:
   - "Practitioner Pat" – busy, skims for actionable steps
   - "Curious Casey" – likes context, wants to understand why
   - "Skeptical Sam" – questions assumptions and edge cases
   
   **For fiction**:
   - "Core Fan" – loves the genre and tropes
   - "Voice Lover" – cares most about style and character
   - "Pacing Hawk" – sensitive to slow or confusing sections
   - "Emotional Reader" – needs to feel the story
   - "Logic Checker" – watches for plot holes

2. **For each persona, simulate reading**:
   - Where did you lean in?
   - Where did attention drift?
   - What confused or annoyed you?
   - What would you tell a friend about this piece?
   - What's the one thing that must change?
   - What's the one thing that must stay?

3. **Capture persona responses**:
   - Note section/scene references
   - Flag patterns across personas
   - Identify unique concerns

**Deliverables**:
- Persona feedback notes (can be informal, rolled into synthesis)

**Status Check**: ✅ Complete when all personas have "read" the work

---

### Phase 3: FEEDBACK SYNTHESIS
**Goal**: Collapse persona reactions into clear patterns and priorities

**Tasks**:
1. **Identify converging patterns**:
   - Issues that 60-80% of personas noticed
   - Strengths multiple personas praised
   - Consistent confusion points
   - Repeated emotional responses

2. **Categorize feedback**:
   - **HITS** – keep and maybe emphasize
   - **MISSES** – need fix or cut
   - **MAYBES** – optional improvements

3. **Organize by dimension**:
   - **Concept & promise** (hook, premise, value proposition)
   - **Structure & pacing** (flow, rhythm, scene order)
   - **Clarity & coherence** (logic, transitions, explanations)
   - **Character/voice/tone** (consistency, authenticity)
   - **Emotional impact** (engagement, payoff, satisfaction)

4. **Create priority tiers**:
   - **Must fix**: Breaks reader experience
   - **Should fix**: Significantly improves work
   - **Could fix**: Minor improvements
   - **Won't fix**: Not worth the effort

**Deliverables**:
- `beta-review.md` (synthesized feedback with priorities)

**Status Check**: ✅ Complete when patterns identified and prioritized

---

### Phase 4: REVISION PLAN
**Goal**: Convert beta feedback into actionable revision tasks

**Tasks**:
1. **For each "must fix" issue**:
   - Specific location (section, scene, paragraph)
   - What's wrong (the problem)
   - Why it matters (reader impact)
   - How to fix (concrete action)
   - Estimated effort (quick/moderate/major)

2. **Group related fixes**:
   - Structure changes (reordering, cutting, adding)
   - Clarity improvements (explanations, transitions)
   - Character/voice adjustments
   - Emotional beat enhancements

3. **Create revision sequence**:
   - Structural fixes first (may eliminate other issues)
   - Clarity and content second
   - Voice and polish last

4. **Set acceptance criteria**:
   - How will you know the fix worked?
   - What does success look like?

5. **Get author approval**:
   - Review the plan
   - Adjust priorities if needed
   - Confirm scope

**Deliverables**:
- `revision-plan.md` (from beta feedback, author-approved)

**Status Check**: ✅ Complete when plan is approved

---

## Beta Review Report Template

In `beta-review.md`:

```markdown
# Beta Review: [Title]

**Date**: [Date]  
**Artifact**: [outline.md / draft.md / etc]  
**Target Audience**: [Who this is for]  
**Review Questions**: [What we're looking for]

---

## Executive Summary

**Overall Impression**: [One paragraph synthesis]

**Primary Strength**: [What's working best]

**Primary Concern**: [What needs most attention]

**Recommendation**: [Ready to publish / Needs revision / Needs major work]

---

## What's Working (HITS)

### Concept & Promise
- [Strength 1]
- [Strength 2]

### Structure & Pacing
- [Strength 1]
- [Strength 2]

### Clarity & Coherence
- [Strength 1]
- [Strength 2]

### Voice & Tone
- [Strength 1]
- [Strength 2]

### Emotional Impact
- [Strength 1]
- [Strength 2]

---

## What's Not Working (MISSES)

### Concept & Promise
**Issue**: [Description]  
**Impact**: [How this affects reader]  
**Location**: [Where this occurs]  
**Priority**: MUST / SHOULD / COULD

### Structure & Pacing
**Issue**: [Description]  
**Impact**: [How this affects reader]  
**Location**: [Where this occurs]  
**Priority**: MUST / SHOULD / COULD

### Clarity & Coherence
**Issue**: [Description]  
**Impact**: [How this affects reader]  
**Location**: [Where this occurs]  
**Priority**: MUST / SHOULD / COULD

### Voice & Tone
**Issue**: [Description]  
**Impact**: [How this affects reader]  
**Location**: [Where this occurs]  
**Priority**: MUST / SHOULD / COULD

### Emotional Impact
**Issue**: [Description]  
**Impact**: [How this affects reader]  
**Location**: [Where this occurs]  
**Priority**: MUST / SHOULD / COULD

---

## What's Missing (GAPS)

- [Missing element 1: why it matters]
- [Missing element 2: why it matters]
- [Missing element 3: why it matters]

---

## Persona Breakdown

### [Persona Name]
- **Loved**: [What resonated]
- **Lost interest**: [Where attention drifted]
- **Confused by**: [What wasn't clear]
- **Wanted more**: [What felt lacking]

[Repeat for each persona]

---

## Priority Fixes

### MUST FIX (Breaks reader experience)
1. [Issue] - [Location] - [Fix approach]
2. [Issue] - [Location] - [Fix approach]

### SHOULD FIX (Significantly improves)
1. [Issue] - [Location] - [Fix approach]
2. [Issue] - [Location] - [Fix approach]

### COULD FIX (Minor improvements)
1. [Issue] - [Location] - [Fix approach]
2. [Issue] - [Location] - [Fix approach]

---

## Next Steps

**Recommended**: [Proceed to revision / Need more work / Ready to publish]

**If revising**: Load REVISION-BOOTSTRAP or BLOG-POST-BOOTSTRAP Phase 3+

**Estimated effort**: [X hours/sessions for priority fixes]
```

---

## File Structure

Project folder: `_drafts/[project-name]/`

```
[project-name]/
├── README.md
├── beta-brief.md
├── beta-review.md
├── revision-plan.md (if proceeding to revision)
└── [original artifact being reviewed]
```

---

## Example Sessions

### Beta Review for Blog Post Outline

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/BETA-REVIEW-BOOTSTRAP.md

# Beta Review: How to Build a Story Engine

Artifact: _drafts/story-engine-post/outline.md
Target audience: Fiction writers, productivity enthusiasts
Review for: Structure, clarity, actionability

Run beta review with 4 personas.
```

### Beta Review for Fiction Draft

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/BETA-REVIEW-BOOTSTRAP.md

# Beta Review: The Collector

Artifact: _drafts/the-collector/assembled-draft.md
Target audience: Dark fiction readers
Review for: Pacing, emotional impact, ending

Simulate reader panel and synthesize feedback.
```

---

## Working Principles

- **Single pass**: One focused review, not iterative
- **Patterns over details**: Look for recurring issues
- **Audience-first**: What serves the reader?
- **Actionable**: Every issue needs a concrete fix
- **Honest**: Don't sugarcoat problems
- **Constructive**: Focus on making it better
- **Bounded**: Set time limit, finish the review

---

## Commit Message Standards

- "Initialize beta review: [Title]"
- "Add beta review report: [Title]"
- "Create revision plan from beta feedback: [Title]"

---

## After Beta Review

### If proceeding to revision:

**For blog posts**:
```
Load story-engine/bootstraps/BLOG-POST-BOOTSTRAP.md
Resume at Phase 3: Revision
Use beta-review.md to guide changes
```

**For fiction**:
```
Load story-engine/bootstraps/REVISION-BOOTSTRAP.md
Use beta-review.md as input to revision planning
```

### If ready to publish:
- Proceed to publication workflow
- Archive beta review for reference

### If needs major work:
- Consider whether to continue or table
- Document decision and reasoning

---

**Bootstrap Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
