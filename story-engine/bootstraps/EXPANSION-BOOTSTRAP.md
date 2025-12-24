# EXPANSION Bootstrap

**Purpose**: Grow existing flash/short work into larger scope while preserving core essence.

---

## When to Use This Bootstrap

- ASSESSMENT-BOOTSTRAP recommended expansion
- Existing story has high expansion potential
- Material wants/needs more room to breathe
- Clear development paths identified
- Author wants to deepen the story

---

## Expansion Workflow

### Phase 1: FOUNDATION REVIEW
**Goal**: Understand what to preserve and what to expand

**Tasks**:
1. Load original story from `_posts/`
2. Load assessment report (if exists)
3. Confirm target scope:
   - Flash → Short story (3K-5K words)
   - Short → Novelette (7.5K-17.5K words)
   - Novelette → Novella (17.5K-40K words)
   - Novella → Novel (50K+ words)
4. Identify preservation priorities:
   - Core scenes/moments that work perfectly
   - Voice and style to maintain
   - Key character beats
   - Essential atmosphere
5. Identify expansion targets:
   - Compressed elements to unpack
   - Implied backstory to reveal
   - Hinted world-building to explore
   - Character depth to develop
   - Emotional beats to extend
6. Create project structure
7. Save foundation document to GitHub

**Deliverables**:
- `README.md` (project overview)
- `foundation.md` (what to preserve, what to expand)
- `original-[filename].md` (archived original)

**Status Check**: ✅ Complete when foundation documented

---

### Phase 2: STRUCTURE PLANNING
**Goal**: Design the expanded story architecture

**Tasks**:
1. Map original story structure:
   - Current scenes/beats
   - Current word count per section
   - Current pacing
2. Design expanded structure:
   - New scenes needed (before/during/after original)
   - Integration points with original
   - Pacing adjustments for new length
   - Chapter/section breaks (if applicable)
3. Plan character development:
   - Backstory to reveal (when/how)
   - Relationship development arcs
   - Internal conflict expansion
   - Goals/motivations clarification
4. Plan world-building expansion:
   - Setting details to add
   - Rules to establish
   - Atmosphere to deepen
   - Context to provide
5. Plan subplot integration (if any):
   - What subplots serve the story?
   - How do they interweave?
   - Resolution timing
6. Estimate final word count
7. **GET AUTHOR APPROVAL**
8. Save expansion plan to GitHub

**Deliverables**:
- `expansion-plan.md` (detailed structure, author-approved)

**Status Check**: ✅ Complete when plan is approved and saved

---

### Phase 3: INCREMENTAL BUILDING
**Goal**: Expand scene by scene, preserving voice

**Tasks**:
1. Create working draft starting from original
2. Work through expansion plan systematically:
   - Expand/add scenes in order
   - Maintain voice consistency
   - Preserve core essence
   - Build naturally, not padding
3. For each expansion:
   - Draft new material
   - Integrate with original
   - Check voice/tone match
   - Verify pacing
   - Ensure transitions work
4. Document decisions in expansion-notes.md:
   - What was added and why
   - How it serves the story
   - Any deviations from plan
   - Problems solved
   - New opportunities discovered
5. Commit frequently to GitHub
6. Create save points after each major section

**Working Method**:
- Expand one scene/section at a time
- Get author feedback on major additions
- Adjust plan if needed (document why)
- Don't rush - let story breathe

**Deliverables**:
- `working-[filename].md` (expanded draft)
- `expansion-notes.md` (decision log)

**Status Check**: ✅ Complete when all planned expansions implemented

---

### Phase 4: INTEGRATION & POLISH
**Goal**: Unify expanded elements into cohesive whole

**Tasks**:
1. Read through complete expanded draft
2. Check for:
   - Voice consistency throughout
   - Pacing across new length
   - Transition smoothness
   - Character arc coherence
   - Thematic unity
   - Tonal consistency
3. Polish pass:
   - Refine new material
   - Smooth integration points
   - Adjust pacing as needed
   - Strengthen connections
4. Compose author's note:
   - Original publication context
   - Why expansion was chosen
   - What changed and what stayed
   - Douglas Adams style
5. Update metadata:
   - Mark as expanded edition
   - Add `revised:` and `expanded:` dates
   - Keep original `date:` field
   - Update scope tags
6. Decide publication strategy:
   - Replace original?
   - Publish as new story?
   - Offer both versions?
7. Archive expansion artifacts

**Deliverables**:
- Polished expanded story
- Complete expansion archive

**Status Check**: ✅ Complete when story is publication-ready

---

## Working Principles

- **Preserve essence**: Don't lose what made original work
- **Expand naturally**: Growth should feel inevitable, not padded
- **Maintain voice**: New material should sound like same author
- **Serve the story**: Only add what makes story better
- **Honor original**: Original readers should recognize the core
- **Think structurally**: Expansion changes pacing and rhythm
- **Get feedback**: Check in with author on major additions

---

## File Structure

Project folder: `_drafts/[story-name]/`

```
[story-name]/
├── README.md
├── original-[filename].md
├── foundation.md
├── expansion-plan.md
├── expansion-notes.md
└── working-[filename].md
```

Optionally include:
- `assessment.md` (from ASSESSMENT-BOOTSTRAP)
- `character-notes.md` (if extensive character development)
- `world-notes.md` (if significant world-building)

---

## Example Session

### Starting from Assessment

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/EXPANSION-BOOTSTRAP.md

# Expand: Mitzy and the Butterfly

Original: _posts/2015-08-21-mitzy-and-the-butterfly.md
Assessment: _drafts/mitzy/assessment.md
Target scope: Short story (4,000 words)

Begin foundation review and expansion planning.
```

### Continuing Existing Expansion

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/EXPANSION-BOOTSTRAP.md

# Expand: Mitzy and the Butterfly

Load artifacts: _drafts/mitzy/
Report status and resume from last save point.
```

---

## Expansion Analysis Template

In `foundation.md`:

```markdown
# Expansion Foundation: [Title]

## Original Story
- Current scope: [Flash/Short/etc]
- Current word count: [X words]
- Target scope: [Short/Novelette/etc]
- Target word count: [Y words]
- Expansion factor: [Zx]

## Preserve (Do Not Change)

### Core Scenes
1. [Scene that works perfectly as-is]
2. [Another essential scene]

### Voice & Style
- [Key voice characteristics to maintain]
- [Style elements that define the work]

### Character Essence
- [Character 1]: [Essential traits]
- [Character 2]: [Essential traits]

### Atmosphere
- [Mood/tone that must persist]

## Expand (Development Targets)

### New Scenes Needed
1. **[Scene Name]** - [Purpose, placement]
2. **[Scene Name]** - [Purpose, placement]
3. **[Scene Name]** - [Purpose, placement]

### Character Development
- **[Character 1]**: [What to develop, how]
- **[Character 2]**: [What to develop, how]

### World-Building
- [Element to explore]
- [Detail to establish]
- [Context to provide]

### Backstory to Reveal
- [What happened before]
- [When/how to reveal it]

### Emotional Beats to Extend
- [Beat 1]: [How to deepen]
- [Beat 2]: [How to deepen]

## Integration Strategy

[How new material will weave with original]
```

---

## Author's Note Template (Expanded Edition)

```markdown
## Expanded Edition Note

This story first appeared as flash fiction in [Publication/Date]. This expanded 
edition (December 2025) grows the original [X] words into a [Y]-word [scope]. 

The core story remains - [brief description of what's preserved] - but now 
there's room to explore [what's been expanded].

[Optional: what you learned about the story through expansion]

Sometimes stories want more space to breathe.
{: .notice--info}
```

---

## Common Expansion Patterns

### Flash → Short Story (500 → 4,000 words)
- Add 2-3 new scenes
- Deepen 1-2 characters
- Expand world-building
- Extend emotional beats

### Short → Novelette (5,000 → 12,000 words)
- Add subplot
- Develop secondary characters
- Expand setting significantly
- Add complexity to conflict

### Novelette → Novella (15,000 → 30,000 words)
- Multiple subplots
- Full character arcs for supporting cast
- Rich world-building
- Multi-layered themes

---

## Commit Message Standards

**Foundation phase**:
- "Initialize [Story Name] expansion project"
- "Document expansion foundation for [Story Name]"

**Planning phase**:
- "Add expansion plan for [Story Name]"
- "Update expansion plan with author feedback"

**Building phase**:
- "Expand [Story Name]: add [specific scene/section]"
- "Expand [Story Name]: deepen [character/element]"
- "Update expansion notes: [progress summary]"

**Integration phase**:
- "Polish expanded [Story Name]: [specific work]"
- "Finalize expanded [Story Name] with author's note"
- "Archive [Story Name] expansion artifacts"

---

## Save Point Format

In `expansion-notes.md`:

```markdown
## Save Point: [Date/Time]

**Phase**: [Current phase]
**Progress**: [X of Y new scenes complete]
**Current Word Count**: [X words / Y target]
**Last Completed**: [What was just finished]
**Next Steps**: [What to expand next]
**Open Questions**: [Any unresolved items]
**Integration Notes**: [How new material is fitting]
**Session Duration**: [Approximate time]
**Commits Made**: [List of commits]

**To Resume**: [Specific instruction for next session]
```

---

**Bootstrap Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench