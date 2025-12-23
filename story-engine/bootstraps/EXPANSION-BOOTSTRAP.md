<!--
STORY ENGINE: EXPANSION BOOTSTRAP

PURPOSE:
Grow existing flash/short stories into larger works.
Preserve original core while adding depth and scope.

USE WHEN:
- Assessment shows high expansion potential
- Story has "more to say"
- Want to deepen characters, world, or plot

SESSION STARTUP:
  Connect to Workbench.
  Load story-engine/bootstraps/EXPANSION-BOOTSTRAP.md
  
  # Expand: [Story Title]
  Original: _posts/[filename].md
  Assessment: _drafts/[story-name]-assessment/assessment-report.md
  Target scope: [Short Story / Novella / Novel]
  Target word count: [estimate]
  Initialize expansion project.

OUTPUT:
- Expansion plan (structure, new scenes, integration)
- Expanded story preserving original voice
- Complete documentation of additions
-->

# Expansion Bootstrap

## Role

You are expanding an existing story to a larger scope while preserving its core essence and voice.

## Working Principles

- **Core preservation**: Original "seed" material is sacred
- **Voice consistency**: Maintain authorial style throughout
- **Organic growth**: Expansions feel natural, not bolted-on
- **Structural integrity**: Pacing appropriate to new scope
- **Integration**: New and old blend seamlessly

## File Structure

```
_drafts/[story-name]-expansion/
├── README.md (project overview)
├── original-[filename].md (frozen copy)
├── assessment-report.md (copy from assessment)
├── expansion-plan.md (structure and approach)
├── expansion-notes.md (session log, decisions)
├── scene-outlines/ (detailed scene plans)
├── working-draft.md (expanded story)
└── integration-map.md (original → expanded mapping)
```

## Workflow Phases

### Phase 1: FOUNDATION REVIEW

**Goal:** Understand what to preserve and what to expand

**Tasks:**
1. Load original story
2. Load assessment report (if exists)
3. Confirm target scope and word count
4. Identify preservation priorities:
   - Core scenes/moments that must stay
   - Voice characteristics to maintain
   - Thematic elements to strengthen
   - Character essences to preserve
5. Identify expansion opportunities:
   - Compressed moments to open up
   - Implied backstory to explore
   - Relationships to deepen
   - World-building to enrich
   - Consequences to examine

**Deliverables:**
- Project README with scope and goals
- Archive of original story
- Foundation analysis document

**Status Check:** ✅ Ready when preservation/expansion priorities clear

---

### Phase 2: STRUCTURE PLANNING

**Goal:** Design expanded story architecture

**Tasks:**
1. Map original story structure:
   - Current scenes/beats
   - Current word allocation
   - Current pacing
2. Design target structure:
   - Act/section breakdown (appropriate to scope)
   - Scene sequence (original + new)
   - Word count targets per section
   - Pacing strategy for new length
3. Plan new content:
   - **New scenes needed**: [list with purpose]
   - **Character development arcs**: [for each character]
   - **Subplot integration**: [if appropriate to scope]
   - **World-building expansion**: [what to add]
   - **Thematic deepening**: [how to enrich]
4. Create integration map:
   - Show where original content appears in expanded version
   - Show where new content inserts
   - Ensure seamless flow
5. **GET AUTHOR APPROVAL** ← Critical before writing

**Deliverables:**
- `expansion-plan.md` (complete structural blueprint)
- `integration-map.md` (original → expanded mapping)
- Scene outlines for all new scenes

**Status Check:** ✅ Complete when plan is approved

---

### Phase 3: INCREMENTAL BUILDING

**Goal:** Write the expanded story section by section

**Approach:** Work in acts/sections, committing frequently

**For each section:**
1. Review plan for this section
2. Include preserved original material (adapted as needed)
3. Write new scenes/content
4. Ensure voice consistency
5. Check pacing within section
6. Document decisions in expansion-notes.md
7. Commit to GitHub
8. Create save point

**Guidelines:**
- Preserve original prose where possible (may need transitions)
- Match voice in all new material
- Maintain tonal consistency
- Check pacing - longer works need different rhythm
- Build character arcs gradually
- Layer in world-building naturally

**Deliverables:**
- `working-draft.md` (growing incrementally)
- `expansion-notes.md` (decision log)
- Regular GitHub commits

**Status Check:** ✅ Complete when all sections written

---

### Phase 4: INTEGRATION & POLISH

**Goal:** Ensure seamless blend and appropriate pacing

**Tasks:**
1. Read complete draft
2. Check integration points:
   - Original → new transitions smooth?
   - Voice consistent throughout?
   - Pacing appropriate to length?
3. Verify character arcs:
   - Development feels earned?
   - Consistent with original essence?
4. Check world-building:
   - Details consistent?
   - Enriches rather than contradicts?
5. Verify thematic consistency:
   - Themes deepened not diluted?
6. Polish prose throughout
7. **Author review and approval**

**Deliverables:**
- Polished expanded story
- Final expansion notes

**Status Check:** ✅ Complete when author approves

---

### Phase 5: FINALIZATION

**Goal:** Prepare for publication

**Tasks:**
1. Final polish pass
2. Compose author's note:
   - Original publication history
   - Expansion rationale and process
   - What was preserved vs. added
   - Douglas Adams style (self-aware, engaging)
3. Update metadata:
   - Mark as "expanded edition"
   - Include `revised:` date
   - Keep `original_date:` field
4. Decide on publication:
   - Replace original in `_posts/`? OR
   - Publish as new story with reference to original?
5. Archive expansion artifacts

**Deliverables:**
- Final expanded story in `_posts/`
- Complete expansion documentation in `_drafts/`

---

## Session Initialization

### For New Expansion Project:

```
# Expand: [Story Title]
Original: _posts/[filename].md
Target scope: Short Story
Target word count: ~4,000 words
Initialize expansion project.
```

### For Continuing Work:

```
# Expand: [Story Title]
Load _drafts/[story-name]-expansion/ and report status.
Resume from last save point.
```

## Author's Note Template

```markdown
## Expanded Edition Note

This story began as flash fiction published in [Original Publication/Date]. 
This expanded edition (December 2025) [description of what was added and why].

The original seed remains at the heart - I've simply given it room to breathe 
and explore what was always implied but never shown.

[Optional reflection on the expansion process]

{: .notice--info}
```

## Commit Standards

**Planning:**
- "Initialize expansion project for [Story Name]"
- "Add expansion plan for [Story Name] (target: [scope])"
- "Complete integration map for [Story Name] expansion"

**Execution:**
- "Expand [Story Name]: [section name]"
- "Add new scene: [scene description]"
- "Integrate original material into [section]"

**Finalization:**
- "Complete [Story Name] expansion ([original WC] → [new WC] words)"
- "Finalize [Story Name] expanded edition with author's note"

## Save Point Format

```markdown
## Save Point: [Date/Time]

**Phase**: [Current phase]
**Progress**: [X of Y sections complete]
**Current Word Count**: [X words] (Target: [Y words])
**Last Completed**: [What section/scene]
**Next Steps**: [What section comes next]
**Open Questions**: [Any issues to resolve]
**Commits Made**: [List]

**To Resume**: Continue with [specific section/scene]
```
