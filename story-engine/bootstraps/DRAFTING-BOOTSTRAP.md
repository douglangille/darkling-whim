<!--
STORY ENGINE: DRAFTING BOOTSTRAP

PURPOSE:
Build complete stories from brain dumps, fragments, or partial drafts.
Take raw material and create structured, finished work.

USE WHEN:
- Have notes/ideas that need structure
- Partial draft needs completion
- Want to reboot existing story with fresh approach
- Have scenes but need connective tissue

SESSION STARTUP:
  Connect to Workbench.
  Load story-engine/bootstraps/DRAFTING-BOOTSTRAP.md
  
  # Draft: [Working Title]
  Source material: [description or file location]
  Target scope: [Flash / Short Story / Novella]
  Initialize drafting project.

OUTPUT:
- Story outline/structure
- Complete draft
- Documentation of decisions
-->

# Drafting Bootstrap

## Role

You are building a complete story from raw material - notes, fragments, partial drafts, or concepts.

## Working Principles

- **Structure first**: Understand the whole before writing parts
- **Voice discovery**: Find and maintain the right narrative voice
- **Complete the circle**: Every setup gets payoff
- **Pacing matters**: Rhythm appropriate to scope
- **Scene purpose**: Every scene earns its place
- **Author collaboration**: Check in on major structural decisions

## File Structure

```
_drafts/[story-name]-draft/
├── README.md (project overview)
├── source-material.md (raw input preserved)
├── story-outline.md (structure plan)
├── character-notes.md (character development)
├── world-notes.md (world-building details)
├── scene-outlines/ (individual scene plans)
├── working-draft.md (the growing story)
└── drafting-notes.md (session log, decisions)
```

## Workflow Phases

### Phase 1: MATERIAL REVIEW

**Goal:** Understand what you have to work with

**Tasks:**
1. Load/receive source material:
   - Brain dumps
   - Scene fragments
   - Character notes
   - Partial drafts
   - Concept descriptions
2. Identify what exists:
   - **Complete elements**: What's finished?
   - **Partial elements**: What's started?
   - **Implied elements**: What's hinted at?
   - **Missing elements**: What's needed?
3. Extract core components:
   - **Premise**: What's the story about?
   - **Characters**: Who exists and who's needed?
   - **Conflict**: What's at stake?
   - **Setting**: Where/when does it happen?
   - **Voice**: What tone/style is emerging?
4. Confirm target scope with author
5. Archive source material

**Deliverables:**
- Project README
- `source-material.md` (preserved)
- Material analysis document

**Status Check:** ✅ Ready when you understand the raw material

---

### Phase 2: OUTLINE & STRUCTURE

**Goal:** Create complete story architecture

**Tasks:**
1. Develop story structure appropriate to scope:
   - **Flash (500-1,000)**: Single scene or moment
   - **Short Story (3,000-7,500)**: 3-5 scenes
   - **Novella (15,000-40,000)**: Multi-chapter/act structure
2. Map story arc:
   - Opening: Hook and setup
   - Development: Escalation and complication
   - Climax: Crisis point
   - Resolution: Consequence and closure
3. Develop characters:
   - Protagonist goals and obstacles
   - Supporting cast roles
   - Character arcs (if scope allows)
4. Build world as needed:
   - Setting details
   - Rules (if speculative)
   - Atmosphere
5. Plan scene sequence:
   - Purpose of each scene
   - POV for each scene
   - Key beats/moments
   - Transitions between scenes
6. **GET AUTHOR APPROVAL** on structure

**Deliverables:**
- `story-outline.md` (complete structure)
- `character-notes.md`
- `world-notes.md` (if needed)
- Scene outlines in `scene-outlines/`

**Status Check:** ✅ Complete when structure approved

---

### Phase 3: SCENE DRAFTING

**Goal:** Write the complete story scene by scene

**Approach:** Work sequentially or by section

**For each scene:**
1. Review scene outline and purpose
2. Incorporate any existing material (fragments, notes)
3. Write complete scene:
   - Strong opening
   - Clear purpose/beats
   - Vivid details
   - Natural dialogue (if present)
   - Smooth close/transition
4. Maintain voice consistency
5. Check pacing within scene
6. Document decisions
7. Commit to GitHub after each scene
8. Create save points

**Guidelines:**
- Show don't tell (when appropriate to scope)
- Sensory details for immersion
- Dialogue reveals character
- Every paragraph earns its place
- Maintain momentum
- Trust the reader

**Deliverables:**
- `working-draft.md` (growing scene by scene)
- `drafting-notes.md` (decision log)
- Regular commits

**Status Check:** ✅ Complete when all scenes drafted

---

### Phase 4: ASSEMBLY & POLISH

**Goal:** Ensure complete story works as whole

**Tasks:**
1. Read complete draft
2. Check story arc:
   - Setup pays off?
   - Escalation feels earned?
   - Climax satisfying?
   - Resolution complete?
3. Verify character consistency:
   - Voices distinct?
   - Behavior consistent?
   - Arcs complete (if present)?
4. Check world consistency:
   - Details align?
   - Rules followed?
5. Assess pacing:
   - Rhythm appropriate to scope?
   - No sagging middle?
   - Satisfying momentum?
6. Polish prose:
   - Tighten weak passages
   - Strengthen dialogue
   - Vivify descriptions
   - Cut excess
7. **Author review**

**Deliverables:**
- Polished complete draft
- Final drafting notes

**Status Check:** ✅ Complete when author satisfied

---

### Phase 5: FINALIZATION

**Goal:** Prepare for publication

**Tasks:**
1. Final polish pass
2. Format for publication:
   - Add frontmatter metadata
   - Apply any special formatting
3. Compose author's note (if appropriate):
   - Context for the story
   - Any relevant background
4. Move to `_posts/` or keep in `_drafts/` for further work
5. Archive drafting materials

**Deliverables:**
- Publication-ready story
- Archived drafting process

---

## Session Initialization

### For New Drafting Project:

```
# Draft: [Working Title]
Source: [Brain dump / Attached file / Fragments in _drafts/]
Target scope: Short Story (~5,000 words)
Initialize drafting project.
```

### For Continuing Work:

```
# Draft: [Working Title]
Load _drafts/[story-name]-draft/ and report status.
Resume from last save point.
```

## Commit Standards

**Planning:**
- "Initialize drafting project: [Working Title]"
- "Add story outline for [Working Title]"
- "Complete character and world notes for [Working Title]"

**Execution:**
- "Draft [Working Title]: [scene name/number]"
- "Add scene: [brief description]"

**Finalization:**
- "Complete draft of [Working Title] ([word count] words)"
- "Finalize [Working Title] for publication"

## Save Point Format

```markdown
## Save Point: [Date/Time]

**Phase**: [Current phase]
**Progress**: [X of Y scenes complete]
**Current Word Count**: [X words] (Target: [Y words])
**Last Completed**: [Scene name/number]
**Next Steps**: [What scene comes next]
**Open Questions**: [Any story issues to resolve]
**Commits Made**: [List]

**To Resume**: Draft [next scene name]
```
