# DRAFTING Bootstrap

**Purpose**: Build complete story from brain dump, partial draft, concept, or rebooted idea.

---

## When to Use This Bootstrap

- Starting from scratch with a concept
- Have notes/brain dump that needs structure
- Partial draft that needs completion
- Rebooting existing story with fresh approach
- IDEATION-BOOTSTRAP produced a solid concept

---

## Drafting Workflow

### Phase 1: FOUNDATION
**Goal**: Understand what you're building

**Tasks**:
1. Gather source material:
   - Concept from IDEATION-BOOTSTRAP
   - Brain dump notes
   - Partial draft
   - Reference story (if reboot)
2. Clarify story elements:
   - **Premise**: What's the core idea?
   - **Protagonist**: Who is this about?
   - **Conflict**: What's at stake?
   - **Setting**: Where/when does this happen?
   - **Tone**: What's the emotional flavor?
   - **Scope**: Target length (flash/short/novelette/etc)
3. Define target:
   - Word count goal
   - Intended audience
   - Publication venue (if known)
4. Create project structure
5. Save foundation document

**Deliverables**:
- `README.md` (project overview)
- `foundation.md` (story elements and targets)
- `source-material.md` (brain dump, notes, references)

**Status Check**: ✅ Complete when foundation documented

---

### Phase 2: OUTLINE
**Goal**: Create structural blueprint

**Tasks**:
1. Choose story structure:
   - Three-act (classic)
   - Hero's journey
   - In medias res
   - Frame narrative
   - Vignette collection
   - Other experimental structure
2. Map key story beats:
   - Opening hook
   - Inciting incident
   - Rising action points
   - Midpoint
   - Crisis
   - Climax
   - Resolution
3. Plan high-level scenes:
   - Major beats and turning points
   - Estimated scene count
   - POV for each scene
   - Key conflicts
   - Character development moments
4. Consider pacing:
   - Action vs. reflection balance
   - Tension escalation
   - Breathing room
5. **GET AUTHOR APPROVAL**
6. Save outline to GitHub

**Deliverables**:
- `outline.md` (beat-level plan, author-approved)

**Status Check**: ✅ Complete when outline is approved

---

### Phase 2.5: SCENE BRIEF DEVELOPMENT
**Goal**: Plan all scenes at atomic level before drafting any prose

**Scope Decision**:
- **Flash Fiction (< 1,000 words)**: Scene briefs optional—skip to Phase 3
- **1,000+ words**: Scene briefs recommended—proceed with this phase

**Reference**: Load and review `story-engine/bootstraps/SCENE-WORKFLOW.md` for complete scene brief protocol

**Tasks**:
1. **Break structure into atomic scenes**:
   - Convert each beat/turning point into one or more Scenes/Sequels
   - Scene = Goal-Conflict-Disaster (proactive)
   - Sequel = Reaction-Dilemma-Decision (reactive)
   - Number sequentially from story start

2. **Create scene brief for each scene**:
   - Use Scene Brief Template from SCENE-WORKFLOW.md
   - Define Goal/Conflict/Disaster OR Reaction/Dilemma/Decision
   - Specify POV, setting, connections
   - Estimate word count per scene
   - Note key story elements (character development, plot advancement, theme)

3. **Validate scene chain integrity**:
   - Check: Each Scene disaster connects to next Sequel reaction
   - Check: Each Sequel decision creates Goal for next Scene
   - Check: No orphaned scenes (all connect to chain)
   - Check: Escalating tension throughout
   - Adjust briefs as needed

4. **Make authorship decisions**:
   - For each scene, decide:
     - [ ] Human First Draft (author writes, AI reviews)
     - [ ] AI First Draft (AI writes, author edits)
     - [ ] TBD (decide later)
   - Mark in each scene brief

5. **Create scene tracker**:
   - Use Scene Tracker Template from SCENE-WORKFLOW.md
   - List all scenes with status, authorship, target words
   - Track progress through drafting

6. **GET AUTHOR APPROVAL**:
   - Review complete scene brief list
   - Confirm scene chain makes sense
   - Approve authorship decisions
   - Commit to GitHub before drafting

**DO NOT DRAFT PROSE YET**—all scene briefs must be complete and validated first

**Deliverables**:
- `scene-briefs.md` (complete scene/sequel brief list) OR
- `scenes/` folder (individual scene brief files: `scene-01.md`, `scene-02.md`, etc.)
- `scene-tracker.md` (progress tracking table)

**Status Check**: 
- ✅ Complete when all scene briefs created
- ✅ Scene chain validated
- ✅ Authorship decisions made
- ✅ Author approved

---

### Phase 3: SCENE DRAFTING
**Goal**: Draft prose for each scene using chosen authorship approach

**Reference**: Use Scene Drafting Protocol from `SCENE-WORKFLOW.md`

**Tasks**:
1. **Work scene by scene** (in sequence or strategic order—author's choice):
   - Review scene brief before drafting
   - Confirm Goal/Conflict/Disaster or Reaction/Dilemma/Decision structure
   - Check connections to previous and next scenes

2. **Execute drafting per scene's authorship choice**:

   **If Human First Draft**:
   - Author writes the scene prose
   - Focus on hitting structural beats from brief
   - Don't self-edit excessively—maintain momentum
   - AI reviews for: structure integrity, pacing, voice consistency
   - AI suggests improvements (author decides whether to apply)

   **If AI First Draft**:
   - AI drafts scene prose from brief
   - AI hits structural beats, maintains voice
   - Author reviews for: authenticity, character truth, emotional accuracy
   - Author edits/rewrites as needed
   - Iterate until scene works

3. **Scene-level review after each draft**:
   - **Structure Check**:
     - [ ] Scene fulfills the brief?
     - [ ] Goal/Conflict/Disaster clear? (if Scene)
     - [ ] Reaction/Dilemma/Decision clear? (if Sequel)
     - [ ] Connects to previous scene?
     - [ ] Sets up next scene?
   - **Craft Check**:
     - [ ] Voice consistent with story/character
     - [ ] Pacing appropriate
     - [ ] Show vs. tell balance
     - [ ] Sensory details present
   - **Continuity Check**:
     - [ ] Character knowledge consistent
     - [ ] Setting details match previous scenes
     - [ ] Timeline coherent

4. **Update tracking**:
   - Mark scene status in scene tracker (Brief → Drafted → Reviewed)
   - Note actual word count
   - Flag any issues for later revision
   - Update drafting notes

5. **Commit to GitHub**:
   - Save scene draft with clear naming
   - Commit message: "Draft [Story Name]: Scene [X] - [scene title]"
   - Create save points frequently

6. **Proceed to next scene**:
   - Don't revise entire story yet
   - Trust the scene brief chain
   - Maintain drafting momentum

**Working Principles**:
- One scene at a time—complete before moving on
- Hit the structural beats from brief
- Mark trouble spots with [NOTE] and continue
- Scene briefs can be adjusted if story evolves
- Completion beats perfection in first draft

**Deliverables**:
- Individual scene draft files OR
- `working-draft.md` (all scenes assembled incrementally)
- `drafting-notes.md` (process log with scene-by-scene notes)

**Status Check**: ✅ Complete when all scenes drafted and reviewed

---

### Phase 4: ASSEMBLY
**Goal**: Weave scenes into cohesive story

**Tasks**:
1. Assemble all scene drafts into single document (if not already)
2. Read through complete draft
3. Check for:
   - Plot holes
   - Character consistency
   - Pacing issues
   - Tonal shifts
   - Missing transitions
   - Continuity errors
4. Address major structural issues:
   - Reorder scenes if needed
   - Add missing scenes (create brief → draft → integrate)
   - Cut redundant material
   - Strengthen connections between scenes
5. Ensure:
   - Story arc completes
   - Character arcs resolve
   - Themes emerge clearly
   - Ending satisfies
6. Update drafting notes with assembly decisions
7. Save assembled draft

**Deliverables**:
- `assembled-draft.md` (structurally sound version)

**Status Check**: ✅ Complete when structure is solid

---

### Phase 5: POLISH
**Goal**: Refine prose and prepare for publication

**Tasks**:
1. Line-level revision:
   - Tighten prose
   - Strengthen voice
   - Enhance descriptions
   - Sharpen dialogue
   - Cut unnecessary words
2. Technical polish:
   - Grammar and punctuation
   - Consistency checks
   - Format for publication
3. Final read-through:
   - Does it work as a whole?
   - Is the voice consistent?
   - Does pacing feel right?
   - Would you want to read this?
4. Prepare metadata:
   - Title (final)
   - Tags/categories
   - Publication date
   - Content warnings if needed
5. Format for publication platform

**Deliverables**:
- Publication-ready story in `_posts/`
- Complete drafting archive in `_drafts/`

**Status Check**: ✅ Complete when story is published

---

## Working Principles

- **Plan completely, then draft**: All scene briefs before any prose
- **Finish the draft**: Completion beats perfection
- **Stay in voice**: Establish and maintain consistent voice
- **Show, don't tell**: Let readers experience the story
- **Every scene must**: advance plot OR develop character OR both
- **Trust the process**: First draft is discovery
- **Embrace mess**: You can fix it in revision
- **Keep momentum**: Don't get stuck perfecting early scenes
- **Flex authorship**: Use human/AI strengths per scene

---

## File Structure

Project folder: `_drafts/[story-name]/`

```
[story-name]/
├── README.md
├── foundation.md
├── source-material.md
├── outline.md
├── scene-briefs.md (or scenes/ folder)
├── scene-tracker.md
├── drafting-notes.md
├── working-draft.md
├── assembled-draft.md
└── [optional character/world notes]
```

---

## Example Sessions

### Starting from Brain Dump

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# New Story: The Collector

Attached: brain dump notes about character who collects lost memories
Target scope: Short story (4,000 words)
Target tone: Dark, bittersweet

Begin foundation and outline development.
```

### Scene Brief Phase

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/DRAFTING-BOOTSTRAP.md
Load story-engine/bootstraps/SCENE-WORKFLOW.md

# Drafting: The Collector - Scene Brief Development

Project: _drafts/the-collector/
Load outline.md and break into atomic scene briefs.
Target: ~8 scenes for 4,000 words.
```

### Scene Drafting Phase

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# Drafting: The Collector - Scene 3

Project: _drafts/the-collector/
Load scene-briefs.md and scene-tracker.md
Draft Scene 3 using [Human/AI] first draft approach.
```

### Continuing Existing Draft

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# Drafting: The Collector

Load artifacts: _drafts/the-collector/
Report status and resume from last save point.
```

### Rebooting Existing Story

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# Reboot: Mitzy and the Butterfly

Original for reference: _posts/2015-08-21-mitzy-and-the-butterfly.md
Assessment: _drafts/mitzy/assessment.md
Approach: Fresh draft preserving core concept
Target scope: Short story (4,000 words)

Begin foundation using assessment insights.
```

---

## Foundation Template

In `foundation.md`:

```markdown
# Story Foundation: [Title]

## Source Material
[Brain dump / concept / partial draft / reference story]

## Story Elements

### Premise
[One-sentence story idea]

### Protagonist
- **Name**: [Name]
- **Want**: [External goal]
- **Need**: [Internal need/growth]
- **Flaw**: [Character weakness]

### Conflict
- **External**: [Plot-level conflict]
- **Internal**: [Character-level conflict]
- **Stakes**: [What happens if protagonist fails?]

### Setting
- **Where**: [Location]
- **When**: [Time period]
- **World Rules**: [If speculative]

### Tone
- [Emotional flavor: dark/hopeful/comedic/etc]
- [Reference works with similar tone]

### Theme
- [What is this story really about?]

## Target

### Scope
- **Length**: [Flash/Short/Novelette/etc]
- **Word Count**: [Target]
- **Estimated Scenes**: [X]

### Audience
- **Who will read this**: [Target audience]
- **Publication**: [Venue if known]

### Unique Elements
- [What makes this story special/different?]

## Voice Notes
- [POV: First/Third/etc]
- [Tense: Past/Present]
- [Style notes]
- [Voice characteristics to establish]
```

---

## Outline Template

In `outline.md`:

```markdown
# Story Outline: [Title]

**Structure**: [Three-act / Hero's Journey / etc]
**Target Length**: [X,000 words]
**Estimated Scenes**: [Y]

---

## Act I: Setup (~25% / X words)

### Beat 1: Opening Hook
**Purpose**: Hook reader, establish normal world
**Key Events**: 
- [Event 1]
- [Event 2]
**Character Reveal**: [What we learn]
**Will become**: Scene(s) [X]

### Beat 2: Inciting Incident
**Purpose**: Disrupt status quo
**Key Events**:
- [Event 1]
- [Event 2]
**Conflict Introduced**: [What's at stake?]
**Will become**: Scene(s) [Y]

[Continue for all Act I beats]

---

## Act II: Confrontation (~50% / X words)

[Beat breakdown continuing...]

---

## Act III: Resolution (~25% / X words)

[Beat breakdown continuing...]

---

## Story Arc Check

- [ ] Opening hook strong?
- [ ] Inciting incident clear?
- [ ] Rising tension throughout?
- [ ] Midpoint reveals/shifts something?
- [ ] Crisis forces hard choice?
- [ ] Climax satisfying?
- [ ] Resolution addresses theme?
- [ ] Character arc completes?

---

## Next Step

Proceed to Phase 2.5: Scene Brief Development
- Break each beat into atomic Scene/Sequel briefs
- See SCENE-WORKFLOW.md for complete protocol
```

---

## Commit Message Standards

**Foundation phase**:
- "Initialize [Story Name] draft project"
- "Document story foundation for [Story Name]"

**Outline phase**:
- "Add story outline for [Story Name]"
- "Update outline with author feedback"

**Scene brief phase**:
- "Add scene briefs for [Story Name]"
- "Create scene tracker for [Story Name]"

**Drafting phase**:
- "Draft [Story Name]: Scene [X] - [scene title]"
- "Update scene tracker: [progress summary]"

**Assembly phase**:
- "Assemble [Story Name]: structural revision"
- "Fix [Story Name]: [specific issue]"

**Polish phase**:
- "Polish [Story Name]: [specific work]"
- "Finalize [Story Name] for publication"

---

## Save Point Format

In `drafting-notes.md`:

```markdown
## Save Point: [Date/Time]

**Phase**: [Current phase]
**Progress**: 
- Scenes briefed: [X of Y]
- Scenes drafted: [X of Y]
- Current word count: [X words / Y target]
**Last Completed**: [What scene/section]
**Next Steps**: [What to draft next]
**Problems Encountered**: [Any issues]
**Story Evolution**: [How it's changing from plan]
**Session Duration**: [Approximate time]
**Commits Made**: [List of commits]

**To Resume**: [Specific instruction for next session]
```

---

## Drafting Tips

- **Plan all scenes first**: Complete scene briefs before any prose
- **Write badly first**: Get words down, fix later
- **Use placeholders**: [DESCRIPTION] or [NAME] if stuck
- **Mark trouble spots**: [NOTE: This feels weak] and move on
- **Follow brief structure**: Hit Goal-Conflict-Disaster or Reaction-Dilemma-Decision
- **Trust scene chain**: Each scene builds on previous
- **Choose right authorship**: Use human/AI strengths per scene
- **Don't look back**: Resist urge to re-read and polish early scenes
- **Celebrate progress**: Each scene completed is victory

---

## Version History

**v1.1** - December 24, 2025
- Added Phase 2.5: Scene Brief Development
- Integrated SCENE-WORKFLOW.md for atomic scene planning
- Updated Phase 3 with per-scene authorship flexibility
- Added scene-level review protocol
- Updated file structure to include scene briefs and tracker

**v1.0** - December 23, 2025  
Initial DRAFTING-BOOTSTRAP created

---

**Bootstrap Version**: 1.1  
**Author**: Doug Langille  
**Repository**: github.com/douglangille/Workbench