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

3. **Optional: Scene-Level Analysis**
   
   **Reference**: `story-engine/bootstraps/SCENE-WORKFLOW.md` for atomic scene structure
   
   For stories with multiple distinct scenes (typically 1,000+ words), consider analyzing at scene level:
   
   **For each scene**:
   - Identify if Scene (Goal-Conflict-Disaster) or Sequel (Reaction-Dilemma-Decision)
   - Check structure integrity:
     - Scene: Is Goal clear? Conflict genuine? Disaster a real setback?
     - Sequel: Is Reaction authentic? Dilemma presents real choice? Decision specific?
   - Assess scene purpose:
     - Advances plot?
     - Develops character?
     - Both?
     - Neither? (problem)
   - Note scene issues:
     - Weak goal
     - Insufficient conflict
     - Easy disaster (not setback)
     - Vague decision
     - Doesn't connect to adjacent scenes
   
   **Scene-level analysis benefits**:
   - Identifies specific weak scenes (not just "pacing issue")
   - Reveals scene chain breaks (disaster doesn't lead to reaction, etc.)
   - Pinpoints structural problems precisely
   - Makes revision plan more surgical
   
   **Deliverable**: `scene-analysis.md` (optional, if using scene-level approach)

4. **Create revision categories**:
   - **Structure**: Scene order, pacing, arc
   - **Character**: Motivation, consistency, development
   - **Plot**: Logic, causality, stakes
   - **Prose**: Sentence-level, word choice, rhythm
   - **Voice**: Tone, POV, style consistency
   - **Technical**: Grammar, punctuation, format

5. **Archive original**:
   - Save frozen copy to `original-[filename].md`
   - Never edit the original during revision
   - Preserve publication history

6. **Create project README**:
   - Document current state
   - Track revision goals
   - Note workflow history

**Deliverables**:
- `README.md` (project overview)
- `dossier.md` (comprehensive analysis)
- `critique.md` (literary evaluation)
- `scene-analysis.md` (optional, if using scene-level approach)
- `original-[filename].md` (frozen copy)

**Status Check**: ✅ Complete when analysis is documented

---

### Phase 2: PLANNING
**Goal**: Develop approved revision strategy with surgical precision

**Tasks**:

1. **Review analysis with author**:
   - Discuss dossier findings
   - Validate critique observations
   - If scene-level analysis exists, review scene-by-scene notes
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
   - **If scene-level analysis exists**: Target specific scenes identified as weak

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

5. **Optional: Scene-Level Revision Plan**
   
   **Reference**: `story-engine/bootstraps/SCENE-WORKFLOW.md`
   
   If scene-level analysis revealed specific scene problems, plan scene-level rewrites:
   
   **For each problematic scene**:
   - Create or update scene brief:
     - If Scene: Define clear Goal, genuine Conflict, real Disaster
     - If Sequel: Define authentic Reaction, difficult Dilemma, specific Decision
   - Choose authorship approach:
     - [ ] Human Rewrite (author rewrites scene)
     - [ ] AI Assisted (AI suggests rewrite, author edits)
   - Specify scene-level changes:
     - Strengthen goal
     - Heighten conflict
     - Sharpen disaster
     - Clarify decision
   - Note integration concerns:
     - How does revised scene connect to unchanged scenes?
     - What transitions need adjustment?
   
   **Scene-level revision benefits**:
   - More precise than "fix pacing in middle"
   - Can rewrite specific scenes while preserving others
   - Maintains scene chain integrity
   - Surgical rather than broad-stroke

6. **Create revision sequence**:
   - Work through story chronologically OR
   - Address by revision type OR
   - Tackle high-impact items first OR
   - Rewrite problem scenes first, then integrate
   - Document chosen approach and why

7. **Estimate scope**:
   - Time per revision
   - Total sessions needed
   - Potential complications
   - Decision points

8. **GET AUTHOR APPROVAL**:
   - Review complete plan
   - Adjust priorities
   - Confirm approach
   - Set scope boundaries

9. **Save plan to GitHub**

**Deliverables**:
- `revision-plan.md` (detailed, author-approved)
- `scene-briefs.md` (optional, if using scene-level rewrites)

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

   **For scene-level rewrites** (if using scene-level approach):
   
   **Reference**: Scene Drafting Protocol from `SCENE-WORKFLOW.md`
   
   - Work scene by scene on identified problem scenes:
     1. Review original scene and scene brief
     2. Confirm Goal/Conflict/Disaster or Reaction/Dilemma/Decision structure
     3. Execute rewrite per authorship choice:
        
        **If Human Rewrite**:
        - Author rewrites scene from brief
        - Hit structural beats (Goal/Conflict/Disaster or Reaction/Dilemma/Decision)
        - Maintain voice consistency with unchanged scenes
        - AI reviews: structure, voice match, integration
        
        **If AI Assisted**:
        - AI drafts revised scene from brief
        - AI maintains voice and structure
        - Author edits for authenticity and voice match
     
     4. Scene-level review:
        - [ ] Scene now fulfills brief?
        - [ ] Structure clear and effective?
        - [ ] Connects to adjacent (unchanged) scenes?
        - [ ] Voice matches rest of story?
        - [ ] Improves on original?
     
     5. Integrate revised scene:
        - Replace original scene in working draft
        - Check transitions with unchanged scenes
        - Adjust connections if needed
     
     6. Update scene tracker (if using):
        - Mark scene as revised
        - Note actual changes made
   
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
   - **If using scene-level rewrites**: Ensure revised scenes integrate seamlessly with unchanged scenes

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
   - Verify voice consistency (especially for scene-level rewrites)
   - Test transitions
   - Ensure changes don't create new problems

**Deliverables**:
- `working-[filename].md` (revised draft)
- `revision-notes.md` (decision log with save points)
- `scene-tracker.md` (optional, if using scene-level rewrites)
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
   - **If scene-level rewrites used**: Do revised scenes integrate seamlessly with unchanged scenes?

3. **Verify revision goals met**:
   - Review original critique
   - Check: did you fix the problems?
   - Check: did fixes create new problems?
   - Check: is story stronger now?
   - **If scene-level analysis used**: Re-check problem scenes—are they fixed?

4. **Integration fixes**:
   - Smooth any rough transitions (especially between revised and unchanged scenes)
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
   - Scene briefs if used

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
├── scene-analysis.md (optional)
├── scene-briefs.md (optional, if scene-level rewrites)
├── scene-tracker.md (optional, if scene-level rewrites)
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

### Starting Revision with Scene-Level Analysis

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/REVISION-BOOTSTRAP.md
Load story-engine/bootstraps/SCENE-WORKFLOW.md

# Revising: The Collector

Original: _posts/2024-10-15-the-collector.md
No prior assessment.

Begin Phase 1 with scene-level analysis.
Break story into atomic scenes and analyze each.
```

### Scene-Level Rewrite Session

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/REVISION-BOOTSTRAP.md
Load story-engine/bootstraps/SCENE-WORKFLOW.md

# Revising: The Collector - Rewrite Scene 3

Project: _drafts/the-collector/
Load scene-briefs.md and revision-plan.md
Rewrite Scene 3 (weak goal identified in analysis).
Use Human Rewrite approach.
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
**Scene-Level Approach**: Yes / No

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

Working approach: [Chronological / By type / High-impact first / Scene rewrites first]

Estimated sessions: [X]

---

## SCENE-LEVEL REWRITES (if using)

### Scene 3: [Scene Name]
**Type**: Scene (Goal-Conflict-Disaster)  
**Current Problem**: [Weak goal, insufficient conflict, etc.]  
**Solution**: [Rewrite with clearer goal, stronger conflict, etc.]  
**Authorship**: Human Rewrite / AI Assisted  
**Priority**: MUST  
**Impact**: [Word count, integration concerns]

### Scene 7: [Scene Name]
**Type**: Sequel (Reaction-Dilemma-Decision)  
**Current Problem**: [Vague decision, missing dilemma, etc.]  
**Solution**: [Rewrite with difficult dilemma, specific decision]  
**Authorship**: Human Rewrite / AI Assisted  
**Priority**: SHOULD  
**Impact**: [Word count, integration concerns]

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

**Total Scene Rewrites**: [X scenes] (if using scene-level approach)  
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
**Scenes Revised**: [X of Y] (if using scene-level approach)  
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

[Optional: specific scene-level changes if noteworthy]

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
- **Surgical precision**: Targeted improvements (scene-level when appropriate)
- **Author approval**: Required for plan
- **Document everything**: Log all decisions
- **Commit frequently**: Save progress regularly
- **Protect strengths**: Don't fix what works
- **Test changes**: Verify improvements improve
- **Stay focused**: Follow the plan
- **Scene integrity**: If rewriting scenes, maintain chain connections
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
- Scene rewrites break scene chain

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
- "Add scene-level analysis for [Story Name]" (if using)
- "Archive original: [Story Name]"

**Planning phase**:
- "Add revision plan for [Story Name]"
- "Create scene briefs for [Story Name] revision" (if using scene-level)
- "Update revision plan with author feedback"

**Execution phase**:
- "Revise [Story Name]: [Scene/Section] - [specific change]"
- "Rewrite [Story Name]: Scene [X] - [scene name]" (if scene-level rewrite)
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
- [ ] Goals and conflicts present (if Scene)
- [ ] Reactions and decisions clear (if Sequel)
- [ ] Scene chain intact (no breaks)
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

## Version History

**v2.1** - December 24, 2025
- Added optional scene-level analysis in Phase 1
- Added optional scene-level revision planning in Phase 2
- Added scene-level rewrite protocol in Phase 3
- Integrated SCENE-WORKFLOW.md for atomic scene rewrites
- Added scene briefs and tracker to file structure (optional)
- Updated examples with scene-level revision sessions

**v2.0** - December 23, 2025  
Major revision with comprehensive workflow

---

**Bootstrap Version**: 2.1  
**Author**: Doug Langille  
**Repository**: github.com/douglangille/Workbench