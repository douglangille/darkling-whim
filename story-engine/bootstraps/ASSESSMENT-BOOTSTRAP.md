<!--
STORY ENGINE: ASSESSMENT BOOTSTRAP

PURPOSE:
Analyze existing published work to determine the optimal path forward.
Decide whether to revise, expand, reboot, or leave as-is.

USE WHEN:
- Revisiting published stories
- Deciding between polish vs. expansion
- Evaluating scope and potential

SESSION STARTUP:
  Connect to Workbench.
  Load story-engine/bootstraps/ASSESSMENT-BOOTSTRAP.md
  
  # Assess: [Story Title]
  Original: _posts/[filename].md
  Analyze and recommend path forward.

OUTPUT:
- Comprehensive story assessment
- Scope analysis (current vs. natural)
- Expansion potential evaluation
- Path recommendations
- Decision framework for author
-->

# Assessment Bootstrap

## Role

You are analyzing an existing published story to determine its optimal path forward.

## Process

### Phase 1: Load and Analyze

1. **Load the story** from `_posts/[filename].md`
2. **Read completely** - understand as published
3. **Generate comprehensive analysis**:
   - Story metadata (title, date, word count, genre)
   - Synopsis (2-3 sentences)
   - Core elements (premise, characters, conflict, resolution)
   - Thematic content
   - Technical execution (prose, pacing, structure)
   - Strengths (what works well)
   - Weaknesses or limitations (what could improve)

### Phase 2: Scope Assessment

**Analyze scope on multiple dimensions:**

#### Current Scope
- Actual form: flash/vignette/short/novella/novel
- Word count
- Scene count
- Character depth level
- World-building detail
- Plot complexity
- What the story accomplishes as-is

#### Natural Scope
- What the material "wants" to be
- Where does it feel compressed or constrained?
- What elements are hinted at but unexplored?
- What questions does it raise but not answer?
- What scope would let the story breathe?

#### Expansion Potential: [HIGH / MEDIUM / LOW / NONE]

**For each potential target scope, analyze:**

**If expanded to Short Story (3,000-7,500 words):**
- Additional scenes needed: [list]
- Character development opportunities: [list]
- World-building to explore: [list]
- Subplot potential: [list]
- What would be gained: [analysis]
- What risks losing original charm: [concerns]

**If expanded to Novella (15,000-40,000 words):**
- [Similar analysis]

**If expanded to Novel (50,000+ words):**
- [Similar analysis]

### Phase 3: Path Recommendations

Present clear options:

#### Option 1: Leave As-Is
**Recommend if:** Story is complete and satisfying at current scope
**Rationale:** [Why it works as-is]

#### Option 2: Polish/Revise (Current Scope)
**Recommend if:** Story is right scope but needs refinement
**Work involved:** [Describe changes needed]
**Estimated effort:** [Low/Medium/High]
**Next step:** Load REVISION-BOOTSTRAP.md

#### Option 3: Expand to [Target Scope]
**Recommend if:** Material has more to explore
**Work involved:** [Describe what needs building]
**Target word count:** [estimate]
**Estimated effort:** [Medium/High]
**Next step:** Load EXPANSION-BOOTSTRAP.md

#### Option 4: Reboot/Reimagine
**Recommend if:** Core idea strong but execution needs fresh start
**Work involved:** [Describe approach]
**Next step:** Load DRAFTING-BOOTSTRAP.md

#### Option 5: Series/Universe Potential
**Recommend if:** World/characters could support multiple stories
**Work involved:** [Describe universe building]
**Next step:** Load UNIVERSE-BOOTSTRAP.md or SERIAL-BOOTSTRAP.md

### Phase 4: Generate Assessment Document

Create comprehensive assessment report:

**File:** `_drafts/[story-name]-assessment/assessment-report.md`

**Contents:**
- Story analysis
- Scope assessment
- Expansion analysis (all potential target scopes)
- Path recommendations with clear rationale
- Decision framework for author

**Also create:**
- `_drafts/[story-name]-assessment/original-[filename].md` (archive copy)
- `_drafts/[story-name]-assessment/README.md` (project overview)

**Commit to GitHub**

### Phase 5: Present Decision Point

**Report to author:**
1. Summary of analysis
2. Current vs. natural scope
3. Expansion potential rating
4. Clear recommendation with rationale
5. Alternative paths to consider

**Ask author to choose:**
- Which path do you want to take?
- What's your priority: polish existing or explore expansion?
- Are you excited by any of the expansion possibilities?

**Based on choice, provide next session startup command**

## Commit Standards

- "Initialize assessment for [Story Name]"
- "Complete story analysis for [Story Name]"
- "Add scope assessment and recommendations for [Story Name]"

## File Structure

```
_drafts/[story-name]-assessment/
├── README.md
├── assessment-report.md
└── original-[filename].md
```

## Next Steps

After author decision:
- **Revision** → New session with REVISION-BOOTSTRAP.md
- **Expansion** → New session with EXPANSION-BOOTSTRAP.md
- **Reboot** → New session with DRAFTING-BOOTSTRAP.md
- **Universe** → New session with UNIVERSE-BOOTSTRAP.md
- **Leave as-is** → Archive assessment for reference
