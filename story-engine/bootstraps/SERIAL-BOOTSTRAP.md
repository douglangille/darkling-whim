<!--
STORY ENGINE: SERIAL BOOTSTRAP

PURPOSE:
Manage multi-part stories, series, or episodic fiction.
Track continuity, arcs, and progression across installments.

USE WHEN:
- Writing connected story series
- Managing episodic fiction
- Tracking novel chapters
- Coordinating multi-part narratives

SESSION STARTUP:
  Connect to Workbench.
  Load story-engine/bootstraps/SERIAL-BOOTSTRAP.md
  
  # Serial: [Series Name]
  Initialize series management.
  
  OR
  
  # Serial: [Series Name]
  Load _drafts/[series-name]/ and report status.

OUTPUT:
- Series bible
- Episode/chapter tracking
- Arc management
- Continuity documentation
-->

# Serial Bootstrap

## Role

You are managing a multi-part story - tracking continuity, arcs, and progression across installments.

## Working Principles

- **Series continuity**: Track everything across installments
- **Arc progression**: Overall and per-installment arcs
- **Episodic satisfaction**: Each part complete yet connected
- **Momentum building**: Each part propels to next
- **Easy navigation**: Clear organization for reference

## File Structure

```
_drafts/[series-name]/
├── README.md (series overview)
├── series-bible.md (complete reference)
├── series-outline.md (overall structure)
├── arcs/
│   ├── overall-arc.md
│   └── [arc-name].md (subplot arcs)
├── episodes/ (or chapters/)
│   ├── episode-tracker.md (status overview)
│   ├── 01-[title]/
│   │   ├── outline.md
│   │   ├── draft.md
│   │   └── notes.md
│   ├── 02-[title]/
│   └── ...
├── characters/
│   ├── character-tracker.md
│   └── [character-name].md
├── continuity/
│   ├── timeline.md
│   ├── plot-threads.md
│   └── continuity-log.md
└── world/ (if needed)
    └── [world-building docs]
```

## Workflow Phases

### Phase 1: SERIES FOUNDATION

**Goal:** Establish series structure

**Tasks:**
1. Define series concept:
   - Overall premise
   - Number of installments (planned)
   - Format (episodes/chapters/books)
   - Target audience and scope
2. Outline series arc:
   - Beginning state
   - Major turning points
   - Ending state (or direction)
   - Key milestones
3. Establish structure:
   - Episode/chapter length targets
   - Pacing rhythm
   - Consistency requirements
4. Create README and series-outline.md

**Deliverables:**
- `README.md`
- `series-outline.md`
- `arcs/overall-arc.md`

---

### Phase 2: CHARACTER TRACKING

**Goal:** Manage character development across series

**For each character:**
- Role in series
- Character arc across installments
- Development milestones
- Relationships evolution
- Key moments per episode
- Voice/personality notes
- Continuity details (appearance, habits, etc)

**Track:**
- Character status in each installment
- When characters introduced
- When arcs begin/end
- Relationship changes

**Deliverables:**
- `characters/character-tracker.md`
- Individual character files

---

### Phase 3: ARC MANAGEMENT

**Goal:** Track story threads across installments

#### Overall Arc
- Series beginning, middle, end
- Major plot points
- How arc progresses each installment

#### Subplot Arcs
For each subplot:
- What is it?
- When does it start?
- Which installments does it span?
- Key beats/developments
- When does it resolve?

#### Per-Episode Arcs
- Contained story in each installment
- How it connects to overall arc
- Cliffhangers or hooks to next

**Deliverables:**
- Arc documentation in `arcs/`
- Plot thread tracker

---

### Phase 4: EPISODE/CHAPTER MANAGEMENT

**For each installment:**

#### Planning
1. Episode outline:
   - Place in overall arc
   - Episode-specific story
   - Character development beats
   - Plot thread progression
   - Cliffhanger/hook
2. Continuity check:
   - What must be consistent from previous?
   - What new elements introduced?
   - What threads progress?

#### Drafting
- Use DRAFTING-BOOTSTRAP for individual episodes
- Reference series bible
- Track continuity during writing

#### Post-Draft
- Update character tracker
- Update plot threads
- Update timeline
- Note new continuity elements
- Update episode tracker status

**Deliverables:**
- Complete episode/chapter drafts
- Updated tracking documents

---

### Phase 5: CONTINUITY MAINTENANCE

**Goal:** Keep everything consistent

**Track:**
- Timeline of events
- Plot threads (active, resolved, dormant)
- Character states/locations
- World-building details
- Callbacks and references
- Contradictions to resolve

**Tools:**
- `continuity/timeline.md` - chronological events
- `continuity/plot-threads.md` - active storylines
- `continuity/continuity-log.md` - changes and fixes

**Deliverables:**
- Complete continuity documentation

---

### Phase 6: SERIES BIBLE

**Goal:** Comprehensive reference document

**Contents:**
1. Series overview
2. Overall arc summary
3. Episode/chapter summaries
4. Character reference
5. World-building essentials
6. Timeline
7. Plot thread status
8. Continuity notes
9. Future plans

**Update after each installment**

**Deliverables:** `series-bible.md`

---

## Session Types

### Initialize Series
```
# Serial: [Series Name]
Initialize series management.
Format: [Episodes / Chapters / Books]
Planned installments: [number or "ongoing"]
```

### Plan Episode/Chapter
```
# Serial: [Series Name] - Episode [X]
Load series and plan episode [X]: [title]
```

### Draft Episode/Chapter
```
# Serial: [Series Name] - Episode [X]
Load series and draft episode [X]: [title]
(This may use DRAFTING-BOOTSTRAP internally)
```

### Update Continuity
```
# Serial: [Series Name]
Load series and update continuity.
Just completed: Episode [X]
```

### Series Review
```
# Serial: [Series Name]
Load series and review status.
Report: overall progress, active threads, next installment needs.
```

## Commit Standards

- "Initialize series: [Series Name]"
- "Add series outline for [Series Name]"
- "Plan episode [X]: [title]"
- "Draft episode [X]: [title]"
- "Update [Series Name] continuity after episode [X]"
- "Update [Series Name] series bible"

## Integration with Other Bootstraps

**Serial + Universe:**
Series within shared universe - reference universe bible

**Serial + Drafting:**
Draft individual episodes using DRAFTING-BOOTSTRAP

**Serial + Novel:**
Manage novel as serial chapters

**Workflow:**
1. Initialize series structure
2. Plan overall arc
3. Plan individual episodes
4. Draft episodes (using DRAFTING-BOOTSTRAP)
5. Update continuity after each
6. Maintain series bible
