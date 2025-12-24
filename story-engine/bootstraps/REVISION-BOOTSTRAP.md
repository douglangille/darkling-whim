# REVISION Bootstrap

**Purpose**: Polish and refine existing work at its current scope. For expanding scope, use EXPANSION-BOOTSTRAP instead.

---

## When to Use This Bootstrap

- Story is complete at current scope (flash, short, etc.)
- Needs refinement, not expansion
- ASSESSMENT-BOOTSTRAP recommended revision path
- Technical improvements and polish needed
- Voice is strong but execution has issues
- Structure works but scenes need strengthening

---

## Revision Workflow

### Phase 1: ANALYSIS
**Goal**: Understand the story completely before changing anything

**Prerequisites**: 
- Usually done via ASSESSMENT-BOOTSTRAP
- If starting revision directly, complete analysis here

**Tasks**:

1. **Generate story dossier**:
   - **Synopsis**: 2-3 sentence summary
   - **Scene breakdown**: List each scene with purpose
   - **Character analysis**: 
     - Protagonist: want, need, arc
     - Supporting cast: roles and functions
     - Relationships and dynamics
   - **Structure analysis**:
     - Opening hook
     - Inciting incident
     - Rising action beats
     - Climax
     - Resolution
   - **World-building inventory**: Setting details, rules, atmosphere
   - **Theme identification**: What's this story really about?
   - **Voice characteristics**: POV, tense, style elements

2. **Generate literary critique**:
   - **Strengths** (what's working):
     - Strong scenes/moments
     - Effective character beats
     - Compelling prose
     - Atmospheric elements
   - **Weaknesses** (what needs work):
     - Unclear motivations
     - Pacing issues
     - Weak transitions
     - Inconsistent voice
     - Plot holes
     - Character inconsistencies
   - **Technical notes**:
     - POV slips
     - Tense shifts
     - Dialogue issues
     - Description balance

3. **Create revision categories**:
   - **Structure**: Scene order, pacing, arc
   - **Character**: Motivation, consistency, development
   - **Plot**: Logic, causality, stakes
   - **Prose**: Sentence-level, word choice, rhythm
   - **Voice**: Tone, POV, style consistency
   - **Technical**: Grammar, punctuation, format

4. **Archive original**:
   - Save frozen copy to `original-[filename].md`
   - Never edit the original during revision
   - Preserve publication history

5. **Create project README**:
   - Document current state
   - Track revision goals
   - Note workflow history

**Deliverables**:
- `README.md` (project overview)
- `dossier.md` (comprehensive analysis)
- `critique.md` (literary evaluation)
- `original-[filename].md` (frozen copy)

**Status Check**: ✅ Complete when analysis is documented

---

### Phase 2: PLANNING
**Goal**: Develop approved revision strategy with surgical precision

**Tasks**:

1. **Review analysis with author**:
   - Discuss dossier findings
   - Validate critique observations
   - Identify priorities together
   - Clarify revision goals

2. **Prioritize revision targets**:
   - **Must fix**: Breaks story or reader experience
   - **Should fix**: Significantly improves story
   - **Could fix**: Minor improvements
   - **Won't fix**: Working well enough

3. **Develop detailed revision plan**:

   **For each revision target, specify**:
   - **Location**: Exact scene, paragraph, or line reference
   - **Current state**: What's there now
   - **Problem**: Why it needs revision
   - **Solution**: Specific change to make
   - **Rationale**: Why this fix serves the story
   - **Impact**: Word count change (should stay near current)
   - **Ripple effects**: What else might need adjustment

4. **Organize by revision type**:

   **Structural revisions**:
   - Scene reordering
   - Pacing adjustments
   - Arc strengthening
   - Transition improvements

   **Character revisions**:
   - Motivation clarification
   - Consistency fixes
   - Voice strengthening
   - Relationship development

   **Plot revisions**:
   - Logic holes
   - Causality chains
   - Stakes elevation
   - Foreshadowing

   **Prose revisions**:
   - Sentence tightening
   - Word choice
   - Description balance
   - Rhythm improvement

   **Voice revisions**:
   - POV consistency
   - Tense consistency
   - Style uniformity
   - Tone adjustment

   **Technical revisions**:
   - Grammar
   - Punctuation
   - Format
   - Continuity

5. **Create revision sequence**:
   - Work through story chronologically OR
   - Address by revision type OR
   - Tackle high-impact items first
   - Document chosen approach and why

6. **Estimate scope**:
   - Time per revision
   - Total sessions needed
   - Potential complications
   - Decision points

7. **GET AUTHOR APPROVAL**:
   - Review complete plan
   - Adjust priorities
   - Confirm approach
   - Set scope boundaries

8. **Save plan to GitHub**

**Deliverables**:
- `revision-plan.md` (detailed, author-approved)

**Status Check**: ✅ Complete when plan is approved and saved

---

### Phase 3: EXECUTION
**Goal**: Implement approved changes with surgical precision

**Tasks**:

1. **Create working draft**:
   - Copy from original
   - Name: `working-[filename].md`
   - This is your revision canvas

2. **Work through revision plan systematically**:

   **For structural revisions**:
   - Mark scenes to move with [MOVE TO AFTER SCENE X]
   - Cut scenes cleanly, save separately if might reuse
   - Add scene placeholders: [NEW SCENE: Description]
   - Check transitions after each change
   - Verify pacing after structural changes

   **For character revisions**:
   - Track character knowledge/awareness
   - Ensure motivation clarity in each scene
   - Check dialogue voice consistency
   - Strengthen character agency
   - Verify emotional arc progression

   **For plot revisions**:
   - Test causality: does A lead to B?
   - Verify stakes are clear
   - Check setup/payoff pairs
   - Strengthen conflict in each scene
   - Ensure resolution satisfies

   **For prose revisions**:
   - Tighten weak sentences
   - Replace bland verbs
   - Cut unnecessary adverbs
   - Balance show/tell
   - Vary sentence structure
   - Maintain rhythm

   **For voice revisions**:
   - Check POV: everything filtered through character
   - Verify tense consistency
   - Ensure style matches tone
   - Remove out-of-voice moments
   - Strengthen distinctive elements

   **For technical revisions**:
   - Fix grammar/punctuation
   - Correct spelling
   - Standardize formatting
   - Fix continuity errors
   - Check name consistency

3. **Maintain revision discipline**:
   - **Follow the plan**: Don't improvise major changes
   - **Preserve voice**: Maintain authorial style
   - **Stay at scope**: Don't expand, refine
   - **Mark deviations**: If you change approach, note why
   - **Check ripple effects**: Every change affects something else

4. **Document decisions**:
   
   Create `revision-notes.md` with entries like:
   ```
   ## [Date] - [Section/Scene]
   
   **Planned change**: [What plan said to do]
   **Actual change**: [What you did]
   **Rationale**: [Why, if different from plan]
   **Impact**: [Word count, other effects]
   **Complications**: [Issues encountered]
   **Follow-up needed**: [Related fixes]
   ```

5. **Create save points**:
   - After each major section
   - Before attempting risky changes
   - When reaching natural stopping point
   - Include status summary in revision-notes

6. **Commit frequently to GitHub**:
   - After completing each planned revision
   - With descriptive commit messages
   - Preserving work-in-progress

7. **Quality checks during execution**:
   - Re-read revised sections immediately
   - Check against critique: did fix work?
   - Verify voice consistency
   - Test transitions
   - Ensure changes don't create new problems

**Deliverables**:
- `working-[filename].md` (revised draft)
- `revision-notes.md` (decision log with save points)
- Frequent GitHub commits

**Status Check**: ✅ Complete when all planned changes implemented

---

### Phase 4: INTEGRATION
**Goal**: Ensure all revised pieces work together as unified whole

**Tasks**:

1. **Full read-through**:
   - Read entire story start to finish
   - Don't stop to fix, just note issues
   - Experience as reader would
   - Mark rough spots

2. **Check overall coherence**:
   - **Story arc**: Does it build and resolve?
   - **Character arc**: Does protagonist change?
   - **Pacing**: Does rhythm work throughout?
   - **Voice**: Consistent from start to finish?
   - **Tone**: Unified emotional flavor?
   - **Logic**: Everything make sense?

3. **Verify revision goals met**:
   - Review original critique
   - Check: did you fix the problems?
   - Check: did fixes create new problems?
   - Check: is story stronger now?

4. **Integration fixes**:
   - Smooth any rough transitions
   - Fix new inconsistencies
   - Adjust pacing if needed
   - Strengthen weak connections
   - Resolve any contradictions

5. **Comparative read**:
   - Compare key scenes to original
   - Verify improvements are improvements
   - Check that strengths preserved
   - Ensure voice still yours

6. **Final technical pass**:
   - Grammar and punctuation
   - Spelling
   - Formatting
   - Consistency (names, details, timeline)

**Deliverables**:
- `integrated-[filename].md` (cohesive revision)
- Updated revision notes

**Status Check**: ✅ Complete when story works as unified whole

---

### Phase 5: FINALIZATION
**Goal**: Prepare revised story for publication

**Tasks**:

1. **Final polish pass**:
   - Line-by-line read
   - Tighten any remaining weak prose
   - Check opening hook strength
   - Verify ending satisfaction
   - Remove any [NOTES] or placeholders

2. **Author's note composition**:
   - Original publication context
   - What changed and why (high-level, not exhaustive)
   - What you learned through revision
   - Douglas Adams style: self-aware, witty
   - Optional: what stayed the same (what's core)

   **Example tone**:
   ```markdown
   ## Revision Note
   
   This story first appeared in [Publication] in [Date]. I always knew 
   the ending was rushed—written at 2 AM to hit a contest deadline—but 
   didn't realize how much the middle sagged until I read it again five 
   years later. This revision (December 2025) gives the protagonist 
   actual motivations, fixes the logic hole you definitely noticed, and 
   lets the ending breathe.
   
   The darkness remains. Just more focused.
   {: .notice--info}
   ```

3. **Metadata updates**:
   - Add `revised:` date field
   - Keep original `date:` field for publication history
   - Update tags if story focus shifted
   - Add `revision:` tag
   - Note if scope changed slightly

4. **Before/after comparison**:
   - Original word count vs. revised
   - Major changes summary
   - Preserved elements
   - Lessons learned

5. **Prepare for publication**:
   - Format for target platform
   - Verify all formatting correct
   - Check links (if any)
   - Test on publication platform

6. **Replace original or publish new**:
   - **Option A**: Replace original in `_posts/`
     - Preserve revision history in front matter
     - Add revision note
   - **Option B**: Publish as separate "revised edition"
     - Keep original available
     - Link between versions
   - **Author decides which approach**

7. **Archive revision artifacts**:
   - Complete revision history in `_drafts/[story-name]/`
   - All analysis and planning docs
   - Revision notes and decisions
   - Save points preserved

**Deliverables**:
- Published revised story in `_posts/`
- Complete revision archive in `_drafts/[story-name]/`
- Documented lessons learned

**Status Check**: ✅ Complete when story published and archived

---

## File Structure

Project folder: `_drafts/[story-name]/`

```
[story-name]/
├── README.md
├── original-[filename].md
├── dossier.md
├── critique.md
├── revision-plan.md
├── revision-notes.md
├── working-[filename].md
├── integrated-[filename].md
├── save-points/
│   ├── save-20251223-section1.md
│   ├── save-20251223-section2.md
│   └── ...
└── final-[filename].md
```

---

## Example Sessions

### Starting Revision from Assessment

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/REVISION-BOOTSTRAP.md

# Revising: Mitzy and the Butterfly

Assessment exists: _drafts/mitzy/assessment.md
Original: _posts/2015-08-21-mitzy-and-the-butterfly.md

Initialize revision project using assessment as analysis foundation.
```

### Starting Revision Directly (No Assessment)

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/REVISION-BOOTSTRAP.md

# Revising: The Collector

Original: _posts/2024-10-15-the-collector.md
No prior assessment.

Begin with Phase 1: Complete analysis before revision planning.
```

### Continuing Existing Revision

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/REVISION-BOOTSTRAP.md

# Revising: Mitzy and the Butterfly

Load artifacts: _drafts/mitzy/
Report status and resume from last save point.
```

---

## Revision Plan Template

In `revision-plan.md`:

```markdown
# Revision Plan: [Title]

**Original**: [Filename and publication info]  
**Current Word Count**: [X words]  
**Target Word Count**: [Y words] (stay near current)  
**Plan Created**: [Date]  
**Author Approved**: [Date]

---

## Revision Goals

**Primary Goal**: [Main thing to accomplish]

**Secondary Goals**:
- [Goal 2]
- [Goal 3]

**Must Preserve**:
- [Strength 1 to keep]
- [Strength 2 to keep]

---

## Revision Sequence

Working approach: [Chronological / By type / High-impact first]

Estimated sessions: [X]

---

## STRUCTURAL REVISIONS

### Scene 1: [Scene Name]
**Location**: Paragraphs 1-5  
**Current State**: [What's there now]  
**Problem**: [Why it needs work]  
**Solution**: [Specific change]  
**Rationale**: [Why this serves story]  
**Impact**: [Word count, pacing effects]  
**Priority**: MUST / SHOULD / COULD

### Scene 2: [Scene Name]
[Same structure]

---

## CHARACTER REVISIONS

### Protagonist Motivation
**Location**: [Where in story]  
**Current State**: [What's there now]  
**Problem**: [Why it needs work]  
**Solution**: [Specific change]  
**Rationale**: [Why this serves story]  
**Impact**: [Ripple effects]  
**Priority**: MUST / SHOULD / COULD

[Continue for each character revision]

---

## PLOT REVISIONS

### Logic Hole: [Description]
**Location**: [Where in story]  
**Current State**: [The problem]  
**Solution**: [How to fix]  
**Rationale**: [Why necessary]  
**Impact**: [What else changes]  
**Priority**: MUST / SHOULD / COULD

[Continue for each plot revision]

---

## PROSE REVISIONS

### Opening Hook
**Location**: First paragraph  
**Current State**: [Current opening]  
**Problem**: [Why weak]  
**Solution**: [New approach]  
**Rationale**: [Why stronger]  
**Priority**: SHOULD

### Weak Verbs - Section 2
**Location**: Paragraphs 15-20  
**Problem**: Bland verb choice  
**Solution**: Replace with stronger alternatives  
**Priority**: COULD

[Continue for prose items]

---

## VOICE REVISIONS

### POV Slip - Scene 3
**Location**: Paragraph 47  
**Current**: [Breaks POV]  
**Solution**: [Fix to maintain POV]  
**Priority**: MUST

[Continue for voice items]

---

## TECHNICAL REVISIONS

### Continuity Error
**Location**: Scene 5  
**Problem**: [Inconsistency]  
**Solution**: [Correction]  
**Priority**: MUST

[Continue for technical items]

---

## Summary

**Total Must Fix**: [X items]  
**Total Should Fix**: [Y items]  
**Total Could Fix**: [Z items]  

**Estimated Impact**: [Overall word count change]

**Biggest Risk**: [What might go wrong]

**Success Criteria**: [How we'll know revision worked]
```

---

## Revision Notes Template

In `revision-notes.md`:

```markdown
# Revision Notes: [Title]

---

## Session: [Date/Time]

**Phase**: [Current phase]  
**Goal**: [What attempting this session]  
**Time**: [Duration]

### Work Completed
- [Item 1 from plan]
- [Item 2 from plan]

### Changes Made

#### [Section/Scene Name]
**Planned**: [What plan said]  
**Actual**: [What did]  
**Rationale**: [Why, if different]  
**Word Impact**: [+/- X words]  
**Quality Check**: [Did it work?]

### Deviations from Plan
- [Any unplanned changes and why]

### Problems Encountered
- [Issue 1: how resolved]
- [Issue 2: how resolved]

### Follow-Up Needed
- [Related fixes identified]
- [New issues to address]

### Next Session Plan
- [What to tackle next]
- [Any preparation needed]

---

## Save Point: [Date/Time]

**Status**: [X% complete]  
**Last Completed**: [Section/scene]  
**Current Word Count**: [X words]  
**Next Steps**: [Specific instructions]  
**Open Questions**: [Unresolved items]  
**Commits Made**: [List]

**To Resume**: [Exact instruction for next session]

---

[Repeat for each session]
```

---

## Author's Note Templates

### Minimal Note (for minor revisions):
```markdown
## Revision Note

This story originally appeared in [Publication/Date]. This revised 
edition (December 2025) tightens the prose and fixes a few logic 
issues. The core remains unchanged.
{: .notice--info}
```

### Standard Note (for moderate revisions):
```markdown
## Revision Note

This story first appeared in [Publication] in [Year]. This revision 
(December 2025) [specific changes: strengthens the ending / clarifies 
the protagonist's motivation / fixes pacing in the middle section]. 

[Optional: brief reflection on what you learned or why revision mattered]

The heart of the story remains the same.
{: .notice--info}
```

### Detailed Note (for significant revisions):
```markdown
## Revision Note

This story originally appeared in [Publication] in [Year], written 
[context: during a 24-hour challenge / for a themed anthology / etc]. 
This revised edition (December 2025) represents substantial work:

- [Major change 1]
- [Major change 2]
- [Major change 3]

What didn't change: [Core elements preserved]. Those felt right from 
the beginning.

[Optional: What you learned through revision, Douglas Adams style]

Sometimes stories need time to become what they wanted to be.
{: .notice--info}
```

---

## Working Principles

- **Preserve scope**: Refine, don't expand
- **Preserve voice**: Maintain distinctive style  
- **Surgical precision**: Targeted improvements
- **Author approval**: Required for plan
- **Document everything**: Log all decisions
- **Commit frequently**: Save progress regularly
- **Protect strengths**: Don't fix what works
- **Test changes**: Verify improvements improve
- **Stay focused**: Follow the plan
- **Trust the process**: Systematic beats intuitive

---

## Revision Red Flags

**Stop and reconsider if**:
- Word count increasing significantly (might need EXPANSION instead)
- Losing authorial voice
- Creating more problems than solving
- Fighting the story's natural shape
- Revising same section repeatedly
- Scope creeping toward rewrite

**When to switch to different bootstrap**:
- Story wants to be bigger → EXPANSION-BOOTSTRAP
- Story needs complete rebuild → DRAFTING-BOOTSTRAP (reboot)
- Story is actually fine → Table the revision

---

## Commit Message Standards

**Analysis phase**:
- "Initialize revision project: [Story Name]"
- "Create story dossier for [Story Name]"
- "Add literary critique for [Story Name]"
- "Archive original: [Story Name]"

**Planning phase**:
- "Add revision plan for [Story Name]"
- "Update revision plan with author feedback"

**Execution phase**:
- "Revise [Story Name]: [Scene/Section] - [specific change]"
- "Fix [Story Name]: [specific issue]"
- "Polish [Story Name]: [section]"
- "Update revision notes: [session summary]"

**Integration phase**:
- "Integrate revised sections: [Story Name]"
- "Final polish: [Story Name]"

**Finalization phase**:
- "Finalize revised [Story Name] with author's note"
- "Publish revised [Story Name]"
- "Archive [Story Name] revision artifacts"

---

## Quality Checklist

Before declaring revision complete:

**Story Level**:
- [ ] Opening hooks effectively
- [ ] Protagonist's goal clear
- [ ] Stakes evident
- [ ] Conflict drives story
- [ ] Pacing appropriate
- [ ] Climax satisfying
- [ ] Resolution earned
- [ ] Theme emerges naturally

**Character Level**:
- [ ] Motivation clear
- [ ] Actions consistent
- [ ] Voice distinct
- [ ] Arc complete (if arc story)
- [ ] Relationships believable

**Scene Level**:
- [ ] Each scene necessary
- [ ] Goals and conflicts present
- [ ] Transitions smooth
- [ ] Setting clear
- [ ] Pacing varied

**Prose Level**:
- [ ] Sentences varied
- [ ] Strong verb choice
- [ ] Show/tell balanced
- [ ] Rhythm works
- [ ] No awkward phrasing

**Technical Level**:
- [ ] Grammar correct
- [ ] Punctuation correct
- [ ] Spelling correct
- [ ] Formatting consistent
- [ ] Continuity accurate

**Voice Level**:
- [ ] POV consistent
- [ ] Tense consistent
- [ ] Style unified
- [ ] Tone appropriate
- [ ] Sounds like you

---

**Bootstrap Version**: 2.0  
**Updated**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
