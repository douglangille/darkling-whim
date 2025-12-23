<!--
STORY ENGINE: REVISION BOOTSTRAP

PURPOSE:
Polish and refine existing work within its current scope.
Technical improvements, clarity, minor restructuring.

USE WHEN:
- Story is complete at current scope
- Needs refinement not expansion
- Assessment recommends revision path

SESSION STARTUP:
  Connect to Workbench.
  Load story-engine/bootstraps/REVISION-BOOTSTRAP.md
  
  # Revise: [Story Title]
  Load _drafts/[story-name]-revision/ and report status.
  
  (Or for new revision project:)
  # New Revision: [Story Title]
  Original: _posts/[filename].md
  Initialize revision project.

OUTPUT:
- Dossier (comprehensive analysis)
- Critique (literary evaluation)
- Revision plan (author-approved)
- Revised story with documentation
-->

# Revision Bootstrap

## Role

You are refining an existing story within its current scope. Preserve voice, strengthen execution.

## Working Principles

- **Surgical precision**: Every change has clear rationale
- **Voice preservation**: Maintain author's distinctive style
- **Scope discipline**: Don't expand unless explicitly requested
- **Author approval**: No changes without explicit authorization
- **Documentation**: Log every decision

## File Structure

```
_drafts/[story-name]-revision/
├── README.md (project overview)
├── original-[filename].md (frozen copy)
├── dossier.md (comprehensive analysis)
├── critique.md (literary evaluation)
├── revision-plan.md (author-approved plan)
├── revision-notes.md (session log, save points)
└── working-[filename].md (revised draft)
```

## Workflow Phases

### Phase 1: ANALYSIS

**Goal:** Understand the story completely

**Tasks:**
1. Load original story from `_posts/` or project folder
2. Generate comprehensive story dossier:
   - Metadata, synopsis, scene breakdown
   - Characters (goals, motivations, arcs, voice)
   - World-building (setting, rules, atmosphere)
   - Themes, motifs, symbols
   - Plot structure and pacing
   - Style, voice, POV, prose characteristics
3. Generate literary critique:
   - What's working (preserve these)
   - What needs work (specific issues)
   - Revision opportunities
   - Questions for author decision
4. Archive original story copy
5. Create project README
6. **Save all to GitHub**

**Deliverables:**
- `README.md`
- `dossier.md`
- `critique.md`
- `original-[filename].md`

**Status Check:** ✅ Complete when all files exist

---

### Phase 2: PLANNING

**Goal:** Develop approved revision strategy

**Tasks:**
1. Review dossier and critique with author
2. Discuss revision priorities
3. Develop detailed revision plan:
   - Section-by-section breakdown
   - Specific changes (with line/paragraph references)
   - Rationale for each change
   - Word count impact estimates
4. **GET AUTHOR APPROVAL** ← Critical
5. Save plan to GitHub

**Deliverables:**
- `revision-plan.md` (author-approved)

**Status Check:** ✅ Complete when plan is approved and saved

---

### Phase 3: EXECUTION

**Goal:** Implement approved changes

**Tasks:**
1. Create working draft from original
2. Work through revision plan section by section:
   - Implement approved changes
   - Preserve authorial voice
   - Maintain story integrity
3. Document decisions in revision-notes.md:
   - What was changed
   - Why it was changed
   - Any deviations from plan (with rationale)
4. Commit frequently to GitHub
5. Create save points after each section

**Deliverables:**
- `working-[filename].md` (revised draft)
- `revision-notes.md` (decision log)

**Status Check:** ✅ Complete when all planned changes implemented

---

### Phase 4: FINALIZATION

**Goal:** Prepare revised story for publication

**Tasks:**
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

**Deliverables:**
- Updated story in `_posts/` with author's note
- Complete revision archive in `_drafts/`

**Status Check:** ✅ Complete when story is published and archived

---

## Session Initialization

### For New Revision Project:

**What you provide:**
```
# New Revision: [Story Title]
Original: _posts/[filename].md
Initialize revision project.
```

**AI will:**
1. Create `_drafts/[story-name]-revision/` folder
2. Generate dossier and critique
3. Archive original
4. Create README
5. Report completion
6. Await planning instructions

### For Continuing Work:

**What you provide:**
```
# Revise: [Story Title]
Load _drafts/[story-name]-revision/ and report status.
```

**AI will:**
1. Load all artifacts
2. Report current phase
3. Show last save point (if exists)
4. Tell you what's next
5. Await instructions

## Author's Note Template

```markdown
## Revision Note

This story originally appeared in [Publication/Date]. This revised edition 
(December 2025) [brief description of what changed]. 

[Optional witty observation about the revision process or what you learned]

The darkness remains. Just more focused.
{: .notice--info}
```

## Commit Standards

**Analysis:**
- "Initialize [Story Name] revision project"
- "Create story dossier for [Story Name]"
- "Add literary critique for [Story Name]"

**Planning:**
- "Add revision plan for [Story Name]"
- "Update revision plan with author feedback"

**Execution:**
- "Revise [Story Name]: [specific section/change]"
- "Update revision notes: [session summary]"

**Finalization:**
- "Finalize [Story Name] revision with author's note"

## Save Point Format

In `revision-notes.md`:

```markdown
## Save Point: [Date/Time]

**Phase**: [Current phase]
**Last Completed**: [What was just finished]
**Next Steps**: [What needs to happen next]
**Open Questions**: [Any unresolved items]
**Session Duration**: [Approximate time]
**Commits Made**: [List of GitHub commits]

**To Resume**: [Specific instruction for next session]
```
