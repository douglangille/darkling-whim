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

### Phase 2: STRUCTURE PLANNING & SCENE BRIEFS
**Goal**: Design expanded story architecture with atomic scene-level detail

**Reference**: Load and review `story-engine/bootstraps/SCENE-WORKFLOW.md` for complete scene brief protocol

**Tasks**:

**2A. Map Original Story Structure**:
1. Break original into atomic scenes:
   - Identify current Scenes (Goal-Conflict-Disaster)
   - Identify current Sequels (Reaction-Dilemma-Decision)
   - Note what's compressed or implied
   - Create briefs for original scenes (mark as "preserved" or "anchor")
2. Analyze original:
   - Current word count per scene
   - Current pacing
   - Structural gaps where expansion could occur

**2B. Design Expansion Structure**:
1. Plan new scenes:
   - Where do new Scenes/Sequels fit?
     - Before original scenes (setup/backstory)
     - Between original scenes (unpacking compressed moments)
     - After original scenes (extended resolution)
   - How do new scenes connect to preserved scenes?
   - Estimated new scene count
2. Character development through scenes:
   - Which new scenes reveal backstory?
   - Which scenes develop relationships?
   - Which scenes expand internal conflict?
   - Which scenes clarify goals/motivations?
3. World-building through scenes:
   - Which scenes establish setting details?
   - Which scenes explore world rules?
   - Which scenes deepen atmosphere?
4. Subplot integration (if any):
   - Which new scenes carry subplot?
   - How does subplot interweave with main plot?
   - Subplot resolution timing

**2C. Motivation Integrity Check**:

Before finalizing scene briefs, verify expansion preserves original's core motivations:

**Checklist**:
- [ ] Does expansion change WHY characters act?
- [ ] Are accidental discoveries still accidental?
- [ ] Do new scenes add mission objectives that weren't there originally?
- [ ] Would the original author recognize the character's decision-making process?
- [ ] Does reactive character remain reactive (or vice versa)?

**Warning Signs of Motivation Drift**:
- ❌ Adding "heist objectives" to characters who were wandering/exploring
- ❌ Making deliberate what was originally spontaneous
- ❌ Turning reactive characters into planners (or planners into reactive)
- ❌ Adding "because I planned this" explanations to serendipitous discoveries
- ❌ Replacing "stumbled upon" with "infiltrated to find"

**How to Fix Motivation Drift**:
1. Re-read original's key decision points
2. Ask: "Is this character SEEKING or DISCOVERING?"
3. If discovering: preserve the accident, expand the recognition/response
4. If seeking: preserve the goal, expand the pursuit/obstacles
5. Revise new scene briefs to match original causality pattern

**Example - Thoughtful Magic**:
- ❌ **Wrong**: Amy infiltrates party on mission to steal intel
- ✅ **Right**: Amy wanders to party seeking distraction, accidentally discovers truth

If motivations have drifted, revise expansion plan before proceeding to scene briefs.

**2D. Create Complete Scene Brief List**:
1. **Number all scenes sequentially** (preserved + new):
   - Example: Scene 1 (new), Scene 2 (preserved), Scene 3 (new), Scene 4 (new), Scene 5 (preserved), etc.
2. **Create briefs for NEW scenes only**:
   - Use Scene Brief Template from SCENE-WORKFLOW.md
   - Define Goal/Conflict/Disaster OR Reaction/Dilemma/Decision
   - Specify POV, setting, connections
   - Estimate word count per scene
   - Note how scene serves expansion goals
3. **Mark preserved scenes**:
   - "Scene X (Preserved): [Original scene title]"
   - Note word count of original
   - Identify connection points with new scenes
4. **Validate integrated scene chain**:
   - Check: New scenes connect properly to preserved scenes
   - Check: Disaster → Reaction flow maintained
   - Check: Decision → Goal flow maintained
   - Check: Overall escalation preserved
   - Adjust briefs as needed
5. **Make authorship decisions for new scenes**:
   - For each NEW scene, decide:
     - [ ] Human First Draft (author writes, AI reviews)
     - [ ] AI First Draft (AI writes, author edits)
     - [ ] TBD (decide later)
   - Mark in each scene brief
   - Preserved scenes already have authorship (original author)
6. **Create scene tracker**:
   - Use Scene Tracker Template from SCENE-WORKFLOW.md
   - List all scenes (preserved + new)
   - Track status, authorship, word counts
   - Mark preserved scenes clearly

**Ending Scene Best Practices**:

Final scenes in expansions must be **demonstrative, not promissory**.

**Weak ending patterns to avoid**:
- ❌ "They discussed what to do next"
- ❌ "She began to plan her strategy"
- ❌ "Everything was about to change"
- ❌ "He decided to take action"

**Strong ending patterns**:
- ✅ Character takes concrete first action of their plan
- ✅ Character makes choice that demonstrates growth through specific act
- ✅ Character sends/says/does something specific with immediate consequences
- ✅ Character executes opening move that begins the "next chapter"

**Example - Thoughtful Magic**:
- ❌ **Weak**: "Amy gathered her team and began planning how to use this knowledge."
- ✅ **Strong**: Amy drafts and sends the first anonymous message to Tim: "Mr. Brandt, the Crimson Syndicate meets Thursday..."

**Why This Matters**: 
- Readers should see the strategy in action, not just hear it described
- Endings should plant story seeds, not just announce planting season
- Show the first domino falling, don't just describe the domino setup

**2E. Estimate & Approve**:
1. Calculate final word count:
   - Preserved scenes: [X words]
   - New scenes: [Y words estimated]
   - Total: [X + Y]
2. Verify expansion factor:
   - Original: [A words]
   - Expanded: [B words]
   - Factor: [B/A]x
3. **GET AUTHOR APPROVAL**:
   - Review complete scene brief list
   - Confirm preservation strategy
   - Approve expansion approach
   - Commit to GitHub before drafting

**DO NOT DRAFT NEW PROSE YET**—all scene briefs must be complete and validated first

**Deliverables**:
- `expansion-plan.md` (high-level expansion strategy)
- `scene-briefs.md` (complete scene list: preserved + new scene briefs) OR
- `scenes/` folder (individual scene brief files)
- `scene-tracker.md` (progress tracking table)

**Status Check**: 
- ✅ Original scenes identified and mapped
- ✅ All new scene briefs created
- ✅ Scene chain validated (preserved + new)
- ✅ Motivation integrity verified
- ✅ Authorship decisions made for new scenes
- ✅ Author approved

---

### Phase 3: INCREMENTAL BUILDING
**Goal**: Draft new scenes, integrate with preserved material

**Reference**: Use Scene Drafting Protocol from `SCENE-WORKFLOW.md`

**Tasks**:

**3A. Preserve Original Scenes as Anchors**:
1. Copy original scene text into working draft
2. Mark clearly: "[PRESERVED SCENE X: Original Title]"
3. These act as anchors for new material
4. Voice reference for new scenes

**3B. Draft New Scenes**:
1. **Work through new scenes** (in sequence or strategic order):
   - Review scene brief before drafting
   - Confirm Goal/Conflict/Disaster or Reaction/Dilemma/Decision
   - Check connections to preserved and other new scenes
   - Note where scene integrates with preserved material

2. **Execute drafting per scene's authorship choice**:

   **If Human First Draft**:
   - Author writes the new scene
   - Match voice/tone to preserved scenes
   - Hit structural beats from brief
   - AI reviews for: voice consistency with original, structure integrity, integration smoothness
   - AI suggests improvements (author decides)

   **If AI First Draft**:
   - AI drafts new scene from brief
   - AI matches voice/tone to preserved scenes
   - AI hits structural beats
   - Author reviews for: authenticity, character truth, voice match
   - Author edits/rewrites as needed

3. **Scene-level review after each new draft**:
   - **Structure Check**:
     - [ ] Scene fulfills the brief?
     - [ ] Goal/Conflict/Disaster clear? (if Scene)
     - [ ] Reaction/Dilemma/Decision clear? (if Sequel)
     - [ ] Connects to adjacent preserved/new scenes?
   - **Voice Consistency Check** (critical for expansion):
     - [ ] Matches original story's voice?
     - [ ] Tone consistent with preserved scenes?
     - [ ] Style feels seamless?
     - [ ] Would reader know this is new material?
   - **Integration Check**:
     - [ ] Transitions smoothly from preserved scenes?
     - [ ] Sets up next scene properly?
     - [ ] Character knowledge consistent?
     - [ ] Timeline coherent?

4. **Update tracking**:
   - Mark scene status in scene tracker
   - Note actual word count
   - Flag any integration issues
   - Update expansion notes

5. **Commit to GitHub**:
   - Save new scene draft
   - Commit message: "Expand [Story Name]: Scene [X] - [new scene title]"
   - Create save points frequently

**3C. Integration as You Go**:
1. As each new scene is drafted:
   - Insert into working draft at correct position
   - Check transitions with adjacent scenes
   - Verify continuity
   - Ensure pacing flows
2. Document integration decisions in expansion-notes.md:
   - What was added and why
   - How it serves the expansion goals
   - Any deviations from plan
   - Problems solved
   - New opportunities discovered

**Working Principles**:
- Preserve original scenes as written (voice anchors)
- Draft new scenes one at a time
- Match voice to original meticulously
- Check integration with preserved material constantly
- Scene briefs can be adjusted if story evolves
- Maintain expansion momentum

**Deliverables**:
- `working-[filename].md` (expanded draft: preserved + new scenes)
- `expansion-notes.md` (decision log)

**Status Check**: ✅ Complete when all new scenes drafted and integrated

---

### Phase 4: INTEGRATION & POLISH
**Goal**: Unify expanded elements into cohesive whole

**Tasks**:
1. Read through complete expanded draft
2. Check for:
   - Voice consistency throughout (new material sounds like original)
   - Pacing across new length
   - Transition smoothness (especially at preserved/new boundaries)
   - Character arc coherence
   - Thematic unity
   - Tonal consistency
3. Polish pass:
   - Refine new material
   - Smooth integration points
   - Adjust pacing as needed
   - Strengthen connections
   - May need minor tweaks to preserved scenes (transitions only)
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

- **Plan completely, then draft**: All scene briefs (preserved + new) before any new prose
- **Preserve essence**: Don't lose what made original work
- **Expand naturally**: Growth should feel inevitable, not padded
- **Maintain voice**: New material must sound like same author/story
- **Serve the story**: Only add what makes story better
- **Honor original**: Original readers should recognize the core
- **Think structurally**: Expansion changes pacing and rhythm
- **Use anchors**: Preserved scenes guide voice for new scenes
- **Flex authorship**: Use human/AI strengths per new scene
- **Guard motivations**: Preserve why characters act, not just what they do
- **Show the move**: Endings demonstrate, they don't just promise

---

## File Structure

Project folder: `_drafts/[story-name]/`

```
[story-name]/
├── README.md
├── original-[filename].md
├── foundation.md
├── expansion-plan.md
├── scene-briefs.md (or scenes/ folder)
├── scene-tracker.md
├── expansion-notes.md
└── working-[filename].md
```

Optionally include:
- `assessment.md` (from ASSESSMENT-BOOTSTRAP)
- `character-notes.md` (if extensive character development)
- `world-notes.md` (if significant world-building)

---

## Example Sessions

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

### Scene Brief Development Phase

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/EXPANSION-BOOTSTRAP.md
Load story-engine/bootstraps/SCENE-WORKFLOW.md

# Expand: Mitzy - Scene Brief Development

Project: _drafts/mitzy/
Load original and expansion-plan.md
Break into atomic scenes (preserved + new).
Create scene briefs for new material.
```

### Scene Drafting Phase

```
Connect to my Workbench repo on GitHub.

Load story-engine/bootstraps/EXPANSION-BOOTSTRAP.md

# Expand: Mitzy - Draft New Scene 3

Project: _drafts/mitzy/
Load scene-briefs.md and scene-tracker.md
Draft Scene 3 (new material) using [Human/AI] first draft approach.
Integrate with preserved Scene 2.
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
- Current scene count: [Y atomic scenes]
- Target scope: [Short/Novelette/etc]
- Target word count: [Z words]
- Expansion factor: [Z/X]x

## Preserve (Do Not Change)

### Core Scenes (will be preserved as anchors)
1. **Scene [X]**: [Brief description] - [words]
2. **Scene [Y]**: [Brief description] - [words]

### Voice & Style
- [Key voice characteristics to maintain]
- [Style elements that define the work]
- [POV, tense, narrative distance]

### Character Essence
- [Character 1]: [Essential traits to preserve]
- [Character 2]: [Essential traits to preserve]

### Atmosphere
- [Mood/tone that must persist]

### Causality & Motivation (from ASSESSMENT)
- [Note if discoveries are accidental vs. deliberate]
- [Note if character is proactive vs. reactive]
- [Flag what must be preserved to maintain story's magic]

## Expand (Development Targets)

### New Scenes Needed
1. **New Scene [A]**: [Purpose] - Insert [before/after/between] Scene [X]
2. **New Scene [B]**: [Purpose] - Insert [before/after/between] Scene [Y]
3. **New Scene [C]**: [Purpose] - Insert [before/after/between] Scene [Z]

### Character Development
- **[Character 1]**: [What to develop] - via Scenes [list]
- **[Character 2]**: [What to develop] - via Scenes [list]

### World-Building
- [Element to explore] - via Scene [X]
- [Detail to establish] - via Scene [Y]
- [Context to provide] - via Scene [Z]

### Backstory to Reveal
- [What happened before] - revealed in Scene [X]
- [Character history] - revealed in Scene [Y]

### Emotional Beats to Extend
- [Beat 1]: [How to deepen] - via new Sequel after Scene [X]
- [Beat 2]: [How to deepen] - via new Scene [Y]

## Integration Strategy

### Scene Chain (Preserved + New)
- Scene 1: [Preserved/New] - [Brief title]
- Scene 2: [Preserved/New] - [Brief title]
- Scene 3: [Preserved/New] - [Brief title]
[Continue for all scenes...]

### Voice Anchors
[How preserved scenes will guide voice for new material]

### Transition Points
[Key places where new material connects to preserved scenes]
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
- Preserve: 1-2 core scenes (~500 words)
- Add: 5-7 new scenes (~3,500 words)
- Focus: Deepen 1-2 characters, expand key emotional beats

### Short → Novelette (5,000 → 12,000 words)
- Preserve: 3-5 core scenes (~5,000 words)
- Add: 8-12 new scenes (~7,000 words)
- Focus: Add subplot, develop secondary characters, expand setting

### Novelette → Novella (15,000 → 30,000 words)
- Preserve: 10-15 core scenes (~15,000 words)
- Add: 15-25 new scenes (~15,000 words)
- Focus: Multiple subplots, full character arcs, rich world-building

---

## Commit Message Standards

**Foundation phase**:
- "Initialize [Story Name] expansion project"
- "Document expansion foundation for [Story Name]"

**Planning phase**:
- "Add expansion plan for [Story Name]"
- "Add scene briefs for [Story Name] expansion"
- "Create scene tracker for [Story Name] expansion"

**Building phase**:
- "Expand [Story Name]: Scene [X] - [new scene title]"
- "Integrate [Story Name]: Scene [X] with preserved material"
- "Update scene tracker: [progress summary]"

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
**Progress**: 
- Preserved scenes: [X scenes / Y words]
- New scenes briefed: [A of B]
- New scenes drafted: [C of B]
- Current total word count: [X+C words / Target]
**Last Completed**: [What was just finished]
**Next Steps**: [What to draft/integrate next]
**Voice Check**: [How well new material matches original]
**Integration Notes**: [How new scenes are fitting with preserved]
**Open Questions**: [Any unresolved items]
**Session Duration**: [Approximate time]
**Commits Made**: [List of commits]

**To Resume**: [Specific instruction for next session]
```

---

## Version History

**v1.2** - December 29, 2025
- Added Motivation Integrity Check (Phase 2C)
- Added Ending Action Beat best practices
- Updated Working Principles with motivation and ending guidance
- Added causality section to foundation template
- Renumbered Phase 2 sections (2C→2D, 2D→2E)

**v1.1** - December 24, 2025
- Integrated SCENE-WORKFLOW.md for atomic scene planning
- Updated Phase 2 with scene brief development for preserved + new scenes
- Updated Phase 3 with per-scene authorship flexibility
- Added scene-level voice consistency checks
- Emphasized preserved scenes as voice anchors

**v1.0** - December 23, 2025  
Initial EXPANSION-BOOTSTRAP created

---

**Bootstrap Version**: 1.2  
**Author**: Doug Langille  
**Repository**: github.com/douglangille/Workbench
