Use the **ChatGPT Mac app overlay + Safari’s Share/Shortcuts → Obsidian** combo; you don’t need API keys or sketchy extensions.

  

# **What actually works with Plus-only (Safari)**

- **ChatGPT for Mac overlay everywhere (incl. Safari).** Install the official app and pop it over Safari with **⌥-Space**; it accepts pasted files/snippets and stays inside your Plus account. 
    
- **Apple Intelligence → ChatGPT** (macOS Sequoia): in system writing fields (including Safari text areas), you can route to ChatGPT via Apple’s built-in “Writing Tools”/Siri extension—again with your ChatGPT account. 
    

  

# **Safari → Obsidian capture (no API, portable)**

- **Shortcuts + Obsidian URIs.** Use **Actions for Obsidian** (adds 40+ Shortcuts actions) to create/append notes from Safari’s Share menu; under the hood it can call **Obsidian Advanced URI** (e.g., obsidian://advanced-uri?...&mode=append). 
    
- **Bookmarklet clipper (works in Safari).** The lightweight **Obsidian Web Clipper** bookmarklet saves the current page as Markdown to your vault—handy for research links you cite in your Bible. 
    
- **Hookmark for deep links.** From Safari, create a persistent link and “hook” it to your scene or bible note in Obsidian to round-trip later. 
    
- **Seatbelt on mobile/Mac.** If you browse/edit in Obsidian, keep **File Recovery** on for short-term rollbacks (this is not a backup—Time Machine still is). 
    

  

## **Minimal setup (5 minutes)**

1. Install **ChatGPT for Mac**; confirm **⌥-Space** opens over Safari. 
    
2. In macOS **Settings → Apple Intelligence & Siri → ChatGPT**, enable the extension (optional, Sequoia only). 
    
3. Install **Actions for Obsidian** (Mac App Store). In **Shortcuts**, create “Send to Obsidian” that appends Safari selection/URL to _bible.md or an “Inbox” note via **Advanced URI**. Add it to **Safari’s Share menu**. 
    
4. (Optional) Add the **Obsidian Web Clipper** bookmarklet to Safari for one-click full-page Markdown capture. 
    

  

# **About “ChatGPT in Safari” extensions**

- Safari has third-party “ChatGPT sidebars” (e.g., **Sider**, **GPTWebHelper**), but they’re not the official ChatGPT app and usually rely on their own backends/credentials. Since you want **Plus-only, no API**, prefer the **official Mac app overlay** and Apple’s integration. 
    

  

# **Recommendation**

- **Day-to-day:** Safari for reading → Share to the **Shortcuts → Obsidian** note; summon **⌥-Space** for ChatGPT over the page when you want analysis/rewrites.
    
- **When drafting:** Paste the whole scene file (YAML brief + prose) into ChatGPT; paste the result back to your scene note (or run a Shortcut to append). Keep your portable Markdown spine intact. 
    

  

Want a ready-made Shortcut that **appends Safari selection to _bible.md** (using Advanced URI), plus a second one that **creates a new scene note from selection**?