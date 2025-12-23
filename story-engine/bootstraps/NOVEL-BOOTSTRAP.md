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

### Phase 1: CONCEPT (Snowflake Steps 1-3)
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

### Phase 2: EXPANSION (Snowflake Steps 4-5)
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

### Phase 3: CHAPTER STRUCTURE (Snowflake Steps 6-7)
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

### Phase 4: SCENE BREAKDOWN (Snowflake Step 8)
**Goal**: Fractal expansion to atomic scene level

**Tasks**:

**Step 11: Scene List Per Chapter**
- Break each chapter into scenes
- Scene = one continuous unit of action/time/place
- Typical chapter: 2-5 scenes
- Each scene should:
  - Advance plot OR
  - Develop character OR
  - Both

**Step 12: Scene vs. Sequel Pattern**
- **Scene**: Action, conflict, goal pursuit
  - Goal
  - Conflict
  - Disaster (things go wrong)
- **Sequel**: Reaction, processing, decision
  - Reaction (emotional response)
  - Dilemma (what now?)
  - Decision (new goal)
- Alternate scenes and sequels for pacing
- Mark each unit as SCENE or SEQUEL

**Step 13: Scene Briefs**
- Create detailed brief for each scene/sequel:
  
  **Scene Brief Template:**
  ```markdown
  ## Chapter X, Scene Y: [Scene Name]
  
  **Type**: SCENE / SEQUEL
  **POV**: [Character name]
  **Setting**: [Where/when]
  **Characters Present**: [List]
  **Word Count Target**: [X words]
  
  ### Scene Structure (if SCENE):
  - **Goal**: [What POV character wants]
  - **Conflict**: [What opposes them]
  - **Disaster**: [How it goes wrong]
  
  ### Sequel Structure (if SEQUEL):
  - **Reaction**: [Emotional response]
  - **Dilemma**: [The problem]
  - **Decision**: [New course of action]
  
  ### Key Elements:
  - **Plot advance**: [What moves story forward]
  - **Character reveal**: [What we learn]
  - **Tension**: [Source of conflict]
  - **Atmosphere**: [Mood/tone]
  - **Foreshadowing**: [If any]
  
  ### Scene Opening:
  [How this scene begins - first line or two]
  
  ### Scene Ending:
  [How this scene ends - hook or transition]
  
  ### Notes:
  [Any other important details]
  ```

**Step 14: Scene Sequence Validation**
- Read through all scene briefs in order
- Check for:
  - Logical flow
  - Pacing (scene/sequel balance)
  - Character arc progression
  - Plot continuity
  - Tension escalation
  - Subplot integration
- Adjust as needed

**Step 15: Get Author Approval**
- Review complete scene structure
- This is the blueprint for drafting
- Changes now are easier than later

**Deliverables**:
- `scenes/` folder with all scene briefs
- `scene-sequence.md` (full list in order)
- Author approval to proceed to drafting

**Status Check**: ✅ Complete when all scenes planned and approved

---

### Phase 5: DRAFTING (Snowflake Steps 9-10)
**Goal**: Write prose from scene briefs

**Tasks**:

**Step 16: Draft Scenes**
- Work scene by scene (or out of order if preferred)
- Each scene brief becomes full prose
- Drafting options:
  - **Human draft**: Author writes
  - **AI-assisted draft**: AI drafts from brief, author revises
  - **Hybrid**: AI drafts, human rewrites
- Track completion per scene

**Step 17: Chapter Assembly**
- Assemble completed scenes into chapters
- Check transitions between scenes
- Ensure chapter unity
- Verify chapter arc

**Step 18: Act Assembly**
- Assemble completed chapters into acts
- Read each act as continuous text
- Check pacing across act
- Verify act structure

**Working Method**:
- Draft linearly or by priority
- Don't over-revise during drafting
- Mark problem areas with [NOTE]
- Keep momentum
- Commit completed scenes to GitHub
- Save point after each chapter

**Deliverables**:
- `draft/scenes/` - completed scene drafts
- `draft/chapters/` - assembled chapters
- `drafting-notes.md` - progress and decisions

**Status Check**: ✅ Complete when full draft exists

---

### Phase 6: SCENE-LEVEL ANALYSIS
**Goal**: Analyze and revise at atomic level

**Tasks**:

**Step 19: Scene-by-Scene Analysis**
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

**Step 20: Scene Revision**
- Revise scenes based on analysis:
  - Strengthen weak goals
  - Heighten conflict
  - Sharpen disasters
  - Clarify decisions
  - Enhance character voice
  - Tighten prose

**Step 21: Pattern Analysis**
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

**Step 22: Full Read-Through**
- Read entire novel start to finish
- Note:
  - Continuity errors
  - Pacing issues
  - Character inconsistencies
  - Plot holes
  - Tonal shifts

**Step 23: Macro Revision**
- Address structural issues:
  - Reorder scenes/chapters if needed
  - Cut unnecessary scenes
  - Add missing scenes
  - Strengthen act breaks
  - Enhance climax

**Step 24: Line-Level Polish**
- Polish prose:
  - Tighten sentences
  - Enhance descriptions
  - Sharpen dialogue
  - Strengthen voice
  - Cut redundancy

**Step 25: Final Technical Pass**
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
├── scenes/
│   ├── ch01-scene01-brief.md
│   ├── ch01-scene02-brief.md
│   └── ...
├── draft/
│   ├── scenes/
│   │   ├── ch01-scene01-draft.md
│   │   └── ...
│   └── chapters/
│       ├── chapter-01.md
│       └── ...
├── analysis/
│   ├── scene-analysis.md
│   └── pattern-analysis.md
├── revisions/
│   └── revision-notes.md
└── final/
    └── [novel-name]-manuscript.md
```

---

## Example Session

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
- **Scene atomicity**: Each scene is complete unit
- **Structure flexibility**: Choose structure that serves story
- **Analysis at all levels**: Macro and micro
- **Iterate freely**: Adjust outline as you learn
- **Trust the process**: Snowflake method works

---

## Commit Message Standards

- "Initialize novel: [Novel Name]"
- "Snowflake Step X: [description]"
- "Add chapter summaries for [Novel Name]"
- "Create scene briefs: Chapters X-Y"
- "Draft scenes: Chapter X"
- "Analyze scenes: Chapter X"
- "Revise [Novel Name]: [specific work]"

---

**Bootstrap Version**: 1.0  
**Created**: December 23, 2025  
**Author**: Douglas Langille  
**Repository**: github.com/douglangille/Workbench
