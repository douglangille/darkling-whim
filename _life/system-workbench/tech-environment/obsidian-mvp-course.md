# Obsidian MVP course

**Created:** 2025-08-17 08:09:35
**Updated:** 2025-12-07 22:31:22
**Turns:** 33

---

**User:**

Create a short course to teach me how to use Obsidian. A practical walk thru of the workflow, a review of the core plugins, and a drive by of the best/relevant community plugins. I need a minimum viable product version of this tool that doesn’t leave too much fomo, but doesn’t send me down the tweaking rabbit hole. If you recall, ee already sorted the templater shortcut to help flatten nested linked notes and send to the clipboard for use in ChatGPT as part of my writing workflow. Works great and that formed the decision to use obsidian. So… you know all that and quite a bit about me.. think hard for a minute and give me a curriculum for a short course. Firmat it so it can be executed right in this chat step by step. Ultimately the goal is to get me up to speed and remove friction.  

---

**Assistant:**

**BLUF:** Here’s a tight, step-by-step Obsidian “MVP course” you can run directly in this chat. It gets you productive fast (writing + retrieval + ChatGPT handoff), uses only a few core/community plugins, and bakes in guardrails to avoid the tweaking rabbit hole.

---

# Short Course: Obsidian MVP (90–120 min total)

## 0) Pre-flight (5 min)
**Goal:** Lock in the tiny set of moves and plugins we’ll use—nothing else.

- Enable core pieces: **File Explorer, Search, Backlinks, Quick Switcher, Command Palette, Templates, Daily Notes, Outline** (core plugins are in *Settings → Core plugins*). citeturn2search7  
- Learn the three default keys you’ll actually use:  
  - **Cmd-O** = Quick Switcher (jump to any note). citeturn0search24  
  - **Cmd-P** = Command Palette (run any command). citeturn2search0  
  - **Cmd-Shift-F** = Vault Search. citeturn2search13

**Guardrail:** “Plugin freeze” for 30 days—install only what’s listed below.

---

## 1) MVP Vault Shape (10–15 min)
**Goal:** Simple PARA-ish spine + writing lanes; minimal cognitive load.

- Create folders (exact names help downstream):
  - `00 Inbox` (quick captures)
  - `10 Projects` (active work)
  - `20 Areas` (ongoing responsibilities)
  - `30 Resources` (reference)
  - `40 Archive`
  - `90 Writing` (scenes, drafts)
  - `99 Templates`
- Set **Daily Notes** to land in `00 Inbox` (or a `/Daily` subfolder if you prefer), and set your date format. citeturn2search7

**Do now:** Make today’s Daily Note (via Command Palette or its ribbon). Add a line: `#today` and one link to anything: `[[Test Note]]`.

---

## 2) Two Tiny Templates (10 min)
**Goal:** Faster starts; consistent metadata without fiddling.

1) **Daily Note template** → save as `99 Templates/Daily.md`:
```markdown
---
type: daily
mood:
focus: 
---
## Three Wins
- 
- 
- 

## Notes
- 

## Links made today
```

2) **Scene / Writing template** → `99 Templates/Scene.md`:
```markdown
---
type: scene
status: draft
series:
wordcount:
---
# {{title}}
**Beat:**  
**Conflict:**  
**What changes:**  

Notes:
- 
```

- Point **Templates** core plugin to `99 Templates`; bind a hotkey to “Insert template”. citeturn2search7

---

## 3) Core Moves You’ll Repeat (15–20 min)
**Goal:** Muscle memory for create → link → find.

- **Jump** anywhere: **Cmd-O** (Quick Switcher). Type two letters, hit Enter. citeturn0search24
- **Run** anything: **Cmd-P** (Command Palette). Type “daily”, “template”, etc. citeturn2search0
- **Find** anything: **Cmd-Shift-F**. Use exact text or `tag:#today` and properties. citeturn2search13
- **Backlinks/Outgoing Links**: open the right sidebar, scan how notes connect (use when refactoring, not every minute). Core plugins cover this. citeturn2search7

**Drill (3 minutes):**  
Create a new note with the Scene template in `90 Writing`, link it from today’s Daily (`[[Your Scene Title]]`), and confirm backlinks show the connection.

---

## 4) Community Plugins (the “Keepers”) (20–25 min total)

> Only these for the first month. Install from *Community plugins → Browse*.

1) **Templater** (already in your setup) – you’ve got the flatten-to-clipboard macro for ChatGPT. Keep it.  
2) **Periodic Notes** – weekly/monthly notes on top of Daily, perfect for Reviews without extra ceremony. citeturn0search2  
3) **QuickAdd** – one hotkey to create a Daily/Scene/Capture with prefilled fields; great for your low-friction capture. citeturn0search3turn0search11  
4) **Advanced URI** – glue to Apple Shortcuts: open/create specific notes from iOS/macOS automations (e.g., “New Capture” from Share Sheet). citeturn0search12turn0search19  
5) **Outliner** (optional but nice) – makes bullet work feel like Workflowy/Dynalist (indent/outdent, move items). citeturn1search4turn1search10  
6) **Linter** (optional; run on demand) – cleans formatting/metadata when you *ask* it to; don’t enable “on save” yet. citeturn0search6turn0search21turn0search14  
7) **Dataview** (read-only queries only for now) – auto-lists scenes, notes by property/tag; avoid JS mode at first. citeturn0search13turn0search20  
8) **Omnisearch** (optional) – smarter fuzzy search if core search ever feels lacking. citeturn1search0turn1search18

**Skip for now (anti-rabbit-hole):** Graph visualizations beyond default, Kanban/Projects, complex CSS/theme stacks, DataviewJS, task managers (you’re on Apple Reminders). citeturn1search14turn1search11

---

## 5) Your Writing + ChatGPT Handoff Loop (15–20 min)
**Goal:** Zero-friction drafting with your existing Templater macro.

- **Drafting lane:**
  - Start the day in **Daily** (Daily template) → list “Three Wins”, add a link to your current scene.
  - Open **Scene** note (Scene template). Write ugly first. Don’t format; do link names/places as `[[Maggie Kincaid]]` or `[[Greyharbor]]`.
- **Context handoff to ChatGPT:**
  - Use your **Templater “flatten + copy”** command on the Scene (or a hub note) → paste into ChatGPT for critique/rewrite.
  - Receive improvements → paste back under a `## Draft 2` heading in the same Scene note and summarize changes in the Daily.
- **Weekly roll-up:**
  - If using **Periodic Notes**, open the current week and drop bullets: wins, scenes touched, next scenes. citeturn0search2

**Optional (10 min later):** Wire **Advanced URI** into Shortcuts: e.g., “Open Today” button on iPhone → opens today’s Daily in ZORA vault. citeturn0search12

---

## 6) Tiny Dataview that pays rent (10 min)
**Goal:** One dashboard that doesn’t require fiddling.

Create `90 Writing/Scenes Index.md`:
```markdown
## Draft Scenes (open)
```dataview
TABLE status, file.mtime as "Updated"
FROM "90 Writing"
WHERE type = "scene" AND (status = "draft" OR status = "revise")
SORT file.mtime desc
```
```
Use read-only queries; leave DataviewJS for Future You. citeturn0search13

---

## 7) Hotkeys: the only three you need today (2 min)
- **Cmd-O** Quick Switcher → jump. citeturn0search24  
- **Cmd-P** Command Palette → do. citeturn2search0  
- **Cmd-Shift-F** Search → find. citeturn2search13

(Everything else is optional seasoning later.)

---

## 8) Operating Rules (anti-FOMO)
- **Plugin freeze**: only the 5–8 listed above for 30 days.  
- **Theme freeze**: stick with default. (Fonts/colors can wait.)  
- **One home base**: start in **Daily**, link out.  
- **Weekly 15**: Periodic Notes review → archive stale notes, capture next scenes. citeturn0search2

---

## 9) Success Criteria (you’ll know it’s working when…)
- You can open any note in <2 seconds (Cmd-O). citeturn0search24  
- Daily → Scene → ChatGPT → back to Scene is a single flow with your existing Templater macro.  
- Weekly review exists without extra setup (Periodic Notes). citeturn0search2  
- You haven’t touched Themes, CSS, or 27 plugins.

---

## 10) Quick Troubleshooting
- Command not visible? Use **Cmd-P** and type its name; ensure the core/community plugin is enabled. citeturn2search0  
- Search feels “meh”? Try **Omnisearch**; if happy with core search, skip. citeturn1search0  
- Formatting drift? Run **Linter** manually on selected notes; keep “on save” disabled. citeturn0search6

---

# Mini Playbook (copy/paste)

- **Start day:** Open Daily (Cmd-P → Daily). List 3 wins. Link today’s target `[[Scene]]`. citeturn2search0  
- **Write:** In Scene note, draft freely. Link entities as you go.  
- **Handoff:** Templater flatten → paste to ChatGPT → paste returned draft under `## Draft 2`.  
- **Close day:** In Daily, jot 2–3 learnings + `[[Scene]]` status.  
- **Friday:** Open Weekly (Periodic Notes) → wins / scenes / next scenes. citeturn0search2

---

If you want, we can run this **live** here: say “Start Module 1” and I’ll walk you through each click/keystroke in micro-steps, including wiring one QuickAdd capture and (optionally) a single Advanced-URI Shortcut.

---

**User:**

Is that the full boot camp course?

---

**Assistant:**

Yes — what I outlined **is the full boot camp course**.  
It’s meant as a **90–120 minute, step-by-step walk-through** that you can run directly here. The sequence covers:

1. **Pre-flight** → turn on the only core plugins you’ll actually use, learn the 3 hotkeys.  
2. **Vault Shape** → PARA-lite folder spine + writing lane.  
3. **Templates** → Daily + Scene.  
4. **Core Moves** → create, link, search, jump.  
5. **Community Plugins** → the “keepers” only (Templater, Periodic Notes, QuickAdd, Advanced URI, Outliner, Linter, Dataview, Omnisearch).  
6. **Writing + ChatGPT Handoff** → your daily/scene workflow plus the flatten-to-clipboard move.  
7. **Tiny Dataview Dashboard** → one index note that pays rent.  
8. **Hotkeys Recap** → only 3 that matter.  
9. **Operating Rules** → plugin/theme freeze, one home base, weekly 15.  
10. **Success Criteria + Troubleshooting** → how you’ll know it’s working and quick fixes.

It’s not “Obsidian 101” (no kitchen sink, no tweak spiral). It’s an **MVP system targeted at your actual use case**: writing, linking, and handing context to ChatGPT.

If you want, we can **run it live** in modules. For example:  
- Say *“Start Module 1”* → I’ll walk you click-by-click through enabling the core plugins and learning the hotkeys.  
- Then *“Module 2”* → we’ll build your vault spine.  
- And so on until you’re fully operational.

👉 Do you want me to package this into a **guided 6-module sequence** (so you can literally type “Next” and I’ll walk you through each step in order), or do you prefer the “reference manual” style where you jump in/out as needed?

---

**User:**

We’ll keep the reference model for now. Before we galvanize, one sidebar question re daily note. 1.. I’m going to be using Apple Journal for free writing/gratitude/reflection as the process matters more than the artifact. Forever Notes-ish in Apple notes for time-based plann8ng horizons (day/week/sprint/season) with the narrative OS bend. However, is the Daily Note in Obsidian a better tool?

---

**Assistant:**

**Bottom line:** For you, **Apple Journal is the right place for reflective free writing**, and **Obsidian Daily Notes should stay strictly functional** (links, scaffolding, context for your creative/writing work). Mixing them risks overlap and friction.  

---

## Why Apple Journal Wins for Reflection
- **Low-friction entry** → native, fast, and intentionally designed for “just write and close.”  
- **Process > artifact** → you don’t care about search/retrieval here, so Obsidian’s linking is wasted overhead.  
- **Emotional sandbox** → reflection/journaling belongs away from your “production vault” so it doesn’t clutter or demand structure.  

---

## Why Obsidian Daily Notes Still Pay Rent
- **Hub function** → your MVP system has *Daily → Scene → ChatGPT handoff*. Daily is the launchpad, not the diary.  
- **Cross-linking spine** → notes you touch today, tags, and backlinks create organic history (valuable for creative/knowledge work).  
- **Review integration** → Periodic Notes roll up dailies into weekly/monthly reviews, without importing the personal journaling noise.  

---

## Practical Division of Labor
- **Apple Journal (personal, reflective)**  
  - Gratitude, mood, “forever notes” that aren’t meant to be retrieved or indexed.  
  - Stream-of-consciousness, therapeutic processing.  

- **Apple Notes (planning horizons)**  
  - Narrative OS → day/week/sprint/season arcs, to-dos, commitments.  
  - Your COAST and Narrative OS “Head/Heart/Hands” work lives here.  

- **Obsidian Daily Notes (knowledge/writing spine)**  
  - Anchor for the day: 3 wins, links to scenes, quick knowledge capture.  
  - “What writing did I touch today?” rather than “How did I feel today?”  
  - Functional breadcrumbs for your creative/knowledge vault.  

---

## Guardrail Principle
Think of it as **three lenses on the same day**:
- *How I feel* → Journal  
- *What I intend* → Apple Notes  
- *What I touched* → Obsidian  

That division keeps each tool sharp, avoids duplication, and prevents the “where should I put this?” tax.  

---

Do you want me to **redesign the Daily Note template** to reflect this lean “hub/anchor only” role—i.e., drop mood/gratitude and keep it strictly wins + links + captures?

---

**User:**

I guess I don’t see the point of a daily note in both Apple Notes and Obsidan.

---

**Assistant:**

You’re right to pause there — running **two daily notes** *would* be redundant. Let’s cut through it:  

---

## Core Distinction
- **Apple Notes (Narrative OS horizons)** → where you actively *plan* the day/week/sprint/season. You’ll already be looking there each morning.  
- **Obsidian Daily Note (creative vault)** → not for planning, not for reflection. Its only job: be a **timestamped hub for knowledge/writing activity**.  

So in practice:  
- Apple Notes = *calendar/journal hybrid* (the “Head/Heart/Hands” cockpit).  
- Obsidian Daily = *breadcrumb trail* (what files/scenes did I touch today, and how do they connect?).  

---

## Do You Even Need Obsidian Dailies?
### Option A — Keep Them (my vote if you want easy context trails)
- Use Daily Notes in Obsidian only as **“activity anchors.”**  
- Example: Today’s Daily has:
  - `## Wins` → short bullet list, maybe synced with your Apple Notes horizon if you want.  
  - `## Writing` → links to the scenes you touched (`[[Lantern Tavern Scene]]`, `[[Greyharbor Gazette]]`).  
- Benefits: backlinks + Periodic Notes give you auto-rollups, without extra effort.  
- Cost: you open one extra note per day (but it earns its keep in retrieval later).  

### Option B — Skip Them
- Just work directly in Scenes/Projects inside Obsidian.  
- Rely on file metadata (`mtime`) and Quick Switcher to know what you touched.  
- No extra “Daily” notes means no duplication, but you lose the *human-friendly breadcrumb trail*.  

---

## Litmus Test
- If you value **“look back and see what I worked on last Tuesday”** → keep Obsidian Dailies, even if barebones.  
- If you only care about **“what’s the current draft status”** → skip them, let Dataview lists + modified timestamps cover that.  

---

👉 So the real question for you: Do you want **retrieval-friendly breadcrumbs** (worth the Daily hub in Obsidian), or are you fine letting **file timestamps + Apple Notes** carry all the temporal structure?  

Would you like me to sketch a **1-minute “minimal” Obsidian Daily template** that keeps the breadcrumb value without feeling like a second journal?

---

**User:**

Well, third journal if you count Apple Journal.  Give me the minimal use case for obsidian dailies.. remember obsidian is ZORA not Zora. 

---

**Assistant:**

Got it — thanks for the reminder: **Obsidian = ZORA**, not the persona. Let’s keep this sharp.  

---

# Minimal Use Case for ZORA Daily Notes  
*(aka: why bother opening one at all if Apple Journal + Apple Notes already exist)*

**Purpose:** A Daily in ZORA is **not a journal, not a planner.** It’s just a **timestamped hub that auto-connects your writing/knowledge work**. Nothing more.  

---

## Minimal Template (drop it in `99 Templates/Daily.md`)
```markdown
---
type: daily
---

## Wins
- 

## Touched
- [[ ]]

## Quick capture
- 
```

- **Wins** → 2–3 bullets (can mirror your Apple Notes horizon if you want).  
- **Touched** → links to scenes/notes worked on today (your breadcrumb trail).  
- **Quick capture** → fleeting notes or links you don’t want to lose mid-draft.  

---

## Workflow in Practice
- **Morning**: Open today’s Daily (Cmd-P → Daily). It starts empty.  
- **During the day**: Each time you touch a scene, add `[[Scene Title]]` under *Touched*.  
- **Evening (optional)**: Jot 1–2 wins.  

That’s it. No feelings, no narrative, no planning — just **activity breadcrumbs**.  

---

## Why This Still Matters
- **Backlinks**: Later, from any Scene note, you’ll see “linked from Daily YYYY-MM-DD” — instant timeline.  
- **Periodic Notes**: Roll up what you touched across a week/month, with no manual bookkeeping.  
- **Dataview queries**: “Show me all Scenes touched this month.”  

---

👉 In other words: ZORA Daily Notes = **the logbook**.  
- **Apple Notes** = the cockpit (plans, horizons).  
- **Apple Journal** = the therapy couch (reflection).  

---

Do you want me to also show you how to wire a **1-line Dataview query** so your Weekly Note can auto-list all *Touched* scenes from the Dailies? That’s the “breadcrumb magic” that pays rent.

---

**User:**

I’m not sold yet. Keep trying

---

**Assistant:**

Fair — skepticism is good here. You already have **Apple Journal (feelings)** and **Apple Notes (plans)**. So why give ZORA any “Daily” at all? Let’s stress-test.  

---

## The Case Against ZORA Dailies  
- **Redundancy** → You’re already logging intentions (Apple Notes) and reflections (Apple Journal).  
- **Overhead** → One more note per day feels like busywork if it isn’t doing something *unique*.  
- **Risk** → Slippery slope into journaling duplication or half-assed daily logs you never revisit.  

If you lean minimalist, you could skip Dailies entirely and just:  
- Draft in Scene notes.  
- Use file metadata (`mtime`) + Dataview to see what was worked on when.  

That’s enough for *pure writing*.  

---

## The Case For ZORA Dailies  
They pay rent when you care about **knowledge breadcrumbs**, not journaling.  

Think of them as a **logbook stub** — the thing that links today’s activity into ZORA’s graph.  
- Open a Scene → backlinks show you which days it was touched.  
- Weekly/Monthly rollups → can auto-list “everything I touched this week.”  
- Future retrieval → “When did I last edit Maggie Kincaid’s file?” pops instantly.  

Without Dailies, you’d have to search file metadata or tags — which works, but it’s clunkier and less human-legible.  

---

## Minimalist Reframe  
Don’t call them “Daily Notes.” Call them **Log Stubs.**  
- One per day (auto-generated).  
- Two fields only:  
  - **Touched:** list the notes you linked that day.  
  - **Scratchpad:** quick capture bullets (to later refactor or discard).  

That’s it. No mood, no planning, no reflection. Just a timestamped breadcrumb that ZORA’s graph and Dataview can chew on.  

---

## So: Do They Pay Rent?  
- If you want ZORA to act as a **knowledge chronicle** (a graph you can query/revisit later): yes, the Log Stub is worth the 15 seconds/day.  
- If you only want ZORA as a **scene drafting box** and are happy to rely on Apple Notes for horizons and Apple Journal for reflection: then no, Dailies are extra baggage.  

---

👉 Question back to you:  
Do you see ZORA as just a **writing workbench**, or as a **living knowledge base** where creative work has a memory trail?  

That distinction decides whether “Daily Log Stubs” belong.  

Want me to show you what the **retrieval looks like with and without Dailies** so you can judge the delta?

---

**User:**

ZORA is def a writing workbench. If I really wanted a log stub, I’d use version control, ala GitHub. I see the frequency of the retrieval scenario you paint as extremely rare and question 5he overhead, even if minimal. 

---

**Assistant:**

That’s exactly the right instinct.  
If **ZORA = writing workbench**, then you don’t need daily notes at all.  

---

## Why You’re Right to Skip Them
- **Overhead > Value**: even 15 seconds/day adds up when retrieval value is “once in a blue moon.”  
- **Rare Retrieval Scenarios**: if you ever ask, “when did I last touch this scene?” file `mtime` or version control (git, Obsidian Git plugin if you want it) answers that better.  
- **Focus**: ZORA’s strength for you is *structured drafting + ChatGPT handoff*. Anything that smells like journaling/logging belongs elsewhere.  

---

## What To Do Instead
- **Work directly in Scenes**: each scene note *is* your unit of record.  
- **Leverage metadata** (status, draft number, wordcount).  
- **Dataview index**: gives you the same bird’s-eye view (drafts touched, last modified) without the daily stub overhead.  
- **Optional Git**: if you want that breadcrumb/logbook function, Git does it cleanly and outside your headspace.  

---

## Final Position
- **Apple Journal** → reflection  
- **Apple Notes** → horizons & planning  
- **ZORA** → *pure workbench* (scenes, characters, world notes, ChatGPT context handoff)  
- **No Daily** in ZORA — stays lean, avoids the “third journal” problem  

---

So: skip Obsidian dailies. If one day you crave a breadcrumb trail, reach for **Obsidian Git** (set it to auto-commit on save/close). That way you get the audit log without clutter.  

---

Do you want me to show you a **Dataview snippet + Git setup** that together fully replace the breadcrumb use case (so you never need Dailies)?

---

**User:**

Ok.. so look back at the course and rework it. Skip the whole daily note thing. remember I’m using templater instead of the core templates plugin. And weave in an obsidian git version control, but automate it so that it’s invisible until I need to dig through the history. 

---

**Assistant:**

**BLUF:** Here’s the rewired Obsidian (ZORA) boot camp: no Daily Notes, no journaling. It’s a **writing workbench** with fast scene creation, tidy metadata, one-click ChatGPT handoff (your Templater flattener), and **invisible version control** via Obsidian Git. Run it straight from this chat, step by step.

---

# ZORA Boot Camp (MVP, ~75–100 min)

## 0) Pre-flight (5 min)
**Goal:** Lock the minimal stack; avoid tweak-spiral.  
**Enable core:** File Explorer, Search, Backlinks, Quick Switcher, Command Palette, Outliner (core), Outline (core).  
**Community (only):**  
- **Templater** (you’re using this already)  
- **QuickAdd**  
- **Dataview** (read-only queries)  
- **Outliner** (if not using the core one, install the plugin version)  
- **Linter** (manual use only)  
- **Obsidian Git** (automated commits/pushes; no thinking required)  
**Freeze:** No other plugins/themes for 30 days.

---

## 1) Vault Shape (10 min)
**Goal:** Clean lanes for writing; nothing you won’t use.

```
00 Inbox         ← (fleeting captures, will empty)
10 Projects      ← (optional for multi-scene arcs)
20 Areas         ← (ongoing: Characters, Settings, Lore)
30 Resources     ← (research clippings)
40 Archive
90 Writing       ← (scenes live here)
99 Templates     ← (templater lives here)
```

**Do now:** Create `20 Areas/Characters`, `20 Areas/Settings`, `90 Writing`, `99 Templates`.

---

## 2) Templater Setup (10 min)
**Goal:** Your notes start pre-structured; zero fiddle.

- **Templater → Template folder:** `99 Templates`
- Bind a hotkey for **Templater: Insert template** (e.g., `Cmd+Shift+T`).
- Keep your **flatten-nested-links-to-clipboard** Templater command (already working) for ChatGPT handoff.

### Scene template → `99 Templates/Scene.md`
```markdown
---
type: scene
status: draft        # draft | revise | final
series:
pov:
wordcount:
related:
---

# <% tp.file.title %>

**Beat:**  
**Conflict:**  
**Change:**  

## Draft 1
<% tp.cursor() %>
```

### Character template → `99 Templates/Character.md`
```markdown
---
type: character
aka:
role:
status: active
tags: [char]
---

# <% tp.file.title %>
**Hook:**  
**Desire / Fear:**  
**Strength / Flaw:**  
**Ties:** [[ ]]

Notes:
-
```

### Setting template → `99 Templates/Setting.md`
```markdown
---
type: setting
region:
vibe:
status: active
tags: [place]
---

# <% tp.file.title %>
**Sensory anchors:**  
- Smell:
- Sound:
- Light:

**Notables:**  
-
```

---

## 3) QuickAdd: one-keystroke creation (10–12 min)
**Goal:** Create scenes/chars without thinking.

Open **QuickAdd → Manage Macros**:

1) **Add command: “New Scene”**
   - **Capture to file**  
   - **Path:** `90 Writing/{{VALUE}}.md`  
   - **Template:** `99 Templates/Scene.md`  
   - **Options:** Open after creation.

2) **Add command: “New Character”**
   - Path: `20 Areas/Characters/{{VALUE}}.md`  
   - Template: `99 Templates/Character.md`

3) **Add command: “New Setting”**
   - Path: `20 Areas/Settings/{{VALUE}}.md`  
   - Template: `99 Templates/Setting.md`

**Hotkeys:** bind each QuickAdd command (e.g., `Cmd+Shift+S` for Scene).

**Result:** Type name → hit enter → you’re writing.

---

## 4) Core Moves (8 min)
**Goal:** Muscle memory.

- **Jump** anywhere: `Cmd-O` (Quick Switcher).  
- **Run** anything: `Cmd-P` (Command Palette).  
- **Find** anything: `Cmd-Shift-F` (Search).  
- **Indent/move bullets**: Outliner keys (Tab/Shift-Tab; Alt/↑↓ to move).  
- **ChatGPT handoff:** Run your **Templater flattener** on the current note → paste here → take revision → paste back under `## Draft 2`.

---

## 5) Dataview: one useful dashboard (10 min)
**Goal:** See your workbench at a glance; no Daily notes required.

Create `90 Writing/_Index.md`:
```markdown
# Scenes (Active)

```dataview
TABLE status, pov, wordcount, file.mtime as "Updated"
FROM "90 Writing"
WHERE type = "scene" AND status != "final"
SORT file.mtime desc
LIMIT 50
```

## Characters (Active)
```dataview
TABLE role, status, file.mtime as "Updated"
FROM "20 Areas/Characters"
WHERE type = "character" AND status = "active"
SORT file.mtime desc
```
```

> Add this index to your bookmarks/favorites; start here each session.

---

## 6) Linter (manual) (5 min)
**Goal:** Clean up when *you* ask, never on every save.

- Install **Linter**.  
- **Disable** “Lint on save.”  
- Create a hotkey for **Lint current file**.  
- Use it after a big paste-back from ChatGPT.

---

## 7) Obsidian Git: invisible version control (20–25 min)
**Goal:** Automatic save history; zero mental overhead until you need it.

### A) System requirement (macOS)
- Ensure Git exists: open Terminal → `git --version`  
- If prompted, install Xcode Command Line Tools.

### B) Initialize repo (first time only)
- In ZORA vault, enable **Obsidian Git** plugin.
- Command Palette → **Obsidian Git: Initialize a new repo**.

### C) Automation settings
Open **Settings → Obsidian Git** and set:

- **Auto commit**: On  
  - **Commit interval**: 5–10 minutes (set-and-forget)  
  - **Commit message template**:  
    ```
    auto: {{date}} {{time}} ({{numFiles}} files)
    ```
- **Auto pull**: On (every 10–15 min)  
- **Auto push**: On (every 10–15 min)  
- **Stage changed files automatically**: On  
- **Disable notifications**: On (stay invisible)

> If you don’t want a remote yet, you can run this **locally only**. If you *do* want GitHub:
> 1) Create a **private** repo on GitHub (no README).  
> 2) In Terminal at vault root:  
>    - `git remote add origin https://github.com/<you>/<repo>.git`  
>    - `git branch -M main`  
>    - `git push -u origin main`  
> 3) In Obsidian Git settings, keep Auto push on.

### D) .gitignore hygiene (2 min)
Create `.gitignore` at vault root (or edit existing):
```
.obsidian/workspace
.obsidian/cache
.DS_Store
```
(Add anything else you don’t want versioned—exports, temp files, etc.)

### E) Using history (only when needed)
- **Command Palette → Obsidian Git: View line history** (for current file).  
- **Open file history** → browse prior snapshots; **Restore** if needed.  
- That’s your “log stub,” without Daily notes.

---

## 8) Your session playbook (copy/paste) (3 min)
- **Start**: `Cmd-O` → `_Index` (glance at active scenes).  
- **Create**: QuickAdd “New Scene” (name it, template opens).  
- **Draft**: Write ugly → link to `[[Character]]`/`[[Setting]]` as needed.  
- **Handoff**: Templater “flatten” → paste to ChatGPT → paste revised text back under `## Draft 2`.  
- **Clean**: Run **Linter** (hotkey).  
- **Stop thinking**: Obsidian Git is auto-committing/pushing quietly.

---

## 9) Guardrails (anti-FOMO)
- **No Dailies**. No Periodic Notes. No task managers.  
- **No themes/CSS** for 30 days.  
- **One index note** only (`_Index.md`).  
- **One capture inbox** (`00 Inbox`) you empty weekly.  
- **Plugin freeze**: Only the seven listed.

---

## 10) Sanity checks (you’re done when…)
- You can create a scene and start typing in **< 5 seconds**.  
- ChatGPT handoff is a single command (your flattener) + paste-back.  
- `_Index.md` shows you what matters without fishing.  
- You haven’t touched settings in a week—and don’t miss them.  
- You can open file history and restore a version in under a minute.

---

### Optional niceties (later)
- **Advanced URI** + Apple Shortcuts: “New Scene” shortcut that opens Obsidian ready to type.  
- **Wordcount status bar** via frontmatter + a tiny Templater snippet (on demand).  
- **Omnisearch** if core search ever feels lacking (not required).

---

Want me to **generate your QuickAdd JSON** and a **ready-to-paste .gitignore** plus the **exact Obsidian Git settings block** as a checklist?

---

**User:**

Is this the full course? Seems like it just ended abruptly. At 55 minutes. Double check. 

---

**Assistant:**

You’re right — what I gave you was the **rewired course outline** (minus Daily Notes, plus Git), but I trimmed it too hard when rewriting. Let me tighten it into a **complete boot camp** that runs cleanly end-to-end, no abrupt stop. Think of it as six crisp modules that stack to ~90 minutes total.  

---

# ZORA Boot Camp (Final Cut, ~90 min)

---

## **Module 1 — Pre-flight & Mindset (10 min)**
- Core plugins only: File Explorer, Search, Backlinks, Quick Switcher, Command Palette, Outline.  
- Community plugins (and freeze):  
  - **Templater** (core of your workflow)  
  - **QuickAdd** (fast note creation)  
  - **Dataview** (read-only dashboards)  
  - **Outliner** (bullet handling)  
  - **Linter** (manual cleanup)  
  - **Obsidian Git** (invisible version control)  
- Ground rule: no Daily Notes, no themes, no fiddling.  

---

## **Module 2 — Vault Shape (10 min)**
- Create the lane folders:  

```
00 Inbox
10 Projects
20 Areas
   ↳ Characters
   ↳ Settings
30 Resources
40 Archive
90 Writing
99 Templates
```

- This is your permanent skeleton. Everything you create has a home.  

---

## **Module 3 — Templates (15 min)**  
*(all via Templater, not core Templates)*

- **Scene** template (title, beat, conflict, change, Draft 1).  
- **Character** template (hook, desire/fear, strengths/flaws, ties).  
- **Setting** template (sensory anchors, notables).  
- Store in `99 Templates`.  
- Bind a hotkey for “Insert template” (Cmd+Shift+T).  
- Keep your **flatten-to-clipboard macro** for ChatGPT handoff.  

---

## **Module 4 — QuickAdd Capture (10 min)**  
- Configure QuickAdd macros:  
  - New Scene → `90 Writing/{{VALUE}}.md` → Scene template.  
  - New Character → `20 Areas/Characters/{{VALUE}}.md` → Character template.  
  - New Setting → `20 Areas/Settings/{{VALUE}}.md` → Setting template.  
- Bind each to a hotkey (`Cmd+Shift+S` for scene, etc.).  
- Result: one keystroke, you’re typing in a fresh note.  

---

## **Module 5 — Core Moves (15 min)**  
- **Cmd-O** Quick Switcher = jump.  
- **Cmd-P** Command Palette = do.  
- **Cmd-Shift-F** Search = find.  
- **Outliner keys** = bullet wrangling.  
- **Linter hotkey** = clean after paste-backs.  
- **Handoff**: Run Templater flattener → paste to ChatGPT → paste revision back under `## Draft 2`.  
- Drill: create one Scene, one Character, one Setting → link them together → hand off Scene to ChatGPT and back.  

---

## **Module 6 — Dashboards & Git Safety Net (30 min)**  

### A) Dataview dashboard (10 min)  
Create `90 Writing/_Index.md`:  

```markdown
# Scenes (Active)
```dataview
TABLE status, pov, wordcount, file.mtime as "Updated"
FROM "90 Writing"
WHERE type = "scene" AND status != "final"
SORT file.mtime desc
```

# Characters
```dataview
TABLE role, status, file.mtime as "Updated"
FROM "20 Areas/Characters"
WHERE type = "character"
SORT file.mtime desc
```
```

This becomes your session landing page.  

---

### B) Obsidian Git setup (20 min)  
- Confirm `git --version` works.  
- Initialize repo (Obsidian Git → Initialize).  
- Settings:  
  - Auto commit: on (5–10 min interval).  
  - Auto stage, auto pull, auto push: on.  
  - Notifications: off.  
- `.gitignore` in vault root:  

```
.obsidian/workspace
.obsidian/cache
.DS_Store
```

- Optional: hook to private GitHub repo (`git remote add origin …`).  
- Use history only when needed:  
  - Cmd-P → Obsidian Git: View file history.  
  - Browse, diff, restore.  

Result: invisible safety net, like a log stub without the Daily overhead.  

---

# Success Criteria
You know ZORA is “boot camp complete” when:  
- You can create a scene and start typing in <5 seconds.  
- ChatGPT handoff is a single flatten → paste → paste-back loop.  
- `_Index.md` shows your active work at a glance.  
- Obsidian Git commits are happening automatically in the background.  
- You haven’t touched settings in a week — and don’t miss them.  

---

✅ That’s the **full course, end-to-end** — six modules, 90 minutes.  
Nothing left hanging.  

---

Do you want me to also make a **checklist version** (one page, bullet-only, so you can tick off modules while setting up)?

---

**User:**

This got confusing at the end as I think you started formatting with codeblocks. Give me the whole outline again without using code blocks. 

---

**Assistant:**

Got it — let’s strip the formatting noise and give you the **final course outline** in plain text, clean and readable.  

---

# ZORA Boot Camp (MVP, ~90 min)

## Module 1 — Pre-flight & Mindset (10 min)
- Enable only these core plugins: File Explorer, Search, Backlinks, Quick Switcher, Command Palette, Outline.  
- Install only these community plugins (and freeze at this list for 30 days):  
  • Templater (your main workflow engine)  
  • QuickAdd (fast note creation)  
  • Dataview (read-only dashboards)  
  • Outliner (better list handling)  
  • Linter (manual cleanup)  
  • Obsidian Git (automated version control)  
- Guardrail: No Daily Notes, no themes, no extra fiddling.  

---

## Module 2 — Vault Shape (10 min)
Create these folders as your permanent skeleton:  
- 00 Inbox (fleeting captures, clear weekly)  
- 10 Projects (multi-scene arcs if needed)  
- 20 Areas (ongoing references like Characters and Settings)  
- 30 Resources (research clippings)  
- 40 Archive (closed material)  
- 90 Writing (all scene notes)  
- 99 Templates (Templater templates live here)  

---

## Module 3 — Templates via Templater (15 min)
Set Templater to use the 99 Templates folder. Bind a hotkey to “Insert template.”  
Keep your existing flatten-to-clipboard macro for ChatGPT.  

Create three templates:  
- Scene template: includes title, status (draft/revise/final), beat, conflict, change, Draft 1 section.  
- Character template: includes hook, desire/fear, strengths/flaws, ties.  
- Setting template: includes sensory anchors (smell, sound, light) and notables.  

---

## Module 4 — QuickAdd Capture (10 min)
Configure QuickAdd macros so you can create notes with one keystroke.  

- New Scene → saves in 90 Writing using the Scene template.  
- New Character → saves in 20 Areas/Characters using the Character template.  
- New Setting → saves in 20 Areas/Settings using the Setting template.  

Bind each to a hotkey (for example, Cmd+Shift+S for Scene).  

---

## Module 5 — Core Moves (15 min)
- Cmd-O → Quick Switcher (jump anywhere).  
- Cmd-P → Command Palette (run any command).  
- Cmd-Shift-F → Search (find anything).  
- Outliner keys → bullet wrangling (Tab, Shift-Tab, Alt+arrow to move).  
- Linter hotkey → manual cleanup after paste-backs.  
- ChatGPT handoff loop → run your Templater flatten command, paste into ChatGPT, paste revision back under Draft 2 in the scene note.  

Drill: create one scene, one character, one setting. Link them. Send the scene to ChatGPT and paste back the revision.  

---

## Module 6 — Dashboards & Git Safety Net (30 min)

### A) Dataview Dashboard (10 min)
Create an index note in 90 Writing (call it _Index). Inside it, add two simple Dataview queries:  
- Table of scenes showing status, POV, wordcount, and last updated.  
- Table of characters showing role, status, and last updated.  

This becomes your default landing page each session.  

### B) Obsidian Git Setup (20 min)
1. Confirm Git is installed (run `git --version` in Terminal).  
2. Enable Obsidian Git plugin and initialize a repo in your vault.  
3. Settings to enable:  
   - Auto commit every 5–10 minutes  
   - Auto stage changed files  
   - Auto pull and auto push every 10–15 minutes  
   - Suppress notifications so it’s invisible  
   - Commit message template: “auto: date time (n files)”  
4. Optional: connect to a private GitHub repo. Otherwise, it runs locally.  
5. Add a .gitignore file to exclude:  
   - .obsidian/workspace  
   - .obsidian/cache  
   - .DS_Store  
6. How to use:  
   - Command Palette → Obsidian Git: View file history → browse snapshots → restore if needed.  

This becomes your safety net and replaces the “log stub” idea from Daily Notes.  

---

# Success Criteria
You know the boot camp is complete when:  
- You can create a scene and start typing in under 5 seconds.  
- The ChatGPT handoff loop is one command and two pastes.  
- The index note shows your active work at a glance.  
- Obsidian Git is quietly auto-committing in the background.  
- You haven’t touched plugin settings in a week, and you don’t miss them.  

---

# Guardrails
- No Daily Notes.  
- No themes or CSS tinkering for 30 days.  
- One index note only.  
- One inbox only (00 Inbox, cleared weekly).  
- No new plugins beyond the approved list.  

---

That’s the **full boot camp course** — six modules, ~90 minutes, end-to-end. Nothing hanging.  

---

Do you want me to spin this into a **checklist version** (bullet-only, one pager you can tick off as you set ZORA up), or keep it as a reference outline?

---

**User:**

I don’t need a checklist as I’ll be running it in chat, unless you need such a thing to track my progress…

---

**Assistant:**

Perfect — no checklist needed on your end if you’re running the boot camp live in chat. I don’t need one to track you either; I can just keep us aligned module by module.  

So the course now lives as:  
- **Reference outline** (what I gave you).  
- You call a module (“Start Module 1”) and I’ll walk you through micro-steps and keystrokes in real time.  

That way, no extra overhead, no redundant artifacts — just execution inside this thread.  

Would you like me to prep the **“guided mode” script** (basically, bite-sized instructions for each module, so you can say “Next” and I’ll feed you the exact steps)? Or do you want to stay with the higher-level outline and dip in/out as needed?

---

**User:**

Let’s  go with the guide approach on the first run through. I’m not ready to start yet, but when I return, I’ll ask you to start the course. 

---

**Assistant:**

Got it. When you’re ready and say “Start the course” (or “Start Module 1”), I’ll switch into **guided mode**: small, actionable steps you can follow in ZORA one at a time, with you just saying “Next” to proceed.  

No prep work required — I’ll keep the outline in mind and pace it so you end the run-through with a working, minimal Obsidian setup.  

When you come back, just tell me to kick it off.

---

**User:**

start

---

**Assistant:**

Alright — let’s fire up **ZORA Boot Camp, Guided Mode**.  
We’ll move in small steps; you can just reply with **“Next”** when you’re ready to advance.  

---

## Module 1 — Pre-flight & Mindset  

**Step 1. Enable core plugins**  
Open Obsidian → Settings → Core plugins. Make sure these are toggled ON:  
- File Explorer  
- Search  
- Backlinks  
- Quick Switcher  
- Command Palette  
- Outline  

(Don’t enable anything else right now.)  

👉 Do this first, then let me know when you’re ready for Step 2.

---

**User:**

is there any config to do with these?

---

**Assistant:**

Good question — **no heavy config needed** on these. They’re basically “on/off switches.”  

The only quick tweaks worth doing up front:  

- **Quick Switcher** → in Settings you can check “Show more context” if you want snippets of the file around your search result. Most people leave defaults.  
- **Command Palette** → you can pin frequently used commands later, but don’t bother now.  
- **Backlinks** → decide if you want backlinks in the right sidebar (default) or a separate pane. Again, default is fine.  

Everything else works great out of the box. The goal here is *muscle memory*, not fiddling.  

👉 If you’ve confirmed those plugins are on (defaults are fine), say **“Next”** and I’ll move you to the community plugins setup.

---

**User:**

next

---

**Assistant:**

Great — onto **Step 2: Community plugins (the essentials only).**  

Open **Settings → Community plugins → Turn on “Safe mode” OFF → Browse.**  
Install and enable only these:  

1. **Templater** – already in your setup (for templates and your flatten-to-clipboard macro).  
2. **QuickAdd** – one keystroke to create new scenes/characters/settings with templates.  
3. **Dataview** – lets you build dashboards (read-only mode; no JavaScript yet).  
4. **Outliner** – better handling of bullet lists (tab/shift-tab, move bullets easily).  
5. **Linter** – cleans up notes, but only when you ask (we’ll disable auto-lint).  
6. **Obsidian Git** – invisible version control; automatic commits and history.  

⚠️ Guardrail: **stop here.** Don’t add others (no themes, no Daily Notes, no extra toys).  

👉 Once these six are installed and enabled, say **“Next”** and we’ll shape your vault folders.

---

**User:**

hotkeys for templates is already added

---

**Assistant:**

Perfect — that saves us a step later. 👍  

---

## Module 2 — Vault Shape  

**Step 3. Create your folder skeleton.**  
In your vault, create these top-level folders:  

- 00 Inbox (fleeting captures; clear weekly)  
- 10 Projects (multi-scene arcs if needed)  
- 20 Areas  
   • Characters  
   • Settings  
- 30 Resources (research, reference)  
- 40 Archive (closed material)  
- 90 Writing (all scene notes go here)  
- 99 Templates (your Templater templates live here)  

That’s your permanent spine. Every note you make will live in one of these lanes.  

👉 Build that folder structure, then let me know with **“Next.”**

---

**User:**

enable these plugins or leave them disabled?

---

**Assistant:**

Enable them right away. Each one has a role in the boot camp flow, and it’s easier if they’re active from the start:  

- **Templater** → enabled (already hotkeyed).  
- **QuickAdd** → enable now; we’ll configure macros soon.  
- **Dataview** → enable now; needed for the dashboard later.  
- **Outliner** → enable now; gives you proper bullet handling immediately.  
- **Linter** → enable now, but we’ll turn off “lint on save” in settings later.  
- **Obsidian Git** → enable now; we’ll configure auto-commit/push in Module 6.  

No further config yet — defaults are fine until we reach each plugin’s setup step.  

👉 If all six are enabled, go ahead and set up the folder skeleton from Module 2. Then reply **“Next.”**

---

**User:**

next

---

**Assistant:**

Nice — folders in place, good foundation.  

---

## Module 3 — Templates via Templater  

**Step 4. Add your base templates into `99 Templates`.**  
We’ll keep it lean: Scene, Character, Setting. These give structure without overkill.  

**Scene Template (file: `Scene.md` in 99 Templates):**  
Frontmatter: type, status, series, POV, wordcount, related  
Body: title, beat, conflict, change, Draft 1 section  

**Character Template (file: `Character.md`):**  
Frontmatter: type, aka, role, status, tags  
Body: hook, desire/fear, strengths/flaws, ties  

**Setting Template (file: `Setting.md`):**  
Frontmatter: type, region, vibe, status, tags  
Body: sensory anchors (smell, sound, light), notables  

Since your Templater hotkey is already set, all you need to do is drop these three templates in `99 Templates`.  

👉 Once you’ve added them, say **“Next”** and we’ll wire up QuickAdd so you can spawn new notes with a keystroke.

---

**User:**

is there a reason to start folders with numbers?

---

**Assistant:**

Yep — it’s a **sorting trick, not a doctrine.**  

Obsidian’s File Explorer sorts folders alphabetically. If you prefix them with numbers, your lanes always appear in the same predictable order — Inbox on top, Templates on bottom — no matter what else you add later.  

Benefits:  
- Keeps your **spine folders together and ordered**.  
- Reduces “where did it go?” scanning, especially when you’re moving fast.  
- Makes it easy to distinguish system folders (00, 90, 99) from ad hoc ones you might create.  

Without numbers, Obsidian will list alphabetically: Archive above Areas, Resources between Random Research and Writing, etc. Not broken, but more cognitive friction.  

👉 Short version: the numbers aren’t required, but they’re cheap insurance against folder sprawl.  

Do you want to keep the numbers for clarity, or drop them and go purely alphabetical?

---

**User:**

i'll keep the numbers. just wanted to know why

---

**Assistant:**

Good call — they’re purely an **ordering hack**, not magical metadata. You can always rename later if you change your mind.  

Alright, with the folder skeleton clear, we’re set.  

👉 Next step is wiring **QuickAdd macros** so you can spin up new Scenes, Characters, and Settings in the right folders with the right template — one keystroke, no friction.  

Ready to move on?

---

**User:**

under 20 Areas, you have Charaters and settings.. create these folders or are they just examples?

---

**Assistant:**

Those are **real subfolders** you should create.  

Reasoning:  
- Keeps your **Characters** and **Settings** organized under the “Areas” lane (ongoing references, not one-off projects).  
- Keeps `90 Writing` clean so it only holds **scenes/drafts**, not support material.  
- Later, Dataview queries can target `"20 Areas/Characters"` or `"20 Areas/Settings"` cleanly.  

So your structure should literally look like:  

- 20 Areas  
  • Characters  
  • Settings  

👉 Go ahead and make those two subfolders. Once done, we’ll move on to QuickAdd.

---

**User:**

still in module 3.. can you give me the code for those three templates? just so I understand frontmatter in obsidian's context

---

**Assistant:**

Perfect place to pause and dig in — frontmatter is just a **YAML block** at the very top of a note, between triple dashes (`---`). Obsidian (and plugins like Dataview) read those fields as structured data. Everything below the frontmatter is “normal” note text.  

Here are the three templates in full, written exactly as you’d drop them into `99 Templates`.  

---

**Scene.md**  

```
---
type: scene
status: draft          # draft | revise | final
series: 
pov: 
wordcount: 
related: 
---

# <% tp.file.title %>

**Beat:**  
**Conflict:**  
**Change:**  

## Draft 1
<% tp.cursor() %>
```

---

**Character.md**  

```
---
type: character
aka: 
role: 
status: active
tags: [char]
---

# <% tp.file.title %>

**Hook:**  
**Desire / Fear:**  
**Strength / Flaw:**  
**Ties:** [[ ]]

Notes:  
- 
```

---

**Setting.md**  

```
---
type: setting
region: 
vibe: 
status: active
tags: [place]
---

# <% tp.file.title %>

**Sensory anchors:**  
- Smell:  
- Sound:  
- Light:  

**Notables:**  
- 
```

---

**What’s happening here:**  
- `--- … ---` at the top = YAML frontmatter. Plugins like Dataview can query these fields (e.g. `WHERE type = "scene"`).  
- `<% tp.file.title %>` = Templater snippet; auto-inserts the filename as the note’s H1 title.  
- `<% tp.cursor() %>` = where your cursor lands when the template loads.  

👉 Once you’ve saved these three into `99 Templates`, you’re fully equipped for QuickAdd macros.  

Want me to walk you through wiring QuickAdd so you can spawn a Scene/Character/Setting in the right folder with these templates?

---

**User:**

so.. when createing scene.md.. just create a new note.. title it scene.md and paste as plain text?

---

**Assistant:**

Exactly 👍  

Here’s the clean way to do it in ZORA:  

1. In your `99 Templates` folder, create a new note.  
2. Name it `Scene` (Obsidian will save it as `Scene.md` automatically — you don’t need to type the `.md`).  
3. Paste the plain text I gave you (including the triple dashes for frontmatter).  
4. Do the same for `Character` and `Setting`.  

When you use Templater or QuickAdd later, these files are just “source blueprints.” Obsidian copies their content into a brand-new note in the right folder, swapping in `<% tp.file.title %>` for whatever you name the new note.  

👉 Once those three are in place under `99 Templates`, you’re ready for Module 4 (QuickAdd wiring). Want me to walk you through that next?

---

**User:**

okay caught up in module 3.. next

---

**Assistant:**

Great—moving on.

## Module 4 — QuickAdd wiring (one-keystroke new notes)

**Goal:** Create Scene/Character/Setting notes in the right folders, with your Templater templates, in one move.

**Step 4.1 — Point QuickAdd at Templater**
- Open Settings → Community plugins → QuickAdd.
- Turn on “Use Templater to replace templates” (wording may be “Template engine: Templater”).

**Step 4.2 — Create a QuickAdd “choice” for New Scene**
- QuickAdd → “Manage choices” → Add Choice → Type: Capture.
- Name: New Scene.
- Capture to: File.
- File name: `{{VALUE}}`
- Folder: `90 Writing`
- Template file: `99 Templates/Scene`
- Options: check “Open” (open after creation). Optional: “Create folder(s) if they don’t exist,” “Increment file name if it exists.”

**Step 4.3 — Create choices for New Character and New Setting**
- Repeat Step 4.2 twice:
  - New Character → Folder: `20 Areas/Characters` → Template: `99 Templates/Character`
  - New Setting → Folder: `20 Areas/Settings` → Template: `99 Templates/Setting`

**Step 4.4 — Bind hotkeys**
- Settings → Hotkeys → search “QuickAdd:”
  - Bind New Scene to something fast (e.g., Cmd+Shift+S).
  - Bind New Character (e.g., Cmd+Shift+C).
  - Bind New Setting (e.g., Cmd+Shift+E).

**Smoke test (30 seconds)**
- Trigger “New Scene,” type a title, hit Enter. You should land in `90 Writing/<Your Title>.md` with the Scene template populated and the cursor in Draft 1.
- Do the same for Character and Setting.

If all three work, QuickAdd is done and you’re ready to draft without friction.

Reply **“Next”** when you’re set, and we’ll do Module 5 (core moves + a tiny drill with your ChatGPT handoff).

---

**User:**

hmm.. doesn't ask about my template engine

---

**Assistant:**

Right — QuickAdd changed its UI a bit. Some builds don’t explicitly ask “Template engine,” they just assume **Templater** if you have it installed.  

Here’s how to check:  

1. In **QuickAdd settings → Choices → (pick your choice, e.g. New Scene)**.  
2. Look for a field called “Template path” or “Template file.”  
   - Point that at `99 Templates/Scene`.  
3. If you see a toggle for “Use Templater,” enable it.  
   - If not, don’t worry — QuickAdd will still pass the template through Templater automatically if it detects Templater.  

👉 Short version: as long as QuickAdd is grabbing your template note (Scene/Character/Setting) and the `<% … %>` snippets (like `tp.file.title`) resolve properly, you’re good.  

Do you want me to walk you through creating one **New Scene** choice step by step so we can confirm it’s behaving?

---

**User:**

hmmm.. thinking about the Longform plugin and that its compile feature can strip out frontmatter... my copy script does this so I can paste it in an llm... however, I could leave all the scene brief and meta data in the scene front matter in longform and copy all the frontmatter into the llm prompt ...

---

**Assistant:**

Ah, I see exactly what you’re thinking — this is about **how much context to hand off to the LLM** versus keeping it internal in Obsidian. Let’s break it down:  

---

### 1. Keep frontmatter separate
- **Pros:**  
  - Scene metadata (status, POV, wordcount, related notes) stays in ZORA.  
  - Your flatten-to-clipboard macro can strip out everything except the note body when sending to ChatGPT.  
  - Keeps the LLM prompt clean, focusing only on narrative content.  
- **Cons:**  
  - LLM doesn’t see your metadata unless you explicitly copy it.  

---

### 2. Include frontmatter in the LLM prompt
- **Pros:**  
  - Gives the LLM full context: scene status, POV, beats, characters, related notes.  
  - Can be useful if you want the AI to respect constraints or make informed revisions.  
- **Cons:**  
  - Adds clutter; might bloat prompts.  
  - Could confuse the model if the frontmatter uses shorthand it doesn’t understand.  

---

### 3. Hybrid approach
- Leave all meta in the scene note frontmatter.  
- When sending to the LLM:  
  - Copy full frontmatter + body.  
  - Optionally prepend a one-line “context summary” to orient the AI, e.g., “Scene POV: Alice, Draft status: 1, Wordcount: 243.”  
- Your flatten script can optionally **strip or preserve frontmatter** based on a hotkey or command — so you have flexibility per session.  

---

**Bottom line:**  
Since ZORA is your **writing workbench**, there’s no harm leaving metadata in the frontmatter. You can always decide on a per-scene basis whether the LLM needs it. The Longform plugin compile feature doesn’t force you to strip it — your Templater copy script already handles this elegantly.  

If you want, I can sketch a **minimal LLM-friendly workflow** that integrates scene frontmatter, the flatten script, and a “copy for AI” command — so you don’t have to think about it while writing.  

Do you want me to do that?

---

**User:**

maybe I need a second version of my flatten_to_clip.js script that would leave the front matter in place? I could call one or the other as my needs dictate

---

**Assistant:**

Exactly — that’s the cleanest approach. You basically have **two “flatten” scripts**:  

1. **Flatten for LLM (current)**  
   - Strips YAML frontmatter.  
   - Only pastes the body text.  
   - Ideal for when you want the AI to focus purely on narrative.  

2. **Flatten with frontmatter (new)**  
   - Leaves the YAML intact.  
   - Body follows as usual.  
   - Ideal when you want the AI to see scene metadata: POV, status, beats, related notes, wordcount.  

---

### Implementation suggestions:
- Name the scripts clearly: `flatten_to_clip.js` and `flatten_to_clip_with_meta.js`.  
- Keep both in the same folder, with the same interface (takes the current note, outputs clipboard).  
- Optional: add a **hotkey or Templater command** for each, so you can choose at the moment.  
- Both scripts can still call your existing **paste-to-ChatGPT workflow**; just toggle which flatten you run.  

This gives you **flexibility without touching notes**, and you’re not losing any metadata.  

If you want, I can sketch a **tiny skeleton for the second version** so it’s ready to drop in. Do you want me to do that?

---

**User:**

it's basically the existing script with the call to strip front matter changed... eg: 

  const src = stripFrontmatter(content);

becomes: 

const src = content;

that do the trick?

---

**Assistant:**

Exactly — that’s all you need.  

Current script:  

```js
const src = stripFrontmatter(content);
```

New “with frontmatter” version:  

```js
const src = content;
```

Everything else can stay identical — clipboard copy, line breaks, flattening of links, etc.  

✅ That will leave all the YAML intact while keeping the body in the same format, so your LLM sees the full scene context.  

You can safely call one or the other depending on whether you want metadata included.  

If you want, we can integrate this into a **Templater/QuickAdd command** so the choice of flatten version is just a hotkey away. Do you want me to do that?

---

**User:**

for the flatten_to_fm.js script..... if I put internal links in the frontmatter, would it expand?

---

**Assistant:**

No — **YAML frontmatter is treated as plain text** by Obsidian and by most scripts. Internal links (`[[Note Name]]`) inside the frontmatter will **not automatically expand** or resolve into note content when you flatten or copy. They’ll stay as literal `[[Note Name]]` strings.  

Here’s what that means for your flatten script:  

- `const src = content;` will copy **everything**, including frontmatter.  
- Any `[[links]]` in the frontmatter remain links — they won’t pull in the linked note’s text.  
- Only links in the **body of the note** can be resolved and flattened if your script explicitly handles that.  

If you wanted frontmatter links to expand, the script would need an extra step: parse YAML, detect `[[ ]]` links, and recursively replace them with the target note content. That’s doable, but adds complexity and potential performance issues.  

💡 My take for your workflow: **keep links in frontmatter for reference**, and only flatten linked content from the note body. That way, LLM prompts get context but you avoid pulling in huge amounts of text unintentionally.  

Do you want me to sketch how a frontmatter-expanding version could work, or just leave them literal?

---

**User:**

ok.. so it's not _quite_ as useful as I thought

---

**Assistant:**

Right — it’s useful for giving the AI structured context (POV, status, tags, etc.), but **any internal links in frontmatter won’t automatically expand**.  

So the LLM sees “`[[Alice]]`” or “`[[Forest Clearing]]`,” not the full note content. It’s still valuable for reference or constraints, but not for giving the AI the linked text itself.  

For full expansion, you’d need an extra script pass to traverse links, which is doable but heavier and probably overkill for most scenes.  

For your workflow, leaving metadata in frontmatter is still the **lightweight win**, and you can rely on body flattening for any actual content you want the AI to process.  

If you want, we can sketch a **pragmatic way to include selected linked note content** in the prompt without fully automating a recursive expansion. That usually hits the sweet spot for writing workflows. Do you want me to do that?

---

**User:**

the only place where front matter _might_ make sense would be in the draft of the scene itself... maybe

---

**Assistant:**

Exactly — that’s the sweet spot if you want to experiment.  

- **Scene draft frontmatter** could hold:  
  - Draft status (1, 2, final)  
  - POV, wordcount, beat  
  - Optional tags/metadata useful for the AI (like “key character: Alice”)  

- Keep **all other notes** (Characters, Settings, Research) free of frontmatter for flattening purposes. Just leave their info in the body or as links — simpler, less friction.  

This way:  
- Your flatten-to-clipboard script can optionally include frontmatter **only when needed** for the scene draft.  
- Everything else is lean, so AI prompts stay focused.  

If you want, we can define a **minimal frontmatter schema** for scene drafts that gives maximum value to the AI without adding clutter. Do you want me to do that?

---

**User:**

ok.. I thought I might be able to combine the scene brief with the scene draft by putting the brief and its linked context in the frontmatter and then the written prose in the body...

doesn't sound like that makes sense..

maybe I'm just better off a proper scene brief note with linked context and keep the scene draft note clean

---

**Assistant:**

Exactly — that’s the cleaner, more practical approach.  

Trying to jam the brief, linked context, and the draft into **one note** with frontmatter quickly becomes messy:  

- YAML frontmatter isn’t meant for large text or recursive links.  
- LLM-friendly flattening gets complicated if you want linked notes expanded.  
- Editing the draft inside a big frontmatter block is awkward.  

Better workflow:  

1. **Scene Brief note**  
   - Holds beats, conflict, change, and links to characters, settings, research.  
   - All structured metadata, easy to query with Dataview.  
2. **Scene Draft note**  
   - Pure prose.  
   - Templater flatten-to-clipboard script handles this cleanly.  
   - Keep optional frontmatter minimal (status, POV, maybe draft #).  

This keeps your **writing workbench modular**: briefs drive context, drafts are for the actual text, and flattening scripts stay simple and predictable.  

If you want, we can sketch the **linking convention between briefs and drafts** so you always know which draft belongs to which brief, and can hand off to ChatGPT cleanly. Do you want me to do that?

---

**User:**

I think that'll be handled by longform.. I'll know by the scene titile/number where it belongs in the outline

---

**Assistant:**

Perfect — that keeps it simple and reliable.  

With Longform handling the compile/linking, you don’t need to jam context into the draft itself. Scene title/number as the anchor is enough to:  

- Keep drafts tied to their briefs in your outline.  
- Let your flatten-to-clipboard script stay lean.  
- Avoid confusion with frontmatter-heavy notes.  

We can move forward with the boot camp workflow without worrying about combining brief + draft into a single note.  

Ready to pick up **Module 5: Core Moves and the ChatGPT handoff drill**?

---
