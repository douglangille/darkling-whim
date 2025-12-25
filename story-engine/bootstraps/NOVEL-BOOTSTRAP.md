# NOVEL Bootstrap

**Purpose**: Manage long-form fiction (50,000+ words) using fractal scene-building from concept to completion.

**Method**: Inspired by Randy Ingermanson's Snowflake Method - start with one sentence, expand fractally to full novel.

---

## When to Use This Bootstrap

- Writing a novel (50,000+ words)
- Need systematic approach to long-form
- Want to build from macro to micro
- Planning both structure and execution
- Human drafting or AI-assisted drafting

---

## Novel Development Workflow

### Phase 1: CONCEPT (Snowflake Steps 1-4)
**Goal**: Establish core story at macro level

**Tasks**:

**Step 1: One-Sentence Summary**
- The entire novel in one sentence (15 words or less)
- Captures: protagonist, goal, conflict, stakes
- Example: "A reluctant hero must save the kingdom from darkness before ancient evil awakens."

**Step 2: One-Paragraph Summary**
- Expand to full paragraph (5 sentences):
  1. Setup and hook
  2. First major plot point
  3. Midpoint
  4. Crisis/Third plot point
  5. Climax and resolution
- Still high-level, no names yet

**Step 3: Character Summaries**
- One page per major character:
  - Name
  - One-sentence summary of storyline
  - Motivation (what drives them)
  - Goal (what they want)
  - Conflict (what opposes them)
  - Epiphany (what they learn)
  - One-paragraph summary of character arc

**Step 4: Story Structure Analysis**
- Choose primary structure(s):
  - **Three-Act** (classic)
  - **Hero's Journey** (Campbell/Vogler)
  - **Heroine's Journey** (Murdock)
  - **Save the Cat** (Blake Snyder beats)
  - **Fichtean Curve** (rising crises)
  - **Kishotenketsu** (Japanese 4-act)
  - **Other** (specify)
- Map paragraph summary to chosen structure
- Identify where structure beats fall

**Deliverables**:
- `concept.md` (one-sentence, one-paragraph, structure choice)
- `characters/` folder with character summaries

**Status Check**: ✅ Complete when core story is clear

---

### Phase 2: EXPANSION (Snowflake Steps 5-7)
**Goal**: Expand story and character understanding

**Tasks**:

**Step 5: Expand to One-Page Synopsis**
- Expand paragraph to full page (multiple paragraphs)
- Cover major plot movements
- Still high-level but more detailed
- Focus on cause-and-effect chain

**Step 6: Expand Character Pages**
- Each major character gets full page:
  - Detailed motivation
  - Abstract of storyline
  - Specific goals and conflicts
  - How they change
  - Key relationships

**Step 7: Three-Act Breakdown**
- **Act I** (25%): Setup and inciting incident
- **Act II** (50%): Rising action and midpoint
- **Act III** (25%): Climax and resolution
- Identify major beats within each act
- Assign approximate word count to each act

**Deliverables**:
- `synopsis.md` (expanded story)
- Updated character files
- `structure.md` (three-act breakdown with beats)

**Status Check**: ✅ Complete when acts are defined

---

### Phase 3: CHAPTER STRUCTURE (Snowflake Steps 8-9)
**Goal**: Break story into chapters/sequences

**Tasks**:

**Step 8: Chapter List**
- Divide each act into chapters
- One sentence per chapter describing what happens
- Typical novel: 20-40 chapters
- Chapters group related scenes
- Note POV character for each chapter

**Step 9: Chapter Summaries**
- Expand each chapter to paragraph:
  - Opening situation
  - Key events
  - Character development
  - Conflict/tension
  - Chapter ending/hook
  - Approximate word count
- Ensure chapters flow logically
- Check pacing across acts

**Step 10: Subplot Integration**
- Identify major subplots:
  - Romantic subplot
  - Character relationship arcs
  - Secondary conflicts
  - Thematic threads
- Map subplot beats into chapter structure
- Ensure subplots weave with main plot

**Deliverables**:
- `chapters/` folder
- One file per chapter with paragraph summary
- `subplots.md` (subplot tracking)

**Status Check**: ✅ Complete when all chapters outlined

---

### Phase 4: SCENE BREAKDOWN & BRIEFS (Snowflake Step 10)
**Goal**: Fractal expansion to atomic scene level with complete planning

**Reference**: Load and review `story-engine/bootstraps/SCENE-WORKFLOW.md` for complete scene brief protocol

**Tasks**:

**Step 11: Scene List Per Chapter**
- Break each chapter into atomic scenes
- Scene = Goal-Conflict-Disaster (proactive)
- Sequel = Reaction-Dilemma-Decision (reactive)
- Typical chapter: 2-5 scenes
- Number scenes consecutively across entire novel
- Each scene must advance plot OR develop character OR both

**Step 12: Create Scene Briefs for All Scenes**
- Use Scene Brief Template from SCENE-WORKFLOW.md
- For each scene/sequel, define:
  
  **If Scene (proactive)**:
  - **Goal**: What POV character wants in this scene (specific, visible)
  - **Conflict**: What prevents them from getting it
  - **Disaster**: How it goes wrong (genuine setback)
  
  **If Sequel (reactive)**:
  - **Reaction**: Emotional response to previous disaster
  - **Dilemma**: Analyzing bad options (all choices have costs)
  - **Decision**: Commitment to new action (becomes next Scene goal)
  
- Also specify:
  - POV character
  - Setting (location, time, atmosphere)
  - Word count target
  - How scene connects to adjacent scenes
  - Key story elements (plot advancement, character development, theme)

**Step 13: Validate Scene Chain Integrity**
- Check each Scene disaster leads to Sequel reaction
- Check each Sequel decision creates next Scene goal
- Verify no orphaned scenes (all connect to chain)
- Check escalating tension throughout novel
- Verify Scene/Sequel pacing serves story
- Adjust briefs as needed

**Step 14: Make Authorship Decisions**
- For each scene, decide:
  - [ ] Human First Draft (author writes, AI reviews)
  - [ ] AI First Draft (AI writes, author edits)
  - [ ] TBD (decide later)
- Mark in each scene brief
- Consider: complexity, familiarity with content, energy level, experimentation

**Step 15: Create Scene Tracker**
- Use Scene Tracker Template from SCENE-WORKFLOW.md
- List all scenes with:
  - Chapter number
  - Scene number
  - Type (Scene/Sequel)
  - Title
  - Status
  - Authorship approach
  - Target word count
  - Notes/issues

**Step 16: Get Author Approval**
- Review complete scene brief list (all chapters)
- This is the complete blueprint for drafting
- Changes now are easier than during drafting
- Commit to GitHub before drafting

**DO NOT DRAFT PROSE YET**—all scene briefs must be complete and validated first

**Deliverables**:
- `scene-briefs.md` (complete list) OR
- `scenes/` folder (individual scene brief files: `ch01-scene01.md`, etc.)
- `scene-tracker.md` (progress tracking table for entire novel)

**Status Check**: 
- ✅ Complete when all scene briefs created
- ✅ Scene chain validated across entire novel
- ✅ Authorship decisions made
- ✅ Author approved

---

### Phase 5: DRAFTING (Snowflake Step 11)
**Goal**: Write prose from scene briefs

**Reference**: Use Scene Drafting Protocol from `SCENE-WORKFLOW.md`

**Tasks**:

**Step 17: Draft Scenes**
- Work scene by scene (linearly or strategic order)
- For each scene:
  1. Review scene brief
  2. Confirm Goal/Conflict/Disaster or Reaction/Dilemma/Decision structure
  3. Check connections to previous and next scenes
  
- Execute drafting per scene's authorship choice:
  
  **If Human First Draft**:
  - Author writes the scene prose
  - Focus on hitting structural beats from brief
  - Maintain momentum, don't over-edit
  - AI reviews for: structure integrity, pacing, voice consistency
  - AI suggests improvements (author decides)
  
  **If AI First Draft**:
  - AI drafts scene prose from brief
  - AI hits structural beats, maintains voice
  - Author reviews for: authenticity, character truth, emotional accuracy
  - Author edits/rewrites as needed
  - Iterate until scene works
  
- Scene-level review after each draft:
  - [ ] Scene fulfills the brief?
  - [ ] Structure clear (Goal/Conflict/Disaster or Reaction/Dilemma/Decision)?
  - [ ] Connects to adjacent scenes?
  - [ ] Voice consistent?
  - [ ] Pacing appropriate?
  - [ ] Continuity maintained?
  
- Update scene tracker:
  - Mark status (Drafted, Reviewed)
  - Note actual word count
  - Flag issues for later revision
  
- Commit scene draft to GitHub
- Maintain drafting momentum—don't revise entire novel yet

**Working Method**:
- One scene at a time—complete before moving on
- Hit structural beats from brief
- Mark problem areas with [NOTE] and continue
- Scene briefs can be adjusted if story evolves
- Trust the scene chain
- Completion beats perfection in first draft

**Step 18: Chapter Assembly**
- Assemble completed scenes into chapters
- Check transitions between scenes
- Ensure chapter unity
- Verify chapter arc
- Read each chapter as continuous text

**Step 19: Act Assembly**
- Assemble completed chapters into acts
- Read each act as continuous text
- Check pacing across act
- Verify act structure
- Ensure act breaks are strong

**Deliverables**:
- `draft/scenes/` - completed scene drafts
- `draft/chapters/` - assembled chapters
- `draft/acts/` - assembled acts
- `drafting-notes.md` - progress and decisions

**Status Check**: ✅ Complete when full draft exists

---

### Phase 6: SCENE-LEVEL ANALYSIS (Snowflake Step 12)
**Goal**: Analyze and revise at atomic level

**Tasks**:

**Step 20: Scene-by-Scene Analysis**
- For each scene, analyze:
  
  **Structure Check**:
  - Does scene follow Scene/Sequel pattern?
  - Is Goal → Conflict → Disaster clear?
  - Does Reaction → Dilemma → Decision work?
  
  **Content Check**:
  - Does scene advance plot?
  - Does it develop character?
  - Is conflict present?
  - Is tension maintained?
  - Does ending hook to next?
  
  **Technical Check**:
  - POV consistent?
  - Setting clear?
  - Dialogue natural?
  - Pacing appropriate?
  - Voice consistent?
  
  **Purpose Check**:
  - Why is this scene here?
  - Could it be cut?
  - Could it be combined with another?
  - Does it earn its place?

**Step 21: Scene Revision**
- Revise scenes based on analysis:
  - Strengthen weak goals
  - Heighten conflict
  - Sharpen disasters
  - Clarify decisions
  - Enhance character voice
  - Tighten prose

**Step 22: Pattern Analysis**
- Look across all scenes:
  - Scene/sequel ratio
  - Pacing patterns
  - Chapter lengths
  - POV distribution
  - Subplot balance
  - Tension curve

**Deliverables**:
- `analysis/scene-analysis.md` - findings per scene
- `analysis/pattern-analysis.md` - macro patterns
- Revised scene drafts

**Status Check**: ✅ Complete when all scenes analyzed and revised

---

### Phase 7: INTEGRATION & POLISH
**Goal**: Unify novel into cohesive whole

**Tasks**:

**Step 23: Full Read-Through**
- Read entire novel start to finish
- Note:
  - Continuity errors
  - Pacing issues
  - Character inconsistencies
  - Plot holes
  - Tonal shifts

**Step 24: Macro Revision**
- Address structural issues:
  - Reorder scenes/chapters if needed
  - Cut unnecessary scenes
  - Add missing scenes (create brief → draft → integrate)
  - Strengthen act breaks
  - Enhance climax

**Step 25: Line-Level Polish**
- Polish prose:
  - Tighten sentences
  - Enhance descriptions
  - Sharpen dialogue
  - Strengthen voice
  - Cut redundancy

**Step 26: Final Technical Pass**
- Grammar and punctuation
- Consistency checks (names, dates, details)
- Format for publication
- Prepare front/back matter

**Deliverables**:
- Publication-ready novel manuscript
- Complete development archive

**Status Check**: ✅ Complete when novel is publication-ready

---

## Story Structure Templates

### Three-Act Structure
```markdown
## Act I: Setup (25% / ~20K words for 80K novel)
- Opening image
- Introduce protagonist in normal world
- Inciting incident (10-15%)
- Debate/refusal
- Plot Point 1: Commitment (25%)

## Act II: Confrontation (50% / ~40K words)
### Act IIA: Rising Action
- B Story begins (subplot)
- Fun & games (promise of premise)
- Midpoint: False victory or defeat (50%)

### Act IIB: Complications
- Bad guys close in
- All is lost moment
- Dark night of the soul
- Plot Point 2: Discovery (75%)

## Act III: Resolution (25% / ~20K words)
- Finale: Execute solution
- Climax: Final battle
- Resolution: New world
- Closing image
```

### Save the Cat Beat Sheet
```markdown
1. Opening Image (0-1%)
2. Theme Stated (5%)
3. Setup (1-10%)
4. Catalyst/Inciting Incident (10%)
5. Debate (10-20%)
6. Break into Two (20%)
7. B Story (22%)
8. Fun and Games (20-50%)
9. Midpoint (50%)
10. Bad Guys Close In (50-75%)
11. All Is Lost (75%)
12. Dark Night of the Soul (75-80%)
13. Break into Three (80%)
14. Finale (80-99%)
15. Final Image (99-100%)
```

### Hero's Journey
```markdown
## Act I: Departure
1. Ordinary World
2. Call to Adventure
3. Refusal of Call
4. Meeting the Mentor
5. Crossing the Threshold

## Act II: Initiation
6. Tests, Allies, Enemies
7. Approach to Inmost Cave
8. Ordeal
9. Reward

## Act III: Return
10. The Road Back
11. Resurrection
12. Return with Elixir
```

### Fichtean Curve
```markdown
- Opening crisis
- Rising crises (2-4 major ones)
- Each crisis worse than last
- Escalating tension
- Climax
- Brief falling action
- Resolution
```

### Kishotenketsu (Japanese 4-Act)
```markdown
## Ki (Introduction) - 25%
- Establish status quo
- Introduce characters
- Set scene and mood

## Sho (Development) - 25%
- Develop situation
- Build on introduction
- No major conflict yet

## Ten (Twist) - 25%
- Introduce unexpected element
- Shift perspective
- Change direction

## Ketsu (Conclusion) - 25%
- Resolve tension from twist
- Harmonize elements
- Reconcile contradiction
- New understanding
```

---

## File Structure

```
[novel-name]/
├── README.md
├── concept.md (Steps 1-4)
├── synopsis.md (Step 5)
├── structure.md (Steps 7, chosen framework)
├── characters/
│   ├── protagonist.md
│   ├── antagonist.md
│   └── supporting-cast.md
├── subplots.md
├── chapters/
│   ├── ch01-summary.md
│   ├── ch02-summary.md
│   └── ...
├── scene-briefs.md (or scenes/ folder)
├── scene-tracker.md
├── draft/
│   ├── scenes/
│   │   ├── ch01-scene01-draft.md
│   │   └── ...
│   ├── chapters/
│   │   ├── chapter-01.md
│   │   └── ...
│   └── acts/
│       ├── act-i.md
│       ├── act-ii.md
│       └── act-iii.md
├── drafting-notes.md
├── analysis/
│   ├── scene-analysis.md
│   └── pattern-analysis.md
├── revisions/
│   └── revision-notes.md
└── final/
    └── [novel-name]-manuscript.md
```

---

## Example Sessions

### Starting New Novel

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/NOVEL-BOOTSTRAP.md

# New Novel: The Memory Thief

One-sentence premise: A memory thief must recover her own stolen past 
before she forgets who she truly is.

Target length: 80,000 words
Structure: Save the Cat beat sheet

Begin Snowflake development.
```

### Scene Brief Development

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/NOVEL-BOOTSTRAP.md
Load story-engine/bootstraps/SCENE-WORKFLOW.md

# Novel: The Memory Thief - Scene Brief Development

Project: _drafts/memory-thief/
Load chapter summaries.
Break all chapters into atomic scene briefs.
Create complete scene tracker.
```

### Scene Drafting Phase

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/NOVEL-BOOTSTRAP.md

# Novel: The Memory Thief - Draft Chapter 3

Project: _drafts/memory-thief/
Load scene-briefs.md and scene-tracker.md
Draft scenes for Chapter 3 using per-scene authorship decisions.
```

### Continuing Novel Development

```
Connect to my Workbench repo on GitHub.

Load and follow story-engine/bootstraps/NOVEL-BOOTSTRAP.md

# Novel: The Memory Thief

Load artifacts: _drafts/memory-thief/
Report current phase and resume from last save point.
```

---

## Working Principles

- **Fractal building**: Each expansion reveals more detail
- **Top-down design**: Big picture first, details last
- **Scene atomicity**: Each scene is complete unit with Goal-Conflict-Disaster or Reaction-Dilemma-Decision
- **Structure flexibility**: Choose structure that serves story
- **Complete planning before drafting**: All scene briefs validated before any prose
- **Per-scene authorship**: Choose human/AI approach per scene
- **Analysis at all levels**: Macro and micro
- **Iterate freely**: Adjust outline as you learn
- **Trust the process**: Snowflake method works

---

## Commit Message Standards

- "Initialize novel: [Novel Name]"
- "Snowflake Step X: [description]"
- "Add chapter summaries for [Novel Name]"
- "Create scene briefs for [Novel Name]: Chapters X-Y"
- "Create scene tracker for [Novel Name]"
- "Draft [Novel Name]: Chapter X, Scene Y - [scene title]"
- "Assemble [Novel Name]: Chapter X"
- "Analyze scenes: [Novel Name] Chapter X"
- "Revise [Novel Name]: [specific work]"

---

## Version History

**v1.1** - December 24, 2025
- Integrated SCENE-WORKFLOW.md for atomic scene planning
- Updated Phase 4 (Step 10) with complete scene brief development
- Added per-scene authorship flexibility in Phase 5 (Step 11)
- Emphasized complete planning before drafting
- Added scene-level review protocol
- Updated file structure to include scene briefs and tracker

**v1.0** - December 23, 2025  
Initial NOVEL-BOOTSTRAP created

---

**Bootstrap Version**: 1.1  
**Author**: Doug Langille  
**Repository**: github.com/douglangille/Workbench