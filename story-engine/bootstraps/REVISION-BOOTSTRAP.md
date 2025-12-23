# REVISION Bootstrap

**Purpose**: Polish and refine existing work at its current scope. For expanding scope, use EXPANSION-BOOTSTRAP instead.

---

## When to Use This Bootstrap

- Story is complete at current scope (flash, short, etc.)
- Needs refinement, not expansion
- ASSESSMENT-BOOTSTRAP recommended revision path
- Technical improvements and polish needed

---

## Workflow Phases

### Phase 1: ANALYSIS ✅
**Goal**: Understand the story completely

**Prerequisites**: Usually done via ASSESSMENT-BOOTSTRAP. If starting here directly:

**Tasks**:
1. Generate comprehensive story dossier
2. Generate literary critique
3. Archive original story copy
4. Create project README
5. Save all to GitHub

**Deliverables**:
- `README.md` (project overview)
- `dossier.md` (comprehensive analysis)
- `critique.md` (literary evaluation)
- `original-[filename].md` (frozen copy)

**Status Check**: ✅ Complete when all files exist

---

### Phase 2: PLANNING
**Goal**: Develop approved revision strategy

**Tasks**:
1. Review dossier and critique with author
2. Discuss revision priorities
3. Develop detailed revision plan:
   - Section-by-section breakdown
   - Specific changes (with line/paragraph references)
   - Rationale for each change
   - Word count impact estimates (should stay near current length)
4. **GET AUTHOR APPROVAL**
5. Save plan to GitHub

**Deliverables**:
- `revision-plan.md` (author-approved)

**Status Check**: ✅ Complete when plan is approved and saved

---

### Phase 3: EXECUTION
**Goal**: Implement approved changes

**Tasks**:
1. Create working draft from original
2. Work through revision plan section by section:
   - Implement approved changes
   - Preserve authorial voice
   - Maintain story integrity
   - Stay at current scope
3. Document decisions in revision-notes.md:
   - What was changed
   - Why it was changed
   - Any deviations from plan (with rationale)
4. Commit frequently to GitHub
5. Create save points after each section

**Deliverables**:
- `working-[filename].md` (revised draft)
- `revision-notes.md` (decision log)

**Status Check**: ✅ Complete when all planned changes implemented

---

### Phase 4: FINALIZATION
**Goal**: Prepare revised story for publication

**Tasks**:
1. Final polish pass
2. Compose author's note:
   - Original publication context
   - What changed and why
   - Douglas Adams style (self-aware, witty)
3. Update metadata:
   - Add `revised:` date field
   - Keep original `date:` field
   - Update any changed tags
4. Replace original in `_posts/` with revised version
5. Archive revision artifacts in `_drafts/`

**Deliverables**:
- Updated story in `_posts/` with author's note
- Complete revision archive in `_drafts/`

**Status Check**: ✅ Complete when story is published and archived

---

## Working Principles

- **Preserve scope**: Don't expand, refine
- **Preserve voice**: Maintain distinctive style
- **Surgical precision**: Targeted improvements
- **Author approval**: Required for plan
- **Document decisions**: Log everything
- **Commit frequently**: Save progress

---

## File Structure

Project folder: `_drafts/[story-name]-revision/`

```
[story-name]-revision/
├── README.md
├── original-[filename].md
├── dossier.md
├── critique.md
├── revision-plan.md
├── revision-notes.md
└── working-[filename].md
```

---

## Example Session

### Starting from Assessment

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/REVISION-BOOTSTRAP.md

# Revising: Mitzy and the Butterfly

Load assessment: _drafts/mitzy-assessment/assessment.md
Initialize revision project.
```

### Continuing Existing Revision

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/REVISION-BOOTSTRAP.md

# Revising: Mitzy and the Butterfly

Load artifacts: _drafts/mitzy-revision/
Report status and resume from last save point.
```

---

## Author's Note Template

```markdown
## Revision Note

This story originally appeared in [Publication/Date]. This revised edition 
(December 2025) [brief description of what changed]. 

[Optional witty observation about the revision process or what you learned]

The darkness remains. Just more focused.
{: .notice--info}
```

---

## Commit Message Standards

**Analysis phase**:
- "Initialize [Story Name] revision project"
- "Create story dossier for [Story Name]"
- "Add literary critique for [Story Name]"

**Planning phase**:
- "Add revision plan for [Story Name]"
- "Update revision plan with author feedback"

**Execution phase**:
- "Revise [Story Name]: [specific section/change]"
- "Update revision notes: [session summary]"

**Finalization phase**:
- "Finalize [Story Name] revision with author's note"
- "Archive [Story Name] revision artifacts"

---

## Save Point Format

In `revision-notes.md`:

```markdown
## Save Point: [Date/Time]

**Phase**: [Current phase]
**Last Completed**: [What was just finished]
**Next Steps**: [What needs to happen next]
**Open Questions**: [Any unresolved items]
**Session Duration**: [Approximate time]
**Commits Made**: [List of commits]

**To Resume**: [Specific instruction for next session]
```

---

**Bootstrap Version**: 2.0  
**Updated**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
