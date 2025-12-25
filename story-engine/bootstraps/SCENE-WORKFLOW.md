# Scene Workflow

**Purpose**: Atomic scene brief creation and drafting protocol for systematic prose development

---

## When to Use Scene Briefs

### Scope-Based Decision

**Flash Fiction (<1,000 words)**:
- Scene briefs **optional**
- Flash typically functions as single atomic unit
- Can proceed directly to drafting

**Short Stories and Longer (1,000+ words)**:
- Scene briefs **recommended/standard**
- Enables structural planning before prose commitment
- Maintains continuity across multiple scenes
- Supports hybrid human/AI authorship

### Applicable Workflows

Scene briefs integrate with:
- **DRAFTING-BOOTSTRAP** (Phase 2.5)
- **EXPANSION-BOOTSTRAP** (Phase 2)
- **NOVEL-BOOTSTRAP** (Step 8)
- **REVISION-BOOTSTRAP** (optional, for scene-level rewrites)

---

## File Organization

**Core Principle**: Keep scene briefs and scene drafts in separate files/locations for tight context control.

### Project Structure

```
_drafts/[project-name]/
├── scene-briefs.md              # All briefs in single file (short stories), OR
├── scenes/                       # Individual brief files (novels, long works)
│   ├── ch01-scene01-brief.md
│   ├── ch01-scene02-brief.md
│   ├── ch02-scene01-brief.md
│   └── ...
├── scene-tracker.md             # Progress tracking (optional but recommended)
├── draft/
│   └── scenes/                  # Drafted scene prose (always separate)
│       ├── ch01-scene01-draft.md
│       ├── ch01-scene02-draft.md
│       ├── ch02-scene01-draft.md
│       └── ...
└── [other project files]
```

### Why Separate Briefs from Drafts?

**Context Control**:
- When drafting Scene 3, load:
  - `scenes/ch01-scene03-brief.md` (current instructions)
  - `draft/scenes/ch01-scene02-draft.md` (previous scene for transition)
  - NOT all briefs + all drafts (avoids context bloat)

**Phase Separation**:
- Briefs = planning phase (complete before drafting)
- Drafts = execution phase (one at a time)
- Clear workflow progression

**Status Visibility**:
- Brief exists = planned
- Draft exists = executed
- Easy to see what's done vs. pending

**Iterative Work**:
- Brief might get tweaked during drafting (as story evolves)
- Draft might go through multiple revisions
- Separation preserves original planning intentions

### Typical Session Patterns

**Planning Session**:
```
Load: scene-briefs.md (or scenes/ folder)
Create briefs for Chapter 3, scenes 1-4
Validate scene chain
Commit scene-briefs.md
```

**Drafting Session**:
```
Load: scenes/ch03-scene01-brief.md (instructions)
Load: draft/scenes/ch02-scene04-draft.md (for transition)
Draft ch03-scene01 prose
Save to: draft/scenes/ch03-scene01-draft.md
Commit
```

**Review Session**:
```
Load: draft/scenes/ch03-scene01-draft.md
Load: scenes/ch03-scene01-brief.md (to check fulfillment)
Scene-level review
Revise draft if needed
Commit
```

**Clean, focused, no context pollution.** ✅

---

## Scene vs. Sequel Framework

Based on Randy Ingermanson's atomic scene structure.

### Scene (Proactive)

Characters act to achieve goals. Ends badly.

**Structure**:
1. **Goal**: What does the POV character want in this scene? Must be specific and visible.
2. **Conflict**: What prevents them from getting it? Opposition, obstacles, complications.
3. **Disaster**: How does it go wrong? Setback, failure, or complication that forces change.

**Example**:
- Goal: Sarah must convince the judge to grant custody
- Conflict: Ex-husband's lawyer presents damaging evidence
- Disaster: Judge rules against her, awards custody to ex-husband

### Sequel (Reactive)

Characters process disasters and decide next action. Ends with commitment.

**Structure**:
1. **Reaction**: Emotional response to the previous disaster. Show how it hits them.
2. **Dilemma**: Analyzing bad options. All choices have costs.
3. **Decision**: Character commits to new course of action (becomes Goal of next Scene).

**Example**:
- Reaction: Sarah breaks down in courthouse bathroom, rage and despair
- Dilemma: Accept defeat? Flee with child? Fight dirty like ex-husband?
- Decision: Hire private investigator to find dirt on ex-husband (→ next Scene goal)

### The Chain

Stories alternate between Scenes and Sequels:

```
Scene → Sequel → Scene → Sequel → Scene → Sequel
 |         |       |         |       |         |
Goal    Reaction  Goal    Reaction  Goal    Reaction
 ↓         ↓       ↓         ↓       ↓         ↓
Disaster Decision Disaster Decision Disaster Decision
```

Each Disaster requires a Reaction. Each Decision creates the next Goal.

**Pacing Control**:
- More Scenes = faster pacing (action-heavy)
- More Sequels = slower pacing (introspective)
- Short Sequels = breathless tension
- Long Sequels = emotional depth

---

## Scene Brief Template

Use this template for each atomic scene or sequel:

```markdown
## Scene [Number]: [Short Title]

**Type**: Scene / Sequel

**POV Character**: [Name]

**Setting**: [Location, time of day, atmosphere]

**Word Count Target**: [Estimate]

---

### Structure

#### If Scene (Goal-Conflict-Disaster):

**Goal**: 
[What does the POV character want in this scene? Be specific and visible.]

**Conflict**: 
[What prevents them from getting it? Who or what opposes? What obstacles?]

**Disaster**: 
[How does it go wrong? What's the setback? How does this force change?]

#### If Sequel (Reaction-Dilemma-Decision):

**Reaction**: 
[Emotional response to previous disaster. How does it hit the character?]

**Dilemma**: 
[What are the bad options? What's at stake with each choice?]

**Decision**: 
[What does the character commit to? This becomes the Goal of the next Scene.]

---

**Leads to**: Scene/Sequel [Number]

**Comes from**: Scene/Sequel [Number]

---

### Drafting Information

**Drafting Approach**: [ ] Human First Draft  [ ] AI First Draft  [ ] Collaborative

**Status**: [ ] Brief Only  [ ] Drafted  [ ] Scene-Level Review Complete  [ ] Revised  [ ] Final

**Notes**: 
[Any special considerations, tone requirements, critical details, continuity concerns]
```

---

## Creating Complete Scene Brief Lists

**Core Principle**: Plan all scene briefs BEFORE drafting any prose.

### Process

**Step 1: Story Structure Foundation**
- Identify major story beats (acts, turning points, climax)
- Rough sequence of events
- Key character arcs

**Step 2: Scene Sequence Mapping**
- List all major scenes in sequence
- Identify which are Scenes (proactive) vs. Sequels (reactive)
- Number consecutively

**Step 3: Create Individual Briefs**
- Use template for each scene/sequel
- Fill in Goal-Conflict-Disaster OR Reaction-Dilemma-Decision
- Be specific—vague briefs create vague drafts

**Step 4: Chain Validation** (see next section)

**Step 5: Authorship Decisions**
- Mark each scene's drafting approach
- Consider: complexity, familiarity, energy, experimentation
- No right answer—choose per scene

**Step 6: Review Complete Structure**
- Read through all briefs in sequence
- Check pacing (Scene/Sequel ratio)
- Verify emotional arcs
- Confirm all setups have payoffs
- Adjust briefs as needed

**Do NOT draft prose yet**—all briefs complete and validated first.

---

## Scene Chain Validation

Ensure structural integrity before drafting.

### Validation Checklist

**For Each Scene**:
- [ ] Goal is specific and visible?
- [ ] Conflict actually prevents goal achievement?
- [ ] Disaster is genuine setback (not easy out)?
- [ ] Disaster leads to emotional response (next Sequel)?

**For Each Sequel**:
- [ ] Reaction authentically responds to previous Disaster?
- [ ] Dilemma presents real bad options (not easy choice)?
- [ ] Decision is specific commitment?
- [ ] Decision creates clear Goal for next Scene?

**For Overall Chain**:
- [ ] Every Scene Disaster leads to Sequel Reaction?
- [ ] Every Sequel Decision leads to Scene Goal?
- [ ] No orphaned scenes (unconnected to chain)?
- [ ] Pacing rhythm serves story (not arbitrary)?
- [ ] Character emotional arc tracks through chain?

### Common Chain Breaks

**Missing Sequel**: Scene disaster → immediately to new Scene goal
- Fix: Add Sequel to process disaster emotionally and show decision

**Missing Scene**: Sequel decision → immediately to emotional reaction
- Fix: Add Scene showing goal pursuit and resulting disaster

**Weak Disaster**: Scene ends with partial success or neutral outcome
- Fix: Make disaster worse—genuine setback that creates story problem

**Easy Decision**: Sequel presents false dilemma (one obviously right choice)
- Fix: Make all options bad—force hard choice with real costs

---

## Scene Drafting Protocol

Execute after all scene briefs are complete and validated.

### Per-Scene Process

**1. Review Scene Brief**
- Re-read the brief thoroughly
- Confirm Goal-Conflict-Disaster or Reaction-Dilemma-Decision is clear
- Note any special considerations from Notes field
- Check connection to previous/next scenes

**2. Load Context**
- Load current scene brief: `scenes/[scene-number]-brief.md`
- Load previous scene draft: `draft/scenes/[previous-scene]-draft.md` (for transition)
- Do NOT load all briefs or all drafts (context control)

**3. Execute Drafting Approach**

#### Human First Draft:
```
Author writes complete scene draft.
Then: AI reviews for:
- Structure integrity (does draft fulfill brief?)
- Voice consistency
- Pacing
- Continuity with adjacent scenes
- Suggestions (not prescriptions)
```

#### AI First Draft:
```
AI drafts complete scene from brief.
Then: Author edits/rewrites:
- Voice adjustment to match author style
- Emotional authenticity
- Specific details and grounding
- Any needed structural changes
Author owns final version—not "AI with tweaks"
```

#### Collaborative:
```
Real-time back-and-forth:
- AI drafts paragraph/beat
- Author reviews, edits, directs next section
- Iterative until scene complete
Best for: Complex scenes, learning new techniques
```

**4. Save Draft**
Save to: `draft/scenes/[scene-number]-draft.md`
Separate from brief file

**5. Scene-Level Review**

Check each drafted scene for:
- [ ] **Structure**: Does it deliver on the brief? Goal achieved/denied? Disaster clear?
- [ ] **Voice**: Consistent with previous scenes and overall story voice?
- [ ] **Pacing**: Right rhythm for this moment in story?
- [ ] **Continuity**: Details/emotions match adjacent scenes?
- [ ] **Grounding**: Enough sensory detail and physical reality?
- [ ] **Emotional Truth**: Characters' reactions feel authentic?

**6. Update Status**
- Mark scene as "Drafted" or "Scene-Level Review Complete" in tracker
- Note any issues or revision needs
- Flag if scene needs rework before assembly

**7. Commit Scene Draft**
Commit with clear message:
- "Draft [Project]: Scene [X] - [scene title]"
- "Review [Project]: Scene [X] - structural check"

**8. Proceed to Next Scene**
- Do not skip ahead unless strategic reason
- Maintain sequence for continuity

---

## Scene Tracker Template

Track progress across all scenes in project.

```markdown
# Scene Tracker: [Project Name]

**Total Scenes**: [X]  
**Total Sequels**: [Y]  
**Target Word Count**: [Z]

---

## Progress Summary

- Briefs Complete: X/Total
- Drafted: X/Total
- Scene Review Complete: X/Total
- Final: X/Total

---

## Scene List

| # | Type | Title | Status | Approach | Target | Actual | Issues | Updated |
|---|------|-------|--------|----------|--------|--------|--------|---------||
| 1 | Scene | Opening Hook | Final | Human | 800 | 850 | - | Dec 23 |
| 2 | Sequel | Aftermath | Drafted | AI | 600 | 650 | Needs emotion depth | Dec 23 |
| 3 | Scene | Confrontation | Brief Only | TBD | 1200 | - | - | Dec 22 |
| 4 | Sequel | Dark Choice | Brief Only | TBD | 700 | - | - | Dec 22 |
| 5 | Scene | Point of No Return | Not Started | - | 1500 | - | - | - |

---

## Notes

[Any global notes about pacing, continuity issues, structural concerns, etc.]

---

**Last Updated**: [Date]
```

---

## Integration with Bootstraps

### DRAFTING-BOOTSTRAP
- Scene briefs created in Phase 2.5 (after Outline, before Scene Building)
- Scene drafting executes in Phase 3
- Assembly integrates drafted scenes in Phase 4

### EXPANSION-BOOTSTRAP
- Scene briefs for new material created in Phase 2 (Structure Planning)
- Identify original scenes to preserve
- Scene drafting for new scenes in Phase 3 (Incremental Building)

### NOVEL-BOOTSTRAP
- Scene briefs replace simple scene lists in Snowflake Step 8
- Complete all chapter scene briefs before drafting
- Scene drafting becomes Step 9
- Assembly at chapter and novel level in Step 10

### REVISION-BOOTSTRAP
- Optional: Scene-level analysis in Phase 1
- Scene-level revision plan in Phase 2
- Rewrite specific scenes in Phase 3 (using scene brief + drafting protocol)

---

## FAQ

### When should I use Scene vs. Sequel?

**Use Scene when**: Character is acting to achieve goal, pushing story forward actively.

**Use Sequel when**: Character needs to process what just happened, make hard decision, transition to next action.

**General rhythm**: Big action scenes often need Sequel after to process. Multiple small Scenes in row = breathless pacing. Multiple Sequels in row = introspective, slow (use sparingly).

### Can I combine Scene and Sequel in one unit?

Yes, but be aware you're compressing. Sometimes a character experiences Disaster, has brief Reaction, and immediately commits to new Goal in single scene. This speeds pacing dramatically—use intentionally.

### What if my scene doesn't fit Goal-Conflict-Disaster?

Question whether it's actually a Scene. Could be:
- Sequel (character processing, deciding)
- Exposition dump (usually revise to integrate into Scene/Sequel)
- Transition (consider cutting or folding into adjacent scene)

True Scenes have character wanting something specific, facing opposition, ending badly.

### How long should each brief be?

Brief enough to guide drafting, detailed enough to prevent vagueness.

Typical: 100-200 words per brief. Goal/Conflict/Disaster or Reaction/Dilemma/Decision each get 2-4 sentences.

**Too vague**: "Sarah confronts her ex-husband and it goes badly."
**Good brief**: "Sarah wants ex-husband to admit he's been coaching their daughter against her. He deflects with lawyer-speak and veiled threats. She loses her temper, says things that will be used against her in court."

### Should all scenes have equal word count targets?

No. Action Scenes often shorter (sharp, punchy). Sequels can be quite short (quick decision) or longer (deep introspection). Climax scenes often longer. Let story needs dictate.

### Can I revise briefs after drafting starts?

Yes, but carefully. If you change a brief for Scene 8 after drafting Scenes 1-7, check ripple effects. Might require revision of already-drafted scenes.

Better: Get all briefs solid before drafting. Saves rework.

### What if AI drafts don't match my voice?

This is normal. AI first drafts are scaffolding—you're expected to rewrite heavily. Think of it as a rough structural draft you then translate into your voice.

If you find you're rewriting 80%+ of AI drafts, consider switching to Human First Draft for remaining scenes.

### How do I handle flashbacks or non-linear structure?

Scene/Sequel chain still applies, just follow POV character's experience order, not chronological story order.

Brief for flashback scene: Note in "Setting" that it's flashback, identify when it occurs in character's timeline. Still needs Goal-Conflict-Disaster if it's a full scene.

### Why separate brief files from draft files?

**Context control**. When drafting, you only need:
- Current scene brief (instructions)
- Previous scene draft (for transition)

Loading all briefs + all drafts = context bloat, confusion, slower AI responses.

Separate files = clean, focused sessions.

---

## Version History

**v1.1** - December 24, 2025  
Added explicit file organization section with separate brief/draft locations for context control.

**v1.0** - December 24, 2025  
Initial scene workflow protocol with atomic Scene/Sequel structure, complete planning before drafting, per-scene authorship flexibility.

---

**Author**: Doug Langille  
**Repository**: github.com/douglangille/Workbench