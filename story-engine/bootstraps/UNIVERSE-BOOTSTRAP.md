<!--
STORY ENGINE: UNIVERSE BOOTSTRAP

PURPOSE:
Build story bibles, world-building documents, and cross-story continuity.
Establish foundations for multiple stories in shared universe.

USE WHEN:
- Creating shared universe for multiple stories
- Need comprehensive world-building
- Managing continuity across stories
- Building series foundation

SESSION STARTUP:
  Connect to Workbench.
  Load story-engine/bootstraps/UNIVERSE-BOOTSTRAP.md
  
  # Universe: [Universe Name]
  Initialize universe building.
  
  OR
  
  # Universe: [Universe Name]
  Load _drafts/[universe-name]/ and report status.

OUTPUT:
- Story bible/universe guide
- Character registry
- World-building documentation
- Timeline/chronology
- Continuity tracking
-->

# Universe Bootstrap

## Role

You are building and maintaining a story universe - the foundation for multiple connected stories.

## Working Principles

- **Consistency is key**: Track everything
- **Allow flexibility**: Don't over-constrain future stories
- **Living document**: Universe grows with stories
- **Easy reference**: Organized for quick lookup
- **Version control**: Track changes to continuity

## File Structure

```
_drafts/[universe-name]/
├── README.md (universe overview)
├── story-bible.md (complete reference)
├── world/
│   ├── overview.md
│   ├── locations.md
│   ├── rules.md (magic/tech/physics)
│   ├── history.md
│   ├── culture.md
│   └── organizations.md
├── characters/
│   ├── registry.md (index)
│   └── [character-name].md (individual profiles)
├── timeline.md
├── stories/
│   ├── chronology.md (story order)
│   └── [story-name]-notes.md (per-story details)
└── continuity-log.md (changes and updates)
```

## Workflow Phases

### Phase 1: FOUNDATION

**Goal:** Establish universe basics

**Tasks:**
1. Define universe scope:
   - Genre/type
   - Core concept
   - What makes it unique?
   - Planned story types
2. Create README with universe overview
3. Set up file structure

---

### Phase 2: WORLD-BUILDING

**Goal:** Establish setting and rules

#### A. World Overview
- Type of world (contemporary/historical/fantasy/SF/etc)
- Core premise
- Scope (single city/planet/galaxy/multiverse)
- Tone and atmosphere

#### B. Locations
For each key location:
- Name and type
- Physical description
- Significance
- Who lives/works there
- Connections to other locations

#### C. Rules and Systems
**If speculative fiction:**
- Magic/tech systems
- How they work
- Limitations/costs
- Who can use them
- Consequences

**Social/political:**
- Power structures
- Important organizations
- Social rules/norms
- Economic systems

#### D. History
- Key historical events
- How past shapes present
- Unresolved historical tensions
- Legends and myths

#### E. Culture
- Languages
- Customs and traditions
- Arts and entertainment  
- Religion/belief systems
- Daily life details

**Deliverables:** Complete `world/` folder

---

### Phase 3: CHARACTER REGISTRY

**Goal:** Track all characters across stories

**For each character:**
- Full name and aliases
- Physical description
- Background/history
- Personality traits
- Abilities/skills
- Relationships
- Story appearances
- Character arc notes
- Important quotes/moments

**Registry organization:**
- Alphabetical index
- By story appearance
- By faction/organization
- By location

**Deliverables:** 
- `characters/registry.md`
- Individual character files

---

### Phase 4: TIMELINE

**Goal:** Track chronology

**Include:**
- Historical events (backstory)
- Story events (plot)
- Character lifecycles
- Clear dating system
- Cross-references to stories

**Format options:**
- Linear chronology
- By story
- By character
- Multiple views for complex timelines

**Deliverables:** `timeline.md`

---

### Phase 5: STORY TRACKING

**Goal:** Manage stories within universe

**For each story:**
- Title and status
- When it takes place (timeline placement)
- Key characters involved
- Locations used
- Plot summary
- Continuity notes
- Connections to other stories
- What new elements it introduces

**Deliverables:**
- `stories/chronology.md`
- Individual story notes

---

### Phase 6: STORY BIBLE COMPILATION

**Goal:** Create comprehensive reference

**Contents:**
1. Universe overview
2. World-building essentials
3. Character registry highlights
4. Timeline summary
5. Story chronology
6. Quick reference sections
7. Index

**Deliverables:** `story-bible.md`

---

### Phase 7: CONTINUITY MAINTENANCE

**Ongoing:**
- Log changes to universe
- Track retcons or revisions
- Note contradictions to resolve
- Version universe elements
- Update bible after each story

**Deliverables:** `continuity-log.md`

---

## Session Types

### Initial Universe Creation
```
# Universe: [Name]
Initialize universe building.
Concept: [brief description]
```

### Adding World-Building
```
# Universe: [Name]
Load universe and expand world-building.
Focus: [specific aspect - locations/rules/history/etc]
```

### Adding Characters
```
# Universe: [Name]
Load universe and add characters.
[List characters to profile]
```

### Adding Story
```
# Universe: [Name]
Load universe and integrate story.
Story: [title and location]
```

### Continuity Check
```
# Universe: [Name]
Load universe and check continuity.
Focus: [what to verify]
```

## Commit Standards

- "Initialize [Universe Name] story bible"
- "Add world-building: [aspect] to [Universe Name]"
- "Add character profiles to [Universe Name]"
- "Update [Universe Name] timeline"
- "Integrate [Story Title] into [Universe Name]"
- "Update [Universe Name] continuity log"

## Integration with Other Bootstraps

**Universe + Ideation:**
Use universe as foundation for new story concepts

**Universe + Drafting:**
Reference universe docs while writing stories

**Universe + Serial:**
Manage connected story series

**Workflow:**
1. Build universe foundation
2. Ideate stories within universe
3. Draft stories referencing bible
4. Update universe with story additions
