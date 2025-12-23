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
3. Plan scenes:
   - Scene list with purpose
   - Estimated length per scene
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
- `outline.md` (scene-by-scene plan, author-approved)

**Status Check**: ✅ Complete when outline is approved

---

### Phase 3: SCENE BUILDING
**Goal**: Draft scenes one by one

**Tasks**:
1. Draft scenes in order (or key scenes first, author's choice)
2. For each scene:
   - Establish POV and voice
   - Set scene clearly (where/when)
   - Drive conflict forward
   - Reveal character
   - Advance plot
   - Maintain tone
3. Don't self-edit too much:
   - Get words down
   - Maintain momentum
   - Mark problem areas with [NOTES]
   - Keep moving forward
4. Track progress:
   - Scenes completed
   - Current word count
   - Pacing check
5. Document in drafting-notes.md:
   - Scene completion status
   - Problems encountered
   - Solutions found
   - Deviations from outline
   - New ideas that emerged
6. Commit frequently to GitHub
7. Create save points after each scene

**Working Method**:
- One scene per session (or per day)
- Author can provide feedback on scenes
- Adjust outline if story evolves
- Focus on completion, not perfection

**Deliverables**:
- `working-draft.md` (complete first draft)
- `drafting-notes.md` (process log)

**Status Check**: ✅ Complete when all scenes drafted

---

### Phase 4: ASSEMBLY
**Goal**: Weave scenes into cohesive story

**Tasks**:
1. Read through complete draft
2. Check for:
   - Plot holes
   - Character consistency
   - Pacing issues
   - Tonal shifts
   - Missing transitions
   - Continuity errors
3. Address major structural issues:
   - Reorder scenes if needed
   - Add missing scenes
   - Cut redundant material
   - Strengthen connections
4. Ensure:
   - Story arc completes
   - Character arcs resolve
   - Themes emerge clearly
   - Ending satisfies
5. Update drafting notes with assembly decisions
6. Save assembled draft

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

- **Finish the draft**: Completion beats perfection
- **Stay in voice**: Establish and maintain consistent voice
- **Show, don't tell**: Let readers experience the story
- **Every scene must**: advance plot OR develop character OR both
- **Trust the process**: First draft is discovery
- **Embrace mess**: You can fix it in revision
- **Keep momentum**: Don't get stuck perfecting early scenes

---

## File Structure

Project folder: `_drafts/[story-name]-draft/`

```
[story-name]-draft/
├── README.md
├── foundation.md
├── source-material.md
├── outline.md
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

### Starting from Concept

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# New Story: What Remains

Concept: _drafts/what-remains-concept/concept.md
Target scope: Novelette (12,000 words)

Begin outlining.
```

### Continuing Existing Draft

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# Drafting: The Collector

Load artifacts: _drafts/the-collector-draft/
Report status and resume from last save point.
```

### Rebooting Existing Story

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/DRAFTING-BOOTSTRAP.md

# Reboot: Mitzy and the Butterfly

Original for reference: _posts/2015-08-21-mitzy-and-the-butterfly.md
Assessment: _drafts/mitzy-assessment/assessment.md
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

### Scene 1: [Title/Summary]
**Purpose**: Hook reader, establish normal world
**POV**: [Character]
**Setting**: [Where/when]
**Key Events**: 
- [Event 1]
- [Event 2]
**Character Reveal**: [What we learn]
**Estimated Length**: [X words]

### Scene 2: Inciting Incident
**Purpose**: Disrupt status quo
**POV**: [Character]
**Setting**: [Where/when]
**Key Events**:
- [Event 1]
- [Event 2]
**Conflict Introduced**: [What's at stake?]
**Estimated Length**: [X words]

[Continue for all Act I scenes]

---

## Act II: Confrontation (~50% / X words)

[Scene breakdown continuing...]

---

## Act III: Resolution (~25% / X words)

[Scene breakdown continuing...]

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

```

---

## Commit Message Standards

**Foundation phase**:
- "Initialize [Story Name] draft project"
- "Document story foundation for [Story Name]"

**Outline phase**:
- "Add story outline for [Story Name]"
- "Update outline with author feedback"

**Drafting phase**:
- "Draft [Story Name]: Scene [X] - [scene name]"
- "Update drafting notes: [progress summary]"

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
**Progress**: [X of Y scenes complete]
**Current Word Count**: [X words / Y target]
**Last Completed**: [What scene/section]
**Next Steps**: [What to draft next]
**Problems Encountered**: [Any issues]
**Story Evolution**: [How it's changing from outline]
**Session Duration**: [Approximate time]
**Commits Made**: [List of commits]

**To Resume**: [Specific instruction for next session]
```

---

## Drafting Tips

- **Write badly first**: Get words down, fix later
- **Use placeholders**: [DESCRIPTION] or [NAME] if stuck
- **Mark trouble spots**: [NOTE: This feels weak] and move on
- **Follow energy**: If a scene excites you, write it out of order
- **Trust emergence**: Stories reveal themselves in the writing
- **Don't look back**: Resist urge to re-read and polish early scenes
- **Celebrate progress**: Each scene completed is victory

---

**Bootstrap Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
