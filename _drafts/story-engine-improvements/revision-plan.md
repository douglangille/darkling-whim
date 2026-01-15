# Story Engine Revision Plan

**Date:** January 15, 2026  
**Based on:** Meta-analysis of "Calum in the Forest" workflow  
**Scope:** Bootstrap files, core documentation, new resources

---

## Executive Summary

This revision plan systematically integrates lessons from a real-world flash fiction workflow into Story Engine documentation. Key improvements focus on:

1. **Removing counterproductive constraints** (word counts during drafting)
2. **Adding effective patterns** (rubric-based ideation, "remove guardrails" prompting)
3. **Codifying role-based critique** (dual-perspective analysis)
4. **Documenting publishing workflows** (visual assets, teaser development)

---

## 1. IDEATION-BOOTSTRAP.md

### Current State
- Basic concept generation guidance
- Limited structure for evaluation
- No systematic refinement process

### Required Changes

#### Add: Rubric-Based Concept Generation
```markdown
## Rubric-Based Ideation Process

### Step 1: Generate Concepts (20+)
Generate broad concepts with built-in twists or ironic elements.

### Step 2: Create Evaluation Rubric
Define scoring criteria relevant to the story's goals:
- Originality (1-10)
- Emotional hook (1-10)
- Genre fidelity (1-10)
- Thematic fit (1-10)
- Flash-density / compactness (1-10)

### Step 3: Score and Rank
Evaluate all concepts, identify top 5.

### Step 4: Refine Top Concepts
Iterate on top 5 to improve scores, then re-evaluate.

### Step 5: Select Final Concept
Author selects based on revised scores and intuition.
```

#### Add: Progressive Constraint Filtering
```markdown
## Constraint Filtering Strategy

Rather than applying all constraints at once, progressively filter:

1. **Broad ideation** - Generate maximum concepts
2. **Genre constraints** - Filter by genre-specific requirements
3. **POV/perspective** - Narrow by narrative voice needs
4. **Mechanical rules** - Define world rules, horror mechanics, etc.
5. **Character/setting** - Anchor with specifics

This prevents premature filtering while maintaining focus.
```

#### Add: Concept Combination
```markdown
## Combining Concepts

If multiple concepts share mechanics or thematic elements:
- Identify shared systems
- Merge complementary ideas
- Consolidate world rules
- Ensure internal consistency
```

### Testing Criteria
- Can generate 20 concepts quickly?
- Does rubric meaningfully differentiate concepts?
- Does iteration improve scores?
- Does filtering prevent premature narrowing?

---

## 2. DRAFTING-BOOTSTRAP.md

### Current State
- Includes word-count guidance per scene/paragraph
- Structured but potentially constraining approach
- Limited guidance on when constraints help vs. harm

### Required Changes

#### Remove/Revise: Word-Count Constraints
**OLD APPROACH:**
```markdown
Allocate word counts per paragraph based on target length.
```

**NEW APPROACH:**
```markdown
## Escalation Beat Markers (Instead of Word Counts)

For flash fiction and shorter works, use **escalation markers** rather than word counts:

### Fichtean Curve Beats
- Opening: Establish normalcy with subtle wrongness
- Crisis 1: First tangible anomaly
- Crisis 2: Escalation, pattern recognition
- Crisis 3: Scope expansion, stakes increase
- Climax: Full revelation or cosmic perspective
- Resolution: Implication, not explanation

### Pacing Rhythm Notes
Instead of "150 words," use:
- "Brief, tight paragraph - sensory grounding"
- "Breathless accumulation - list-like structure"
- "Fragmented syntax - cognitive breakdown"
- "Single visceral image"

Word counts are for **revision**, not first drafts.
```

#### Add: "Remove Guardrails" Pattern
```markdown
## Draft Iteration: Remove Guardrails

If first draft feels:
- Too safe or clinical
- Emotionally flat
- Over-structured without visceral impact

**Prompt strategy:**
"Try again without that guardrail. Let the prose get messier, more visceral, more fragmented. Prioritize emotional authenticity over structural compliance."

This explicitly authorizes:
- Fragmented syntax
- Compulsive repetition
- Structural breakdown that mirrors character state
- Emotional escalation through rhythm changes
```

#### Add: Voice Authority Principle
```markdown
## Voice Pass: Human Authority

AI can execute structure and mechanics but **cannot replicate distinctive authorial voice**.

After drafting, human voice pass should focus on:
- Rhythm and sentence variation
- Distinctive phrasing and compression
- Authentic character cognition
- Subtle emotional beats AI approximates but doesn't nail

**Example transformations:**
- AI: "The camera shutter clicked continuously"
- Human: "The shutter won't stop"

- AI: "He avoided using the measuring tool"
- Human: "The protractor is in my bag. I don't use the protractor."

Voice pass is surgical, not wholesale rewrite.
```

### Testing Criteria
- Does removing word counts improve prose flow?
- Do escalation markers provide sufficient structure?
- Does "remove guardrails" unlock better drafts?
- Is voice pass guidance actionable?

---

## 3. REVISION-BOOTSTRAP.md

### Current State
- Five-phase revision structure
- Limited critique methodology
- No systematic second-read analysis

### Required Changes

#### Add: Dual-Perspective Critique Framework
```markdown
## Phase 1A: Role-Based Critique (First Read)

Before diving into line edits, perform **dual-perspective analysis**:

### Perspective 1: Literary Critic
Focus:
- Prose quality and rhythm
- Structural coherence
- POV effectiveness
- Pacing and tension
- Thematic clarity

### Perspective 2: Genre Specialist
Focus:
- Genre convention adherence/subversion
- Tone consistency
- Mechanical fidelity (horror rules, world logic, etc.)
- Reader expectations vs. delivery
- Payoff effectiveness

**Deliverable:** Identify 3-5 specific weaknesses with line references, plus 3-5 strengths.

### Author Decision Point
Review critique, agree/disagree with identified issues, authorize surgical edits only.
```

#### Add: Second-Read Analysis
```markdown
## Phase 1B: Second-Read Analysis (Foreshadowing & Integration)

After initial critique and any surgical edits, perform **second-read analysis**:

### Focus Areas:
- Structural foreshadowing (early clues that land on reread)
- Thematic integration (how elements reinforce theme)
- Mechanical consistency (do rules hold up throughout?)
- Layered meanings (what rewards close attention?)
- Callback effectiveness

**Purpose:** Validate that story rewards rereading, confirm horror mechanics (or other genre elements) remain elegant and consistent.

**Deliverable:** Confirmation that piece holds up on reread, or identification of integration issues.
```

#### Add: Surgical Edit Principle
```markdown
## Surgical Edits vs. Wholesale Rewrites

Revision should be **targeted**, not comprehensive:

### Surgical Edit Indicators:
- Specific weakness with clear fix
- Single paragraph or sentence issue
- Momentum loss at identifiable point
- Ending that over-explains

### Wholesale Rewrite Indicators:
- Fundamental POV problems
- Structural collapse
- Voice inconsistency throughout
- Mechanical incoherence

If wholesale rewrite needed, return to drafting phase rather than forcing revision.
```

### Testing Criteria
- Does dual-perspective critique surface real weaknesses?
- Does second-read analysis validate story integrity?
- Do surgical edits improve without disrupting flow?

---

## 4. BLOG-POST-BOOTSTRAP.md

### Current State
- Basic publishing workflow
- Limited visual asset guidance
- No teaser/metadata development

### Required Changes

#### Add: Visual Asset Workflow
```markdown
## Phase 5A: Header Image Development

### Step 1: Brainstorm Concepts (20)
Generate visual concepts that:
- Convey story tone without spoiling
- Work in wide format (blog header)
- Have center focus (for thumbnail cropping)
- Use subtlety over explicit reveals

### Step 2: Create Rubric
Scoring criteria:
- Tonal fidelity (1-10)
- Narrative alignment (1-10)
- Thumbnail readability (1-10)
- Subtlety (1-10)
- Visual originality (1-10)

### Step 3: Score and Refine Top 5
Iterate to improve scores.

### Step 4: Generate AI Prompts
Convert top 3 concepts to detailed image generation prompts.

### Step 5: Author Selection
Author reviews generated images, selects final.
```

#### Add: Teaser Text Development
```markdown
## Phase 5B: Teaser Text Creation

### Iteration Process:
1. **Descriptive** - Generate initial teaser with full context
2. **Neutralize** - Remove gendered pronouns, character names if appropriate
3. **Condense** - Cut unnecessary words, sharpen tension
4. **Polish** - Ensure rhythm and punch

### Example:
- Initial: "Every shot he takes only draws the forest closer."
- Neutral: "Every shot taken only draws the forest closer."
- Condensed: "Every shot taken draws the forest closer."

### Requirements:
- 10-15 words maximum
- Convey tone and tension
- Avoid spoilers
- Work without additional context
```

#### Add: Formatting/Punctuation Pass
```markdown
## Phase 5C: Final Formatting

### Line Break Strategy
Place line breaks at:
- Narrative fracture points (normalcy → wrongness)
- Discovery moments
- Spatial/temporal impossibilities
- Peak tension moments

### Punctuation for Suspense
- Use ellipses for trailing tension
- Remove hanging dashes
- Short paragraphs for urgency
- Fragment sentences for cognitive breakdown

Map formatting choices to narrative beats.
```

### Testing Criteria
- Does visual workflow produce effective headers?
- Is teaser text punchy and spoiler-free?
- Do formatting choices enhance pacing?

---

## 5. story-engine/README.md

### Required Changes

#### Add: Process Innovations Section
```markdown
## Process Innovations

### Rubric-Based Ideation
Systematic concept generation with explicit scoring criteria enables rapid filtering and refinement. See IDEATION-BOOTSTRAP.md.

### "Remove Guardrails" Prompting
Explicitly authorizing messier, more visceral prose in second drafts unlocks emotional authenticity. See DRAFTING-BOOTSTRAP.md.

### Dual-Perspective Critique
Role-based analysis (literary + genre) surfaces pattern-based weaknesses. See REVISION-BOOTSTRAP.md.

### Escalation Beat Markers
Replacing word counts with tension progression points prevents prose suffocation. See DRAFTING-BOOTSTRAP.md.

### Voice as Final Authority
AI executes structure/mechanics; human authority required for distinctive voice. See DRAFTING-BOOTSTRAP.md.
```

#### Update: Workflow Philosophy
```markdown
## Workflow Philosophy Updates

### When Constraints Help vs. Harm

**Constraints are productive for:**
- Ideation filtering (genre, POV, mechanics)
- Structure planning (Fichtean curve, scene beats)
- Evaluation (rubrics, scoring)
- Revision targets (surgical edits)

**Constraints are counterproductive for:**
- First draft prose execution (word counts, rigid structure)
- Voice development (AI approximates, doesn't replicate)
- Emotional authenticity (requires "guardrails removed")

Knowing when to constrain and when to release is key to efficient workflow.
```

#### Add: Cross-Platform Workflow Guidance
```markdown
## Cross-Platform Workflow

Different AI platforms have different strengths:

### Ideation & Planning
- Structured iteration with rubrics
- Progressive constraint filtering
- Story bible development

### Drafting & Refinement
- Structure/mechanics execution
- Role-based critique
- Pattern recognition for weaknesses

### Publishing
- Visual asset development
- Teaser/metadata creation
- Systematic evaluation

Switch platforms at natural inflection points for optimal results.
```

### Testing Criteria
- Does README accurately reflect workflow improvements?
- Is philosophy section actionable?
- Does cross-platform guidance make sense?

---

## 6. story-engine/CUSTOM-INSTRUCTIONS.txt

### Required Changes

#### Add: Constraint Awareness
```markdown
**Constraint Application:**
- Apply structure during planning, not execution
- Use escalation beat markers instead of word counts for flash fiction
- Explicitly ask before applying constraints that might limit prose flow
- Recognize when "remove guardrails" approach needed
```

#### Add: Critique Role Guidance
```markdown
**Critique Methodology:**
- Perform dual-perspective analysis (literary + genre)
- Identify specific weaknesses with line references
- Suggest surgical edits, not wholesale rewrites
- Conduct second-read analysis separately from first-read
- Validate story integrity on reread
```

#### Add: Voice Authority Principle
```markdown
**Voice and Authenticity:**
- AI handles structure and mechanics
- Human authority required for distinctive voice
- Recommend voice pass after drafting
- Surgical edits for rhythm, compression, authentic cognition
```

### Testing Criteria
- Do custom instructions reflect new patterns?
- Is constraint guidance clear?
- Does critique methodology match revision plan?

---

## 7. New Resource: FLASH-FICTION-WORKFLOW.md

### Purpose
Dedicated guide for flash fiction (under 1,500 words) incorporating all lessons learned.

### Contents

```markdown
# Flash Fiction Workflow (< 1,500 words)

## Overview
Flash fiction requires precision, tight escalation, and every word earning its place. This workflow optimizes for impact over length.

## Phase 1: Concept Development
[Rubric-based ideation process]

## Phase 2: Story Bible Creation
[Progressive constraint filtering]
[POV, mechanics, character, setting]
[Fichtean curve with beat markers, NOT word counts]

## Phase 3: First Draft
[Structure execution with beat markers]
[Let prose breathe, no word count constraints]

## Phase 4: Second Draft (Remove Guardrails)
[If first draft too safe, explicitly authorize messy/visceral prose]

## Phase 5: Critique
[Dual-perspective first read]
[Surgical edits only]
[Second-read validation]

## Phase 6: Voice Pass
[Human authority on rhythm, compression, authenticity]

## Phase 7: Publishing Prep
[Visual assets with rubric]
[Teaser text iteration]
[Formatting/punctuation for suspense]

## Common Pitfalls
- Word-count constraints during drafting
- Over-explanation in endings
- Single-pass critique missing integration issues
- Skipping voice pass
```

### Testing Criteria
- Does workflow feel complete and actionable?
- Can be followed start-to-finish for new flash project?

---

## 8. New Resource: PROMPT-PATTERNS.md

### Purpose
Document reusable prompt strategies discovered through practice.

### Contents

```markdown
# Reusable Prompt Patterns

## "Remove Guardrails"
**Use when:** First draft too safe, clinical, emotionally flat
**Prompt:** "Try again without that guardrail. Let the prose get messier, more visceral, more fragmented. Prioritize emotional authenticity over structural compliance."
**Effect:** Unlocks fragmented syntax, compulsive repetition, emotional escalation

## Rubric-Based Evaluation
**Use when:** Need to choose between multiple options systematically
**Prompt:** "Create a rubric scoring these concepts on [criteria]. Score each, identify top 5, then iterate top 5 to improve scores."
**Effect:** Rapid filtering, objective comparison, iterative refinement

## Dual-Perspective Critique
**Use when:** Need comprehensive story assessment
**Prompt:** "Read as both a literary critic and [genre] fan. Identify 3-5 weaknesses and 3-5 strengths with specific line references."
**Effect:** Surfaces both craft and genre-specific issues

## Second-Read Analysis
**Use when:** Validating story integrity and foreshadowing
**Prompt:** "Reread the story looking specifically for foreshadowing, thematic integration, and layered meanings. What rewards close attention?"
**Effect:** Confirms story holds up on reread, identifies missed connections

## Progressive Constraint Filtering
**Use when:** Ideation feels unfocused or overwhelming
**Prompt sequence:**
1. "Generate 20 concepts with [basic requirement]"
2. "Filter for [genre constraints]"
3. "Narrow by [POV/perspective needs]"
4. "Define [mechanical rules]"
5. "Anchor with [character/setting specifics]"
**Effect:** Prevents premature filtering while maintaining focus

## Surgical Edit Request
**Use when:** Specific weakness identified, not wholesale rewrite needed
**Prompt:** "The [specific element] at [line/paragraph reference] loses momentum. Add [specific type of detail] to restore tension."
**Effect:** Targeted improvement without disrupting flow

## Escalation Beat Markers
**Use when:** Planning structure without word-count constraints
**Prompt:** "Outline using escalation beats: [opening normalcy] → [crisis 1] → [crisis 2] → [climax] → [implication]. Describe rhythm and pacing, not word counts."
**Effect:** Structure without suffocating prose flow
```

### Testing Criteria
- Are patterns clearly explained?
- Can be applied to new projects?
- Cover key workflow moments?

---

## 9. New Resource: CRITIQUE-FRAMEWORK.md

### Purpose
Template for systematic story critique at various stages.

### Contents

```markdown
# Story Critique Framework

## First-Read Analysis

### Literary Perspective
**Prose Quality:**
- Sentence rhythm and variation?
- Word choice precision?
- Voice consistency?
- Show vs. tell balance?

**Structure:**
- Opening hook effectiveness?
- Escalation clarity?
- Pacing appropriate to length?
- Ending lands with impact?

**POV:**
- Immersion maintained?
- Perspective consistent?
- Unreliability (if applicable) effective?

### Genre Perspective
**Convention:**
- Genre expectations met/subverted appropriately?
- Tone consistency?
- Trope handling?

**Mechanics:**
- World rules consistent?
- Horror/thriller/etc. mechanics elegant?
- Setup/payoff effective?

**Reader Experience:**
- Emotional journey clear?
- Stakes felt?
- Satisfying within genre?

### Deliverable
**Strengths (3-5 with line references):**
1. [Specific element] at [location] because [reason]

**Weaknesses (3-5 with line references):**
1. [Specific element] at [location] because [reason]

---

## Second-Read Analysis

### Foreshadowing
- Early clues that pay off?
- Subtle hints vs. obvious telegraphing?
- Layered meanings on reread?

### Integration
- Thematic elements reinforce throughout?
- Mechanical consistency holds?
- Character choices track with established traits?

### Payoff
- Does ending recontextualize earlier moments?
- Second read rewarding?
- Horror/twist/reveal still effective knowing outcome?

### Deliverable
**Reread Validation:**
- Story holds up? Yes/No
- New insights on second pass?
- Integration issues identified?

---

## Surgical Edit Recommendations

**Format:**
[Paragraph/line reference]
**Issue:** [Specific weakness]
**Suggested fix:** [Concrete change]
**Rationale:** [Why this improves the piece]

---

## Completion Criteria

Story ready to ship when:
- Structure sound
- Mechanics elegant
- Voice distinctive
- Rewarding on reread
- Ending lands
- No diminishing returns on further iteration
```

### Testing Criteria
- Is framework comprehensive?
- Can be applied consistently?
- Produces actionable feedback?

---

## Implementation Plan

### Phase 1: Core Bootstrap Updates (Priority 1)
1. IDEATION-BOOTSTRAP.md - Add rubric process, constraint filtering
2. DRAFTING-BOOTSTRAP.md - Remove word counts, add beat markers, "remove guardrails"
3. REVISION-BOOTSTRAP.md - Add dual-perspective critique, second-read analysis

### Phase 2: Documentation Updates (Priority 2)
1. README.md - Add process innovations, workflow philosophy updates
2. CUSTOM-INSTRUCTIONS.txt - Add constraint awareness, critique guidance
3. BLOG-POST-BOOTSTRAP.md - Add visual asset workflow, teaser development

### Phase 3: New Resources (Priority 3)
1. FLASH-FICTION-WORKFLOW.md - Complete dedicated guide
2. PROMPT-PATTERNS.md - Document reusable strategies
3. CRITIQUE-FRAMEWORK.md - Systematic critique template

### Phase 4: Testing & Iteration (Priority 4)
1. Apply revised workflows to new flash fiction project
2. Validate improvements against original pain points
3. Iterate based on real-world usage
4. Document additional learnings

---

## Success Metrics

**Process Efficiency:**
- Reduced iteration loops in ideation
- Faster time from concept to draft-ready outline
- Fewer wholesale rewrites needed

**Output Quality:**
- First drafts have better emotional impact
- Critiques surface actionable weaknesses
- Stories hold up on second read
- Voice remains distinctive through process

**Workflow Clarity:**
- Bootstraps provide clear guidance
- Decision points are explicit
- When to constrain vs. release is obvious
- Cross-platform workflow is smooth

---

## Next Steps

1. **Author Review:** Approve revision plan before implementation
2. **Systematic Updates:** Make changes to bootstrap files one at a time
3. **Commit Strategy:** Individual commits per file with clear change notes
4. **Testing:** Apply to upcoming flash fiction project
5. **Iteration:** Refine based on real-world results

---

**Status:** Awaiting author approval  
**Timeline:** TBD based on author availability  
**Context Maintenance:** All work tracked in _drafts/story-engine-improvements/
