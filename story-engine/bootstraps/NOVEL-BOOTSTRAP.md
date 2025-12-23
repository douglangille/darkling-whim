<!--
STORY ENGINE: NOVEL BOOTSTRAP

PURPOSE:
Manage long-form work (50,000+ words).
Coordinate multiple acts, chapters, subplots, and character arcs.

USE WHEN:
- Writing a novel
- Managing complex long-form narrative
- Coordinating multiple plot threads
- Tracking extensive character development

SESSION STARTUP:
  Connect to Workbench.
  Load story-engine/bootstraps/NOVEL-BOOTSTRAP.md
  
  # Novel: [Title]
  Initialize novel project.
  
  OR
  
  # Novel: [Title]
  Load _drafts/[novel-name]/ and report status.

OUTPUT:
- Novel outline and structure
- Act/chapter management
- Subplot coordination
- Character arc tracking
- Pacing and momentum tools
-->

# Novel Bootstrap

## Role

You are managing a novel - coordinating complex structure, multiple arcs, and long-form pacing.

## Working Principles

- **Structure supports story**: Clear architecture
- **Multiple threads**: Weave plots, subplots, character arcs
- **Pacing over length**: Maintain momentum across 50,000+ words
- **Modular work**: Build chapter by chapter
- **Living outline**: Structure evolves as you write

## File Structure

```
_drafts/[novel-name]/
├── README.md (project overview)
├── novel-bible.md (complete reference)
├── premise.md (core concept)
├── structure/
│   ├── outline.md (overall structure)
│   ├── act-breakdown.md
│   ├── chapter-tracker.md
│   └── pacing-notes.md
├── characters/
│   ├── character-tracker.md
│   ├── [character-name].md (profiles)
│   └── relationships.md
├── plots/
│   ├── main-plot.md
│   ├── subplot-[name].md
│   └── thread-tracker.md
├── world/
│   └── [world-building docs]
├── chapters/
│   ├── 01-[title]/
│   │   ├── outline.md
│   │   ├── draft.md
│   │   └── notes.md
│   ├── 02-[title]/
│   └── ...
├── continuity/
│   ├── timeline.md
│   └── continuity-log.md
└── manuscript/
    └── complete-draft.md (assembled novel)
```

## Workflow Phases

### Phase 1: FOUNDATION

**Goal:** Establish novel concept and scope

**Tasks:**
1. Develop premise (may use IDEATION-BOOTSTRAP first)
2. Determine target length:
   - Standard novel: 70,000-100,000 words
   - Genre considerations
   - Story needs
3. Identify core elements:
   - Protagonist and key characters
   - Central conflict
   - Main plot arc
   - Major subplots
   - World/setting
   - Themes
4. Create project README

**Deliverables:**
- `README.md`
- `premise.md`

---

### Phase 2: STRUCTURE PLANNING

**Goal:** Design novel architecture

#### A. Act Structure

**Three-Act (classic):**
- Act I (25%): Setup, inciting incident
- Act II (50%): Rising action, midpoint reversal
- Act III (25%): Climax, resolution

**Or alternate structure:**
- Four-act
- Five-act
- Hero's Journey
- Other frameworks

#### B. Chapter Planning

**Determine:**
- Estimated chapter count
- Average chapter length
- Chapter purposes/beats
- POV structure
- Timeline/chronology

**Create chapter outline:**
- Chapter number/title
- Act placement
- POV character
- Time/place
- Plot beats
- Chapter arc
- Word count target

#### C. Pacing Strategy

**Plan momentum:**
- Act pacing rhythm
- Key story beats placement
- Tension/release patterns
- Subplot integration timing
- Midpoint considerations
- Climax positioning

**Deliverables:**
- `structure/outline.md`
- `structure/act-breakdown.md`
- `structure/chapter-tracker.md`
- `structure/pacing-notes.md`

---

### Phase 3: CHARACTER DEVELOPMENT

**Goal:** Develop complete character arcs

**For each major character:**
- Full background
- Goals and motivations
- Internal and external conflicts
- Character arc across novel
- Key development beats by chapter
- Relationships with other characters
- Voice and mannerisms
- Growth/change trajectory

**Track:**
- Character state per chapter
- Relationship evolution
- Arc milestones

**Deliverables:**
- `characters/character-tracker.md`
- Individual character files
- `characters/relationships.md`

---

### Phase 4: PLOT COORDINATION

**Goal:** Weave multiple plot threads

#### Main Plot
- Central conflict
- Major plot points
- Escalation strategy
- Climax and resolution

#### Subplots
For each subplot:
- What is it?
- Which characters involved?
- When does it start/resolve?
- How does it intersect main plot?
- Thematic connection?

#### Thread Tracking
- Active threads by chapter
- Thread intersections
- Pacing of revelations
- Setup/payoff tracking

**Deliverables:**
- `plots/main-plot.md`
- `plots/subplot-[name].md` for each
- `plots/thread-tracker.md`

---

### Phase 5: WORLD-BUILDING

**Goal:** Establish consistent setting

**Develop as needed:**
- Locations
- Rules (if speculative)
- History/backstory
- Culture and society
- Technology/magic
- Reference for consistency

**(May integrate with UNIVERSE-BOOTSTRAP if extensive)**

**Deliverables:** `world/` documentation

---

### Phase 6: CHAPTER DRAFTING

**Goal:** Write the novel chapter by chapter

**For each chapter:**

1. **Plan:**
   - Review chapter outline
   - Confirm plot beats
   - Check character states
   - Note continuity needs

2. **Draft:**
   - Write complete chapter
   - Hit planned beats
   - Maintain voice
   - End with hook/transition
   - (May use DRAFTING-BOOTSTRAP internally)

3. **Document:**
   - Update chapter tracker (status: drafted)
   - Note any deviations from outline
   - Update thread tracker
   - Update character states
   - Log continuity elements

4. **Commit:** Save chapter to GitHub

**Work sequentially or modularly as needed**

**Deliverables:**
- Drafted chapters in `chapters/[number]-[title]/draft.md`
- Updated trackers

---

### Phase 7: CONTINUITY MAINTENANCE

**Ongoing throughout drafting:**

**Track:**
- Timeline of events
- Character locations/states
- Plot thread status
- World-building details
- Setups needing payoffs
- Contradictions to resolve

**Tools:**
- `continuity/timeline.md`
- `continuity/continuity-log.md`

---

### Phase 8: MANUSCRIPT ASSEMBLY

**Goal:** Create complete draft

**Tasks:**
1. Assemble all chapters in order
2. Add front matter (title page, etc)
3. Check chapter transitions
4. Verify arc completions
5. Check pacing across full length
6. Create complete draft file

**Deliverables:** `manuscript/complete-draft.md`

---

### Phase 9: NOVEL REVISION

**Goal:** Polish complete manuscript

**Approach:**
- May use REVISION-BOOTSTRAP at novel scale
- Focus on:
  - Overall pacing
  - Arc completions
  - Thread resolution
  - Character consistency
  - Prose quality
  - Structural issues

**Multiple passes likely needed**

---

## Session Types

### Initialize Novel
```
# Novel: [Title]
Initialize novel project.
Target length: [word count]
Genre: [genre]
```

### Structure Planning
```
# Novel: [Title]
Load novel and develop structure.
Focus: [acts / chapters / pacing]
```

### Character Development
```
# Novel: [Title]
Load novel and develop characters.
```

### Draft Chapter
```
# Novel: [Title] - Chapter [X]
Load novel and draft chapter [X]: [title]
```

### Update Tracking
```
# Novel: [Title]
Load novel and update trackers.
Completed: Chapter [X]
```

### Status Review
```
# Novel: [Title]
Load novel and report status.
```

### Assemble Manuscript
```
# Novel: [Title]
Load novel and assemble complete manuscript.
```

## Commit Standards

- "Initialize novel project: [Title]"
- "Add structure outline for [Title]"
- "Develop characters for [Title]"
- "Plan subplot: [subplot name]"
- "Draft chapter [X]: [title]"
- "Update [Title] continuity and trackers"
- "Assemble complete manuscript: [Title]"

## Word Count Tracking

**Monitor progress:**
- Target novel length
- Current total
- Per-act targets and actuals
- Per-chapter actuals
- Remaining needed

**Track in chapter-tracker.md**

## Integration with Other Bootstraps

**Novel + Ideation:**
Use IDEATION first to develop premise

**Novel + Universe:**
Reference universe bible for world-building

**Novel + Drafting:**
Use DRAFTING for individual chapters

**Novel + Revision:**
Use REVISION for polishing complete manuscript

**Novel + Serial:**
Can manage novel as series of chapters
