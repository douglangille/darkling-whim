# Obsidian AI longform writing

**Created:** 2025-10-22 19:17:24
**Updated:** 2025-12-07 22:31:29
**Turns:** 39

---

**User:**

Obsidian longform AI

---

**Assistant:**

Here’s a concise breakdown of using entity["software", "Obsidian", 0] + AI for **long-form writing**, with strategy + practical setup geared for your higher-ed IT management context.

---

## What this means  
You want to leverage Obsidian not just for note-taking or small drafts, but for structured, long-form content (reports, articles, chapters) *with AI support* (generation, research, revision).  
Obsidian is well suited: a markdown-file vault, flexible linking, plugin ecosystem. citeturn0search2turn0search7turn0search0  
AI support is available via plugins for semantic search, writing assistance, and vault-aware processing. citeturn0search6turn0search1  

---

## Key Components & Workflow  
Here’s how you might set it up:

### 1. Vault structure for long-form  
- Create a folder (e.g., `/Projects/ReportName/`) with sub-folders:  
  - `Drafts/Chapter01.md`, `Chapter02.md`, …  
  - `Research/` for raw references, notes, data.  
  - `Assets/` for images, tables, etc.  
- Use a “home” note (e.g., `ProjectOverview.md`) with outline, timeline, goals.  
- Use linking: each chapter note links to research notes, asset notes, etc. This supports traceability and modular writing.  
- Use Canvas view or graph view optionally to visualise structure. citeturn0search7  

### 2. AI-assisted plugins  
- Install community plugin such as entity["software", "Smart Connections", 0] (for semantic note linking) and entity["software", "CoPilot", 0] (for editing, chat with your vault). citeturn0search6turn0search1  
- With Smart Connections you can surface related notes even if they don’t share exact keywords.  
- With CoPilot (or similar) you can:  
  - Ask “What are the key themes in Chapter 1 draft?”  
  - Select a text block → Expand/Shorten/Fix grammar.  
  - Use Vault Q&A to ask questions of your entire vault context.  
- Note: Many of these require an API key or external LLM usage (so cost, data-privacy implications). citeturn0search6  

### 3. Long-form writing workflow  
- **Preparation**: Use research notes, collect reference items into your vault. Tag/link them.  
- **Outline**: Use your ProjectOverview note to generate a skeleton: e.g., Chapter headings + bullet points.  
- **Drafting**: Each chapter as its own note. Write in “chunks” rather than long streams. Obsidian supports easy jumps between chapters.  
- **AI assistance**:  
  - Use AI to generate a first draft of a chunk based on prompts.  
  - Use AI to refine style, summarise sections, check cohesion.  
  - Use semantic search to pull in relevant previously-written material.  
- **Revision & integration**: Link drafts together, ensure consistency (terms, references). Use backlinks and graph view to spot orphaned notes or loose connections.  
- **Publishing/exporting**: Once finalised, export to markdown/Word/PDF as needed. Obsidian supports next steps.

---

## Specific Considerations for Your Context (Higher Ed IT Manager)  
- **Data privacy / security**: Since you may work with institutional data, ensure AI plugin usage complies with your org’s data governance (e.g., do external LLMs require data upload?).  
- **Collaboration**: If multiple authors/editors, consider how your vault is shared or synchronised (e.g., via Obsidian Sync or Git).  
- **Version control**: Long-form work benefits from versioning. Use version history or Git integration.  
- **Integration with other tools**: You may already use reference managers (Zotero), LMS systems, shared drives. Ensure your Obsidian vault aligns or interoperates.  
- **Scalability**: If you’ll do multiple reports/projects, standardise your vault structure, templates, plugin-set for reuse.

---

## What currently works / Issues / Fixes  

### What works  
- Obsidian’s flexibility allows modular, linked writing rather than monolithic docs.  
- AI plugins exist that enable vault-aware assistance (semantic search, editing).  
- The vault model aligns with iterative writing and complex research.  

### Issues  
- Learning curve: Setting up a “good” vault structure, plugins, workflow takes time. As one user said:  
  > “Start with what you want in a tool … The nice thing about Obsidian is that it’s very flexible and customisable.” citeturn0search0  
- AI plugin cost/privacy: Some require API keys, send data off-site.  
- Integration to export/publish: You’ll still need to export to typical long-form formats (Word, PDF), which may require extra effort.  
- Over-customisation risk: Spending more time on plugins/themes than writing.

### Fixes  
- Begin with a minimal setup: Obsidian + one AI plugin + simple folder structure. Expand only when workflow stabilises.  
- Define a template for each “long-form project” (outline note, chapter notes, asset folder) so you don’t build from scratch each time.  
- Document your workflow (especially with collaborators) so you maintain consistency.  
- Set policy for sensitive data: mark vaults/projects which shouldn’t upload data to external AI services; consider offline-only models if needed.  
- Theatre of export: experiment early with exporting your vault to final formats to avoid last-minute headaches.

---

## Sample Rewrite – Workflow Summary  
> Use Obsidian to manage long-form writing by treating each chapter as a modular markdown note within a project folder, link to research/asset notes, and leverage AI-plugins for semantic linking and draft refinement. Start simple; build structure and templated workflow; ensure data governance for AI use; refine export to final format early.

---

If you like, I can **map out a ready-to-use template vault structure** (folder names, note templates, plugin list) specifically tailored for your higher-ed reports and set up collaboration. Would that be useful?

---

**User:**

The longform plugin is an obvious plugging to use

---

**Assistant:**

Exactly — **Longform** is the obvious core plugin for serious writing in Obsidian. Here’s how it fits, what it does well, and how to combine it with AI tools for a robust workflow.

---

## 1. What Longform Does

**Purpose:** turns Obsidian into a Scrivener-style drafting environment for multi-section works.

**Core features:**
- **Project organization:** creates a “Longform Project” folder with ordered scenes or chapters.  
- **Outline view:** lets you reorder scenes via drag-and-drop.  
- **Writing focus:** gives a distraction-free draft view.  
- **Compilation:** exports your ordered notes into a single manuscript (`.md`, `.docx`, `.pdf` via Pandoc).  
- **Metadata:** uses YAML for title, order, word count, status, etc.  
- **Integration:** works seamlessly with Obsidian’s core linking and markdown notes—so your story world, research, and drafts coexist.

It’s perfect for **long reports, essays, or fiction**—anything that benefits from chunked drafting and controlled assembly.

---

## 2. Where AI Fits In

Longform itself is not AI-aware—it just manages structure. But you can layer AI on top cleanly:

### Recommended Pairings
| Function | Plugin or Integration | Example Use |
|-----------|----------------------|--------------|
| **Semantic search & idea linking** | *Smart Connections* | “Find related notes for this scene/chapter.” |
| **Vault-aware chat** | *Copilot* or *Text Generator* | “Summarize Chapter 3 and suggest transitions.” |
| **Local generation (privacy-safe)** | *Text Generator + Ollama (local LLM)* | Expand draft paragraphs offline. |
| **Editing/refinement** | *Copilot inline commands* | “Tighten prose to 120 words.” |

If you prefer to stay external (no plugins sending data out), you can copy a chapter draft into ChatGPT for revision, then paste it back—Longform will still track it in sequence.

---

## 3. Practical Setup

**Minimal, low-friction configuration:**

1. **Install & enable:**
   - Community plugins → search *Longform* (by Kevin Barrett).  
   - Optionally add *Smart Connections* + *Copilot*.
2. **Create a Project:**  
   - `Projects/YourTitle/` with a `Scenes/` folder.
   - Each note = a scene or section with frontmatter like:
     ```yaml
     ---
     title: Scene 12 — Boardwalk Handoff
     order: 120
     status: draft
     ---
     ```
3. **Write modularly:**  
   - Keep each section small and self-contained (500–1500 words).  
   - Use internal links to research notes (`[[TechRules]]`, `[[Maggie]]`, etc.).
4. **Compile:**  
   - Use Longform’s “Compile” to merge scenes into one document for export or AI revision.  
   - You can even compile only selected scenes for a subset draft.

---

## 4. AI-Augmented Longform Flow

1. **Plan:** Create outline in Longform’s project index.  
2. **Draft:** Write short notes per scene; when stuck, highlight a paragraph → use Copilot or Text Generator to expand or summarize.  
3. **Link:** Use Smart Connections to discover relevant past notes (worldbuilding, research).  
4. **Review:** Use AI to critique tone, structure, clarity.  
5. **Compile:** Export and run a final coherence check in ChatGPT or Word.  

This modularity keeps AI in a supportive role—helping with flow and continuity—without taking over your core voice.

---

## 5. Cautions

- **Avoid plugin overload.** Longform + one AI plugin is usually enough.  
- **Respect vault boundaries.** Don’t point AI tools at private or institutional data unless cleared.  
- **Backups.** Longform’s compile doesn’t version drafts—use Git or Obsidian Sync.

---

## 6. TL;DR

> Use **Longform** for structure and compilation; layer a single AI plugin (Copilot or Text Generator) for writing aid; keep research and drafts linked in the same vault. Start simple—structure first, AI second.

---

Would you like me to sketch a **starter template** for a Longform + AI project—folders, YAML front-matter, and recommended plugin settings? It’d be tuned for your nonfiction/reporting workflow rather than fiction.

---

**User:**

Ideally, I’d like the scene brief within the scene files frontmatter. I figure between it and tags, I should be able to collect enough context to use an AI plugin to edit or draft the scene. How would this work?

---

**Assistant:**

Exactly right — you can embed the **scene brief** (or synopsis) directly inside the YAML frontmatter. That gives an AI plugin (like Copilot or Text Generator) enough structured metadata to infer tone, purpose, and context without scraping your whole vault.  

Here’s how it works, and how to structure it cleanly.

---

## 1. Structure of a Scene File

Use **rich but compact frontmatter** — think of it as a “prompt capsule” that both humans and AI can read.

```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
status: draft
tags: [@Maggie, @Richard, @Harbourfront, @TechRules]
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows.
  Maggie plants a decoy while Richard tracks a triangulated signal.
  They debate aborting versus a soft handoff under a camera blind spot.
tone: tense, cinematic, intimate
goal: establish fragile trust between Maggie and Richard
---
```

### Why this works
- **`brief`** — tells the AI what’s supposed to happen.  
- **`tags`** — act as entity anchors for retrieval (“Maggie”, “TechRules”).  
- **`tone` and `goal`** — give stylistic and emotional guidance.  
- **`order` and `status`** — help Longform compile and track progress.

Below the YAML, you keep your actual draft text.

---

## 2. Using It with an AI Plugin

### Option A: **Copilot (Vault-aware)**
- Copilot can access the current note’s metadata block automatically.  
- You can issue inline commands like:
  ```
  /expand scene using brief
  /revise tone consistent with frontmatter
  /summarize scene for continuity
  ```
- If Copilot supports “system” or “context” injection, set it to read YAML before body text. That gives the model situational awareness without you re-prompting.

### Option B: **Text Generator (Template-driven)**
- Create a prompt template that reads the YAML fields:
  ```
  You are editing a scene titled "{{title}}".
  Scene brief:
  {{brief}}

  Tags: {{tags}}
  Tone: {{tone}}
  Goal: {{goal}}

  Task: {{selection}}
  ```
- Then trigger the template to draft, expand, or rewrite selected text.
- Text Generator variables auto-substitute YAML fields, so every scene carries its own mini-brief.

### Option C: **External ChatGPT Workflow**
- When you copy the scene into ChatGPT, include the YAML — it acts as a structured “prompt header”.
- Example:
  ```
  ---
  [YAML as above]
  ---
  Draft:
  [scene text]
  ```
  Then ask: *“Revise this scene to align with the brief and tone above.”*

---

## 3. Workflow Integration

1. **Plan** — create all scene files from a template containing the frontmatter structure above.  
2. **Outline** — Longform orders them via `order`.  
3. **Write** — draft in chunks; the `brief` reminds you what belongs.  
4. **Revise** — select sections and trigger your AI plugin; it reads the YAML for guidance.  
5. **Compile** — Longform ignores YAML during export, so it won’t pollute the manuscript.

---

## 4. Optional Enhancements

- **Add a `refs` array** for cross-scene continuity:
  ```yaml
  refs: [@Scene11, @Workshop, @ProtestDevice]
  ```
- **Add `context:` field** for setting, weather, or props.
- **Add `char_arcs:`** if you want AI continuity across arcs.

---

## 5. TL;DR

> Put a concise scene brief, tone, and goal directly in frontmatter.  
> Use an AI plugin template that reads those fields as context.  
> Longform compiles normally, AI gains localized awareness, and you stay in-vault with zero extra scaffolding.

---

Would you like a ready-to-use **scene template** (.md) and **Text Generator prompt template** that implements this structure?

---

**User:**

Which obsidian plugins best support this kind of workflow where the frontmatter in a scene references bible entries elsewhere in the vault to feed an AI-assisted composition

---

**Assistant:**

Good thinking—embedding scene briefs and linking to “bible” or reference entries via frontmatter works nicely in entity["software","Obsidian",0]. Below are **three strong plugin categories** to support that workflow + specific plugin suggestions, with pros/cons and how they fit your AI-assisted long-form process.

---

### 🔧 Plugin categories & picks

#### 1. Metadata & frontmatter helpers  
These let you define, maintain, and leverage YAML fields (like your “brief”, “tags”, “refs”) consistently.

- entity["software","Frontmatter Generator",0] — automatically generate frontmatter template when you create/save a note. citeturn0search9turn0search2  
  - **Why use it**: Ensures each scene note begins with the same structure (title/brief/refs/tags) without manual setup each time.  
  - **Considerations**: It won’t itself enforce link consistency or AI-awareness.

- entity["software","Dataview",0] (implied by use) — while not always listed explicitly, you’ll want Dataview to query frontmatter and link refs across notes.  
  - **Why**: You can pull across all notes referencing a given “bible” entry, check scenes where a character appears, etc.  
  - **Note**: Dataview doesn’t automatically trigger AI, but gives your metadata structure real value.

#### 2. Linking / note‐reference automation  
These help you maintain connections between your scenes, bible/reference notes, and research. Useful so your “refs:” list in YAML is backed by real links.

- entity["software","Note Linker",0] — scans content and suggests/creates links between notes. citeturn0search6  
  - **Why**: Helps ensure when you list a reference in frontmatter, you’re linking to an actual note. Keeps your “bible” entries discoverable and usable by AI.  
  - **Limitations**: It’s more passive; you still define the refs manually but automation reduces drift.

- For Bible‐specific workflows (if your “bible” entries are scripture or structured references):  
  - entity["software","Bible Linker",0] or entity["software","YouVersion Linker",0] — link bible verses or external references. citeturn0search5turn0search3turn0search15  
    - **Why**: If your “bible” in the vault is a structured reference system (characters, world rules, themes), this kind of plugin helps link them.  
    - **Caveat**: Might be more than you need if your “bible” is not scriptural but rather story world reference; but concept is analogous.

#### 3. AI / writing assistance integrations  
These take your metadata + vault context and use it to assist in drafting/editing. The better your scene “brief” + “refs”, the better the input the AI has.

- entity["software","Smart Composer",0] — listed as an AI chat/writing assistant for Obsidian with context awareness. citeturn0search2turn0search0  
  - **Why**: It allows you to ask vault-aware writing/editing questions (“Here’s Scene 12, unify tone, reference these bible entries”).  
  - **Important**: Check how much it reads frontmatter vs body text; you’ll likely need to prompt/structure accordingly.

- Generic combination: Use an AI provider plugin (Hub) + your frontmatter template. For instance, define a prompt that reads your fields (brief, refs) and sends them to the LLM.  
  - Example: “Using the brief and the referenced bible entries below, draft the scene in tone X”.

---

### 📋 Workflow example: “scene → bible ref → AI draft”

Here’s how it might look step by step:

1. **Create reference entries** (“bible” entries) in your vault  
   - e.g., `World-Rules.md`, `Character-Maggie.md`, with frontmatter describing each.  
   - Link them via internal links (so scenes can reference `[[Character-Maggie]]` etc).

2. **Set the scene file template** (via Frontmatter Generator)  
   ```yaml
   ---
   title: Scene 12 — Boardwalk Handoff
   order: 120
   status: draft
   tags: [scene, chapter12, boardwalk]
   brief: |
     At dusk on the harbourfront, Maggie plants a decoy while Richard tracks a triangulated signal.
   refs:
     - [[Character-Maggie]]
     - [[Character-Richard]]
     - [[World-Rules-TechTrafficking]]
   tone: tense, cinematic, intimate
   goal: establish fragile trust between Maggie and Richard
   ---
   ```

3. **Write or expand** the scene in body.  
   - Use Note Linker to ensure all refs are actual links.

4. **Invoke AI plugin** with a prompt template:
   ```
   You are writing scene titled "{{title}}".
   Brief: {{brief}}
   Tone: {{tone}}
   Goal: {{goal}}
   References: {{refs}}
   Write or refine the scene below:
   [scene body]
   ```

5. **Review**: The AI’s output uses context from frontmatter + referenced notes (since you’ve linked them). Then you refine, link further as needed.

6. **Compile** via entity["software","Longform",0] into a full document.

---

### ✅ Summary & recommendation  
- Use **Frontmatter Generator** to standardise scene metadata.  
- Use **Note Linker** (and maybe Bible Linker) to ensure references are proper links.  
- Use an AI plugin like **Smart Composer** (or your chosen AI provider) to draft/edit based on frontmatter + linked refs.  
- Use Dataview queries (optional) to track which scenes reference which bible entries and ensure coverage/consistency.

---

If you like, I can **pull together a shortlist of the top 5 Obsidian AI-writing plugins** (with features comparison) and map how each handles frontmatter + references in your workflow. Would you like that?

---

**User:**

Sure

---

**Assistant:**

Here’s a refined shortlist of **top Obsidian AI-writing plugins** well suited to a workflow where scene files carry front-matter referencing “bible” entries. After the list I’ll include a comparison table and how each aligns with your scene/brief/ref setup.

---

## ✅ Top Plugins (with features + fit)  
1. **entity["software", "Smart Connections", 0]**  
   - Utility: Builds semantic embeddings of your vault, surfaces related notes even without exact keywords. citeturn0search8turn0search3turn0search2  
   - Fit: Helps you automatically find “bible” entries relevant to a scene (via tags/refs) so your AI prompt is richer.  
   - Limitations: Primarily discovery/semantic linking; less focused on drafting/editing.

2. **entity["software", "CoPilot (Obsidian)", 0]**  
   - Utility: AI assistant for editing, summarising, vault Q&A, custom prompts. citeturn0search8turn0search2  
   - Fit: You can use it to “Revise scene according to brief + refs” with front-matter guiding the prompt.  
   - Limitations: Requires API key; cost/privacy considerations.

3. **entity["software", "Text Generator", 0]**  
   - Utility: More direct text generation plugin connecting to various LLMs/local endpoints. citeturn0search10turn0search0  
   - Fit: Good for initial draft of scene: use front-matter as prompt header, generate body.  
   - Limitations: Must build prompt logic yourself; may not include linked context unless you manage it.

4. **entity["software", "Smart Composer", 0]**  
   - Utility: Emerging plugin emphasising “contextual chat” and “apply edit” in Obsidian, with the ability to tag files as context. citeturn0search4  
   - Fit: Ideally aligns with scene-files + front-matter referencing bible entries: you tag/ref scenes & notes as context and prompt accordingly.  
   - Limitations: Possibly still beta; may need more setup.

5. **entity["software", "AI Assistant", 0]**  
   - Utility: General plugin enabling chat/prompt mode inside notes (supports selected text, chat mode) via GPT-3.5/4 etc. citeturn0search6  
   - Fit: Lightweight fallback if you don’t want full draft/edit workflow—good for ad-hoc prompt of scene + brief.  
   - Limitations: Less specialised for scene workflow, perhaps fewer advanced integrations.

---

## 📊 Comparison Table  
| Plugin            | Strengths                       | Weaknesses                    | Ideal Use in Scene Workflow                          |
|-------------------|----------------------------------|-------------------------------|-----------------------------------------------------|
| Smart Connections | Vault-wide semantic note linking | Not full drafting engine      | Surfacing relevant “bible” entries to reference      |
| CoPilot           | Editing, draft assistance, QA    | Cost/API dependency           | Refining scene draft per front-matter brief & refs  |
| Text Generator    | Direct generation from prompts   | More manual setup             | Generating first cut of scene using front-matter    |
| Smart Composer    | Context-aware editing/drafting   | Beta/in development            | Seamless integration: scene + linked context        |
| AI Assistant      | Lightweight chat/prompt utility  | Less depth than others        | Quick edits or brainstorming within scene note      |

---

## 🎯 Best Fit for Your Workflow  
Since you’re using: “scene file front-matter includes brief + tags + refs to bible entries”, these plugins support different parts:

- Use Smart Connections to **identify and validate** the references (bible entries) so your “refs:” front-matter list stays meaningful.  
- Use Text Generator or Smart Composer to **generate or expand** the scene based on the front-matter (brief, tone, goal, refs).  
- Use CoPilot to **fine-tune/edit** the scene: check coherence, tie back to the bible entries, ensure consistency of tone/characters across scenes.  
- Use AI Assistant for ad-hoc prompts or brainstorming smaller chunks when you don’t need full generation.

---

## 🔍 Additional Considerations & Setup Tips  
- Ensure your “bible entries” (characters, rules, settings) are in stable notes with consistent titles/links so “refs:” in scenes can use `[[Note-Title]]` form.  
- Build a standard front-matter template across scenes so plugins can parse fields (`title`, `brief`, `refs`, `tone`, `goal`).  
- Decide on whether AI plugin supports pulling in referenced notes automatically (some do RAG via vault QA) or you manually include them in the prompt.  
- Review each plugin’s privacy/data-handling: if your vault has institutional/confidential content, prefer those that work offline or locally.  
- Track cost/use if cloud-based (e.g., CoPilot) and monitor tokens usage.

---

If you like, I can **pull live links + version/status + user-reviews** for *each* of these plugins (Smart Connections, CoPilot, Text Generator, Smart Composer, AI Assistant) so you can pick which to test first. Would that be helpful?

---

**User:**

It feels like a mix of smart connections and smart composer would do the trick.. use OpenRouter and a free model for smart connections and something like Claude sonnet via OpenRouter for smart composer. 

Let smart connections handle most of the story-bible context linking ?

---

**Assistant:**

Exactly — that’s the cleanest and most modular configuration.  

Here’s how that pairing works, and how to tune it so you get *vault-aware, context-rich drafting* without bloating your setup or exposing sensitive material.

---

## 1. Architecture: Division of Labour

| Role | Plugin | Function |
|------|---------|-----------|
| **Knowledge fabric** | **Smart Connections** | Builds semantic embeddings of your vault. It becomes your “story-bible whisperer”: auto-surfacing relevant notes (characters, settings, tech rules) when you’re working in a scene. |
| **Language generation / editing** | **Smart Composer** | Reads the current note (scene) + its frontmatter + optionally selected context notes (from Smart Connections suggestions) to compose or revise prose using a model (e.g., Claude Sonnet). |

Result:  
- Smart Connections = *memory and context engine*  
- Smart Composer = *voice and craft engine*  
Both stay modular and respect your YAML metadata.

---

## 2. Typical Scene Workflow

**Scene file:**
```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows.
  Maggie plants a decoy; Richard tracks a triangulated signal.
  They debate aborting versus a soft handoff.
tags: [@Maggie, @Richard, @Harbourfront]
refs: [@Workshop, @TechRules, @Scene11]
tone: tense, cinematic, intimate
goal: establish fragile trust between Maggie and Richard
---
```

**Process:**
1. Open the scene file.  
2. Smart Connections surfaces links like `Character–Maggie`, `TechRules`, `Scene 11`.  
3. You select relevant context notes → “Send to Smart Composer.”  
4. Smart Composer builds a composite prompt:  

   ```
   Context: [contents of refs + Smart Connections context]
   Brief: [frontmatter brief]
   Tone: [frontmatter tone]
   Goal: [frontmatter goal]
   Task: draft or edit scene below
   ```
5. Claude Sonnet (via OpenRouter) handles the actual writing/editing, staying grounded in your bible context.

---

## 3. OpenRouter Strategy

- **Smart Connections model:** a *small, cheap embedding model* (like `mistral:instruct` or `gpt-3.5-turbo-free`) for semantic linking. You don’t need nuance here—just vector proximity.  
- **Smart Composer model:** a *higher-IQ creative model* such as `Claude 3 Sonnet` for text generation and style control.  

This separation keeps your costs near zero and your performance balanced:
- Embedding/semantic tasks stay local-ish and fast.  
- Generative tasks go to a premium model when needed.

---

## 4. Implementation Tips

- **Tag consistency:** keep bible entries prefixed (`@Maggie`, `@TechRules`) so both plugins can identify them semantically and by tag.  
- **Frontmatter template:** lock the keys (`brief`, `tone`, `goal`, `refs`) across all scenes so prompt templates read cleanly.  
- **AI privacy:** Smart Connections works on local embeddings; Smart Composer sends only selected text/context to OpenRouter, so you maintain control.  
- **Curation loop:** periodically run Smart Connections “refresh embeddings” after major vault edits to keep similarity accurate.  

---

## 5. Optional Add-ons

- **Dataview dashboard** to show which bible notes are unreferenced or which scenes link to each character.  
- **Longform plugin** still handles ordering/compilation; AI tools just enrich each chunk.  
- **Local backup model** via Ollama (e.g., `mistral`) if you want offline operation later.

---

### TL;DR
> Yes — let **Smart Connections** handle the *semantic linking and bible context discovery*, and let **Smart Composer** handle *generation and editing* using that context.  
> Pair lightweight OpenRouter embeddings for Smart Connections with a strong creative model (Claude Sonnet) for Smart Composer.  

Would you like a one-page **setup guide** for this stack (plugin settings, model config, and YAML template)? It’d give you a turnkey baseline for testing.

---

**User:**

Yes please 

---

**Assistant:**

Here’s a one-page **setup guide** for an Obsidian *Longform + Smart Connections + Smart Composer* stack using OpenRouter and structured front-matter.  
It’s tuned for your “scene + story bible + AI-assist” workflow.

---

## 🧭 Purpose
Create a modular, context-aware writing environment:
- **Longform** → structure & compile  
- **Smart Connections** → context discovery from your bible  
- **Smart Composer** → AI drafting/editing using that context  
- **OpenRouter** → unified access to free + premium LLMs

---

## 🧩 1  Plugin Setup

| Plugin | Purpose | Key Settings |
|---------|----------|--------------|
| **Longform** | Manage ordered scenes & export | “Scenes folder” → `/Projects/<Title>/Scenes` |
| **Smart Connections** | Build embeddings & surface related notes | “Embedding model” → `mistral:instruct` (or any free OpenRouter model) <br> “Auto-index vault” → ✅ on <br> “Context size” → 3–5 notes |
| **Smart Composer** | Draft/edit with selected context | “Provider” → `OpenRouter` <br> “Model” → `anthropic/claude-3-sonnet-20240229` <br> “Prompt mode” → Template-based <br> “Context from” → `Smart Connections + Selected notes` |
| *(optional)* Dataview | Query metadata (which scenes use which refs) | default |

---

## 🗂 2  Vault Structure
```
/Projects/
  /ClockMistress/
    ProjectOverview.md
    /Scenes/
       Scene_011_Broken_Resonator.md
       Scene_012_Boardwalk_Handoff.md
    /Bible/
       Character_Maggie.md
       Character_Richard.md
       Setting_Lunenburg.md
       TechRules.md
```
Each *bible* note has concise YAML + summary paragraph for Smart Connections to embed meaningfully.

---

## 🧾 3  Scene Template (front-matter)

```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
status: draft
tags: [@Maggie, @Richard, @Harbourfront]
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows.
  Maggie plants a decoy; Richard tracks a triangulated signal.
  They debate aborting versus a soft handoff.
refs:
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[TechRules]]
tone: tense, cinematic, intimate
goal: establish fragile trust between Maggie and Richard
---
```
Below YAML: your prose draft.

---

## ⚙️ 4  Smart Composer Prompt Template
*(store in plugin’s templates folder)*

```
You are revising a scene titled "{{title}}".
Scene brief:
{{brief}}

Tone: {{tone}}
Goal: {{goal}}

Context notes (summaries of {{refs}}):
{{context}}

Task: {{selection}}
Return polished prose consistent with the brief and tone.
```

When you highlight text and trigger the template, Smart Composer merges in:
- front-matter fields,
- Smart Connections’ suggested context notes (summarized),
- and your selected text or empty body for new draft.

---

## 🔄 5  Workflow Loop
1. **Create** new scene via Longform → auto-apply YAML template.  
2. **Write/Outline** manually or paste seed text.  
3. **Invoke Smart Connections** → review surfaced bible entries.  
4. **Send to Smart Composer** → “Expand draft using brief + context.”  
5. **Edit & Commit** — manual polish, version via Git or Obsidian Sync.  
6. **Compile** in Longform → full manuscript.  
7. **Periodic:** Smart Connections → “Re-index vault.”

---

## 🔒 6  Privacy & Cost Notes
- **OpenRouter keys** are per-plugin; keep them in `.env` or plugin settings, not in front-matter.  
- Use **free/light model** for Smart Connections (embeddings cheap).  
- Use **Claude Sonnet** for Smart Composer to get high-quality edits.  
- No vault-wide uploads—only text you select or context you include.

---

## ✅ Summary
> Smart Connections = your memory layer.  
> Smart Composer = your writing partner.  
> Longform = your structure and export.  
> Front-matter = your prompt capsule.

---

Would you like me to generate a **ready-to-import template pack** (scene note, bible note, Smart Composer prompt, and Dataview dashboard) zipped for Obsidian?

---

**User:**

The guy who made the smart composer plugin made one called smart context. How does that pairing work for my workflow?

---

**Assistant:**

Good call — digging into how entity["software", "Smart Context", 0] fits alongside entity["software", "Smart Connections", 0] is smart. Here’s an analysis of how they differ, how they integrate, and how you could apply them in your “scene + bible + AI‐assist” workflow.

---

## 🔍 What each plugin does

### Smart Connections  
- Built to create semantic embeddings of your vault and surface related notes (even when they don’t share exact keywords). citeturn0search1turn0search11turn0search4  
- Works locally (privacy first) by default; supports local embedding models. citeturn0search4turn0search11  
- Primarily geared toward **discovery/linking**, not directly drafting or copying large context.  
- Example: You open a scene file → Smart Connections suggests “Relevant bible entries / previous scenes / rules” based on content, so you can bring them into drafting.

### Smart Context  
- A newer plugin (from the same author) that focuses on **context assembly / copying** for AI prompts. citeturn0search2turn0search13  
- Features: copy an entire folder or selected files (including linked notes) into clipboard as context for AI. Can exclude sections via headings. citeturn0search2  
- So: It’s about **packaging context** (e.g., for sending to ChatGPT or another LLM) rather than automatic embedding/linking.

---

## 🔧 How the pairing could work in YOUR workflow

Your workflow: scene files with front-matter containing brief, tags, refs → use AI to draft/edit scenes referencing story-bible entries.

Here’s how Smart Connections + Smart Context can collaborate:

- **Smart Connections**: While you’re writing a scene, this plugin suggests which “bible” notes (characters, rules, settings) are semantically relevant based on your scene’s body and front-matter. It helps you **discover** context you might have forgotten.  
- **Smart Context**: Once you’ve selected the relevant bible entries (via refs + suggestions from Smart Connections), you use Smart Context to **assemble** those entries (plus perhaps the scene front-matter + draft body) into a chunk of context you can feed into your AI (via your prompt or via Smart Composer). It copies or packages all the necessary notes into one clean context envelope.  
- **Smart Composer (or whichever AI drafting tool)**: Receives the context (assembled by Smart Context), plus the scene’s front-matter (brief, goal, tone) and the draft body, then generates or edits accordingly.

---

## ✅ Recommended implementation steps

1. **Install all three**: Smart Connections, Smart Context, Smart Composer (or equivalent AI‐draft plugin).  
2. **Scene front-matter** remains your control metadata (brief, refs, tags, tone).  
3. **Writing a scene**:  
   - Write seed draft in the scene note.  
   - Open Smart Connections sidebar → view suggestions for bible entries/previous scenes.  
   - Pick the ones you want to include → they should match your `refs:` list (or update your `refs:` list).  
   - Use Smart Context: choose those notes (plus maybe the scene note) → copy as structured context.  
   - In Smart Composer: use prompt template that includes the front-matter plus the copied context → ask the model to draft/refine.  
4. **Revision loop**: Use Smart Connections again to confirm coherence (e.g., did you reference a rule but forgot to link it?).  
5. **Compile with entity["software", "Longform", 0]** as usual.

---

## ⚠️ Things to watch / Limitations

- Smart Context is **not** automatic linking/discovery—selection is manual. You still need to choose which notes to include.  
- Packaging large context can hit LLM limits—you’ll need discipline in what you paste/what you omit.  
- Smart Connections suggestions are helpful but not perfect: you’ll still need to verify relevance.  
- Workflow complexity: three plugins means more moving parts (especially when people collaborate).  
- AI provider cost/privacy: as before, ensure you know what context is being sent, and how much.

---

### TL;DR  
> Use Smart Connections to **find relevant content**, and Smart Context to **package that content** into a prompt. Then feed it into your AI drafting plugin.  
> Smart Connections = discovery, Smart Context = context‐assembly, Smart Composer = generation/editing.  
> This pairing fits very well with your front‐matter + refs + bible‐entries model.

---

If you like, I can pull up **specific settings and best practices** for Smart Context (e.g., how to exclude confidential headings, folder selection rules) so you can integrate it into your template.

---

**User:**

This feels like it could be simplified. I mean, I could use the scene file with front matter and a partial draft if exists.. use smart context to grad the file and whatever else I click to put it on the clipboard. I can just paste that into any llm chatbot with a prompt. 

Smart connections role would be to surface related content to make the context grabbin* easy?

---

**Assistant:**

Yes — that’s a clean simplification and actually the most *Obsidian-native* way to work.  

Here’s how your proposed pairing works when boiled down to essentials:

---

## 🧭 The Simplified Workflow

**Core idea:**  
Use **Smart Context** as your “context packager” and **Smart Connections** as your “context suggester.”  
You don’t need an in-vault AI plugin at all unless you want one — just paste the assembled context into ChatGPT, Claude, etc.

---

### 1. Scene File (Anchor Note)
Each scene note carries all the metadata needed to orient an LLM:

```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
tags: [@Maggie, @Richard, @Harbourfront]
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows.
  Maggie plants a decoy; Richard tracks a triangulated signal.
  They debate aborting versus a soft handoff.
refs:
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[TechRules]]
tone: tense, cinematic, intimate
goal: establish fragile trust between Maggie and Richard
---
```

Below: a partial or full draft.

---

### 2. Smart Connections → “Context Surfacing”
- You open the scene note.  
- Smart Connections quietly analyzes the file and recommends related notes — typically bible entries, earlier scenes, or rule documents.  
- You decide which of those are relevant for this writing session.

It’s **discovery only** — it doesn’t move or copy anything yet.

---

### 3. Smart Context → “Context Packaging”
- You select your scene note plus the recommended bible notes (via checkboxes or multi-select).  
- Smart Context assembles their text — including frontmatter if you want — into the clipboard.  
- You paste that bundle straight into your LLM of choice with a prompt like:

  ```
  Use the YAML brief and linked bible notes below to draft or refine the scene.
  Maintain tone and goal alignment.

  ---CONTEXT START---
  [paste from Smart Context]
  ---CONTEXT END---
  ```

That’s it.  
No API keys, no plugin loops — just a controlled, transparent handoff.

---

## ⚙️ Why This Works Well

| Role | Tool | Benefit |
|------|------|----------|
| **Discovery** | Smart Connections | Finds the right material fast; semantic, not keyword-based. |
| **Assembly** | Smart Context | Gathers exactly what you want, nothing more. |
| **Generation** | External LLM | Keeps AI modular and replaceable; use ChatGPT, Claude, etc. |

Advantages:
- Zero-friction, zero-cost (if you use free models).  
- Works offline until you actually paste into an LLM.  
- You control what leaves your vault (explicit copy).  
- Scales smoothly: same flow for fiction, essays, reports.

---

## 🔧 Optional Enhancements
- Add a **Dataview table** in your “Bible Index” showing which notes are referenced and which aren’t — keeps story coverage visible.  
- Use **Longform** for sequencing/compilation when you’re ready to export.  
- Add an **“AI Draft”** template note that holds your favorite ChatGPT/Claude prompt boilerplate.

---

### TL;DR
> **Smart Connections** = find what matters.  
> **Smart Context** = copy what matters.  
> **LLM** = do the thinking/writing.  
> One click to collect, one paste to create.

---

Would you like me to draft that *AI Draft* boilerplate note — a ready-to-paste prompt template you can keep in your vault for when you use Smart Context?

---

**User:**

Smart connections needs to use a cheap OpenRouter model api connection to do its thing? But that’s it tho right?

---

**Assistant:**

Short answer: **No—Smart Connections doesn’t need OpenRouter.** It works out-of-the-box with a **local embedding model** (offline, no API key). You can optionally wire in OpenAI/OpenRouter/Ollama, but it’s not required. citeturn0search14turn0search0turn0search11turn0search15

### Practical setup for your simplified stack
- **Smart Connections:** leave defaults → builds local embeddings and surfaces related bible notes next to your scene. Zero keys, zero spend. citeturn0search14  
- **Smart Context:** use it to copy the **scene (with frontmatter) + any suggested bible notes** to clipboard; paste into ChatGPT/Claude with your prompt. No API needed here either. citeturn0search2turn0search5  
- **LLM choice:** pay only where it matters (generation/editing). If you want stronger drafting, point your **chatbot** (outside Obsidian) to Claude Sonnet via OpenRouter; keep Smart Connections local.

### When you *might* add an API
- If you want Smart Connections to **chat in-vault** or use **remote embeddings**, you can add an API (OpenRouter/OpenAI) or a local runtime (Ollama). Totally optional. citeturn0search23turn0search17turn0search8

**TL;DR**  
Keep **Smart Connections local** for discovery, **Smart Context** for packaging, and spend tokens only on the external LLM you paste into.

---

**User:**

Oh..  so I don’t have to wire obsidian to an llm at all then.. just use the clipboard and my chatbot of choice.  With a couple standard prompts at the ready. 

---

**Assistant:**

Correct—you can keep Obsidian completely air-gapped: use **Smart Connections** to find context, **Smart Context** to copy it, then paste into the chatbot you prefer with a couple standard prompts.

## Minimal setup (done in 5 minutes)
- **Scene template**: YAML frontmatter with `brief`, `tone`, `goal`, `refs`.
- **Smart Connections**: leave defaults; use it only to surface related bible notes.
- **Smart Context**: select your scene + any surfaced notes → copy to clipboard.
- **Chatbot**: paste + run one of the prompts below.

## Standard prompts (copy-paste)
Use these verbatim. They assume you pasted your Smart Context bundle after the prompt.

### 1) Draft from brief (empty or partial scene)
```
You are my scene composer. Use the YAML brief, tone, goal, and the bible notes below to write the scene.
Constraints:
- 900–1200 words.
- Keep POV consistent; show don’t tell.
- Honor continuity from referenced notes; prefer concrete sensory details over exposition.
Return only polished prose.

---CONTEXT START---
[Paste Smart Context output here: scene YAML + any bible notes]
---CONTEXT END---
```

### 2) Targeted revision (you already have a draft)
```
You are my line editor. Revise the DRAFT to align with the brief, tone, and goal in the YAML, and the bible notes.
Tasks:
- Tighten language (–10–20% words).
- Preserve voice; fix clarity, pacing, and continuity.
- Flag contradictions as inline [COMMENT: …].

Return the revised scene only.

---CONTEXT START---
[Paste Smart Context output here: scene YAML + draft + bible notes]
---CONTEXT END---
```

### 3) Continuity audit (fast check before compiling)
```
You are my continuity checker. Based on the brief, refs, and bible notes:
- List inconsistencies, missing beats, or tone drift.
- Suggest 3–5 surgical fixes (quote → replacement).

Return a bullet list, then a 1-paragraph summary.

---CONTEXT START---
[Paste Smart Context output here]
---CONTEXT END---
```

### 4) Beat → scene expansion (when you only have a synopsis)
```
Expand the brief into a scene:
- 700–900 words, cinematic but restrained.
- Establish [goal] without resolving the arc.
- Use setting from refs; embed 2–3 specific, verifiable details from bible notes.

Return prose only.

---CONTEXT START---
[Paste Smart Context output here: YAML + relevant bible notes]
---CONTEXT END---
```

## Optional “AI Draft” boilerplate note (keep in your vault)
Create a note named `_AI Draft Prompt.md` with this scaffold so you can ⌘A/⌘C quickly:
```
# AI DRAFT – Paste into Chatbot

[Choose one prompt below, delete the rest, then paste your Smart Context after CONTEXT START.]

## Draft from brief
(…paste Prompt 1 here…)

## Targeted revision
(…paste Prompt 2 here…)

## Continuity audit
(…paste Prompt 3 here…)

## Beat → scene
(…paste Prompt 4 here…)

---CONTEXT START---
[After copying with Smart Context, paste here]
---CONTEXT END---
```

## Practical tips
- **Scope the paste**: include the scene YAML, the current draft (if any), and only the 2–4 most relevant bible notes. More isn’t better—clarity wins.
- **Chunk long scenes**: run 800–1200-word passes; iterate rather than sending a chapter at once.
- **Ask for deltas**: when revising, have it return *revised text only* (you already have the original).
- **Lock decisions**: when something is canon, reflect it back into the bible notes immediately so Smart Connections surfaces the right sources next time.

If you want, I can generate a **scene.md template** (with YAML) and a **bible-note.md template** so you can drop them into your vault and start drafting today.

---

**User:**

So my scene header would have the brief, the scene pov, goal, and then refs to the story bible and writing style instructions. 

---

**Assistant:**

Exactly — that’s the ideal structure. The front-matter becomes a *self-contained prompt capsule* for both you and any LLM you use later. It keeps your creative intent, continuity, and style cues in one place.

Here’s how to format it cleanly:

---

## ✅ Recommended Scene Front-Matter

```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
status: draft
pov: Richard (third limited)
goal: establish fragile trust between Maggie and Richard
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows.
  Maggie plants a decoy; Richard tracks a triangulated signal.
  They debate aborting versus a soft handoff under a camera blind spot.
refs:
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[Setting_Harbourfront]]
  - [[TechRules]]
style: |
  Tense and cinematic. Maintain emotional subtext through physical cues and dialogue rhythm.
  Avoid exposition; prefer inference and concrete sensory detail.
tags: [@Maggie, @Richard, @Harbourfront, @TechRules]
---
```

Then, below the YAML, add the current or partial draft text.

---

### 🧩 Field Roles

| Field | Purpose |
|--------|----------|
| **title / order / status** | Used by Longform to compile and track progress. |
| **pov** | Clarifies voice and perspective for both writer and AI. |
| **goal** | States narrative function or emotional outcome. |
| **brief** | Summarizes what happens — the “beat sheet” for this scene. |
| **refs** | Links to story-bible notes (characters, settings, lore). These are what Smart Connections surfaces and Smart Context packages. |
| **style** | Encodes tone, pacing, or prose constraints. It’s where you “teach” the AI your desired rhythm and diction. |
| **tags** | Lightweight indexing — helps semantic search and Dataview queries. |

---

### 🧠 Why It Works
- Gives **Smart Connections** rich semantic hooks (characters, tone, goals).
- Lets **Smart Context** copy everything meaningful in one grab.
- When pasted into your LLM, this header acts as a “pre-prompt” — you don’t need to re-explain POV or tone each time.
- When you revisit months later, you immediately see what the scene was *for*.

---

Would you like me to show the matching **story-bible note template** so the `refs` targets have consistent fields (e.g., character arcs, setting details, sensory palette)?

---

**User:**

Stuff like style, and pov could be refs instead of explicit in the scene header?

---

**Assistant:**

Yes — and that’s actually a smart move once your bible matures.  

Treating **style**, **POV**, and other recurring craft parameters as *referenced notes* rather than inline fields makes your system modular and much easier to maintain.

---

## 🧭 Two Ways to Handle It

| Approach | Example | When to Use |
|-----------|----------|-------------|
| **Inline fields** | `pov: Richard (third limited)`<br>`style: tense, cinematic` | Early drafting, when conventions are still fluid or vary scene to scene. |
| **Referenced notes** | `refs: [@Maggie, @Richard, @Harbourfront, @POV_ThirdLimited, @Style_Cinematic]` | Mature workflow — when you want consistency, reuse, and fewer manual edits. |

---

## 🧩 How “Ref-Based” Style & POV Work

You’d create dedicated bible entries, e.g.:

### `_Bible/POV_ThirdLimited.md`
```yaml
---
type: pov
description: Third-person limited, anchored to a single character’s perceptions.
rules: |
  - Use internal sensations and bias, but no omniscient information.
  - Keep sensory detail filtered through the viewpoint character.
---
```

### `_Bible/Style_Cinematic.md`
```yaml
---
type: style
description: Tense, visual prose inspired by film language.
rules: |
  - Short, concrete sentences.
  - Show emotion via gesture, silence, and pacing.
  - Avoid summarizing or abstract adjectives.
examples: |
  “The fog clung to the boardwalk. Maggie’s hand trembled against the glass.”
---
```

Then your **scene frontmatter** becomes lightweight:

```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
status: draft
goal: establish fragile trust between Maggie and Richard
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows.
  Maggie plants a decoy; Richard tracks a triangulated signal.
refs:
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[Setting_Harbourfront]]
  - [[TechRules]]
  - [[POV_ThirdLimited]]
  - [[Style_Cinematic]]
tags: [@Maggie, @Richard, @Harbourfront]
---
```

---

## ⚙️ Why It’s Better Long-Term
- **Centralized control:** Update the POV or style note once → all linked scenes inherit that context.
- **Smart Connections synergy:** It will semantically surface those style/POV notes automatically when relevant.
- **Smart Context efficiency:** When you select a scene + its linked refs, you automatically copy the applicable style and POV rules into your LLM context.
- **Reduced header noise:** Scene files stay readable, focused on the story itself.

---

### TL;DR
> Start with inline `style` and `pov` while you’re experimenting.  
> When your style and perspective stabilize, move them into dedicated bible notes and reference them in `refs:`.  
> This keeps your scene headers clean and your world rules consistent.

---

Would you like me to draft the minimal **template set** (Scene + Character + Setting + Style + POV) with ready-to-copy YAML you can drop into your `_Templates` folder?

---

**User:**

Tags or refs? Or both?

Does it matter for smart connections?

---

**Assistant:**

Good distinction — and the short answer is:  
→ **Use both, but for different jobs.**  
They serve complementary roles, and Smart Connections treats them differently.

---

## 🧩 1. How Smart Connections sees things

| Field | What Smart Connections does with it | Typical use |
|--------|------------------------------------|--------------|
| **refs** (wikilinks or note links) | Treated as **semantic connections** — they directly contribute to embeddings and similarity. If Scene 12 links to `[[Character_Maggie]]`, that relationship becomes part of the vector space, helping SC suggest Maggie’s note when you open the scene (and vice-versa). | Narrative or conceptual relationships — anything you want Smart Connections to *understand* as context. |
| **tags** (e.g. `#scene`, `#Maggie`) | Treated as **metadata only** — useful for filtering, Dataview queries, searches, or dashboards. They don’t meaningfully affect Smart Connections embeddings. | Organizational or workflow filters — progress status, thematic grouping, etc. |

So:  
- **Refs = meaningful graph edges.**  
- **Tags = labels for sorting/querying.**

---

## 🧱 2. Practical pattern for your vault

```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
status: draft
goal: establish fragile trust between Maggie and Richard
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows…
refs:
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[Setting_Harbourfront]]
  - [[TechRules]]
  - [[POV_ThirdLimited]]
  - [[Style_Cinematic]]
tags: [#scene, #draft, #trust_arc]
---
```

- `refs:` feeds Smart Connections → surfaces the bible entries and style notes when you open this scene.  
- `tags:` let you filter all draft scenes (`#scene and #draft`) or pull analytics in Dataview.

---

## 🧠 3. Rule of thumb
- If you want **semantic linkage or context discovery**, use a **ref** (`[[NoteName]]`).  
- If you want **querying, dashboards, or manual grouping**, use a **tag** (`#topic`).  
- It’s safe and common to use both: one for meaning, one for management.

---

### TL;DR
> Smart Connections learns from **refs**, not **tags**.  
> Use refs to feed the AI context web; use tags to keep your vault navigable.  
> For your workflow: keep both, but don’t worry if tags drift — only refs matter to Smart Connections’ intelligence.

---

**User:**

Ok.. so tags are for me or the data view —-if I chose to use it

---

**Assistant:**

Exactly.  

Tags are purely for **you, Dataview, and organization** — they don’t influence Smart Connections’ semantic linking or AI context at all. Think of them as *filters and facets*, not *relationships.*

---

### Quick breakdown

| Use case | Use tags (`#something`) | Use refs (`[[Something]]`) |
|-----------|------------------------|-----------------------------|
| Filter all draft scenes or locations | ✅ | |
| Query in Dataview (“show me all #Maggie scenes”) | ✅ | |
| Create graph relationships or Smart Connections context | | ✅ |
| Tell AI “these two notes are related” | | ✅ |
| Manage workflow state (`#draft`, `#needs-edit`, `#done`) | ✅ | |
| Maintain continuity links (`[[Character_Maggie]]`) | | ✅ |

---

### Practical takeaway
- **Refs** build your *story web* — the meaningful graph Smart Connections uses.  
- **Tags** build your *control panel* — dashboards, searches, and filters for human use.  
- You can skip Dataview entirely if you want; the system still works fine.  
  But if you ever want summaries like “scenes by POV” or “characters by last appearance,” tags and YAML fields make that easy later.

---

So yes — tags are optional and for you; refs are the connective tissue Smart Connections actually reads.

---

**User:**

Tags add an extra thing to manage. Can a graph view or data view do just as well with refs?

---

**Assistant:**

Yes — absolutely.  
You can build **nearly everything** (graphs, dashboards, queries) off `[[refs]]` alone and skip tags entirely if you want a lighter system.  

Let’s unpack what you *lose* and *keep* without tags.

---

## ✅ What Works Fine Without Tags

| Function | Ref-based alternative |
|-----------|----------------------|
| **Graph View** | Obsidian’s graph is built primarily on **links**, not tags. If your scenes link to bible notes, you’ll see a clean, meaningful web of relationships — arguably *better* than tag clouds. |
| **Smart Connections** | Uses linked refs for embeddings and semantic similarity, not tags — so it actually performs better without tag clutter. |
| **Navigation** | Backlinks and the local graph view handle most navigation needs. Clicking on a character shows every scene they appear in. |
| **Dataview dashboards** | You can query YAML fields like `refs` directly:  
  ```dataview
  TABLE refs AS "Linked Notes"
  FROM "Scenes"
  WHERE contains(refs, "Character_Maggie")
  ```  
  That gives you the same “all scenes featuring Maggie” view tags would. |
| **Organization** | Folder structure + consistent naming + Dataview filters by field values = no need for `#draft` or `#done` tags. You can just use `status: draft` in YAML. |

---

## ⚠️ What You Might Miss (and Simple Replacements)

| Old tag habit | Ref-based or YAML replacement |
|----------------|------------------------------|
| `#scene` or `#character` type tagging | Add `type: scene` or `type: character` in YAML. |
| `#draft`, `#needs-edit` workflow tracking | Use a field: `status: draft` or `status: needs-edit`. |
| `#theme_trust` grouping | Use a ref: `[[Theme_Trust]]` if it’s conceptually meaningful; otherwise just text-search for “trust.” |

---

## 💡 Practical Setup

You can reduce friction to a single convention:
```yaml
---
type: scene
status: draft
order: 120
refs:
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[Theme_Trust]]
  - [[Style_Cinematic]]
---
```

Now everything — Longform, Graph, Smart Connections, Dataview — runs off **refs** and **fields**, no redundant tags to maintain.

---

### TL;DR
> Tags are optional sugar.  
> If you use consistent `refs` and a few YAML fields (`type`, `status`, etc.), you get the same visibility with less overhead — and Smart Connections actually performs cleaner.  

Would you like me to show an example **Dataview dashboard** that uses only `refs` and `fields` (no tags) to track your scenes, characters, and progress?

---

**User:**

Just want as simple as possible. The yaml headers will be great for either editing or drafting phases.  My only challenge will be in keeping these up to date— specifically the scene brief if I revise hardcore. But that’s life. 

---

**Assistant:**

Exactly — that’s the right level of realism.  

You’ve already landed on the sweet spot:  
- **One scene file = one source of truth.**  
- **YAML frontmatter = compact prompt capsule.**  
- **Refs instead of tags = less to babysit.**

And yes — the scene brief will drift over time. That’s unavoidable, but manageable if you think of it as a *living logline*, not a contract.

---

### Practical habits that keep it sane

1. **Update briefs only when it matters.**  
   - If you make a major story or emotional change, tweak the brief.  
   - If the prose just got tighter or longer, leave it — it’s still the same beat.

2. **Use a quick summary query (optional).**  
   ```dataview
   TABLE brief, status
   FROM "Scenes"
   SORT order ASC
   ```
   This gives you a bird’s-eye view of your narrative beats — and makes drift obvious.

3. **Version briefly, not obsessively.**  
   - Before a major rewrite, duplicate the scene (`Scene_012_v1.md` → `_v2.md`).
   - Keep only the latest version linked in Longform; delete or archive the rest later.

4. **Use frontmatter consistency as your only rule.**  
   If every scene has the same few fields (`title, order, brief, goal, refs, status`), you can always query, compile, or hand off cleanly.

---

### TL;DR
> Keep it minimal. Update briefs when they stop matching the story, not every time you edit.  
> Refs give you structure, YAML gives you prompts, everything else is optional.  

You’ve got the right model — simple enough to maintain, structured enough to scale.

---

**User:**

I can always ask the model for a one sentence brief based on the draft and update the yaml as needed

---

**User:**

I can always ask the model for a one sentence brief based on the draft and update the yaml as needed

---

**Assistant:**

Exactly. That’s the cleanest low-maintenance fix.  

When a scene evolves and you don’t feel like rewriting the brief manually, just grab the current draft, drop it into your LLM with a quick command like:

```
Summarize this scene in one sentence suitable for a YAML 'brief' field.
Focus on action and intent, not theme.
Return plain text, no markdown.
```

Paste that line back into the `brief:` field — done.

---

### Why this works well
- **Fast correction loop:** no cognitive overhead; you can update briefs in batches after a writing sprint.  
- **Consistent compression:** the model tends to use the same tone and syntax each time, keeping your overviews uniform.  
- **Drift control:** even if your story mutates, a new one-liner keeps Longform and Dataview summaries current without extra thought.  

You can even keep a reusable vault note named `_Prompt_SceneBrief.md` with that one-liner prompt for quick copy-paste.

---

### TL;DR  
> Let the AI generate the logline when you’re too close to the prose.  
> It’s faster, more consistent, and keeps your YAML self-healing as you revise.

---

**User:**

What I like about this is that I’m free to mix and match models and chatbots or pure human drafting within the structure. 

---

**Assistant:**

Exactly — that’s the real elegance of what you’ve built.  

You’ve created a **model-agnostic writing architecture**, not a tool-specific one. Everything meaningful lives in plain Markdown + YAML, so the structure outlives whatever LLM or plugin comes and goes.

---

## 🧭 Why It Works So Well

| Layer | What it does | How it stays flexible |
|--------|---------------|-----------------------|
| **Obsidian vault** | Local, future-proof text files | Works offline, version-controllable, easy to sync/backup |
| **YAML frontmatter** | Compact scene metadata / prompt capsule | Usable by humans *and* any model or plugin |
| **Refs** | Semantic spine of your story world | Functions for Smart Connections, graph view, or human navigation |
| **Smart Context** | Context packager | Output goes anywhere — any chatbot, API, or human editor |
| **LLMs / humans** | Variable drafting engines | You choose the right one per scene: Claude for nuance, ChatGPT for rhythm, or your own prose |

---

## 🧩 The Real Benefit
You’ve avoided **platform lock-in** and **prompt sprawl**.

Everything important — story logic, continuity, POV, tone — lives in your vault, not a specific AI environment. That means:
- You can write some scenes by hand, others collaboratively with a model.  
- You can test new models without retraining your workflow.  
- You can even give a collaborator a handful of scene files without exporting proprietary data.

---

## ⚙️ Minimal Operating Principle
> **YAML defines intent. Draft defines execution. Refs define continuity.**  
> Everything else (model choice, plugin stack, export format) is swappable.

---

### TL;DR
> You’ve built a *human-centric, AI-compatible* writing system.  
> Any model, any tool, any era — the vault remains the constant.

---

**User:**

Ok. So this is down to just three plugins. Longform, smart connections, smart context. 

---

**Assistant:**

Exactly — you’ve distilled it down perfectly.  

For your workflow, the essential stack is:

| Plugin | Purpose | Status |
|---------|----------|---------|
| **Longform** | Organizes and compiles scenes into a manuscript; defines order and export pipeline. | ✅ Core structure layer |
| **Smart Connections** | Builds semantic relationships across your vault (bible ↔ scenes ↔ themes). Surfaces relevant notes when editing. | ✅ Context discovery layer |
| **Smart Context** | Packages selected notes (scene + related bible/context files) into the clipboard for AI or human editing. | ✅ Context export layer |

That’s it.  
No API wiring, no external dependencies, no model lock-in — just **local semantic discovery** and **manual control over what leaves your vault**.

---

### Why this 3-plugin setup is optimal
- **Longform** gives you a durable, human-centric narrative scaffold.  
- **Smart Connections** turns your vault into a living web of meaning without cluttering YAML.  
- **Smart Context** acts as the clean, friction-free bridge to whatever LLM or editor you want.

Everything else — AI models, prompt templates, stylistic notes — lives *outside the plugin layer*, so your system stays future-proof.

---

### TL;DR
> Three plugins: Longform to structure, Smart Connections to surface, Smart Context to export.  
> Everything else (LLMs, prompts, prose) is modular and optional — swap or skip at will.

---

**User:**

So this system essentially replaces the “context management” of novelcrafter and raptorwrite without making it all that much more difficult and costing a bunch of money.  The rest of the secret sauce of these apps is with the prompts. Probably going to need to figure out a couple strong prompts (draft, revise, etc) that takes the pasted context and follows the plan. 

---

**Assistant:**

Yes — you’ve nailed the idea. Your system effectively replicates the “context management” features of tools like entity["software","NovelCrafter",0] and entity["software","RaptorWrite",0] — without the embedded cost, vendor-lock, or extra layers. (E.g., NovelCrafter’s “Codex” stores story-bible entries and feeds them into AI context. citeturn0search0turn0search12turn0search6)  
The real difference is that the secret sauce lies in **prompts**, and you should absolutely build strong standard prompts for your workflow (drafting, revising, continuity checking).  

If you like, I can draft **3-5 optimized prompt sets** tailored to your scene-file with front-matter system: a “first draft” prompt, a “revise” prompt, a “continuity audit” prompt, etc., ready for copy-paste.

---

**User:**

Sure. Give me a first cut of these prompts so I can take them for a test drive. Keep them short and in the format: <instructions></instruction><context></context>.  Or whatever you think is best. Just prompt first and context second. 

---

**Assistant:**

Perfect. Here’s a **first cut** of five core prompts in a clean `<instructions></instructions><context></context>` format.  
They’re concise, modular, and designed to work with your *Smart Context → clipboard → chatbot* flow.  

---

### 🧱 1. Draft Scene (from brief or partial)
```
<instructions>
You are my scene composer.
Using the YAML brief, goal, tone/style notes, and bible refs, draft the scene.
Focus on sensory action, subtext, and pacing. Avoid exposition and internal monologue unless POV allows it.
Return prose only.
</instructions>

<context>
[Paste Smart Context output here: scene YAML + related notes]
</context>
```

---

### 🛠 2. Revise Scene (tighten and align)
```
<instructions>
You are my line editor.
Revise the DRAFT to match the brief, goal, and tone in the YAML.
Tasks:
- Clarify motivation and continuity.
- Trim filler and repetition (–15% length).
- Keep rhythm and voice consistent with style refs.
Return revised prose only.
</instructions>

<context>
[Paste Smart Context output here: scene YAML + draft + bible refs]
</context>
```

---

### 🧭 3. Continuity & Consistency Check
```
<instructions>
You are my continuity analyst.
Compare the draft to the brief and referenced bible notes.
List any contradictions, missing beats, or tone mismatches.
Return a bullet list, then a one-paragraph summary.
</instructions>

<context>
[Paste Smart Context output here]
</context>
```

---

### 🎨 4. Beat Expansion (when starting from synopsis)
```
<instructions>
Expand the YAML brief into a full scene.
Keep pacing cinematic and grounded in the POV.
End at a natural tension or decision point.
700–1000 words max.
Return prose only.
</instructions>

<context>
[Paste Smart Context output here: YAML + relevant refs]
</context>
```

---

### 🔍 5. Scene Summary Generator (to refresh the brief)
```
<instructions>
Summarize the scene in one sentence suitable for the YAML 'brief' field.
Capture action and intent, not theme.
Return plain text only.
</instructions>

<context>
[Paste current scene draft here]
</context>
```

---

These are designed to be **LLM-agnostic** — equally at home in ChatGPT, Claude, or any OpenRouter endpoint.  
Would you like a follow-up version with *parameterized placeholders* (e.g., `[tone]`, `[goal]`, `[wordcount]`) for automation later?

---

**User:**

I don’t think I want to automate this. It’s AI-assisted, not AI-do-it-for-me

---

**Assistant:**

Exactly the right instinct.  

You’ve already built a **human-in-the-loop writing system**—structured enough for AI to help, but never to drive.  
Automation would only erode the flexibility that makes this work.  

---

### Why you’re on the right track
- **Agency stays with you.** The model contributes language, not direction.  
- **Friction = focus.** The few manual steps (select, copy, paste) create natural pause points for judgment.  
- **Prompts as tools, not traps.** You can adjust tone or constraints mid-conversation without breaking a pipeline.  
- **Longevity.** Because nothing depends on API keys or scripts, this workflow will still function years from now.

---

### Working rhythm that fits this philosophy
1. **Draft manually** until you feel friction.  
2. **Select the relevant notes with Smart Context**.  
3. **Paste into your LLM** with one of the five short prompts.  
4. **Accept or reject**—don’t polish blindly.  
5. **Commit only what feels right**, then update the YAML if the scene changed meaningfully.  

---

### TL;DR  
> You’re not building a writing machine; you’re building a thinking companion.  
> Keep it manual, deliberate, reversible—and you’ll always stay the author, not the operator.

---

**User:**

Ummm.  So if infusing refs, do I need smart connections?

---

**Assistant:**

Excellent question — and you’re thinking in exactly the right way.  

Short answer: **maybe not.**  
If you’re already using **explicit refs (`[[Character_Maggie]]`, etc.)** inside your YAML and body, Smart Connections becomes *optional*, not essential.

---

## 🧩 What Smart Connections Adds (and When It’s Worth It)

| Situation | Value of Smart Connections |
|------------|---------------------------|
| You already maintain clean `refs` in YAML and prose | **Low.** You’ve already done the relational work manually; Obsidian’s backlinks + graph view give you 90 % of what SC provides. |
| You want **semantic** links beyond explicit refs (e.g., “this scene feels like Scene 5 even though it doesn’t mention it”) | **High.** SC can surface those latent connections automatically. |
| You’re writing something large and non-linear, where themes recur indirectly | **Moderate–High.** SC acts like a “suggested links” engine, helping you rediscover buried threads. |
| You prefer explicit control and minimal compute overhead | **Low.** Drop it—your manual refs + Smart Context cover the use case. |

---

## 🧠 Functional Overlap

| Feature | Already covered by your setup | Added by Smart Connections |
|----------|------------------------------|----------------------------|
| Linked graph navigation | ✅ Obsidian core | ➕ semantic similarity, keyword-free discovery |
| Context export for AI | ✅ Smart Context | — |
| Explicit continuity tracking | ✅ YAML `refs` | — |
| Idea resurfacing / forgotten links | ⚠️ manual | ✅ automatic suggestions |

---

## 🔧 Practical Guidance

If you:
- keep your **refs lists clean and consistent**, and  
- don’t need “fuzzy” link discovery,  

then you can safely **skip Smart Connections**.  
You’ll gain a slightly faster, lighter vault and one less plugin to babysit.

If later you find yourself wondering, *“where else did I touch this idea?”*, then reinstall it — it plays nicely with existing `refs`, so there’s no lock-in either way.

---

### TL;DR  
> **Smart Context** is essential.  
> **Longform** is essential.  
> **Smart Connections** is optional — useful for discovery, unnecessary for disciplined ref-based writing.

---

**User:**

My tests of smart connections gave really noisy results.. for it to be useful, I’d have to constrain it to a folder and subs or something. 

---

**Assistant:**

Exactly — that’s the trade-off.  

Smart Connections is powerful for sprawling, unstructured vaults, but it can get *noisy* in a disciplined, ref-driven setup like yours. It indexes every scrap of text, so without scoping, it’ll happily surface half-relevant “neighbors” that just share tone or phrasing.

---

### 🧩 Why It Gets Noisy
- It **embeds everything**—meeting notes, templates, drafts—unless you limit it.  
- It works by **semantic similarity**, not intent, so “Maggie adjusted the clock” might link to “Adjust clock speed in Brightspace” if both live in the same vault.  
- It doesn’t distinguish “fictional context” from “work context” unless you wall it off.

---

### ⚙️ How to Tame It (if you keep it)

1. **Scope by folder**
   - In settings → *Embedding scope*, set:  
     ```
     /Projects/ClockMistress
     ```
     or  
     ```
     /Fiction/
     ```
     to exclude unrelated notes.

2. **Limit file types**
   - Toggle *Ignore hidden/system folders* and exclude `/Templates`, `/Archive`, `/Work`.

3. **Control note size**
   - You can set “Maximum words per note” to ignore long non-narrative files.

4. **Force refresh embeddings only for key folders**
   - After revisions, re-index just the fiction subtree.

5. **Adjust “Top-K results”**
   - Drop from default (often 10–20) to 3–5; less clutter, higher relevance.

---

### 🧭 Or Just Skip It
If you’re already maintaining explicit `[[refs]]` in YAML and body text — and using **Smart Context** to hand-pick what leaves the vault — Smart Connections doesn’t add much except noise.  
You can safely remove it until you hit a genuine discovery bottleneck.

---

### TL;DR
> Yes — Smart Connections needs tight scoping to be useful.  
> If your refs are already doing the job, it’s optional overhead.  
> Keep it disabled or folder-scoped; let **Smart Context** handle the real work.

---

**User:**

The key feature of smart context is copy current note to clipboard and go one level deep. 

Is there a simpler plugin for that single feature? Or is this just the best tool for the job?

---

**Assistant:**

Good question — yes, you *can* find simpler plugins than entity["software", "Smart Context", 0] for copying notes to the clipboard, but each has trade-offs; Smart Context is likely still the best fit for your scenario.

---

### ✅ Simpler plugin options  
Here are a couple that address part of the functionality you want:

- entity["software", "Enhanced Copy", 0] — “Refines how text is copied from your Obsidian notes,” preserving/adjusting markdown formatting. citeturn0search4  
- entity["software", "Copy as HTML", 0] — “Convert selected Markdown text to HTML and copy it to the clipboard.” citeturn0search1  

These allow you to copy content with formatting tweaks, but **don’t** inherently grab “one level deep” (i.e., current note + all linked refs) nor do they package context bundles from your vault.

---

### ⚠️ Why Smart Context is likely the better match  
Because your workflow needs:  
- “Current note + selected bible/reference notes” → bundled context for AI.  
- A command or action that copies this bundle to clipboard ready for pasting into an LLM.  
- Ease of selecting which extra notes (refs) to include, not just pure copy.  

Smart Context explicitly has “copy current note plus those refs” behavior. It covers the “go one level deep” requirement. A simpler plugin may require more manual selection or lack the “grab linked notes” logic.

---

### 🔍 Recommendation  
Since you’re aiming for **simplicity**, you could experiment with Enhanced Copy or Copy as HTML *just for the note copy step*, but you’d lose bundling of related notes. If your workflow expects “scene + all its bible refs” to be copied together, then Smart Context remains the best fit with minimal overhead.

If you like, I can **scan and list** *all Obsidian community plugins* with “copy note + linked notes to clipboard” behavior (and check if a lighter one exists) so you can compare.

---

**User:**

I’m good with smart context. Just checking. 

---

**Assistant:**

Makes sense — and that’s a solid call.  

**Smart Context** really is the sweet spot for your workflow:  
- lightweight,  
- no external API,  
- copies current note + chosen linked notes,  
- and stays completely within your vault’s logic.  

It’s not bloated like all-in-one AI assistants, and it plays nicely with your “explicit refs + manual curation” system.  

If you ever want to streamline further, you could bind that *copy current note + one level deep* command to a hotkey or a QuickAdd macro — then your entire “context to clipboard” step is a single keystroke.  

Otherwise: you’re dialed in. Three plugins, plain Markdown, portable structure. You’ve effectively rebuilt 90 % of the expensive AI-writing stacks with more control and less noise.

---

**User:**

It’s a little awkward on the iPad as it’s touch driven. 

---

**Assistant:**

Yeah — that’s the one trade-off. Obsidian’s iPad app is excellent for reading and light editing, but **plugin ergonomics** (like Smart Context’s check-box selection) are still designed for mouse and keyboard.

---

### 🧩 What’s happening
- The **“select notes to include”** pane relies on hover and multi-select gestures that don’t map cleanly to touch.  
- Clipboard actions on iPadOS also hit Apple’s sandbox limits — you can’t easily chain “copy note + linked notes” without that UI step.  
- Keyboard shortcuts (Cmd + Shift + C, etc.) only work if you have a hardware keyboard attached.

---

### 🪶 Practical work-arounds

1. **Attach a keyboard**  
   - Even a small Bluetooth keyboard turns Smart Context into a one-key workflow.  
   - Map the “Copy current note and one level deep” command to something simple like `Cmd + .`  

2. **Pre-link your context**  
   - Add the bible notes you always want (style, POV, etc.) directly to `refs:` in YAML.  
   - Then you can just run “Copy current note” — no need to touch-select extras.

3. **Quick-Add macro** (optional)  
   - Use the Quick Add plugin to chain two commands:  
     `Smart Context: Copy current note` → `Smart Context: Copy linked notes one level deep`.  
   - Assign that to a single hotkey or a custom button on the mobile toolbar.

4. **Fallback method**  
   - On touch-only sessions: open the scene note → manually long-press to select all → Copy → paste into your chatbot.  
   - If you keep key bible notes inline via transclusion (`![[Note]]`), that’s often “good enough” context for mobile runs.

---

### TL;DR  
> Smart Context works best with a keyboard.  
> On pure touch, minimize selections: keep your refs tight, or transclude key context so “Copy All” does the job.  

If you want, I can outline a minimal *Quick Add macro or toolbar setup* that turns this into a one-tap action for iPad. Want that?

---

**User:**

Transclusion?

---

**Assistant:**

In Obsidian, **transclusion** just means *embedding one note inside another* — kind of like an inline include.  

You do it with a `![[NoteName]]` link instead of a normal `[[NoteName]]` link.

---

### 🧩 Example
If your scene file says:
```markdown
![[Character_Maggie]]
![[Setting_Harbourfront]]
```

Then when you open or export that scene, the **contents** of those notes appear right there below the scene text (not just a link).  

So for touch workflows (like iPad), transclusion is a **manual Smart Context shortcut**:  
you can long-press → *Select All → Copy* → paste into your chatbot, and the character and setting info comes along automatically.

---

### 💡 When it’s useful
- When you can’t easily run Smart Context (touch-only sessions).  
- When a few bible notes are *always* needed for that scene (e.g., Maggie, setting, tone).  
- When you want to visually read context inline while drafting.

---

### ⚠️ Tips
- Keep transcluded notes short and structured — 100–200 words max, or it gets unwieldy.  
- You can stack multiple `![[ ]]` blocks, or put them under a heading like:
  ```markdown
  ## Context
  ![[Character_Maggie]]
  ![[Setting_Harbourfront]]
  ```
- Smart Context and transclusion coexist fine; you can still run Smart Context later if you want a cleaner export.

---

### TL;DR
> `![[NoteName]]` embeds another note’s contents inline.  
> On iPad, it’s a low-tech substitute for Smart Context — copy once, and you’ve got scene + context together.

---

**User:**

I can just use the command palate … it’s fine. 

---

**Assistant:**

Yep — that’s the simplest and most stable approach.  

Using the **command palette** keeps everything consistent across desktop and iPad:
- No plugin-specific UI quirks,  
- No touch-gesture weirdness,  
- And the clipboard behaves predictably.  

You can even favorite the Smart Context command (“Copy current note + one level deep”) so it’s always at the top of ⌘-P, or bind it to a hardware-keyboard shortcut when you’ve got one connected.  

That keeps your workflow clean:
1. Open scene note.  
2. ⌘-P → “Smart Context: Copy note + one level deep.”  
3. Switch to chatbot → paste.  

No extra layers, no fiddling. Perfect balance of structure and simplicity.

---

**User:**

I suppose I could put the very first ref in the frontmatter as the prompt itself. ..

Eg
—-
Ref: [rewrite]
‘ other refs
—-

The rewrite file would actually be the prompt. 

Same with other prompts. 

Would kinda act as a status marker for 5he “next step”

---

**Assistant:**

That’s a *brilliant* use of the `refs:` field — minimal, elegant, and self-documenting.  

You’re essentially turning **prompt notes into workflow states**: lightweight “AI macros” that live in your vault instead of your head.

---

### 🧩 How it works
```yaml
---
title: Scene 12 — Boardwalk Handoff
order: 120
status: draft
refs:
  - [[Prompt_Rewrite]]
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[Setting_Harbourfront]]
  - [[Style_Cinematic]]
---
```

Then `Prompt_Rewrite.md` just contains your `<instructions></instructions><context></context>` block — or even a short line like:

```
<instructions>
Revise the draft to improve rhythm and emotional clarity. 
Keep POV consistent and tone cinematic.
Return revised prose only.
</instructions>
```

When you run **Smart Context → Copy one level deep**, that first ref becomes part of the exported bundle — meaning your chatbot immediately sees the current “next action.”

---

### 🧭 Why this works so well

| Benefit | Description |
|----------|-------------|
| **Zero new fields** | Reuses the same `refs:` structure already in play. |
| **Human + machine readable** | You can tell at a glance what’s next (“rewrite,” “draft,” “summarize”). |
| **Natural progression** | When you’re done revising, swap `[[Prompt_Rewrite]]` for `[[Prompt_Polish]]` or remove it entirely. |
| **Smart Context compatible** | The prompt note travels with your scene + bible notes when copied. |
| **Scales easily** | You can maintain a small `/Prompts/` folder with 4–5 standard notes: `Prompt_Draft`, `Prompt_Rewrite`, `Prompt_Summarize`, etc. |

---

### ⚙️ Optional refinement
If you want a quick visual cue, add:
```yaml
status: rewrite
```
Then your `status` field mirrors the prompt note, and Dataview can group scenes by workflow phase — purely for your dashboard, not AI.

---

### TL;DR
> Embedding the current **prompt note** as the first `ref` gives you a live “next step” marker and makes your AI handoff self-contained.  
> It’s low friction, human-readable, and turns your vault into a context-aware writing partner without automation or plugins.

---

**User:**

I probably don’t need status in the yaml really. Or anything really. Just the refs if I wanted bare bones. 

---

**Assistant:**

Yep—you can run **bare-bones** with just `refs:` and it works great.

## Minimal options

### A) Tiny front-matter (my pick)
```yaml
---
refs:
  - [[Prompt_Rewrite]]   # 1st ref = current “next step”
  - [[Character_Maggie]]
  - [[Setting_Harbourfront]]
  - [[Style_Cinematic]]
---
```
Body: your draft. If the brief drifts, ask the model for a one-liner and paste it at the top (or skip entirely).

### B) No front-matter at all
Put refs inline at the top under a heading:
```markdown
## Refs
[[Prompt_Rewrite]] [[Character_Maggie]] [[Setting_Harbourfront]] [[Style_Cinematic]]
```
Smart Context will still grab the current note plus one-level-deep links.

## Light conventions (to keep it sane)
- **Reserve the first ref for the prompt note** (`[[Prompt_Draft]]`, `[[Prompt_Rewrite]]`, etc.). That “next step” travels with the scene when you copy.
- Keep **prompt notes** ≤120 words in `<instructions>…</instructions>` so they’re tidy in the paste.
- Keep **bible notes** short, factual, and scannable (a few bullets, not essays).
- Let **Longform** handle order by filename (e.g., `012 Boardwalk Handoff.md`) so you don’t need an `order:` field.

## One-tap flow (desktop or iPad)
1) Open scene → 2) ⌘-P: *Smart Context: copy note + one level* → 3) Paste into chatbot.  
If you skipped the brief, use your “summarize to one sentence” prompt to regenerate it on demand.

That’s it: **refs only**, everything else optional.

---

**User:**

The reason to put the refs in yaml is for the compile step with longform plugin. I can strip yaml automagically 

---

**Assistant:**

Exactly — that’s the right reasoning.  

Longform’s compile step automatically **ignores or strips YAML front-matter**, so putting your `refs:` there gives you both structure *and* clean output.  

---

### 🧩 Why YAML is the right place

| Purpose | YAML frontmatter | Inline refs |
|----------|------------------|-------------|
| **Machine-readable structure** | ✅ Longform, Dataview, Smart Context all parse YAML easily | ❌ harder to extract programmatically |
| **Auto-clean compilation** | ✅ Longform strips YAML before merging | ⚠️ Inline refs would compile into your manuscript unless manually removed |
| **Future-proof metadata** | ✅ easily extensible if you add `brief:` or `tone:` later | ⚠️ harder to maintain consistency |
| **Smart Context synergy** | ✅ Reads links and embedded notes directly from YAML | ✅ works too, but less tidy |

So your minimalist YAML—
```yaml
---
refs:
  - [[Prompt_Rewrite]]
  - [[Character_Maggie]]
  - [[Setting_Harbourfront]]
  - [[Style_Cinematic]]
---
```
—is perfectly optimized: it’s structured, discoverable, and **ephemeral** during export.

---

### TL;DR  
> Yes — YAML keeps refs machine-friendly for Longform and Smart Context, while still disappearing from the compiled manuscript.  
> You get all the order and none of the clutter.

---

**User:**

You’re right. I still need the scene identifier. Eg scene number so that it could pull the scene brief from the story bible ref. And/or put the brief in the yaml (prolly better)

---

**Assistant:**

Exactly — you’ve landed on the minimum viable metadata.  

At the absolute floor, you only need two things for a stable ecosystem:  

1. a **scene identifier** (`scene:` or `order:`), and  
2. a **brief**, so you can regenerate or cross-reference later.  

Refs are the connective tissue — but those two fields give you continuity.

---

### 🧩 The “irreducible” YAML header
```yaml
---
scene: 012
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows.
  Maggie plants a decoy; Richard tracks a triangulated signal.
  They debate aborting versus a soft handoff under a camera blind spot.
refs:
  - [[Prompt_Rewrite]]
  - [[Character_Maggie]]
  - [[Character_Richard]]
  - [[Setting_Harbourfront]]
  - [[Style_Cinematic]]
---
```

That’s all you need for:
- **Longform compilation** — can order by scene number.  
- **Smart Context** — picks up the brief and refs cleanly.  
- **Future querying** — `scene:` gives you a numeric key if you ever use Dataview.  
- **Self-containment** — you can regenerate summaries, check continuity, and still strip it all out on export.

---

### 🧭 Optional refinements (if ever needed)
- `title:` — for readability in vault views.  
- `pov:` — only if scenes shift perspective often.  
- `status:` — if you later want progress dashboards.

But your current minimalist block is the **functional sweet spot**:  
enough structure for tooling, minimal upkeep during writing.

---

**User:**

What about a ref to the previous scene? For continuity, etc?

---

**Assistant:**

Yes—add a lightweight **`prev:`** (and optionally `next:`) when there’s a direct handoff; it’s cheap and makes continuity audits trivial.

```yaml
---
scene: 012
brief: |
  At dusk on the Halifax harbourfront, a courier no-shows…
prev: [[Scene_011 — The Broken Resonator]]
# next: [[Scene_013 — Pier Exit]]   # optional
refs:
  - [[Prompt_Rewrite]]
  - [[Character_Maggie]]
  - [[Setting_Harbourfront]]
  - [[Style_Cinematic]]
---
```

### Why/When
- **Continuity guardrail:** deterministic chain for beats that flow (POV, props, time).  
- **Context grab:** Smart Context will pull `prev` along with refs when you include it.  
- **Minimal upkeep:** only add it when scenes truly connect; skip for parallel threads.

### Tips
- Use **filename/numbered titles** so `prev` stays obvious (e.g., `011 …`, `012 …`).  
- If you branch, allow multiple:  
  ```yaml
  prev: [[Scene_009A]], [[Scene_009B]]
  ```
- Keep `prev` separate from `refs` so story-bible links stay distinct from sequence links.

### (Optional) quick Dataview check
```dataview
TABLE prev AS "Previous"
FROM "Scenes"
SORT scene ASC
WHERE !prev
```
(Shows scenes missing a `prev:` so you can fix gaps.)

Short version: add `prev:` where it helps continuity; it costs almost nothing and pays off in cleaner handoffs.

---

**User:**

It could add a couple thousand tokens to the input context, but if 8m only going scene by scene should be fine?

---

**Assistant:**

Exactly — you’re thinking about it correctly.  

Even if each `prev:` link adds a few hundred to a couple thousand tokens of extra context (when Smart Context pulls the previous scene text), it’s **insignificant** at scene scale and well within what modern models handle comfortably.

---

### Rough math
- **Scene draft:** ~800–1 200 words → 1 000–1 500 tokens  
- **Brief + YAML + bible refs:** < 300 tokens  
- **Previous scene:** another 1 000–1 500 tokens  
→ total ≈ 2 500–3 000 tokens  

That’s trivial for any model with a 100k+ context window (Claude Sonnet, GPT-4-turbo, etc.), and still fine for smaller free-tier models that can take 8k–16k.

---

### Practical tip
If you ever start bundling *multiple* scenes (say, for arc continuity or tone checks), you can:
- Keep `prev:` as a **link only**, not a full inclusion (`[[Scene_011]]` but don’t select it in Smart Context) to stay light.  
- Or, if you copy with Smart Context, simply deselect it when the previous beat isn’t needed.

---

### TL;DR
> Yes — linking a previous scene for continuity adds minimal token load and is totally fine for scene-by-scene editing or drafting.  
> Just be selective when you start bundling larger spans; otherwise, it’s a non-issue.

---

**User:**

In a multi scene check, I wouldn’t follow links any way.. just manually select the bible elements that matter. 

---

**Assistant:**

Exactly — that’s the right move.  

You only want to follow links when continuity or context is **explicitly relevant**. For multi-scene passes (tone, arc, character consistency), manual selection beats automation every time.

---

### Why manual selection works better

| Issue | Auto-follow behavior | Manual select advantage |
|--------|----------------------|--------------------------|
| **Token control** | Can balloon fast (each linked note adds text) | You pick only the essentials |
| **Context quality** | Includes redundant or outdated refs | You include only what matters now |
| **Interpretation** | LLM might blur temporal boundaries between scenes | Keeps temporal flow clear—you define the scope |
| **Cognitive clarity** | Hard to see what’s actually being sent | You see the exact package going to the model |

---

### Practical pattern
When you’re doing a continuity or tone sweep:
1. **Select** the 2–3 relevant scene files manually.  
2. **Add** a few bible notes (e.g., `[[Character_Maggie]]`, `[[Theme_Trust]]`, `[[Style_Cinematic]]`).  
3. **Skip** the `prev:`/`next:` entirely unless the handoff itself is under review.  
4. Run **Smart Context → Copy selected** → paste into the “multi-scene check” prompt.

---

### TL;DR  
> For single-scene work, follow `prev:` when it matters.  
> For multi-scene or arc checks, ignore links and hand-pick context.  
> It keeps token count low, context focused, and intent fully in your hands.

---

**User:**

So… an interesting prompting tactic.. instead of a “write this scene” prompt and then paste in the context… how about a “create the best prompt that could write this scene” prompt? And paste in the context. 

---

**Assistant:**

That’s a very sharp twist — and yes, it’s a genuinely powerful technique.  
You’re moving from *content generation* to *prompt synthesis*, which lets the model surface what *it* would find most useful before you spend tokens on the heavy draft.

---

## 🧠 Why this works
When you say *“write the best prompt that could write this scene,”* you’re asking the model to:
- interpret your **brief + context**,  
- reverse-engineer the *ideal instruction set*, and  
- externalize its reasoning instead of burying it in the draft.

That gives you a **meta-prompt** tuned to your current context and model, which you can then reuse or refine manually before running the actual draft.  

It’s effectively **AI-assisted prompt engineering on demand.**

---

## ⚙️ How to do it

### Step 1: Ask for the prompt
```
<instructions>
You are a prompt designer.
Create the best possible prompt that would generate a high-quality draft of the scene described below.
The prompt should include:
- role or persona for the model
- clear writing constraints (tone, POV, pacing, word count)
- how to use the context
Return the prompt text only.
</instructions>

<context>
[Paste Smart Context output: YAML + refs]
</context>
```

### Step 2: Inspect and tune
The model might give you something like:

```
You are an experienced fiction writer...
Write a 900–1100-word scene using the following YAML...
Maintain a tense, cinematic tone...
```

You can tighten or simplify that before feeding it back in.

### Step 3: Run the generated prompt
Paste that new prompt into a second chat, append the same context, and generate the scene.  
Now you’ve separated **prompt synthesis** from **content generation**, giving you full control and clarity over both steps.

---

## 🎯 Advantages

| Benefit | Description |
|----------|-------------|
| **Meta-learning** | You see what the model *thinks* it needs — useful for training yourself on better prompting. |
| **Reusability** | Each generated prompt becomes a template for similar scenes. |
| **Cost control** | You can stop after Step 1 if the prompt is bad — no wasted generation tokens. |
| **Transparency** | You know exactly what instructions are guiding the draft. |
| **Human-AI blend** | Keeps you in charge of creative intent; the AI just scaffolds your directions. |

---

### TL;DR  
> Instead of “Write the scene,” ask “What’s the best prompt to write this scene?”  
> You’ll get smarter, reusable instructions and a clearer sense of what the model understands before you ever hit “Generate.”

---

**User:**

I could use a cheap/free model to write the prompt and a premium model to write the prose. 

---

**Assistant:**

Exactly — that’s the *economically and creatively optimal* approach.  

You’re basically splitting the workflow into two cognitive layers:  
- **cheap model = meta-prompt engineer**  
- **premium model = prose craftsman**

---

## 🧩 1. Why this works
Cheap or open models (Gemma, Mistral, Claude Haiku, etc.) are already excellent at **instruction synthesis**—they understand structure, tone markers, and output formatting.  
Premium models (Claude Sonnet, GPT-4-turbo) excel at **style, nuance, and continuity**, which are the expensive parts.

By decoupling them:
- You save cost and context window on the creative side.  
- You get more consistent, high-quality prompts tuned to your project.  
- You can reuse those prompts for later scenes or revisions.

---

## ⚙️ 2. How to run it

**Phase 1 – Prompt Synthesis (cheap model)**
```
<instructions>
You are a prompt designer.
Write the best possible prompt to generate a strong draft of this scene.
Include: role, tone, POV, pacing, and how to use the YAML + bible refs.
Return only the prompt.
</instructions>

<context>
[Paste Smart Context output]
</context>
```

→ Output: a structured draft prompt, e.g.:

> “You are a cinematic prose writer.  
> Write a 1000-word scene using the YAML brief below…”

---

**Phase 2 – Scene Generation (premium model)**
```
[Paste the synthesized prompt here]
<context>
[Paste the same Smart Context output]
</context>
```

The high-end model now works inside an optimized instruction frame designed by the cheaper one.

---

## 💡 3. Optional variants
- **Add a third mini-step:** ask the cheap model to *evaluate* the premium model’s output (“Does this fulfill the brief?”).  
- **Store good prompts** as `[[Prompt_Draft_X]]` notes for future scenes.  
- **Experiment**: sometimes the cheap model’s own prose is “good enough” for minor beats; reserve the expensive call for key scenes.

---

### TL;DR
> Let the free model design the instruction; let the premium model spend the tokens on artistry.  
> It’s prompt engineering as a service — run locally, cost pennies, and scales cleanly with your Obsidian setup.

---
