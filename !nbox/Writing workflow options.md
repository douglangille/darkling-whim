# Writing workflow options

## PROMPT 1

Okay.. let's talk about plaintext, portable formats, and obsidian. I've been tooling around with plaintext formats for yeas-- especially markdown. To the point where it's my go to writing format. 

As an aside, I'm totally fine with using Apple Notes as my Forever Notes-style planner-- the persistence of the data is somewhat temporal and ephemeral. That is, 5 years from now, my weekly plan this week will have no significant value.  Which is kinda funny since the frame work is Forever Notes.. Anywho..

I'm not a big collector of notes and documents to the point where it's mostly a haphazard collection of documents that I create once and never open again. I'm fine with this as it's just acknowledging the lie everyone tells themselves about PKM.

However, my creative writing is something I care about keeping around. Probably the only thing that has a long tail for me. 

Here's the challenge. I absolutely do not want to lock it into a proprietary format. Something that may last 20 years or more needs to be portable. Markdown is easily that thing. I get that.

We spent some time tooling around with Obsidian and some plugins to try to cobble together an AI-partnered writing studio. I'm totally not using it. I've written several blog posts and essays using ChatGPT and canvas to iterate these pieces. Managing log-form fiction is something I'm feeling friction about as managing the multiple artifacts is, well, friction-y. 

My spider sense says that Obsidian _migt_) not be checking the right boxes give that I don't seem to be using it. It could be seasonal business, but it may be something else. 

Here's the task for you. Think hard about what we've talked about and about patterns you may see across my chat history. CHarGPT is definitely quite reflective of my current work habits.

Identify gaps in your understanding of the pitch and ask me smart one-at-a time questions building upon my responses. Your goal is to help me figure out a real plan going forward to manage my writing. Whether it's just saying fuck it and using a proprietary framework, make Obsidian work, or go filesystem native with folders and markdown and use a tool like VS code.  Or maybe there's something out there I'm not thinking about.

## RESPONSE 1

You need a Markdown-first, tool-agnostic workflow for long-form fiction that minimizes friction now and remains portable for 20+ years.

What’s solid (portable core)
============================

*   **Plain text endures.** Library of Congress treats openly documented, widely adopted formats as most sustainable; plain text/Markdown fits that bill. [The Library of Congress](https://www.loc.gov/preservation/digital/formats/?utm_source=chatgpt.com)
    
*   **Pandoc is your escape hatch.** It reliably compiles Markdown to DOCX/EPUB/PDF/HTML, so you can keep drafting in .md and still hit any delivery format. [pandoc.org](https://pandoc.org/MANUAL.html?utm_source=chatgpt.com)
    
*   **Obsidian isn’t lock-in by itself.** Vaults are just local Markdown files; you can drop Obsidian any time. (Plugins may add overhead, but your text remains portable.) [Obsidian Help](https://help.obsidian.md/import?utm_source=chatgpt.com)
    

Viable stacks (from least to most scaffolding)
==============================================

*   **Filesystem + VS Code** — Folders + `.md` + Git; add “Markdown All in One” for TOCs, shortcuts, preview, and word count. Low friction; zero lock-in. [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one&utm_source=chatgpt.com)
    
*   **Obsidian (lite)** — Treat it as a viewer/organizer over the same folders; keep plugins minimal so it stays invisible when you don’t need it. (Still plain text.) [Obsidian Help](https://help.obsidian.md/import?utm_source=chatgpt.com)
    
*   **novelWriter (open source)** — Purpose-built for novels with scene/metadata structure, stored as human-readable text files. Good if you want scene cards without a proprietary container. [novelwriter.io+1](https://novelwriter.io/?utm_source=chatgpt.com)
    
*   **Scrivener as a front-end, not a vault** — Use its planning/compile power, but routinely **compile to Markdown** so your canonical text stays outside the project file. [Literature & Latte Forums+1](https://forum.literatureandlatte.com/t/seriously-compiling-exporting-to-markdown/122678?utm_source=chatgpt.com)
    
*   **Specialized formats when needed** — If you shift to scripts, write in **Fountain** (plain text screenplay syntax) and compile later. [fountain.io+1](https://fountain.io/?utm_source=chatgpt.com)
    
*   **Apple Notes for ephemeral planning** — Now supports **per-note export to Markdown/PDF**, which aligns with your “Notes = not forever” stance; bulk export is still clunky. [Apple Support+2Apple Support+2](https://support.apple.com/guide/notes/import-export-and-print-notes-not201900c07/mac?utm_source=chatgpt.com)
    

My read on your friction
========================

*   You don’t want to babysit plugins or a knowledge-garden; you want **scene-level structure** and a **clean compile path**.
    
*   ChatGPT + Canvas works for ideation, but **multi-artifact management** (acts/chapters/notes/research) gets messy; you need **one canonical on-disk spine** with simple folders.
    

Gaps to close (so we pick the right stack)
==========================================

*   **Outputs you actually need** in the next 6–12 months (DOCX to editor, EPUB, print-PDF, web).
    
*   **Mobile drafting** importance (iPhone/iPad vs Mac-only).
    
*   **Outlining depth** (barebones folders vs scene cards/metadata).
    
*   **Collaboration/review** (track changes in DOCX? comments in Git? none?).
    
*   **Tolerance for ceremony** (are you okay with Git commits, or do we keep it invisible?).
    

First question (one at a time)
==============================

Which outputs do you need to reliably produce in the next 6 months—pick all that apply, then rank them: **DOCX for editors**, **EPUB**, **print-ready PDF**, **web/HTML/Markdown**, **screenplay**?

## PROMPT 2

Hmm.. I'm not sure how much I need to worry about output formats outside of markdown. To your point, pandoc is pretty much the gold standard, but I often find pasting into another editor just fine. That is, I can copy/paste into Reedsy to format an EPUB or into Word for a transportable format.  So compile to export formats is a "nice to have". Does that get at your question?

## RESPONSE 2

You’re saying export/compile is a nice-to-have; the non-negotiable is **Markdown-native files** and you’re fine pasting into Word or Reedsy when needed.

Implications
============

*   **De-prioritize a build chain.** Keep drafting in `.md`; when you need layout, paste into **Reedsy Book Editor** (clean EPUB/print-PDF export) or Word. [Reedsy+1](https://reedsy.com/studio/format-a-book?utm_source=chatgpt.com)
    
*   **Keep an “escape hatch,” not a dependency.** Have **Pandoc** installed for the rare case you want direct `.md → docx/epub/pdf`, but don’t wire it into daily flow. [pandoc.org+1](https://pandoc.org/?utm_source=chatgpt.com)
    
*   **Optional viewer.** If you keep Obsidian around, treat it purely as a viewer/organizer over your folder of Markdown (no lock-in; vault = plain-text files). [help.obsidian.md](https://help.obsidian.md/data-storage?utm_source=chatgpt.com)
    

One next question
=================

Do you actively draft long-form on **iPad/iPhone**, or is writing effectively **Mac-only**?

## PROMPT 3

I typically draft at a physical keyboard, so MacBook. I do a tone of ideation and planning work from Both the iPad and iPhone. These days, that's almost entirely within ChatGPT. When I get to the point of actual drafting, it's on a laptop. That's been the pattern in recent years. Not that I won't draft on mobile.. Back in the Blackberry days when there was a physical keyboard, I'd tap out drafts on it. The soft keyboard on the iPhone/iPad are unusable for long writing sessions. And if I were to add a keyboard to the iPad, I might as well just grab the macbook.

## RESPONSE 3

Your pattern points to a **filesystem-native Markdown project on the Mac, with Obsidian optional and zero required build chain**.

Implications for the stack
==========================

*   **Keep it plain:** A project folder of `.md` files (acts/chapters/scenes) is the canonical source; Obsidian can sit on top purely as a viewer/organizer because a “vault” is just a normal folder of Markdown. [Obsidian Help](https://help.obsidian.md/data-storage?utm_source=chatgpt.com)
    
*   **Draft in VS Code (lean):** Use built-in Markdown + the “Markdown All in One” extension for shortcuts/TOC/preview; no plugins beyond that. [Visual Studio Code+1](https://code.visualstudio.com/docs/languages/markdown?utm_source=chatgpt.com)
    
*   **Escape hatch only:** Keep **Pandoc** installed for rare one-off conversions from `.md` to DOCX/EPUB/PDF—don’t wire it into daily work. [pandoc.org+1](https://pandoc.org/?utm_source=chatgpt.com)
    
*   **(Optional) scene tool:** If you want scene cards without lock-in, **novelWriter** stores everything as plain text with a Markdown-like syntax; easy to drop in/out. [novelwriter.io+1](https://novelwriter.io/?utm_source=chatgpt.com)
    

Default skeleton (low-ceremony)
===============================

*   `/Project/00_Admin/` (logline, series bible, references)
    
*   `/Project/10_Draft/01_Act1/01_Scene01.md …` (numbered for natural sort)
    
*   `/Project/20_Notes/` (research/ideation dumps copied from ChatGPT when you want to keep them)
    
*   `/Project/_spine.md` (optional: a running synopsis or chapter list)
    

One next question
=================

How much **structure** do you actually want around chapters/scenes—pick one so I size the system right:

*   **Minimal:** just folders + numbered files.
    
*   **Light metadata:** short YAML at the top of each scene (POV, status, wordcount).
    
*   **Full cards:** a compact scene template (goal, conflict, outcome, notes) plus a one-page tracker.

## PROMPT 4

Because I'm using ChatGPT as a planning tool, I think I need different data components at the scene level: scene brief and relevant story bible stuff, and the actual scene itself.  An overall story bible is probably its own artifact. Make sense? Ideally, if I'm working with a scene, I'd like to be able to take it in and out of ChatGPT to work on as needed. There's probably a separate discussion to have around the mechanics of ChatGPT use for long-form or compound documenrs

## RESPONSE 4

You’re right to split each scene into **Brief + Bible refs + Scene text** and keep it all Markdown so you can copy/paste cleanly into ChatGPT.

Two portable “scene packet” options
===================================

**A) Single-file packets (simplest round-trip)**

*   One `.md` per scene with three sections you can lift into ChatGPT in one go.
    
*   Add tiny YAML “properties” at the top (status, POV, time), which Obsidian reads natively as front-matter/properties if you ever open the folder there. [Obsidian Help](https://help.obsidian.md/properties?utm_source=chatgpt.com)
    

```markdown
---
id: S12
title: The Broken Regulator
pov: Maggie
status: drafting
when: 2032-05-12 evening
location: Lunenburg workshop
---

# Scene Brief
- goal: Maggie tests the repaired clock; Richard arrives early
- conflict: the regulator drifts; trust wobbles
- outcome: Maggie hides the protest hardware; Richard senses it

# Bible Snippets
- Character: Maggie → watchmaker; activist “time drift” method; trust issues with Richard (see [[Bible/Characters/Maggie]])  
- Setting: Lunenburg workshop → smells of oil; bench layout (see [[Bible/Settings/Workshop]])

# Scene
[Write the scene here...]
```

**B) Twin-file cards (clean separation)**

*   `/cards/S12 - The Broken Regulator.brief.md` holds Brief + Bible refs.
    
*   `/scenes/S12 - The Broken Regulator.md` holds only prose.
    
*   When you want AI help, open the **brief**, copy it plus the current scene, or keep a temporary `/packets/S12.packet.md` you delete after.
    
*   If you do use Obsidian sometimes, the **Templates** core plugin can stamp the skeleton, and **Note Composer** can merge/extract without breaking links. [Obsidian Help+1](https://help.obsidian.md/plugins/templates?utm_source=chatgpt.com)
    

Folder skeleton (tool-agnostic)
===============================

```
/ProjectName/
  _spine.md                  # chapter/scene list
  /cards/                    # scene briefs (and Bible refs)
  /scenes/                   # prose
  /Bible/Characters/…        # character notes
  /Bible/Settings/…          # locations
  /Assets/                   # images/audio (attachments stay as normal files)
```

*   Attachments remain regular files on disk (portable; Obsidian treats them that way too if you ever browse here). [Obsidian Help](https://help.obsidian.md/attachments?utm_source=chatgpt.com)
    

Optional niceties (still plain text)
====================================

*   **Light YAML only** (POV, status, when). Keeps search/tagging useful in any editor; Obsidian will surface these as “properties” if you open the folder there. [Obsidian Help](https://help.obsidian.md/properties?utm_source=chatgpt.com)
    
*   **VS Code + Markdown All in One** for fast headings, lists, TOC, word count—no other extensions needed. [marketplace.visualstudio.com+1](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one&utm_source=chatgpt.com)
    
*   **Bundling assets later?** If you ever need to ship a scene + images to another app, the open **TextBundle** spec wraps Markdown + media in one portable package; you don’t need it now, but it’s a future-proof escape hatch. [textbundle.org+1](https://textbundle.org/spec/?utm_source=chatgpt.com)
    

One question (to lock the pattern)
==================================

Do you want **A) single-file packets** or **B) twin-file cards + scene**, given your “copy into ChatGPT, draft on Mac” workflow?

## PROMPT 5

Hmm.. there's something here I think. YAML front matter can be annoying to manage, but it can separate actual prose from the meta data.. eg, there is a version of Option A, that has the actual scene brief and relevant bible snippets in the frontmatter as properties and leaving the body of the document as just the prose. That _might_ make compilation of the novel (if that's what I'm writing) easier while preserving the front matter for when chatgpt sees the doc.

## RESPONSE 5

Your idea works: keep **scene brief + bible snippets in YAML front matter** (using block scalars) and **leave the body as prose**—portable now, future-proof, and friendly to occasional Pandoc runs. [Obsidian Help+2yaml.org+2](https://help.obsidian.md/properties?utm_source=chatgpt.com)

Why this is a good fit
======================

*   **Tool-agnostic & Obsidian-friendly.** Obsidian stores “Properties” as YAML at the top of the note, so your metadata lives where Obsidian (and many other tools) already expect it. [Obsidian Help](https://help.obsidian.md/properties?utm_source=chatgpt.com)
    
*   **Clean separation.** YAML front matter is parsed as metadata; the **prose body stands alone**, which is ideal for copy/pasting into ChatGPT or other editors. Pandoc reads YAML metadata blocks and treats them as variables rather than body text. [pandoc.org+1](https://pandoc.org/demo/example33/8.10-metadata-blocks.html?utm_source=chatgpt.com)
    
*   **Multiline snippets are safe.** YAML supports **block scalars** (`|` literal, `>` folded) for multi-paragraph briefs and bible excerpts—no weird escaping. [yaml.org+1](https://yaml.org/spec/1.2.2/?utm_source=chatgpt.com)
    

Practical scene template (Option A′)
====================================

```markdown
---
id: S12
title: The Broken Regulator
chapter: 7
order: 120         # for quick sorting/compiles
pov: Maggie
when: 2032-05-12 evening
location: Lunenburg workshop
status: drafting

brief: |
  Goal: Maggie tests the repaired clock; Richard arrives early.
  Conflict: the regulator drifts; trust wobbles.
  Outcome: Maggie hides the protest hardware; Richard senses it.

bible_snippets: |
  - Maggie: watchmaker; “time drift” activism; distrusts authority.
  - Workshop: oil/metal smell; bench layout; hidden compartment.
  - Richard: RCMP consultant; pattern-spotter; wary but empathetic.

refs:
  characters: ["[[Bible/Characters/Maggie]]","[[Bible/Characters/Richard]]"]
  setting: ["[[Bible/Settings/Workshop]]"]
tags: [draft, act2]
---

[Write the scene prose here; no headings needed.]
```

**Notes**

*   Use `|` (literal) for `brief` and `bible_snippets` to preserve newlines; use `>` (folded) if you prefer wrapped paragraphs. [yaml.org](https://yaml.org/spec/1.2.2/?utm_source=chatgpt.com)
    
*   Keep front matter **only to what you’ll actually search/sort**; everything else belongs in the Bible docs those `[[refs]]` point to.
    

Optional compile (body-only) when you need a single manuscript
==============================================================

Pandoc only interprets the **first** file’s YAML as metadata; later files’ `---` won’t be treated as metadata. So if you compile multiple scene files, strip YAML before piping to Pandoc (simple one-liner or a tiny script) and you’ll get **just the prose** in order. [pandoc.org](https://pandoc.org/demo/example33/8.10-metadata-blocks.html?utm_source=chatgpt.com)

*   After stripping front matter, `pandoc scenes/*.md -o Draft.docx` will produce a clean DOCX/EPUB/etc., with YAML ignored as intended. (Pandoc reads metadata, but doesn’t print it by default unless your template asks it to.) [pandoc.org](https://pandoc.org/MANUAL.html?utm_source=chatgpt.com)
    

Smooth round-tripping with ChatGPT
==================================

*   Copy the **whole file** when you want context; the YAML brief/bible at the top acts as a compact prompt, the body is your working text.
    
*   If you ever split or merge notes, Obsidian’s **Note Composer** core plugin can merge/extract without breaking links—handy if you move from scene → chapter, or vice versa. [Obsidian Help](https://help.obsidian.md/plugins/note-composer?utm_source=chatgpt.com)
    

One question
============

Do you want the **bible material in YAML** to be (a) short excerpts (as in `bible_snippets` above) or (b) just **links** in `refs` with the full bible kept in separate files?

## PROMPT 6

I think this is about the workflow.. For example, maybe I'm working in ChatGPT in a Project or a single chat conversation (pros and cons to either) and add the story bible as a file attachment to either the project or chat as a soft-RAG resource, then the YAML entries for each scene can be either (a) or (b). I think (a) might be more human readable and easier to maintain. (B) would be fine, but I'd have to do some link-expansion shortcut voodoo in Obsidian. It _feels_ like (a) is slightly more tool agnostic.

## RESPONSE 6

Keep everything in plain-text Markdown with **single-file scenes**: prose in the body, and a compact scene brief + bible snippets in YAML front matter, with your story bible attached to your ChatGPT Project for context.

Workflow (low-friction, portable)
=================================

*   **Storage & structure**
    
    *   One folder per project; all scenes are `.md` files.
        
    *   Each scene file = **YAML front matter** (brief, bible\_snippets, pov, when, status) + **body = only prose**. Obsidian treats the YAML as Properties and leaves your prose untouched. [Obsidian Help](https://help.obsidian.md/properties?utm_source=chatgpt.com)
        
    *   Optional numbering (`order: 120`) lets you sort/compile without fiddling with filenames.
        
*   **Round-tripping with ChatGPT**
    
    *   Create a **Project** for the book; **add your story-bible file(s)** to the Project so you can reference them while you paste a scene in to work. Projects are designed to hold chats + files together; you can share individual chats when needed. [OpenAI Help Center](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt?utm_source=chatgpt.com)
        
    *   You can also **upload files into a chat** (or from connected cloud apps) when you want ad-hoc context. [OpenAI Help Center+1](https://help.openai.com/en/articles/8555545-file-uploads-faq?utm_source=chatgpt.com)
        
*   **Why YAML-in-front works**
    
    *   YAML **block scalars** (`|` or `>`) keep multi-paragraph briefs and excerpted bible notes readable. [yaml.org+1](https://yaml.org/spec/1.2.2/?utm_source=chatgpt.com)
        
    *   If you ever compile a manuscript, **Pandoc** reads metadata blocks and ignores printing them unless a template calls for it; you can also strip YAML before concatenation for body-only output. [Pandoc+1](https://pandoc.org/MANUAL.html?utm_source=chatgpt.com)
        
*   **Editing tools (optional, not required)**
    
    *   **VS Code + “Markdown All in One.”** Fast headings, TOC, lists, preview—zero lock-in. [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one&utm_source=chatgpt.com)
        
    *   **Obsidian (lite).** Use it purely as a viewer/organizer; **Note Composer** can merge/split notes without breaking links when you refactor scenes/chapters. [Obsidian Help](https://help.obsidian.md/plugins/note-composer?utm_source=chatgpt.com)
        
*   **Export when you need it**
    
    *   Paste into **Reedsy Book Editor** for clean EPUB/print-PDF exports; keep Markdown as your source of truth. [Reedsy](https://reedsy.com/faq/studio-app/export-options?utm_source=chatgpt.com)
        
    *   Packaging Markdown + images later? **TextBundle** is an open container for exactly that; optional. [textbundle.org+1](https://textbundle.org/spec/?utm_source=chatgpt.com)
        

Scene template (Option A′, trimmed YAML + prose)
================================================

```markdown
---
id: S12
title: The Broken Regulator
order: 120
pov: Maggie
when: 2032-05-12 evening
location: Lunenburg workshop
status: drafting

brief: |
  Goal: Maggie tests the repaired clock; Richard arrives early.
  Conflict: the regulator drifts; trust wobbles.
  Outcome: Maggie hides the protest hardware; Richard senses it.

bible_snippets: |
  - Maggie: watchmaker; “time drift” activism; cautious trust with Richard.
  - Workshop: oil/metal smell; bench with hidden compartment.
  - Richard: RCMP consultant; pattern-spotter; empathetic but wary.
---

[Prose only, no headings.]
```

Tiny compile path (only when needed)
====================================

*   Keep a simple shell step to **strip YAML** and concatenate scenes in `order`, then run `pandoc` → DOCX/EPUB as required; or skip this and paste into Word/Reedsy. Pandoc supports YAML metadata blocks if you ever want to leverage them. [Pandoc](https://pandoc.org/MANUAL.html?utm_source=chatgpt.com)
    

One decision to unblock setup
=============================

Do you want your **story bible** as **one consolidated `Bible.md`** (simplest to attach to the Project) or as **modular files** (e.g., `Bible/Characters/*.md`, `Bible/Settings/*.md`) you attach as a small set? Pick one, and I’ll shape the exact folder tree and starter templates around it next.

## PROMPT 7

I like the order property for easy of sorting during compilation. In initial drafts, I can have each file increment by 10s so that if I need to insert a scene, I can easily do so.

My spider sense is that "it depends" on the project about if I'm using one story bible doc or several. Most of the time, It'll probably be one and I'd attach it to the chat thread (or project) as Im working on it. Regardless, the YAML references will pick up the details from the bible as needed. I hope anyway. :)

To that end, I'm think that regardless if the the bible is one file or several, I should just use a naming convention that puts an underscore at the front. Eg _characters.md or _bible.md or _scenelist.md. That way they'd groom together at the the top and I can exclue in a compile step.

Multiple folders makes my brain itch.

## RESPONSE 7

Single-folder, Markdown-only project with underscore-prefixed bible files and per-scene YAML (brief + bible\_snippets + order) gives you portability now and painless compile later.

Structure you’ll actually use
=============================

*   One folder per book; **no subfolders**.
    
*   Files:
    
    *   `_bible.md` (or `_characters.md`, `_settings.md`—whatever you need)
        
    *   `_scenelist.md` (quick table of scenes; optional)
        
    *   `S010 The Broken Regulator.md`, `S020 …` (use **order** in YAML; increment by 10 for insert-friendly sorting)
        
*   Why this works long-term
    
    *   **Markdown + plain text** stay portable; **Pandoc** is the “escape hatch” to DOCX/EPUB/PDF when you need it. [pandoc.org](https://pandoc.org/MANUAL.html?utm_source=chatgpt.com)
        
    *   **Obsidian reads YAML “Properties”** if/when you browse the folder there—no lock-in. [Obsidian Help](https://help.obsidian.md/properties?utm_source=chatgpt.com)
        
    *   **YAML block scalars** (`|` or `>`) let you keep multi-paragraph briefs/excerpts clean in front matter. [YAML](https://yaml.org/spec/1.2.2/?utm_source=chatgpt.com)
        

Scene file template (YAML up top, prose below)
==============================================

```markdown
---
id: S010
title: The Broken Regulator
order: 10         # 10-step increments for easy inserts
pov: Maggie
when: 2032-05-12 evening
location: Lunenburg workshop
status: drafting

brief: |
  Goal: Maggie tests the repaired clock; Richard arrives early.
  Conflict: the regulator drifts; trust wobbles.
  Outcome: Maggie hides protest hardware; Richard senses it.

bible_snippets: |
  - Maggie: watchmaker; “time drift” activism; cautious trust with Richard.
  - Workshop: oil/metal smell; hidden compartment under bench.
  - Richard: RCMP consultant; pattern-spotter; wary empathy.
---
[Prose only. No headings.]
```

*   Pandoc treats YAML as metadata (not printed) unless a template calls for it; great for keeping context out of the manuscript body. [pandoc.org](https://pandoc.org/demo/example33/8.10-metadata-blocks.html?utm_source=chatgpt.com)
    
*   If you ever need export/formatting, **paste into Reedsy** for EPUB/print-PDF; or run Pandoc directly. [Reedsy](https://reedsy.com/studio/format-a-book?utm_source=chatgpt.com)
    

Compile only when needed (body-only, sorted by `order`)
=======================================================

*   Keep underscore files out of output and stitch scenes by `order`. Save as `build.sh`:
    

```bash
#!/usr/bin/env bash
# Create _manuscript.md by sorting *.md (excluding _files) by YAML 'order' and stripping YAML.
ls -1 *.md | grep -v '^_' | while read f; do
  ord=$(awk '/^---/{y=1;next} /^---/{exit} y && /^order:/{print $2}' "$f")
  printf "%08d\t%s\n" "${ord:-99999999}" "$f"
done | sort -n | cut -f2 | while read f; do
  awk 'BEGIN{in=0} /^---$/{in=!in; next} !in' "$f"
  printf "\n\n"
done > _manuscript.md
# Optional: pandoc _manuscript.md -o Draft.docx   # or .epub / .pdf
```

*   Pandoc understands YAML metadata for EPUB/DOCX if you want it later. [Ubuntu Manpages](https://manpages.ubuntu.com/manpages/jammy/man1/pandoc.1.html?utm_source=chatgpt.com)
    

Optional “nice to have” (still portable)
========================================

*   **VS Code + Markdown All in One** for TOC, list editing, preview, counters—no ceremony. [marketplace.visualstudio.com+1](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one&utm_source=chatgpt.com)
    
*   If you ever need to ship **Markdown + images** as one file, **TextBundle** is an open container used by many editors. (You can ignore this until needed.) [TextBundle+1](https://textbundle.org/spec/?utm_source=chatgpt.com)
    

Your underscore convention
==========================

*   Perfect: `_bible.md`, `_scenelist.md`, etc. stay grouped at the top, easy to **exclude** in compile (see script), and remain plain Markdown.
    

One question (to lock the backup layer)
=======================================

Pick one for version history:  
**A)** Just iCloud/Time Machine snapshots (lowest ceremony), or **B)** lightweight Git (single branch, “savepoints” only, no PRs)?

## PROMPT 8

Hmm.. I'm not sure. I'm pretty comfortable with git, but I'd really like to make that a background automation if we use it.. eg.. auto-commit on save stuff. Maybe. I don't know. iCloud doesn't support versionin

## RESPONSE 8

Short version: use **Time Machine + VS Code’s Local History** for baseline safety, and add **background Git auto-commits** (not in iCloud) if you want off-site history with zero ceremony.

Why iCloud alone isn’t enough
=============================

*   iCloud Drive reliably lets you **recover deleted files for 30 days**, but it doesn’t provide general version history for arbitrary Markdown files (versions exist only for apps that implement Apple’s “Revert To,” like Pages/Preview). [Apple Support+3Apple Support+3Apple Support+3](https://support.apple.com/guide/icloud/recover-deleted-files-mmae56ea1ca5/icloud?utm_source=chatgpt.com)
    

Minimal-ceremony baseline (no Git)
==================================

*   **Time Machine**: automatic hourly/daily/weekly snapshots; set-and-forget. [Apple Support](https://support.apple.com/en-us/104984?utm_source=chatgpt.com)
    
*   **VS Code Local History / Timeline**: keeps per-file save history you can browse/restore—handy oops-button even without Git. [Visual Studio Code](https://code.visualstudio.com/docs/getstarted/userinterface?utm_source=chatgpt.com)
    
*   Pros: zero setup, zero friction. Cons: no off-site copy unless your TM disk is off-site; history is per-machine.
    

Background Git (when you want durable history + off-site)
=========================================================

*   **Don’t put the repo inside iCloud/Dropbox** (sync engines and `.git` can clash). Keep the project in a normal local folder and optionally push to a private remote (GitHub/Codeberg). [Stack Overflow+1](https://stackoverflow.com/questions/69056041/is-it-dangerous-to-put-a-git-directory-in-a-drive-sync-tool?utm_source=chatgpt.com)
    
*   **Auto-commit on change (set-and-forget):**
    
    *   **gitwatch**: watches a folder and commits (and can push) whenever files change. Install via Homebrew and run as a background process/LaunchAgent. [GitHub](https://github.com/gitwatch/gitwatch?utm_source=chatgpt.com)
        
    *   **fswatch + tiny script**: generic file-watcher you trigger with your own `git add/commit/push` command. [Homebrew Formulae+1](https://formulae.brew.sh/formula/fswatch?utm_source=chatgpt.com)
        
    *   **VS Code route**: enable **Auto-commit on save** via an extension if you prefer editor-native automation. [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=YogeshValiya.autogitcommit&utm_source=chatgpt.com)
        
*   Pros: continuous history and optional off-site backup with no manual steps. Cons: very small background complexity (one tool or extension).
    

If you occasionally open the folder in Obsidian
===============================================

*   **Obsidian Git** can auto-commit/push every X minutes while Obsidian is open (handy if you’re reviewing there). Keep the repo **outside** iCloud. [GitHub+1](https://github.com/Vinzent03/obsidian-git?utm_source=chatgpt.com)
    

Suggested setup (fits your single-folder, `_bible.md`, YAML-in-front workflow)
==============================================================================

*   Keep the project in `~/Writing/<Project>/` (not iCloud).
    
*   Baseline: rely on **Time Machine** + **VS Code Timeline**. [Apple Support+1](https://support.apple.com/en-us/104984?utm_source=chatgpt.com)
    
*   Optional add-on for “invisible” versioning: install **gitwatch** and point it at the project; add a private remote only if you want off-site. [GitHub](https://github.com/gitwatch/gitwatch?utm_source=chatgpt.com)
    

One question
============

Do you want to stop at **Baseline** (Time Machine + VS Code Local History) or add **Background Git** (gitwatch/VS Code auto-commit) for automatic, off-site version history?

## PROMPT 9

I'm not sure I want to commit to a private github for my writing (fight me and prove me wrong). Keeping stuff in iCloud seems simplest. Obsidian is the better tool for viewing on mobile, but it doesn't have a non-git version tool. VS code has Timeline as a non-git tool, and that's pretty neat. So if non-git, use Time Machine (on same disk) and Timeline would give the choice to use either tool (Obsidian or VS Code) as my mood suits me at the time. 

## PROMPT 9

I'm not sure I want to commit to a private github for my writing (fight me and prove me wrong). Keeping stuff in iCloud seems simplest. Obsidian is the better tool for viewing on mobile, but it doesn't have a non-git version tool. VS code has Timeline as a non-git tool, and that's pretty neat. So if non-git, use Time Machine (on same disk) and Timeline would give the choice to use either tool (Obsidian or VS Code) as my mood suits me at the time. 

## RESPONSE 10

Your non-git plan works—but make one change: put Time Machine on an external disk because iCloud + same-disk snapshots leave real gaps.

What’s safe (and what isn’t)
============================

*   **iCloud Drive ≠ version history.** You can restore **deleted** files for ~30 days, but there’s no general per-file version history for arbitrary Markdown; app-specific “Revert To” exists only in apps that implement it (Pages/Preview/etc.). [Apple Support+2Apple Support+2](https://support.apple.com/guide/icloud/recover-deleted-files-mmae56ea1ca5/icloud?utm_source=chatgpt.com)
    
*   **Same-disk Time Machine ≠ backup.** APFS “local snapshots” live on the same drive and roll off after ~24 hours; Apple explicitly recommends normal Time Machine backups (i.e., an external or network disk) for real protection. [Apple Support+2Apple Support+2](https://support.apple.com/guide/mac-help/about-time-machine-local-snapshots-mh35933/mac?utm_source=chatgpt.com)
    
*   **VS Code Timeline = good local safety net.** It keeps non-git file history you can browse and restore, right in the editor. [Stack Overflow+1](https://stackoverflow.com/questions/46446901/how-can-i-see-local-history-changes-in-visual-studio-code?utm_source=chatgpt.com)
    

Recommended minimal stack (no GitHub)
=====================================

*   **Storage & access**
    
    *   Keep your **Markdown project in iCloud Drive** so Obsidian on iOS can view it. For smooth iOS access, **create the vault on iPhone/iPad first**, then move your Mac files into that iCloud container path. [Obsidian Help+1](https://help.obsidian.md/sync-notes?utm_source=chatgpt.com)
        
*   **Version safety (non-git)**
    
    *   **Enable Obsidian “File Recovery”** (core plugin). It auto-snapshots notes for short-term rollbacks; it’s not a full backup, just a seatbelt. [Obsidian Help](https://help.obsidian.md/plugins/file-recovery?utm_source=chatgpt.com)
        
    *   **Use VS Code Timeline** when you’re drafting on Mac for quick, per-file restores. [Stack Overflow](https://stackoverflow.com/questions/46446901/how-can-i-see-local-history-changes-in-visual-studio-code?utm_source=chatgpt.com)
        
    *   **Add a real Time Machine disk** (USB/Thunderbolt SSD). This is Apple’s intended model for durable backups; local snapshots are only a stopgap. [Apple Support+1](https://support.apple.com/en-us/102423?utm_source=chatgpt.com)
        
*   **Why this fits you now**
    
    *   Cross-device reading in Obsidian without ceremony; drafting comfort in VS Code; no Git hosting to wrangle.
        
    *   If you later want mobile version history and conflict tools, **Obsidian Sync** (paid, E2E encrypted, with version history UI) layers on without changing your Markdown files. [Obsidian Help+2Obsidian Help+2](https://help.obsidian.md/sync-notes?utm_source=chatgpt.com)
        

Small guardrails (keep it simple)
=================================

*   **Turn on File Recovery** and set a retention window that matches your pace (e.g., 7–30 days). It saves space by snapshotting only when a file changes. [Obsidian Help+1](https://help.obsidian.md/plugins/file-recovery?utm_source=chatgpt.com)
    
*   **Keep underscore admin files** (`_bible.md`, `_scenelist.md`) and your **scene files with YAML** (brief + `order`) as we outlined—clean for Obsidian, easy to paste into ChatGPT, and portable if you ever compile. (Pandoc will ignore printing YAML unless a template asks for it.) [Apple Support](https://support.apple.com/guide/mac-help/view-and-restore-past-versions-of-documents-mh40710/mac?utm_source=chatgpt.com)
    

When to reconsider Git later (optional, not now)
================================================

*   Collaboration, long off-site history, or moving machines often. If that day comes, you can add **Obsidian Git** or a background watcher without changing your file layout. [GitHub](https://github.com/Vinzent03/obsidian-git?utm_source=chatgpt.com)
    

One next decision
=================

Are you willing to add a **small external SSD for Time Machine** so your backups aren’t on the same disk—yes or no?

## PROMPT 10

Yeah, I have an external SSD that I can use for Time Machine when docked

## RESPONSE 11

Use that SSD for **Time Machine** and pair it with iCloud + VS Code Timeline + Obsidian File Recovery; that gives you non-Git safety with zero ceremony.

Set the safety net
==================

*   **Time Machine to the external SSD (automatic):** Connect the SSD → System Settings → Time Machine → _Select Backup Disk_ → choose the SSD. Time Machine then runs hourly/daily/weekly without you doing anything. [Apple Support](https://support.apple.com/en-us/104984?utm_source=chatgpt.com)
    
*   **Remember what local snapshots are (and aren’t):** macOS will keep short-term on-disk snapshots when the SSD isn’t attached, typically up to ~24 hours; Apple still recommends “normal backups” to an external disk for real protection. [Apple Support+1](https://support.apple.com/guide/mac-help/back-up-files-mh35860/mac?utm_source=chatgpt.com)
    
*   **What iCloud does (and doesn’t):** You can restore _deleted_ iCloud Drive files for **30 days**, but there’s no general per-file version history for arbitrary Markdown; don’t treat iCloud as versioning. [Apple Support](https://support.apple.com/guide/icloud/recover-deleted-files-mmae56ea1ca5/icloud?utm_source=chatgpt.com)
    
*   **Editor-level rollbacks on the Mac:** Turn on **Timeline** in VS Code to get per-file local history (save-based snapshots with restore/diff) even without Git. [Visual Studio Code](https://code.visualstudio.com/docs/getstarted/userinterface?utm_source=chatgpt.com)
    
*   **Seatbelt on mobile:** Enable Obsidian’s **File Recovery** (Core plugins). It auto-snapshots notes and lets you restore, but it’s not a full backup—your Time Machine disk is. [Obsidian Help](https://help.obsidian.md/plugins/file-recovery?utm_source=chatgpt.com)
    

Single-folder project (no subfolders)
=====================================

*   Files live in iCloud Drive so Obsidian on iOS can view them; create or store the vault inside **iCloud Drive → Obsidian** for smooth cross-device access. [Obsidian Help](https://help.obsidian.md/sync-notes?utm_source=chatgpt.com)
    
*   Keep admin files underscored so they group at the top and are easy to exclude in compile:  
    `_bible.md`, `_scenelist.md`, `_manifest.md` (optional).
    
*   Scenes are just `.md` with **YAML up top** (brief + bible\_snippets + `order`) and **prose body only**—clean to paste into ChatGPT, easy to sort/compile later. (Pandoc ignores printing YAML unless a template asks for it, so you can compile body-only if needed.) [Visual Studio Code](https://code.visualstudio.com/docs/getstarted/userinterface?utm_source=chatgpt.com)
    

Daily flow (low friction)
=========================

*   **Plan/ideate in ChatGPT.** Attach your `_bible.md` to the Project/chat when useful. Paste a scene file in whole; the YAML brief acts as context, the body is the working text.
    
*   **Draft on the Mac in VS Code.** Timeline quietly snapshots each save; when docked, Time Machine handles the real backups to SSD. [Visual Studio Code+1](https://code.visualstudio.com/docs/getstarted/userinterface?utm_source=chatgpt.com)
    
*   **Read/tweak on mobile in Obsidian.** Flip on File Recovery for short-term “oops” restores while away from the SSD. [Obsidian Help](https://help.obsidian.md/plugins/file-recovery?utm_source=chatgpt.com)
    

Optional later (only if you want)
=================================

*   **Pandoc escape hatch** for .md → DOCX/EPUB/PDF when you prefer not to paste into Word/Reedsy. Keep it installed; don’t wire it into daily work. [Apple Support](https://support.apple.com/en-us/104984?utm_source=chatgpt.com)
    

One question
============

Want me to generate a **starter kit** (scene template file, `_bible.md`, `_scenelist.md`, and a tiny `build.sh` that stitches scenes by `order`) you can drop into iCloud Drive—**yes or no**?

## PROMPT 11

Give me the build.sh script for compiling

## RESPONSE 12

Here’s a portable `build.sh` that sorts scene files by `order` (in YAML), strips YAML front matter, concatenates to `_manuscript.md`, and (optionally) runs Pandoc if you pass an output filename.

```bash
#!/usr/bin/env bash
# build.sh — stitch Markdown scenes into _manuscript.md, optionally compile with Pandoc.
# Requires: POSIX sh tools (find, awk, sort); Pandoc only if you request an output file.

set -euo pipefail

MANUSCRIPT="_manuscript.md"
TMP_INDEX="$(mktemp)"
trap 'rm -f "$TMP_INDEX"' EXIT

# Collect all non-underscore .md files in the current folder.
# (Your admin files like _bible.md are excluded.)
found_any=false
find . -maxdepth 1 -type f -name "*.md" ! -name "_*" -print0 |
while IFS= read -r -d '' f; do
  found_any=true
  # Extract numeric 'order:' from the FIRST YAML block only; default to a big number if missing.
  ord="$(
    awk '
      NR==1 && $0 ~ /^---[[:space:]]*$/ {in=1; next}
      in && $0 ~ /^---[[:space:]]*$/ {exit}
      in && $1=="order:" {print $2; exit}
    ' "$f" | tr -cd "0-9"
  )"
  : "${ord:=99999999}"
  printf "%08d\t%s\n" "$ord" "${f#./}" >> "$TMP_INDEX"
done

if [ "$found_any" = false ]; then
  echo "No scene files found. Put your .md scenes here (not starting with _ ) and try again."
  exit 1
fi

# Concatenate files in order, stripping ONLY the first YAML block from each.
sort -n "$TMP_INDEX" | cut -f2- | while IFS= read -r f; do
  awk '
    # If the VERY FIRST line begins a YAML block, skip that block; otherwise print everything.
    NR==1 && $0 ~ /^---[[:space:]]*$/ {in=1; next}
    in && $0 ~ /^---[[:space:]]*$/ {in=0; next}
    in {next}
    {print}
  ' "$f"
  printf "\n\n"
done > "$MANUSCRIPT"

echo "Wrote $MANUSCRIPT"

# Optional: if you pass an output filename, compile with Pandoc (e.g., build.sh Draft.docx)
if [ $# -ge 1 ]; then
  out="$1"
  if command -v pandoc >/dev/null 2>&1; then
    pandoc "$MANUSCRIPT" -o "$out"
    echo "Wrote $out (via pandoc)"
  else
    echo "pandoc not found; install pandoc or just use _manuscript.md as-is."
    exit 1
  fi
fi
```

*   Notes: Pandoc understands YAML metadata blocks and won’t print them unless your template asks it to; a simple `pandoc _manuscript.md -o Draft.docx` is enough for clean exports. [pandoc.org+1](https://pandoc.org/demo/example33/8.10-metadata-blocks.html?utm_source=chatgpt.com)
    
*   If you prefer a different compile command (e.g., DOCX with template), swap the last line accordingly (Pandoc supports `-f markdown -t docx` and templates). [allthingsopen.org+1](https://allthingsopen.org/articles/pandoc-convert-markdown-documents-office-formats?utm_source=chatgpt.com)

## PROMPT 12

Thanks.. this is great.

## RESPONSE 13

You’re set—two quick reminders to run the script cleanly and one optional upgrade.

Run it
======

*   Make it executable once, then run it from the project folder:
    
    ```bash
    chmod +x build.sh
    ./build.sh             # creates _manuscript.md
    ```
    
    (Apple’s Terminal guide covers making files executable.) [Apple Support](https://support.apple.com/guide/terminal/make-a-file-executable-apdd100908f-06b3-4e63-8a87-32e71241bab4/mac?utm_source=chatgpt.com)
    

Optional compile (when you actually want a file to send)
========================================================

*   Add an output filename to invoke Pandoc:
    
    ```bash
    ./build.sh Draft.docx     # or Draft.epub / Draft.pdf (with LaTeX installed)
    ```
    
    (Pandoc’s manual documents `-o` and format choices: docx, epub, pdf, etc.) [pandoc.org+1](https://pandoc.org/MANUAL.html?utm_source=chatgpt.com)
    

Safety net (non-Git)
====================

*   Point **Time Machine** at your external SSD (hourly/daily/weekly backups): System Settings → Time Machine → Add Backup Disk. [Apple Support+1](https://support.apple.com/en-us/104984?utm_source=chatgpt.com)
    
*   In Obsidian on iOS/Mac, enable **Core → File Recovery** for short-term snapshots while away from the SSD. [Obsidian Help+1](https://help.obsidian.md/plugins/file-recovery?utm_source=chatgpt.com)
    

One quick win: want me to give you a **VS Code task** so `⌘⇧B` runs `build.sh` and (optionally) compiles via Pandoc?

## PROMPT 13

Ok.. let us now talk about the obsidian and viscose toolchains themselves as it pertains to chatgpt. I subscribe to ChatGPT Plus and am every resistant to setting up and paying for API access. I'd prefer to stay 100% within the CHatGPT Plus framework. Are there cascade or obsidian plugins that work with the chatgpt chatbot, directly or indirectly to make the flow easier? Or am I doomed to managing two app windows?

## RESPONSE 14

Short answer: without paying for API, there’s no reliable Obsidian/VS Code plugin that talks to **ChatGPT Plus** directly—your best low-friction path is the ChatGPT **desktop app overlay** + a couple of copy/URI tricks.

What works today (no API keys)
==============================

*   **ChatGPT for Mac overlay.** Install the macOS app and pop it over whatever you’re doing with **⌥ Space**; it accepts files and keeps everything inside ChatGPT (great for scene briefs + YAML headers). This avoids true “two-window juggling.” [OpenAI Help Center+1](https://help.openai.com/en/articles/9275200-downloading-the-chatgpt-macos-app?utm_source=chatgpt.com)
    
*   **Projects for context.** Put your `_bible.md` (or a few `_*.md` files) into a **Project** so any chat in that project has the same context—clean with your “attach once, reuse many times” habit. [OpenAI Help Center](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt?utm_source=chatgpt.com)
    
*   **Drop outputs straight into Obsidian via URI.** Obsidian’s **Advanced URI** lets you create/append notes by opening a URL; pair that with a browser helper like **Obsidian Web** (Chrome extension) to send the clipboard/selection straight into your vault—no API involved. [vinzent03.github.io+1](https://vinzent03.github.io/obsidian-advanced-uri/?utm_source=chatgpt.com)
    
*   **Quickly capture entire chats as Markdown.** Use a “ChatGPT → Markdown” exporter (one-click `.md` to Downloads), then drag into your vault. Handy for parking long ideation threads. [GitHub+1](https://github.com/jsh9/chatgpt-to-markdown?utm_source=chatgpt.com)
    
*   **If you prefer a browser sidebar while researching.** A ChatGPT sidebar extension pins ChatGPT on any webpage—useful when you’re reading sources (not inside the Obsidian/VS Code apps, but great for the web part of your flow). [Chrome Web Store+1](https://chromewebstore.google.com/detail/chatgpt-sidebar-by-cloudh/kapoabaoamgiilmlanmfejgfomlnccph?utm_source=chatgpt.com)
    

What doesn’t fit your constraint (why you kept feeling friction)
================================================================

*   Most **Obsidian AI plugins** (Text Generator, Copilot, ChatGPT-MD) require an **OpenAI API key**—Plus doesn’t cover API usage. That’s why they’re non-starters for a Plus-only plan. [Obsidian TTRPG Tutorials+2Copilot for Obsidian+2](https://obsidianttrpgtutorials.com/Obsidian%2BTTRPG%2BTutorials/Plugin%2BTutorials/Text%2BGenerator/Text%2BGenerator?utm_source=chatgpt.com)
    
*   **VS Code integrations** like Genie also assume an **API key** and explicitly note that API billing is separate from Plus. Unofficial “web session” extensions exist, but they rely on **unofficial APIs/cookies** and break often—wouldn’t recommend for long-form work. [Visual Studio Marketplace+1](https://marketplace.visualstudio.com/items?itemName=genieai.chatgpt-vscode)
    

Two clean, portable flows (pick one to start)
=============================================

*   **Overlay Mode (simplest):** Draft in VS Code/Obsidian; hit **⌥ Space** to summon ChatGPT over the top; paste in the scene file (YAML brief stays in front matter). Keep the **Project** pinned with your bible so context travels. [ChatGPT+1](https://chatgpt.com/features/desktop/?utm_source=chatgpt.com)
    
*   **URI Mode (quicker capture back to vault):** After ChatGPT refactors a scene, click your **“Send to Obsidian”** helper (Advanced URI). It appends/creates the right `.md` in your vault without touching APIs. [vinzent03.github.io+1](https://vinzent03.github.io/obsidian-advanced-uri/?utm_source=chatgpt.com)
    

Nice-to-haves (optional)
========================

*   **MarkDownload** clips any webpage as Markdown straight into your vault—useful for research notes linked from your bible. [Obsidian Forum](https://forum.obsidian.md/t/configuring-the-web-clipper-markdownload-for-a-seamless-workflow-with-obsidian/62441?utm_source=chatgpt.com)
    
*   **Sidebars while browsing.** If you’re reading sources in Chrome/Edge, pin ChatGPT as a sidebar to ask questions without tab-hopping. [support.cloudhq.net](https://support.cloudhq.net/getting-started-with-chatgpt-sidebar-2/?utm_source=chatgpt.com)
    

One at a time: do you want to start with **Overlay Mode** (⌥ Space ChatGPT over VS Code/Obsidian) or **URI Mode** (one-click “Send to Obsidian” from the browser)?

## PROMPT 14

Safari options?

## RESPONSE 15

Use the **ChatGPT Mac app overlay + Safari’s Share/Shortcuts → Obsidian** combo; you don’t need API keys or sketchy extensions.

What actually works with Plus-only (Safari)
===========================================

*   **ChatGPT for Mac overlay everywhere (incl. Safari).** Install the official app and pop it over Safari with **⌥-Space**; it accepts pasted files/snippets and stays inside your Plus account. [OpenAI Help Center+1](https://help.openai.com/en/articles/9275200-downloading-the-chatgpt-macos-app?utm_source=chatgpt.com)
    
*   **Apple Intelligence → ChatGPT** (macOS Sequoia): in system writing fields (including Safari text areas), you can route to ChatGPT via Apple’s built-in “Writing Tools”/Siri extension—again with your ChatGPT account. [Apple Support](https://support.apple.com/guide/mac-help/use-chatgpt-with-apple-intelligence-mchlfc5cf131/mac?utm_source=chatgpt.com)
    

Safari → Obsidian capture (no API, portable)
============================================

*   **Shortcuts + Obsidian URIs.** Use **Actions for Obsidian** (adds 40+ Shortcuts actions) to create/append notes from Safari’s Share menu; under the hood it can call **Obsidian Advanced URI** (e.g., `obsidian://advanced-uri?...&mode=append`). [Apple+2ActionsDotWork.+2](https://apps.apple.com/us/app/actions-for-obsidian/id1659667937?utm_source=chatgpt.com)
    
*   **Bookmarklet clipper (works in Safari).** The lightweight **Obsidian Web Clipper** bookmarklet saves the current page as Markdown to your vault—handy for research links you cite in your Bible. [Gist](https://gist.github.com/kepano/90c05f162c37cf730abb8ff027987ca3?utm_source=chatgpt.com)
    
*   **Hookmark for deep links.** From Safari, create a persistent link and “hook” it to your scene or bible note in Obsidian to round-trip later. [Hookmark+1](https://hookproductivity.com/help/integration/using-hook-with-obsidian/?utm_source=chatgpt.com)
    
*   **Seatbelt on mobile/Mac.** If you browse/edit in Obsidian, keep **File Recovery** on for short-term rollbacks (this is not a backup—Time Machine still is). [Obsidian Help](https://help.obsidian.md/plugins/file-recovery?utm_source=chatgpt.com)
    

Minimal setup (5 minutes)
-------------------------

1.  Install **ChatGPT for Mac**; confirm **⌥-Space** opens over Safari. [OpenAI Help Center](https://help.openai.com/en/articles/9275200-downloading-the-chatgpt-macos-app?utm_source=chatgpt.com)
    
2.  In macOS **Settings → Apple Intelligence & Siri → ChatGPT**, enable the extension (optional, Sequoia only). [Apple Support](https://support.apple.com/guide/mac-help/use-chatgpt-with-apple-intelligence-mchlfc5cf131/mac?utm_source=chatgpt.com)
    
3.  Install **Actions for Obsidian** (Mac App Store). In **Shortcuts**, create “Send to Obsidian” that appends Safari selection/URL to `_bible.md` or an “Inbox” note via **Advanced URI**. Add it to **Safari’s Share menu**. [Apple+1](https://apps.apple.com/us/app/actions-for-obsidian/id1659667937?utm_source=chatgpt.com)
    
4.  (Optional) Add the **Obsidian Web Clipper** bookmarklet to Safari for one-click full-page Markdown capture. [Gist](https://gist.github.com/kepano/90c05f162c37cf730abb8ff027987ca3?utm_source=chatgpt.com)
    

About “ChatGPT in Safari” extensions
====================================

*   Safari has third-party “ChatGPT sidebars” (e.g., **Sider**, **GPTWebHelper**), but they’re not the official ChatGPT app and usually rely on their own backends/credentials. Since you want **Plus-only, no API**, prefer the **official Mac app overlay** and Apple’s integration. [Apple+1](https://apps.apple.com/us/app/sider-ai-gpt-chat/id6447783111?mt=12&utm_source=chatgpt.com)
    

Recommendation
==============

*   **Day-to-day:** Safari for reading → Share to the **Shortcuts → Obsidian** note; summon **⌥-Space** for ChatGPT over the page when you want analysis/rewrites.
    
*   **When drafting:** Paste the whole scene file (YAML brief + prose) into ChatGPT; paste the result back to your scene note (or run a Shortcut to append). Keep your portable Markdown spine intact. [OpenAI Help Center+1](https://help.openai.com/en/articles/9275200-downloading-the-chatgpt-macos-app?utm_source=chatgpt.com)
    

Want a ready-made Shortcut that **appends Safari selection to `_bible.md`** (using Advanced URI), plus a second one that **creates a new scene note from selection**?

