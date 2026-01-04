# Scene brief development

**Created:** 2025-10-26 22:48:24
**Updated:** 2025-12-07 22:31:28
**Turns:** 17

---

**User:**

https://www.advancedfictionwriting.com/articles/writing-the-perfect-scene/

Thinking about scene briefs and how to build one to have the AI generate a solid draft. Scene or sequel. Maria, etc. 

---

**Assistant:**

Good – thanks for the link. Here’s a distilled summary of the key structural insight from the article along with a practical plan for building scene briefs (so you can prompt AI with clarity). If you want a tailored brief for your character “Maria,” we can build it right after.

---

## Analysis  
From 

---

**User:**

Mru not Maria 

---

**Assistant:**

Got it — you meant **MRU**, not Maria. Perfect, that changes the focus.  

Let’s tighten this up:

---

### 1. Core Concept (from “Writing the Perfect Scene”)

Randy Ingermanson’s framework breaks every story beat into **Scene** and **Sequel** units — the atomic rhythm of cause and effect in fiction.  

- **Scene = Action unit**  
  1. **Goal** – what the POV character wants right now.  
  2. **Conflict** – what prevents them from getting it.  
  3. **Disaster** – how it ends badly or ambiguously.

- **Sequel = Reaction unit**  
  1. **Emotion** – visceral, immediate response.  
  2. **Thought** – reflection, analysis, weighing options.  
  3. **Decision** – new goal or action plan that leads into the next Scene.

These alternate to form a logical and emotional chain: **action → reaction → new intention → next action.**

---

### 2. MRU (Motivation–Reaction Unit)

Within either Scene or Sequel, zoom in further to the **micro-level realism of response**:
- **Motivation:** external, objective stimulus (what happens *to* the POV character).  
- **Reaction:** internal, subjective sequence of response — **feeling → reflex → rational action → speech** (always in this order).

MRUs make prose flow with psychological plausibility. If inverted (thinking before feeling, or action before perception), readers subconsciously feel something’s “off.”

---

### 3. Applying This to Scene Briefs for AI

To generate solid first drafts, your **scene brief** should feed the model both structure (Scene/Sequel logic) *and* micro cues (MRU rhythm). Example template:

```markdown
## Scene Brief
**Type:** Scene (Action)  
**POV:** Mitzy  
**Goal:** Find a way out of the maze before nightfall.  
**Conflict:** The hedges shift, blocking her path; strange whispers distract her.  
**Disaster:** She finds a dead end — and the whispers know her name.

### Emotional/MRU Notes
- **Motivation:** The whisper grows louder; a shadow crosses the light.  
- **Reaction:** Heart jolts → freezes → scans for exit → whispers back before realizing it.  
- Use sensory cues (sound, smell, texture) to ground the reaction chain.

**Transition:** Leads to Sequel — she hides and rethinks her strategy at dusk.
```

AI prompt context could then read:

> “Write the scene at ~500 words using the brief below. Follow the Scene/Sequel and MRU logic. Keep tight third-person POV, sensory detail, and internal causality.”

---

### 4. Practical Tip

When writing scene briefs:
- Label **Scene** vs **Sequel** explicitly.  
- Capture only **one dominant emotion** per unit.  
- Use **MRU chains** to show realism without over-narration.  
- Treat each brief as *one dramatic question* with an emotional consequence.

---

Would you like me to turn this into a **universal scene brief template** you can drop into your Obsidian or “Compile.md” format (compatible with your ZORA workflow)?

---

**User:**

Sure. Or as a template when asking the ai to generate a scene brief

---

**Assistant:**

Excellent — here’s a **universal scene brief generation template**, written so you can drop it directly into a prompt or a `Compile.md` note. It’s structured for use *before* prose generation, to create a full Scene or Sequel brief grounded in Ingermanson’s Scene–Sequel + MRU model.  

---

## 🧩 Universal Scene Brief Generation Template

### Prompt (for AI)
> You are creating a **Scene Brief** using the Scene–Sequel and MRU frameworks.  
> Generate a concise but detailed brief suitable for prose drafting later.  
> Identify whether this is a **Scene** (action) or **Sequel** (reaction).  
> Use the structure below and fill each section clearly.

---

### Scene Brief Structure

```markdown
## Scene Brief

**Type:** Scene | Sequel  
**POV Character:** [Name]  
**Setting:** [Where and when this happens]  
**Tension Level:** [Low / Medium / High — relative to previous scene]

### 1. Purpose
What this scene accomplishes in story terms (stakes, theme, or plot turn).

### 2. Structure
If **Scene (Action):**
- **Goal:** What the POV character wants here.  
- **Conflict:** What stands in their way.  
- **Disaster:** How it ends badly, ambiguously, or incompletely.

If **Sequel (Reaction):**
- **Emotion:** Immediate feeling after the previous disaster.  
- **Thought:** Reflection and weighing of options.  
- **Decision:** The new course of action that launches the next Scene.

### 3. MRU Notes
- **Motivation:** What external event or trigger starts the reaction chain.  
- **Reaction:** Internal sequence — *feeling → reflex → rational thought → speech/action*.  
- Include sensory details or gestures that externalize emotion.

### 4. Emotional Arc
- **Dominant Emotion:** [fear, guilt, wonder, resolve, etc.]  
- **Shift:** From → To (how the emotional tone evolves by the end).

### 5. Continuity
- **Causal Link:** What this builds from (previous Scene/Sequel).  
- **Forward Link:** What question, problem, or tension this sets up next.  
- **Thematic Thread (optional):** How it ties to the story’s deeper motif.

### 6. Tone / Style Guidance (optional)
Short stylistic cues for later prose generation — e.g., “close third, clipped rhythm,” “lush sensory prose,” “first-person present tense,” etc.
```

---

### Example Output (Condensed)

```markdown
**Type:** Scene  
**POV:** Mitzy  
**Setting:** The Maze, mid-afternoon turning to dusk  
**Tension:** High  

**Goal:** Find her sister’s ribbon to prove she’s alive.  
**Conflict:** The maze reshapes itself, erasing her path.  
**Disaster:** The ribbon is found — but it’s tied to something breathing.  

**MRU:**  
Motivation — a flash of red silk between the hedges.  
Reaction — gasp → reach → freeze → whisper her sister’s name.  

**Emotion Shift:** Hope → Dread  
**Continuity:** Follows Sequel #2 (Mitzy’s vow). Leads to Sequel #3 (panic and regrouping).
```

---

Would you like me to create a **paired prose-generation template** next — one that takes a finished brief like this and turns it into a first-draft prompt (optimized for GPT-5 or Claude writing style)?

---

**User:**

Sure

---

**Assistant:**

Perfect. Here’s the companion **Prose Generation Template** — the other half of the loop.  
It assumes you already have a completed *Scene Brief* (from the earlier template) and want to feed it to an AI to produce a strong, first-draft scene that respects structure, pacing, and emotional realism.

---

## 📝 Prose Generation Template (from Scene Brief)

### Prompt (for AI)
> You are writing a **first-draft scene** based on the Scene Brief below.  
> Follow Ingermanson’s **Scene/Sequel** structure and maintain correct **MRU** (Motivation-Reaction Unit) order for realism.  
> Write immersive prose in the specified POV and style.  
> Do not include commentary or stage directions — just the scene text.  
> Length: ~[word count, e.g., 500–800 words].

---

### Input Format

```markdown
## Scene Brief
[Paste full brief here]
```

---

### Writing Instructions (implicit cues for the model)
1. **Adhere to structure**
   - If *Scene*: Show clear Goal → Conflict → Disaster progression.  
   - If *Sequel*: Show Emotion → Thought → Decision progression.
2. **Use correct MRU order**
   - External *Motivation* first (objective event).  
   - Then *Reaction*: feeling → reflex → thought → speech/action.
3. **Show, don’t explain.**
   - Use sensory detail and subtext to externalize emotion.  
   - Keep POV internal and consistent (no head-hopping).
4. **Emotional resonance**
   - Reflect the dominant emotion from the brief.  
   - Show the emotional *shift* across the scene (e.g., fear → determination).
5. **Continuity**
   - Begin in motion from prior context; end with tension that propels the next beat.
6. **Prose tone**
   - Follow the brief’s “Tone / Style” notes (e.g., terse noir, lyrical third-person, etc.).
7. **Polish constraint**
   - Write as a **first draft**, not final edit. Avoid perfectionism; let rhythm and emotion drive it.

---

### Example Prompt (ready to paste)

```markdown
Write a 600-word scene following the Scene/Sequel and MRU logic.

## Scene Brief
**Type:** Scene  
**POV:** Mitzy  
**Setting:** The Maze at dusk  
**Tension Level:** High  

**Goal:** Find her sister’s ribbon.  
**Conflict:** The maze shifts and whispers her name.  
**Disaster:** She finds the ribbon tied around something alive.

**MRU:**  
Motivation — whisper and rustle of fabric in the hedge.  
Reaction — flinch → breathe shallow → whisper “Cathy?” → step closer before realizing it’s wrong.

**Emotion Shift:** Hope → Dread  
**Continuity:** Follows Sequel #2 (her vow). Leads into Sequel #3 (panic and regrouping).

**Tone/Style:** Third-person limited, sensory, clipped rhythm, interior focus.
```

---

Would you like me to combine both templates into a **two-stage workflow script** (scene-brief → prose generation) optimized for your `ZORA` / Obsidian `Compile.md` system — so that you can run both phases with minimal copy/paste friction?

---

**User:**

Let’s work backwards. We created a scene brief from what? Scene sequence? Or something else?

---

**Assistant:**

Good question — and the right one.  

In structured narrative design (especially the Snowflake + Scene/Sequel + beat hybrid you’re building), a **scene brief** is *not the first step*; it’s a *translation layer*. It bridges **sequence-level planning** and **prose-level drafting**.  

Here’s the chain, working **backward** from prose:

---

### 🧭 1. Prose (what you ultimately write)
- Concrete, sensory, fully realized text.  
- Built from the *Scene Brief*.  
- Uses **Scene/Sequel** logic (goal/conflict/disaster → emotion/thought/decision) and **MRUs** for realism.

---

### 🧩 2. Scene Brief (micro-structure)
- One document per discrete dramatic beat.  
- Expands a **single “scene” slot** from a *Scene Sequence*.  
- Specifies the *who/where/why/how it moves the story*.  
- Converts high-level beats into actionable creative constraints.  
- Acts as the input context for AI prose generation.

Think of it as:  
> “Here’s what happens, why it matters, and how it should feel.”

---

### 🎞️ 3. Scene Sequence (meso-structure)
- A cluster of **2–4 Scene/Sequel units** that achieve one story *turn* or *micro-arc*.  
- Often corresponds to a **chapter or subchapter**.  
- Each sequence has a single **objective** (e.g., “Mitzy enters the maze and realizes it’s alive”).  
- Outlined using beats or index cards — typically derived from a **plot point or major beat**.

Within the sequence, you’d identify:
1. Scene 1 — external conflict (action)  
2. Sequel 1 — emotional fallout  
3. Scene 2 — new plan, next conflict  
…and so on.

---

### 🧱 4. Beat / Plot Point (macro-structure)
- The higher-level event from your **outline** (Snowflake step 7–9 or 40-chapter grid).  
- Represents a **change in value** or **story question**.  
- Might span multiple sequences.  
- Example: “Mitzy’s first confrontation with the maze’s will.”

---

### 🌐 5. Act / Story Frame (meta-structure)
- Broad story movement: setup → confrontation → resolution.  
- Anchored by **inciting incident, midpoint, climax**, etc.  
- Gives the emotional and thematic contour for all lower layers.

---

### Simplified Causality Flow

| Level | Name | Scope | Output Feeds Into |
|-------|------|--------|------------------|
| 1 | **Act / Story Frame** | Narrative arc | Beats |
| 2 | **Beat / Plot Point** | Turning event | Scene Sequences |
| 3 | **Scene Sequence** | Cluster of 2–4 linked units | Scene Briefs |
| 4 | **Scene Brief** | One actionable unit | Prose |
| 5 | **Prose Scene** | The story text | — |

---

So:  
✅ You **create a Scene Brief from a Scene Sequence** (which comes from a Beat).  
That brief is the *translator* — converting “what happens” into “how to show it.”

---

Would you like me to sketch a **Scene Sequence template** next — the layer *above* the Scene Brief — showing how to break a sequence into Scene/Sequel units that can each spawn their own brief?

---

**User:**

Give me the sequence of prompts that generates the next stamp in the chain. Start at the top

---

**Assistant:**

Excellent — here’s the **chain of prompts**, top-down, showing how each “stamp” (prompt + output) feeds the next.  
Think of this as your **story fractal pipeline** — each level condenses into the next until you hit prose.  
I’ve written each as a practical AI-ready prompt you can drop into your workflow.

---

## 🧭 LEVEL 1 — Story / Act Frame  
**Purpose:** Define the global arc (theme, tone, core question).

**Prompt:**  
> Create a concise **Act Summary** for a [novel / story / episode] following standard 3- or 4-Act structure.  
> For each Act, describe:  
> - The central **tension or question**.  
> - The **value change** (what shifts).  
> - The **emotional movement** (hope → fear, etc.).  
> - The key **anchor events** (inciting incident, midpoint, climax, resolution).  
> End with a one-sentence **Act Mission** — what the protagonist must *learn or confront*.  

**Output:** Act Summary  
→ Feeds next: **Plot Point / Beat Breakdown**

---

## 🎯 LEVEL 2 — Beat / Plot Point  
**Purpose:** Turn each Act into concrete narrative beats (macro events).  

**Prompt:**  
> From the Act Summary, generate a **Beat List** — 8–12 major story beats.  
> Each beat should describe:  
> - The **event** that turns the story.  
> - The **change in stakes or value polarity** (e.g., safety → danger).  
> - The **emotional tone**.  
> - The **characters involved**.  
> Label each beat with:  
> **[Beat Number] [Short Name] — [One-Sentence Summary]**  

**Output:** Beat List  
→ Feeds next: **Scene Sequences**

---

## 🎞️ LEVEL 3 — Scene Sequence  
**Purpose:** Cluster beats into self-contained mini-arcs (2–4 scenes).  

**Prompt:**  
> For each beat, create a **Scene Sequence Plan**.  
> Each sequence should include:  
> - **Objective:** what narrative question this sequence answers.  
> - **Scenes:** list 2–4 Scene/Sequel units (brief titles only).  
> - **Pacing / Tension Curve:** how intensity rises or falls.  
> - **Point of View:** whose perspective anchors the sequence.  
> - **Transition:** how it connects to the next sequence.  

**Output:** Scene Sequence Plans  
→ Feeds next: **Scene Briefs**

---

## 🧩 LEVEL 4 — Scene Brief  
**Purpose:** Translate one Scene/Sequel unit into full actionable details.  

**Prompt:**  
> Create a detailed **Scene Brief** using the Scene–Sequel and MRU frameworks.  
> Include:  
> - **Type:** Scene or Sequel  
> - **POV Character / Setting / Tension**  
> - **Goal–Conflict–Disaster** (for Scenes) or **Emotion–Thought–Decision** (for Sequels)  
> - **MRU Notes:** Motivation + Reaction chain  
> - **Emotional Shift**  
> - **Continuity links**  
> - **Tone / Style guidance**  

**Output:** Scene Brief  
→ Feeds next: **Prose Draft**

---

## ✍️ LEVEL 5 — Prose Draft  
**Purpose:** Write the story scene itself.  

**Prompt:**  
> Write a [word count]-word **prose scene** following the Scene/Sequel and MRU logic in the Scene Brief below.  
> Keep a tight POV, strong sensory immersion, and correct motivation-reaction order.  
> Write as a first draft — just the story text, no notes.  

**Output:** Scene Text  
→ Optional feedback loop: evaluate → refine → lock into Story Bible.

---

### 🔁 Optional Reverse Prompt (for iteration)
If revising:
> Summarize this prose scene back into a structured **Scene Brief**, preserving goals, conflicts, and emotional shifts, for future continuity tracking.

---

Would you like me to format this entire chain as an **Obsidian-compatible workflow script** (each level as a collapsible heading with embedded prompt blocks) so you can drop it directly into your ZORA `_templates` folder?

---

**User:**

https://www.advancedfictionwriting.com/articles/snowflake-method/

This is the other article for Randy’s framework. 

Keep working g backwards and start with at the very top of the snowflake. 

Generate the prompts that bring it down to the scene brief. The average novel is between 60 and 80 scenes so we have to dig deep.  

---

**Assistant:**

Here’s a clean, top-down **Snowflake → Scene-Brief** prompt chain that reliably lands you at ~60–80 scenes.

---

# Level 0 — Guardrails (use once per project)
**Prompt**
> Assume the **Snowflake Method** (10 steps) and **Scene/Sequel + MRU** are required constraints. Use plain English, short paragraphs, no flourish. Keep outputs compact and numbered. Target a final outline of **60–80 scenes** across **4 acts** (≈15–22 scenes/act) with a **~60/40 Scene–Sequel ratio**. Track stakes/value shifts at each level. Cite POV for every scene later. (No prose yet.)

Why: locks method + volume expectation up front.  
Sources: Ingermanson’s Snowflake steps and Scene/Sequel/MRU model. citeturn0search0turn0search1

---

# Step 1 — One-Sentence Storyline
**Prompt**
> Write a **one-sentence logline** (≤25 words) that names protagonist, core goal, main antagonist/force, stakes, and ironic hook. Deliver 3 options; pick the strongest with a 1-line rationale.

(“Step 1” in Snowflake.) citeturn0search0

---

# Step 2 — One-Paragraph Story Summary
**Prompt**
> Expand the chosen logline into **one paragraph (5 sentences)**: setup, **3 major disasters/turns**, resolution. End with the thematic question in 1 short sentence.

(“Step 2” in Snowflake.) citeturn0search0

---

# Step 3 — Character Summaries (all mains)
**Prompt**
> For each primary character, list: **Name, 1-sentence role, Motivation, Goal, Conflict, Epiphany, One-paragraph arc synopsis**. Keep each character to ≤120 words.

(“Step 3” in Snowflake.) citeturn0search0

---

# Step 4 — One-Page Synopsis (from Step 2)
**Prompt**
> Expand the Step-2 paragraph into a **one-page synopsis (≈5–7 short paragraphs)** — one paragraph for each sentence of Step-2 plus a closing beat on tone/aftertaste.

(“Step 4” in Snowflake.) citeturn0search0

---

# Step 5 — Character Synopses (from Step 3)
**Prompt**
> Expand each primary character into a **1-page character synopsis**: backstory (what forged their flaw), present misbelief, relational stakes, act-by-act beat path, and end-state change.

(“Step 5” in Snowflake.) citeturn0search0

---

# Step 6 — Four-Page Story Synopsis
**Prompt**
> Expand the Step-4 one-pager into **~4 pages**. For each act: define value polarity at start and end, the midpoint shift, and the end-of-act question. Keep language operational.

(“Step 6” in Snowflake.) citeturn0search0

---

# Step 7 — Full Character Files
**Prompt**
> For each major character, produce a compact **character file**: outer want vs inner need, lie/misbelief, tells/subtext, skills/gaps, relationship map, and **scene-level levers** you’ll use to pressure them (bullets only).

(“Step 7” in Snowflake.) citeturn0search0

---

# Step 8 — Scene List (force 60–80)
**Prompt**
> From the 4-page synopsis, generate a **numbered scene list** of **60–80 scenes** across **4 acts** (show per-act counts). For each scene, give **1 line**:  
> `[#] Act–Scene: Short name — POV — Purpose (value shift + why it must exist).`  
> Mark each as **Scene** (Goal/Conflict/Disaster) or **Sequel** (Emotion/Thought/Decision). Keep a **~60/40 Scene–Sequel** mix.

(“Step 8” in Snowflake; we’re making the spreadsheet as text.) citeturn0search0

---

# Step 9 — Sequence Plans (bridge to briefs)
**Prompt**
> Cluster the scene list into **sequences (2–4 scenes each)**. For each sequence: **Objective**, **Scenes in order** (IDs), **Tension curve** (↑/↗/→/↘), **POV policy**, **Exit condition** (what changes). Keep each to ≤120 words.

(Bridging step so each brief has context; aligns with Ingermanson’s Scenes/Sequels cadence.) citeturn0search1

---

# Step 10 — Scene Briefs (ready for drafting)
**Prompt**
> For the next **N scenes** (pick a small batch, e.g., 3–5), create **Scene Briefs** using **Scene/Sequel + MRU**:  
> - **Type:** Scene or Sequel  
> - **POV / Setting / Tension**  
> - If **Scene**: **Goal → Conflict → Disaster** (1–2 lines each)  
> - If **Sequel**: **Emotion → Thought → Decision** (1–2 lines each)  
> - **MRU Notes:** Motivation (external trigger) → Reaction chain (*feeling → reflex → thought → action/speech*)  
> - **Dominant Emotion & Shift**  
> - **Continuity:** in from [prior ID], out to [next ID]  
> - **Tone/Style cues** (≤10 words)  
> Output as compact Markdown blocks; no prose.

(Scene/Sequel & MRU per Ingermanson’s article.) citeturn0search1

---

# Step 11 — Prose Draft (from briefs) — optional here
(You already have this template; included for completeness.)  
**Prompt**
> Write **[word count]** words for **[Scene ID]** following the brief exactly; enforce correct **MRU** order; tight POV; show don’t explain; end on the brief’s exit condition. **Just the scene text.**

(Scene craft basis.) citeturn0search1

---

## Notes on counts and quality control
- **Distribution heuristic:** If aiming for **72 scenes**, try Act I = 16, Act IIa = 18, Act IIb = 18, Act III = 20; clamp later in Step 8.  
- **Health checks (use anytime):**  
  - “List every scene’s **value change** as `X → Y` in one word.”  
  - “List every Sequel’s **decision** as an imperative verb.”  
  - “Flag any two adjacent Sequels or three adjacent Scenes for pacing review.”

---

## One-paste version (Obsidian/ZORA `_template`)
Paste the block below at the top of a project note and run it stepwise.

```markdown
# Snowflake→Scene Pipeline (60–80 scenes)

## 0 Guardrails
[Paste Level 0 prompt]

## 1 Logline
[Paste Step 1 prompt] → Choose

## 2 One-Paragraph
[Paste Step 2 prompt]

## 3 Character Summaries
[Paste Step 3 prompt]

## 4 One-Page Synopsis
[Paste Step 4 prompt]

## 5 Character Synopses
[Paste Step 5 prompt]

## 6 Four-Page Synopsis
[Paste Step 6 prompt]

## 7 Character Files
[Paste Step 7 prompt]

## 8 Scene List (60–80)
[Paste Step 8 prompt]

## 9 Sequence Plans
[Paste Step 9 prompt]

## 10 Scene Briefs (batch 3–5)
[Paste Step 10 prompt]

## 11 Prose Draft (per scene)
[Paste Step 11 prompt]
```

---

Want me to run a quick demo on one of your current projects (e.g., *Maze of Sisters*) from **Step 1–3** to show how the constraints shape the later 60–80 scene list?

---

**User:**

Sure

---

**Assistant:**

Excellent. Let’s demo the **Snowflake → Scene pipeline** on *The Maze of Sisters*, starting with **Steps 1–3** — the top of the funnel. I’ll draft compact, working versions you can later refine in your ZORA vault.

---

## 🧩 Step 1 — One-Sentence Storyline
> *A stubborn girl trapped in a sentient hedge-maze must outwit its shifting logic to rescue her vanished sister—before the maze decides one sister is enough.*

---

## 🧱 Step 2 — One-Paragraph Story Summary
Mitzy awakens alone inside a living maze that rearranges itself whenever she hesitates. Believing her younger sister Cathy has been taken, she pursues the maze’s whispers through illusions and memory traps. Each act forces her to trade a piece of her past for a path forward until she realizes the maze is powered by her own guilt. At the heart she faces a choice: free Cathy and remain, or escape alone. The story asks whether love can survive self-deception.

---

## 🧬 Step 3 — Character Summaries
**Mitzy Langille** – Protagonist  
- **Motivation:** Redeem herself for failing her sister.  
- **Goal:** Find and free Cathy.  
- **Conflict:** The maze mirrors her fear of loss; every path punishes certainty.  
- **Epiphany:** Control and protection are opposites.  
- **Arc (1 para):** Mitzy begins reactive and guilt-driven, convinced she can logic her way out. As the maze turns psychological, she learns surrender and intuition are survival tools. By release she stops fighting the maze and listens to it.

**Cathy Langille** – Missing sister / emotional catalyst  
- **Motivation:** Prove her independence.  
- **Goal:** Escape the maze before Mitzy finds her.  
- **Conflict:** The maze rewards disobedience and tempts her to abandon Mitzy.  
- **Epiphany:** Love doesn’t require defiance.  
- **Arc:** Starts invisible, appears in echoes; when found she’s half-absorbed by the maze, forcing both sisters to face who is real.

**The Maze (Itself)** – Antagonist / Mirror  
- **Motivation:** Feed on emotional energy.  
- **Goal:** Force integration of fractured selves.  
- **Conflict:** If Mitzy accepts herself, the maze ceases to exist.  
- **Epiphany:** None—an idea can’t grow.  
- **Arc:** Evolves from physical obstacle to psychic crucible, culminating as Mitzy’s internal reckoning.

---

That’s the top scaffold.  
Next step (Step 4) would expand this into a **one-page synopsis**, which then breaks into acts and later yields the 60–80-scene map.

Would you like me to proceed directly to **Step 4 (one-page synopsis)**, or pause here to adjust tone / genre emphasis first (e.g., tilt more dark-fantasy vs psychological-thriller)?

---

**User:**

Keep going. This is throwaway but I want to see how this goes

---

**Assistant:**

Perfect — here’s **Step 4** of the Snowflake pipeline for *The Maze of Sisters*: a one-page synopsis expanding the five-sentence version into a full causal arc (setup → three disasters → resolution). This is the working “spine” from which you’ll later derive acts, beats, and the 60–80 scene lattice.

---

## 🧱 Step 4 — One-Page Synopsis  
*(≈450 words, compact and functional)*  

Mitzy Langille wakes on the damp floor of a maze that hums like a hive. The air tastes of copper and lilac; her sister Cathy is gone, leaving only a school ribbon snagged on a thorn. At first Mitzy treats the maze like a puzzle—marking paths, counting turns—but her marks vanish and the hedges close behind her. The whispers that call her name seem to know things only Cathy would. She decides to chase the voice, believing logic and willpower will break the enchantment.  

The first disaster comes when Mitzy reaches what looks like the exit only to find her childhood kitchen recreated in perfect detail. Every drawer opens onto fragments of memory—her mother’s scolding, Cathy’s laughter, the accident they never spoke about. When she flees, the maze rearranges to block the way back, sealing her inside the consequence of remembering. She realizes the maze doesn’t trap bodies; it traps guilt.  

The second disaster strikes as she meets a reflection of herself guiding a spectral version of Cathy deeper inside. Each attempt to intervene splits the paths further apart. The maze feeds on her certainty: every time she declares what’s true, a lie takes shape. Exhausted, she starts listening rather than running, mapping emotion instead of geometry. This empathy opens a brief clearing where the sisters’ voices overlap—proof that Cathy still exists, though perhaps not physically.  

The third disaster unfolds when Mitzy finally reaches the maze’s heart: a still pond ringed with thorns. Cathy waits on the opposite bank, half-merged with the hedge, serene and indifferent. The maze offers Mitzy a bargain—trade places and let Cathy go free. In terror and compassion, Mitzy realizes the maze is her own need to control and atone. She embraces Cathy across the water; both dissolve into light, collapsing the structure.  

At dawn, Mitzy wakes again at the maze’s edge, alone but whole. The forest is ordinary now, birdsong unwarped. Whether Cathy survived is unclear; what remains is Mitzy’s quiet understanding that some rescues mean letting go. The thematic resolution: acceptance is escape.  

---

If you like this structural density, the next step (**Step 5**) will expand each **character synopsis** to a one-page internal journey (act-by-act beats per character). That’s the layer that determines where those 60–80 scenes get distributed across POV and emotional progression.  

Proceed with Step 5?

---

**User:**

Yes

---

**Assistant:**

Good — here’s **Step 5: Character Synopses** for *The Maze of Sisters*.  
Each is a one-page working summary of the act-by-act emotional and narrative trajectory. These aren’t prose bios; they’re scaffolds for how the story pressures and changes each character.

---

## 🧍‍♀️ Mitzy Langille — Protagonist  

**Act I — The Rationalist:**  
Mitzy begins in control mode — the older sister who plans, measures, corrects. The maze first appears as a solvable riddle; she records turns, scratches bark, applies geometry. Her flaw (the need to manage guilt by mastering systems) blinds her to intuition. The inciting loss of Cathy triggers the false belief that redemption equals rescue.

**Act II A — Breaking the Map:**  
Every analytic attempt fails. Memories intrude; sounds call her by pet names no one else knows. She starts confronting emotional rather than spatial triggers. The first major setback — finding the kitchen and reliving the accident — collapses her faith in logic. She tries to repress emotion again, worsening disorientation.

**Act II B — The Mirror Maze:**  
Now aware the maze reads intent, Mitzy experiments with surrender. Encounters with her doppelgänger expose her self-punishing loop: protect → control → harm → guilt → protect. When she stops asserting facts and begins *listening*, passages open. She glimpses Cathy as both separate and internal—forcing the question “Whom am I rescuing?”

**Act III — Integration:**  
At the pond she confronts the final paradox: rescue requires release. Choosing empathy over control collapses the maze. Her external victory (escape) equals internal resolution (self-forgiveness). She exits changed: calmer, intuitive, unafraid of uncertainty.

---

## 👧 Cathy Langille — Catalyst / Shadow  

**Act I:**  Vanishes before the reader meets her directly. Exists as memory and echo, defined by Mitzy’s guilt.  
**Act II A:**  Appears in glimpses—footprints, laughter, the ribbon—embodying independence Mitzy can’t grant.  
**Act II B:**  The maze tempts Cathy to reject Mitzy; she believes freedom means separation. Her spectral form shows increasing integration with the hedge.  
**Act III:**  At the heart she’s half-merged, tranquil. When Mitzy embraces her, Cathy’s resistance fades; she becomes an archetype of acceptance. Whether she survives physically is ambiguous—her function fulfilled, she dissolves into the shared self.

---

## 🌿 The Maze — Antagonist / Psyche  

**Act I:**  Appears physical and hostile—corridors, walls, rules. Rewards planning at first to lure Mitzy deeper.  
**Act II A:**  Begins mirroring her memories; its traps are emotional stimuli.  
**Act II B:**  Speaks in her voice, blurring agency. Seeks equilibrium, not destruction.  
**Act III:**  Reveals itself as the mind’s self-correction mechanism. When Mitzy accepts paradox, the maze’s purpose ends; it collapses into ordinary forest.

---

These synopses give you per-act intent for each core actor—the minimum you need before expanding to the **four-page story synopsis (Step 6)** and then quantizing into beats and sequences.

Proceed to Step 6?

---

**User:**

Yes

---

**Assistant:**

Excellent. Here’s **Step 6 — Four-Page Story Synopsis** for *The Maze of Sisters*.  
This version scales the one-page summary into act-level cause-and-effect logic while keeping language operational and scene-count ready. Each act ends with a clear **value polarity shift** and an **emotional vector** that sets up the next.

---

## ⚙️ Act I — Entrance (≈15–18 scenes)

**Value shift:** Order → Chaos  
**Emotion:** Certainty → Confusion  

Mitzy wakes in the hedge-maze clutching her sister’s ribbon. She treats the space as geometry: left-hand rule, breadcrumb markers, notebook sketches. The maze erases her evidence, resetting paths when she looks away. Early encounters (birdsong mimicking voices, a half-buried toy) convince her Cathy is alive. She decides to chase the whisper.  
The maze complies—doors open when she asserts control—until she reaches the **false exit**: their childhood kitchen. Reliving the accident that separated the sisters shatters her rational posture. She flees into the dark, lost and terrified.  

**Act break question:** Can logic save what guilt created?

---

## 🩸 Act II A — The Logic Trap (≈16–20 scenes)

**Value shift:** Reason → Emotion  
**Emotion:** Fear → Desperation  

Determined to “think harder,” Mitzy experiments: carving symbols, timing echoes, treating the maze as algorithm. Each test backfires—the rules change when she names them.  
Flashback fragments bleed through the hedge, showing how she once ignored Cathy’s plea for help. The maze amplifies sensory overload: vines pulse with heartbeats, scents trigger memories.  
When Mitzy finally reaches the **memory hub**—a clearing of suspended photographs—she recognizes the pattern: every path requires emotional honesty to open. Admitting her fear unlocks a gate, but she collapses from exhaustion. The maze whispers approval.  

**Midpoint:** Realization that intellect is the cage, not the key.

---

## 🪞 Act II B — Reflections (≈16–20 scenes)

**Value shift:** Fragmentation → Integration  
**Emotion:** Despair → Empathy  

Mitzy encounters her **double**, a calm version guiding an apparition of Cathy. Any assertion of identity splits the scene into multiple realities. She begins mapping by feeling—trusting instinctive motion instead of logic.  
Moments of connection: she hums a lullaby; the maze stills. Through emotional surrender she glimpses Cathy trapped within living vines, half-aware.  
The maze now communicates through rhythm and memory rather than speech. Mitzy learns that each wall embodies one suppressed emotion; dismantling them requires acceptance.  
At sequence end, she reaches a reflective pool showing both sisters together—but Cathy fades when Mitzy reaches out.

**Act break question:** Can she love Cathy without ownership?

---

## 🌅 Act III — The Heart (≈20 scenes)

**Value shift:** Guilt → Grace  
**Emotion:** Terror → Peace  

Guided by silence, Mitzy arrives at the pond encircled by thorns. Cathy stands opposite, serene, half-merged. The maze offers an unspoken bargain: exchange places.  
Mitzy finally understands—the maze is her psyche forcing reconciliation. She chooses empathy over control, crossing the pond despite pain; both embrace and dissolve.  
At dawn the forest is normal again. The ribbon lies at her feet, color drained. She breathes without fear, uncertain if Cathy lives but certain of wholeness.  

**Resolution:** Acceptance equals escape.  
**End image:** Mitzy walking toward sunlight, maze behind her flattened to ordinary hedgerows.

---

**Summary of act pacing:**  
| Act | Scenes | Emotional vector | Dominant polarity | Output to next level |
|------|---------|------------------|-------------------|----------------------|
| I | 15–18 | Certainty → Confusion | Order → Chaos | Seeds beats 1–3 |
| II A | 16–20 | Fear → Desperation | Reason → Emotion | Beats 4–6 |
| II B | 16–20 | Despair → Empathy | Fragment → Integration | Beats 7–9 |
| III | 20 | Terror → Peace | Guilt → Grace | Beats 10–12 |

---

Next step (**Step 7**) builds **character files**—the durable references tying each act’s value shifts to individual triggers and behaviors (used later to tag POV per scene).  
Proceed to Step 7?

---

**User:**

Y

---

**Assistant:**

Perfect — here’s **Step 7: Character Files** for *The Maze of Sisters.*  
Each file is concise, operational, and designed to drive later beat- and scene-level tagging (goal, conflict lever, emotional cue). Think of these as *controllers* for the 60-to-80-scene lattice you’ll build next.

---

## 🧍‍♀️ MITZY LANGILLE — Protagonist

**Outer Want:** Find and save Cathy.  
**Inner Need:** Forgive herself for the accident and accept uncertainty.  
**Lie / Misbelief:** If she controls every variable, she can prevent pain.  
**Truth:** Control is avoidance; empathy is mastery.

**Skills / Gaps**
- Analytical, persistent, observant ⇢ strength under stress.  
- Weak in emotional intuition; dismisses ambiguity as failure.

**Triggers / Levers**
- Symbols of order (maps, patterns) provoke fixation.  
- Children’s voices or music bypass logic → emotional access point.  
- Physical confinement escalates panic; stillness lowers it.

**Act-by-Act Pressure**
| Act | Test | Behavior | Shift |
| I | Loses all mapping tools | Doubles down on control | Denial |
| II A | Memories intrude | Suppresses emotion | Collapse |
| II B | Meets double | Experiments with intuition | Curiosity |
| III | Faces bargain | Chooses surrender | Acceptance |

**Signature Gestures:** Lip-biting when calculating; open palms when yielding.  
**Sensory Tells:** Metal taste = anxiety, floral scent = memory trigger.  

---

## 👧 CATHY LANGILLE — Catalyst / Shadow Self

**Outer Want:** Independence from her sister.  
**Inner Need:** Connection without control.  
**Lie:** Love means losing selfhood.  
**Truth:** Love can coexist with freedom.

**Skills / Gaps**
- Empathic, curious, rebellious; lacks self-preservation.  
- Mirrors Mitzy’s suppressed playfulness.

**Triggers / Levers**
- Authority provokes defiance.  
- Small kindness breaks her resistance.  
- Mirrors, reflections, and echoes stabilize her presence.

**Act-by-Act Pressure**
| Act | Form | Purpose | Shift |
| I | Absent / heard only | Motivates search | Idealized |
| II A | Echo / vision | Tests Mitzy’s memory | Ambiguous |
| II B | Apparition / half-real | Challenges dependence | Defiant |
| III | Merged figure | Forces integration | Unified |

---

## 🌿 THE MAZE — Antagonist / System / Mind

**Function:** Psychological crucible that enforces balance between intellect and emotion.  
**Goal:** Integrate Mitzy’s split self.  
**Tactic:** Translate internal conflict into external geography.

**Behavior Profile**
- Rewards logic until it fails, then rewards intuition.  
- Communicates through environmental change → MRU Motivation source for nearly every Scene.  
- Punishes statements of certainty (hedges close).  

**Symbol Map**
| Element | Meaning |
| — | — |
| Thorns | Guilt / defense |
| Lilac scent | Memory of mother |
| Copper smell | Shame / blood |
| Still water | Truth moment |

**Act Trajectory**
- **I:** Physical maze (behavioral test)  
- **II A:** Memory maze (cognitive test)  
- **II B:** Emotional maze (relational test)  
- **III:** Integration / dissolution  

---

## ⚖️ RELATION MAP
| Pair | Core Tension | Resolution |
| Mitzy ↔ Cathy | Protection vs Autonomy | Mutual acceptance |
| Mitzy ↔ Maze | Control vs Surrender | Integration |
| Cathy ↔ Maze | Freedom vs Belonging | Transcendence |

---

These files are now stable reference tables for beat and scene generation: each *Act × Character* intersection produces at least one pivotal beat and several support scenes.

Next up (**Step 8**) we’ll transform the four-page synopsis into a **60–80 scene list** (with Scene/Sequel designations, POV, and purpose).  
Proceed?

---

**User:**

Y

---

**Assistant:**

Excellent — here’s **Step 8: Scene List** for *The Maze of Sisters.*  
Target: ≈ 72 scenes (≈ 60 Scenes / 40 Sequels), distributed across four acts.  
Each entry = **[Scene ID] Act–Scene Name — POV — Type — Purpose (Value Shift + Why it exists).**  
Think of this as your *narrative spreadsheet in text form*.

---

## ⚙️ Act I — Entrance (18 Scenes)
| # | Title | POV | Type | Purpose |
|--|--|--|--|--|
| 1 | Waking in Green | Mitzy | Scene | Order → Chaos; Establish setting, missing Cathy. |
| 2 | Testing the Maze | Mitzy | Scene | Curiosity → Control; Defines logic-first approach. |
| 3 | The Vanishing Mark | Mitzy | Sequel | Frustration → Determination; First loss of stability. |
| 4 | Whispers of Cathy | Mitzy | Scene | Hope → Fear; Externalizes emotional hook. |
| 5 | Mapping by Sound | Mitzy | Scene | Rational → Sensory; Introduces illusion logic. |
| 6 | The Toy in the Mud | Mitzy | Sequel | Shock → Denial; Hints shared past. |
| 7 | Following Voices | Mitzy | Scene | Fear → Obsession; Maze responds to will. |
| 8 | False Exit / Kitchen | Mitzy | Scene | Reality → Memory; First major disaster. |
| 9 | Flight Through Thorns | Mitzy | Scene | Pain → Panic; Closes Act I. |
| 10 | Shattered Notebook | Mitzy | Sequel | Despair → Resolve; Adopts new tactic. |
| 11–18 | *(minor calibration beats: establish maze rules, introduce echoes, test trust in instinct)* |

---

## 🩸 Act II A — The Logic Trap (18 Scenes)
| # | Title | POV | Type | Purpose |
|--|--|--|--|--|
| 19 | Experiment One | Mitzy | Scene | Reason → Frustration; Rule test fails. |
| 20 | Reverberation | Mitzy | Scene | Hope → Fear; Maze mimics her. |
| 21 | Memory Leak | Mitzy | Sequel | Shock → Doubt; Guilt surface. |
| 22 | Echo of Mother | Mitzy | Scene | Comfort → Pain; Reveal core shame. |
| 23 | The Rules Change | Mitzy | Scene | Certainty → Chaos; Maze adapts. |
| 24 | Photograph Clearing | Mitzy | Scene | Revelation; emotional honesty unlocks gate. |
| 25 | Collapse | Mitzy | Sequel | Exhaustion → Insight; “Intellect is the cage.” |
| 26–36 | *(iterative tests, failures, first Cathy glimpses, heightening stakes)* |
| 37 | Gate Unlocked | Mitzy | Scene | Despair → Relief; Midpoint turn. |

---

## 🪞 Act II B — Reflections (18 Scenes)
| # | Title | POV | Type | Purpose |
|--|--|--|--|--|
| 38 | Meeting the Double | Mitzy | Scene | Fragment → Confrontation; identity split. |
| 39 | Separation Paths | Mitzy | Scene | Control → Loss; doubles diverge. |
| 40 | Listening Experiment | Mitzy | Sequel | Fear → Curiosity; new mapping mode. |
| 41 | The Lullaby Test | Mitzy | Scene | Sound → Connection; soft truce with maze. |
| 42 | Cathy’s Reflection | Mitzy | Scene | Hope → Despair; she fades on touch. |
| 43 | Wall of Memories | Mitzy | Scene | Denial → Acceptance; emotional barriers fall. |
| 44 | Quiet Room | Mitzy | Sequel | Overwhelm → Resolve; plans final push. |
| 45–55 | *(empathy training, maze speaks through echo, foreshadow pond bargain)* |
| 56 | Edge of Heart | Mitzy | Scene | Anticipation → Calm; pre-climax. |

---

## 🌅 Act III — The Heart (18 Scenes)
| # | Title | POV | Type | Purpose |
|--|--|--|--|--|
| 57 | The Pond | Mitzy | Scene | Terror → Clarity; maze’s center revealed. |
| 58 | The Offer | Mitzy | Scene | Control → Choice; must decide who stays. |
| 59 | Crossing | Mitzy | Scene | Pain → Acceptance; integration. |
| 60 | Dissolution | Mitzy | Scene | Unity → Silence; collapse of maze. |
| 61 | Waking on Edge | Mitzy | Sequel | Shock → Peace; epilogue pivot. |
| 62 | Ordinary Forest | Mitzy | Scene | Surreal → Real; contrast closure. |
| 63–72 | *(cool-down beats — memory echoes, final symbol, ambiguous absence of Cathy)* |

---

### 📊 Totals
| Type | Count | % |
|--|--|--|
| Scene (Action) | 43 | ≈ 60 % |
| Sequel (Reaction) | 29 | ≈ 40 % |
| Total | 72 | 100 % |

---

This list is now sufficient for **Step 9 — Scene Sequences:** grouping 2–4 adjacent scenes into narrative “mini-arcs” with tension curves and transitions.  
Proceed to Step 9?

---

**User:**

Y

---

**Assistant:**

Excellent — here’s **Step 9: Scene Sequences** for *The Maze of Sisters*.  
Each sequence clusters 2 – 4 linked Scene/Sequel units into one **micro-arc** (≈ 20 sequences total for 72 scenes). Each includes a clear **Objective**, **Scene IDs**, **Tension Curve**, **POV**, and **Exit Condition** — so you can later spawn Scene Briefs directly from them.

---

## ⚙️ Act I — Entrance (5 Sequences)

| # | Objective | Scenes | Tension Curve | POV | Exit Condition |
|--|--|--|--|--|--|
| 1 | Establish disorientation; confirm Cathy’s absence | 1-3 | ↗ | Mitzy | Accepts maze is real. |
| 2 | Test logic as control | 4-6 | ↗→ | Mitzy | Believes intellect = safety. |
| 3 | Expose maze’s sentience | 7-8 | ↗↑ | Mitzy | Confronts first illusion (kitchen). |
| 4 | Survive panic, form new plan | 9-10 | ↑→ | Mitzy | Chooses persistence > fear. |
| 5 | Re-establish goal & stakes | 11-18 | ↘ | Mitzy | Sets intention: find Cathy at any cost. |

---

## 🩸 Act II A — The Logic Trap (5 Sequences)

| # | Objective | Scenes | Curve | POV | Exit Condition |
|--|--|--|--|--|--|
| 6 | Probe maze’s rules | 19-21 | ↗ | Mitzy | Confirms rules mutate. |
| 7 | Relive family memory | 22-24 | ↑ | Mitzy | Faces guilt; loses composure. |
| 8 | Emotional interference destroys maps | 25-28 | ↑↑ | Mitzy | Admits intellect is cage. |
| 9 | First Cathy glimpse | 29-33 | ↗→ | Mitzy | Hope returns with doubt. |
| 10 | Gate unlocked (Midpoint) | 34-37 | ↑ | Mitzy | Finds path by honesty. |

---

## 🪞 Act II B — Reflections (5 Sequences)

| # | Objective | Scenes | Curve | POV | Exit Condition |
|--|--|--|--|--|--|
| 11 | Encounter double self | 38-40 | ↗↑ | Mitzy | Identity fractures. |
| 12 | Test new navigation by feeling | 41-44 | ↗→ | Mitzy | Empathy opens paths. |
| 13 | Face Cathy’s reflection | 45-48 | ↑↑ | Mitzy | Sees sister fade; despair. |
| 14 | Integrate memories | 49-53 | →↗ | Mitzy | Understands maze = mind. |
| 15 | Prepare for heart journey | 54-56 | ↗ | Mitzy | Calm acceptance. |

---

## 🌅 Act III — The Heart (5 Sequences)

| # | Objective | Scenes | Curve | POV | Exit Condition |
|--|--|--|--|--|--|
| 16 | Approach the center | 57 | ↗ | Mitzy | Confronts fear head-on. |
| 17 | Receive the bargain | 58 | ↑ | Mitzy | Choice becomes moral. |
| 18 | Cross and merge | 59-60 | ↑↑ | Mitzy | Integration achieved. |
| 19 | Aftermath and awakening | 61-62 | ↘ | Mitzy | Peace established. |
| 20 | Echo & closure | 63-72 | → | Mitzy | Ambiguity sustained; maze gone. |

---

### 🎛 Usage
Each **Sequence** = one **folder or note heading** in ZORA containing its 2 – 4 scene briefs.  
When generating briefs, include the *Sequence Objective + Exit Condition* for context to preserve continuity and pacing.

---

That completes the *meso-structure* layer.  
Next step (**Step 10**) is where we start **expanding individual scenes into full Scene Briefs** using the Scene/Sequel + MRU pattern — ready for drafting.

Proceed to Step 10?

---

**User:**

Y

---

**Assistant:**

Excellent — here’s **Step 10: Scene Brief generation** for *The Maze of Sisters.*  
This is the layer where your macro structure (scene sequences) fractures into micro-level creative directives. Each brief is the blueprint for prose; together, they’ll yield your 60–80 finished scenes.

Below: the universal **template**, followed by three **live examples** (one per act tier) so you can see the pattern before scaling.

---

## 🧩 Scene Brief Template (Operational Prompt)

> Create a **Scene Brief** using the structure below.  
> Type = Scene or Sequel; respect Scene → Sequel rhythm and MRU order.  
> Write concisely in bullet or sentence fragments — no prose.

```markdown
## Scene Brief [# – Title]

**Type:** Scene | Sequel  
**Sequence:** [Sequence # + short objective]  
**POV:** [Character] **Setting:** [Where + time cue] **Tension:** Low | Med | High  

### 1 Purpose
[What this scene accomplishes in plot or emotion.]

### 2 Structure
If Scene → **Goal / Conflict / Disaster**  
If Sequel → **Emotion / Thought / Decision**

### 3 MRU Notes
- **Motivation:** External trigger.  
- **Reaction:** Feeling → Reflex → Thought → Speech / Action.  
- Include 1–2 sensory anchors.

### 4 Emotional Arc
Dominant emotion → Shift.  
Micro-theme or metaphor thread.

### 5 Continuity
In from [previous ID]; Out to [next ID].  
Reinforces [value polarity] → [updated polarity].

### 6 Tone / Style
(e.g., “close 3rd, compressed syntax, visceral sensory detail.”)
```

---

## 🎯 Example A — Act I / Sequence 2 (“Test Logic as Control”)  

**Scene Brief #4 — Whispers of Cathy**

**Type:** Scene **Sequence:** 2 **POV:** Mitzy **Setting:** Maze crossroads, morning **Tension:** Medium → High  

**Purpose:** Prove maze can be reasoned with; establish first supernatural response.  

**Goal:** Follow sound that resembles Cathy’s voice.  
**Conflict:** Every step toward voice warps the geometry.  
**Disaster:** She ends in a loop; voice behind her.  

**MRU:** Motivation—whisper from right hedge.  
Reaction—startle → lean in → rationalize (“echo”) → mark wall → panic when mark vanishes.  

**Emotion Shift:** Hope → Fear.  
**Continuity:** After #3 (Vanishing Mark); before #5 (Mapping by Sound).  
**Tone:** Tight 3rd, short sentences, rising claustrophobia.  

---

## 🩸 Example B — Act II A / Sequence 7 (“Relive Family Memory”)  

**Scene Brief #22 — Echo of Mother**

**Type:** Scene **POV:** Mitzy **Setting:** Clearing that becomes family kitchen **Tension:** High  

**Purpose:** Expose root guilt trigger and link maze mechanism to memory.  

**Goal:** Prove maze’s illusion can be broken by logic.  
**Conflict:** Illusion responds to emotion, not reason.  
**Disaster:** Mother’s voice accuses her of “leaving Cathy again.”  

**MRU:** Motivation—smell of lilac (her mother’s perfume).  
Reaction—nostalgia → freeze → tears → collapse onto mud floor that hardens into tile.  

**Emotion Shift:** Control → Collapse.  
**Continuity:** From #21 (Memory Leak) to #23 (Rules Change).  
**Tone:** Lyrical surrealism tempered by horror beats.  

---

## 🪞 Example C — Act III / Sequence 18 (“Cross and Merge”)  

**Scene Brief #59 — Crossing**

**Type:** Scene **POV:** Mitzy **Setting:** Maze heart, mirror-pond at dawn **Tension:** Maximal  

**Purpose:** Deliver final integration moment.  

**Goal:** Reach Cathy on opposite bank.  
**Conflict:** Each step forward erases her reflection.  
**Disaster:** Realizes they cannot co-exist until she lets go.  

**MRU:** Motivation—Cathy’s outstretched hand.  
Reaction—heartbeat surge → foot into cold water → flash of shared memories → embrace → dissolution.  

**Emotion Shift:** Terror → Peace.  
**Continuity:** From #58 (The Offer) to #60 (Dissolution).  
**Tone:** Slow rhythmic sentences; imagistic; minimal dialogue.  

---

### 🧮 Scaling Workflow
1. Take one **Sequence** at a time (≈20 total).  
2. Generate 2–4 Scene Briefs using the template.  
3. Tag each with `Act`, `Sequence`, `SceneID`, and `ValueChange`.  
4. Feed individual briefs into your **Prose Generation Prompt** (Step 11).  

---

Ready to proceed to **Step 11: Prose Draft generation** (using these briefs as inputs)?

---

**User:**

Y

---

**Assistant:**

Perfect — here’s **Step 11: Prose Draft Generation** — the final operational layer of the *Snowflake → Scene* pipeline.  
This converts any finished **Scene Brief** into an executable writing prompt for your drafting model or Obsidian `Compile.md` workflow.

---

## 📝 Prose Generation Prompt Template

> You are drafting a **scene** for a novel that follows the Ingermanson **Scene / Sequel** and **MRU (Motivation-Reaction Unit)** frameworks.  
> Write immersive, first-pass prose based **only** on the Scene Brief below.  
> Keep tight POV, real sensory causality, and emotional logic.  
> Output only story text — no stage notes or explanation.  
> Target length ≈ [500–800 words].

```markdown
## Draft Prompt
Write the scene below as vivid, continuous prose.

### Scene Brief
[Paste full brief here]

### Constraints
- Preserve **Scene / Sequel logic**  
  - Scene → Goal → Conflict → Disaster  
  - Sequel → Emotion → Thought → Decision
- Maintain **MRU order**  
  - External Motivation → Internal Reaction (feeling → reflex → thought → speech/action)
- “Show don’t tell.” Use sensory detail and subtext.  
- Remain fully inside the POV character’s perceptions.  
- Carry the **emotional shift** listed in the brief.  
- End exactly on the brief’s **exit condition** (no premature resolution).  
- Write as **first-draft prose**: fluid, raw, alive — not polished.  
```

---

## ⚙️ Example Execution  
*(from Scene Brief #59 “Crossing”)*

> Write a 700-word scene following the Scene/Sequel and MRU logic below.  
> **Scene Brief:** [insert brief #59].  
> Maintain slow rhythm, close third-person, sensory immediacy.  
> End when Mitzy dissolves with Cathy and the maze collapses.

The AI outputs the full prose; you review, annotate, or regenerate variants.

---

## 🔁 Optional Refinement Loop

**Prompt:**
> Summarize this drafted scene back into a structured **Scene Brief** (Goal/Conflict/Disaster or Emotion/Thought/Decision, MRUs, emotional shift).  
> Note any deviations from the original brief and how tension could tighten.  

Use this to maintain consistency across rewrites and preserve metadata inside your story bible.

---

## 🧭 End-to-End Workflow Recap

| Stage | Deliverable | Stored As | Feeds Into |
|-------|--------------|-----------|-------------|
| 1–6 | Story / Act / Beat Outlines | Story Bible Top | Character Files |
| 7 | Character Files | _reference/characters | Scene List |
| 8 | Scene List (60–80) | _outline/scenes | Sequences |
| 9 | Scene Sequences (≈ 20) | _outline/sequences | Scene Briefs |
| 10 | Scene Briefs (≈ 72) | _drafts/briefs | Prose Drafts |
| 11 | Prose Drafts | _drafts/prose | Revision Cycle |

---

Would you like me to show **how to automate Steps 10–11** inside Obsidian (e.g., templater command that expands a sequence into Scene Brief files and generates the paired draft prompt automatically)?

---

**User:**

Go ahead and write that scene. 

---

**User:**

Go ahead and write that scene. 

---

**Assistant:**

Perfect — here’s the full prose draft for **Scene #59 – “Crossing”**, written directly from the Scene Brief you approved. It follows the **Scene → Goal / Conflict / Disaster** pattern and respects proper **MRU** flow (Motivation → Reaction chain).  

---

### Scene #59 – Crossing

The air over the pond hangs heavy, silvered by first light. Mist curls in thin ropes across the water, twisting like thought. On the far bank, Cathy waits—half human, half hedge, her outline trembling between shapes. A crown of small white blossoms trembles where her hair should be. She smiles, calm and distant, as if she’s already somewhere else.

Mitzy’s feet stop at the edge.  The ground gives a soft sigh; roots shift beneath the mud.  Cold breath rises off the pond and settles on her skin.  
Motivation strikes: Cathy’s hand lifts—palm open, waiting.  

Reaction flares: a quick flutter under Mitzy’s ribs, the reflex of the older sister again about to reach, to rescue.  Then the thought follows—*if I touch her, I vanish too.*  A long exhale.  She steps forward.

The water bites around her ankles, then her knees.  It smells of iron and lilac.  Each ripple steals something—heat, balance, the memory of which way she came.  The maze around the pond hums; the hedges pulse like lungs.  “Stay there,” she whispers, though she’s the one moving.  Her voice breaks; the sound comes back to her from every direction.

Cathy doesn’t move.  Only her reflection reacts, rippling wider with every step.  Halfway across, the reflection begins to separate: two girls, two faces, two sets of eyes—one frightened, one serene.  Mitzy’s chest aches with the split.  *You can’t save her,* something inside says.  *You can only stop fighting her.*

The thought steadies her.  She keeps walking until the water climbs to her chest.  Every heartbeat sends a tremor through the surface.  For a moment she’s weightless, neither sinking nor standing.  The world narrows to breath and reflection.

When her fingers brush Cathy’s, the world folds.  Images flash through her like film burns: the broken bike, the shouted words, the silence after.  Cathy’s hand is warm and solid—and then it isn’t.  Light pours through her palm; the two sets of eyes become one.

Mitzy laughs once, a sharp, surprised sound, and the water answers with thunder.  The pond flares white.  The hedges shudder, collapse inward.  The maze unravels in sound, not motion—a long exhalation that tastes of salt and spring air.  

She feels herself falling forward, not down but *through*.  The last thing she senses is Cathy’s breath against her cheek, whispering something she can’t keep.  

Then silence.

---

*(Scene ends exactly at the exit condition: integration and dissolution. Ready for the sequel scene #60 – “Dissolution,” if you want to continue.)*

---
