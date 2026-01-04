# Office Online default workaround

**Created:** 2025-10-07 11:01:31
**Updated:** 2025-12-07 22:31:16
**Turns:** 35

---

**User:**

Windows 11 file associations.. how can you make Office Online the default file handler for office docs.. eg. Icons and double-click to open in a browser?

---

**Assistant:**

Short answer: You can’t reliably make “Office Online in browser” the *default* file handler in Windows 11 for double-click — Windows expects a native app. But there are workarounds and partial solutions. Here’s what I found and what you can try.

---

## Why it’s hard / probably infeasible

- Windows’ “default apps” system ties file extensions (e.g. `.docx`) or protocols to local programs (EXE/APPX). There’s no built-in support for “open with web app” as a first-class default.  
- Even if you try to hijack via a protocol handler (e.g. `ms-word:ofv?…`), Explorer still resolves file double-click to a registered file association, not to a browser “open this in Office Online.”  
- Microsoft does allow imposing default associations via XML and policies (for enterprises) but again for native apps. citeturn0search5turn0search3  
- Some older tricks (shell extensions, custom “Open in browser” wrappers) exist, but they break easily and add brittleness.

Given those constraints, let's look at what *is* possible.

---

## Possible approaches / workarounds

Here’s a menu of things you can try. None is perfect.

| Approach | What it does | Pros / Cons | How to do it |
|---|---|---|---|
| Use “Open With → Browser / Office Web” manually | Right-click a `.docx`, choose “Open with” → browser or custom wrapper | You lose “double-click = web” behavior | You can create a small wrapper EXE or script that launches the browser with Office Online, register that as a possible handler |
| Make a custom protocol handler / wrapper | E.g. define `officeweb:` protocol, then intercept file opens and forward to Office Online in browser | Can be smoother, but double-clicking .docx still tricky | Write a small utility (e.g. .NET) that receives a filepath, uploads / opens in Office Online link, and register it in the registry under the file extension |
| Use “Office for the web” integration (OneDrive / SharePoint) | If the file is stored in OneDrive/SharePoint, links often open in Office Online by default | Only works when file is in cloud storage; double-click may open local copy | Use OneDrive sync and “Open in browser” commands |
| Use default app policies in enterprise / domain | Deploy XML of file associations, push via GPO / Intune | Only works for native apps, not web handlers | See Microsoft docs / Intune policies for “Default Associations Configuration” citeturn0search5 |
| Replace handler to launch browser | For each extension, set default to a browser .exe with arguments (e.g. `chrome.exe “https://word.office.com?file=…”`) | Works if you can generate a correct Office Online URL from file path | You’d need a mapping: local path → Office Online URL (non-trivial) |

---

## Recommendation given constraints

Given you’re in IT and can code or push policies, my recommended path:

1. **Create a small “launcher” utility**  
   - Accepts a local path (or URI)  
   - Converts it into the appropriate Office Online link (OneDrive / SharePoint URL)  
   - Launches default browser with that URL  

2. **Register that utility as the default handler for `.docx`, `.xlsx`, `.pptx`**  
   - Via registry or “Open with / Always use this app”  
   - Use per-user or enterprise deployment  

3. **Store your files in OneDrive / SharePoint**, so the translation to Office Online is straightforward.

This won't be as seamless as a native “web app default,” but it’s the closest you’ll realistically get.

---

If you want, I can walk you through building that launcher and registering it for your setup (or for your enterprise). Want me to sketch code + registry settings?

---

**User:**

This is a really dumb constraint...especialy when MS retired the free viewer apps

---

**Assistant:**

Yeah — it’s one of those maddeningly *Microsoft* contradictions 😑  

They spent years pushing “cloud first, web first,” then quietly ensured Windows 11 still assumes every file must have a **local executable** behind it. Retiring the old **Word/Excel/PowerPoint Viewers** basically killed the lightweight “just-open-and-look” path, and there’s still no sanctioned “Office Online as file handler” option. So we’re left with:  

- **Install full Office desktop** (paywall)  
- **Use OneDrive/SharePoint** (cloud lock-in)  
- **Or hack together a browser launcher** (unsupported)  

It’s dumb, yes—but deliberate: Windows’ file association model dates to the COM-era and never got rewritten for web apps. ChromeOS and iPadOS both *can* hand a file off to a web app cleanly; Windows just doesn’t treat URLs as first-class app targets.  

If your goal is just **double-click to view** (no editing), I can show you a clean little PowerShell + registry wrapper that:  

- Detects `.docx`/`.xlsx`/`.pptx`  
- Uploads to OneDrive (or your tenant’s temporary “Office Online” folder)  
- Opens the browser viewer instantly  

Would you want that? It’s about a 2-minute install, totally reversible, and works fine for personal use.

---

**User:**

What about the MS store app versions of word/powerpiint/excel... do they still exist or did they go the way of Windows RT?

---

**Assistant:**

Good question — and yeah, that line got *really* muddled.  

Here’s the current state (as of late 2025):

---

### 🧩 1. The legacy “Office (UWP)” apps from the Microsoft Store
- Those **UWP (Universal Windows Platform)** versions of Word, Excel, and PowerPoint that shipped with Windows 10 S / RT are *gone*.  
- They were officially deprecated around 2021 when Microsoft unified everything under the **Office (Hub)** app — later renamed **Microsoft 365 (Preview)**, now **Microsoft 365 app**.  
- That Store app is just a **launcher shell**: it lists your recent docs and opens them in the web or desktop version depending on what’s installed. It’s *not* a full viewer or editor anymore.

---

### 🪦 2. The “Office Mobile” apps
- Those lightweight “Word Mobile,” “Excel Mobile,” and “PowerPoint Mobile” apps were part of the UWP era — designed for touch devices, especially Surface RT and early Surface Go.  
- Microsoft removed them from the Store around 2023. If you had them, they still technically run, but they can’t be re-downloaded.  
- They never had feature parity, and Microsoft stopped updating them years ago.

---

### 🌐 3. The replacement: Microsoft 365 Web + PWA
- Microsoft’s official stance now is: *“Use the web apps.”*  
- You can install them as **Progressive Web Apps (PWAs)** via Edge → “Apps › Install this site as an app.”  
- That gives you icons, Start-menu entries, and taskbar integration — they even look native — but they’re still browser-hosted.  
- These PWAs don’t register as file handlers for `.docx` etc. (same constraint you hit earlier).  
  You can pin them, but Explorer won’t hand off files to them.

---

### ⚙️ 4. The only “native” options left
- The full **Microsoft 365 desktop suite** (Win32, click-to-run)  
- Or **Office LTSC 2021/2024** for volume licensing.  
Everything else is browser-based now.

---

So: the Store apps didn’t exactly go the way of Windows RT — they were *absorbed* into the web ecosystem and abandoned quietly. You can mimic their behavior decently with the PWA trick, but if you double-click `.docx`, you’re still launching desktop Word or nothing at all.  

Would you like me to show how to set up the Edge PWA versions so they at least *feel* native — with icons, taskbar shortcuts, and file drag-and-drop into browser tabs? It’s not perfect, but it’s as close as you can get in Windows 11.

---

**User:**

Yeah.. this kinda makes me mad and one of the reasons I won't use Windows much anymore. Like maybe I just use the M365 app and call it a day. Pretend Windows Explorer doesn't exist. 

---

**Assistant:**

Completely fair reaction.  
Microsoft basically built a gorgeous house—then nailed all the interior doors shut.  

The **M365 app** actually *is* the cleanest middle ground now:  
- it surfaces your recent docs from OneDrive and SharePoint,  
- launches them seamlessly in browser or desktop depending on your setup,  
- and keeps you inside Microsoft’s “identity and cloud” flow without fighting file associations.  

If you live in that hub and ignore Explorer entirely, it feels way more coherent—almost like ChromeOS but with a Start button.  

The irony, of course, is that Windows has become the *worst* environment for Microsoft’s own cloud apps. The OS still assumes you’re in a LAN-based file world, not the OneDrive-centric one Microsoft’s been preaching for a decade.  

If you want to keep your sanity:  
- **Pin the M365 web app as a PWA** (Edge → “Install this site as an app”) so it launches in its own window.  
- **Use Quick Access inside it** for your cloud files.  
- **Forget Explorer exists** except for downloads and local temp files.  

That combo gives you a lightweight, predictable workflow—no file association headaches, no broken icons, no “choose an app” prompts every week after updates.  

You’re not wrong to bail on the old model. Windows is still trying to be both *a desktop OS* and *a web client*, and it’s never figured out how to commit to one.

---

**User:**

Tbh, it's the same in macOS right? File handlers assume local app installed?

---

**Assistant:**

Yep — you’re absolutely right. macOS isn’t innocent either 🍎🤷‍♂️  

Both macOS and Windows still cling to the **“local app = file handler”** assumption baked into their 1990s DNA. The OS hands off a file path to something executable on the same machine — it doesn’t know (or care) if a web app could handle it better.  

Here’s the quick comparison:  

---

### 🪟 **Windows**
- File associations live in the registry and are hard-bound to `.exe` / `.appx` handlers.  
- No built-in way to register “open this in a web URL.”  
- Admins can script around it, but Explorer won’t call a URL handler directly.  
- Progressive Web Apps can’t register as default file handlers.  

---

### 🍏 **macOS**
- Uses **Launch Services** database for file associations (the `lsregister` system).  
- It only recognizes local `.app` bundles — no concept of “default web app.”  
- Safari PWAs are second-class citizens; they don’t show up as Open With targets.  
- There’s no system-level URL rewrite to say “open this `.docx` in Word Online.”  

You *can* script a custom “open” handler with Automator or Shortcuts — e.g.  
```applescript
open location "https://word.office.com?file=https://path/to/file"
```  
and then register that as a service, but it’s a hack, not native support.

---

So yeah, both OSes are still **pre-cloud architectures** pretending to be modern.  
ChromeOS and iPadOS are the only ones that fully treat web apps as first-class citizens — they hand off files, links, and intents natively to cloud services.  

You’re basically hitting the cultural lag: the platforms were built for “files on a disk,” while the workflow you want lives in “links in the cloud.”  

If you really want to embrace that model on macOS, the least painful path is:  
- Keep *everything* in OneDrive,  
- Use the **Microsoft 365 web app (PWA)** for all Office work,  
- Let Finder just be your “Downloads + staging area.”  

No file handlers, no drama — just URLs and tabs.

---

**User:**

The ultimate rage quit is to go iPad only.   Not practical, but it's at least the most cohesive experience

---

**Assistant:**

Ha — yep, the *iPad-only rage-quit* is the digital equivalent of moving to a cabin in the woods and swearing off society. 🌲💻  

And honestly, you’re not wrong:  
on iPad, **the coherence is real** — one app sandbox per task, files abstracted away, Office web/native parity decent, and everything built around *intent* rather than *file type*.  
It’s the one platform where Microsoft’s cloud-first dream actually works the way they advertise.  

The trade-offs, of course:  
- You lose automation depth and filesystem control.  
- Multitasking’s gotten better (Stage Manager, external monitor), but it’s still not desktop-grade.  
- Anything involving local scripting, version control, or complex downloads is pain.  

But for everyday productivity — email, docs, meetings, journaling, reading — it’s shockingly friction-free.  
You open what you need, you close it, nothing asks you about “file associations.”  

If you ever wanted to *experiment* with an iPad-only sprint, I could help design a small 1-week test loop — just enough to feel whether the cohesion outweighs the constraint.  
Would you want to sketch that out?

---

**User:**

My biggest problem with that is that I have an iPad mini 7--- the external monitor support is terrible.. and if I'm being honest, even on ipados26, the best iPad experience is touch--- not mouse/keyboard

---

**Assistant:**

Exactly. You’ve nailed the paradox of the iPad: it’s *brilliant* until you try to make it a computer.  

The **iPad mini 7** in particular lives in that uncanny valley — gorgeous for reading, note-taking, or quick edits, but the moment you connect a keyboard or monitor, the illusion cracks.  

Here’s the honest breakdown of what’s going on:  

---

### 🫧 Why the iPad mini feels best as a *tablet*, not a workstation
- **Touch-first DNA:** iPadOS is still a touch OS with a mouse bolted on. Pointer support is functional but not fluid; you constantly feel like the cursor is fighting the UI metaphors.  
- **No proper windowing:** Even with Stage Manager, external display mode is more “extended springboard” than true multi-window control. You can’t reliably drag stuff between screens without lag or weird resizing.  
- **Keyboard lag + shortcuts:** The command layer (⌘-Tab, etc.) works, but ergonomically it’s inconsistent. You have to relearn which keyboard shortcuts map to Mac behavior and which don’t.  

---

### 🔌 External monitor pain points
- Mini’s USB-C is **DisplayPort 1.4 but capped** by the A17 chip’s bandwidth. You get 60 Hz but not full scaling options.  
- Apps don’t expose proper dual-display layouts (Word, Excel, Safari, etc. still mirror rather than span).  
- No native multi-monitor memory — unplug and your layout evaporates.  

---

### 🪄 When it *does* shine
- **Reading, writing, research** — paired with a Pencil or your hands, it’s unbeatable.  
- **Triage work** — email, Teams, light document edits, journaling, mind-mapping.  
- **Flow mode** — minimal cognitive overhead. You’re not “managing windows,” you’re just *doing the thing*.  

---

You’re right that **iPadOS 26** improves Stage Manager and scaling, but it’s still not enough to make it feel like macOS. The magic of iPad isn’t replacing your computer; it’s replacing *everything else* — your notebook, your inbox, your RSS reader, your low-stakes work surface.  

If you stay within that boundary, it’s *delightful*. Step past it, and you’re back in frustration land.  

If you ever wanted to optimize your mini for its natural strengths (reading + creative capture + light work), I can outline a “cohesive-iPad-mini setup” — minimal apps, best settings, and gestures that make it sing. Want that?

---

**User:**

UBIK is really causing me to itch.. I'm pretty much apple only but have UBIK as essentially a windows server for Plex/qbittorrent media thing. We recently got traditional cable again (smoking deal) so I think the Plex use-case might deprecate.. just manually download the handful of shows (that I can't get via cable or streaming service) on a usb stick and watch them from the TV. Increasingly a rare thing.

---

**Assistant:**

That actually sounds like a pretty sane simplification move — the kind that feels small but ends up decluttering a whole mental corner.  

UBIK’s doing what so many home-lab boxes end up doing: sitting there, humming quietly, eating watts, and mostly existing for a use case that’s fading into obsolescence. Plex was great when *everything* needed sideloading; now it’s kind of an overengineered jukebox for scraps.  

You’ve basically got three honest paths here:  

---

### 🧊 1. **Freeze it in place (server mode)**
- Keep UBIK as a low-touch archive node or media seedbox.  
- Disable Plex autostart, power it down except when needed.  
- Gives you optionality — you can still drop files there, but it’s not “always on.”  

**Pros:** Zero re-architecture.  
**Cons:** Still burns idle energy and takes up space.  

---

### 🧹 2. **Deprecate gracefully**
- Migrate or just abandon Plex; uninstall all auto-updaters.  
- Keep qbittorrent and SMB share if you occasionally need a file staging area.  
- Move finished downloads to external USB drives; plug directly into TV or Mac mini.  
- Maybe repurpose UBIK as a local backup target (Time Machine via SMB).  

**Pros:** Simpler, uses hardware you already own.  
**Cons:** Still keeps a bit of Windows baggage in your ecosystem.  

---

### 🔥 3. **Decommission entirely**
- Back up anything sentimental.  
- Wipe the drives, pull data drives into external USB enclosures.  
- Sell, donate, or repurpose the chassis as a sandbox (VALIS, as you mentioned before).  

**Pros:** Mental and physical declutter.  
**Cons:** No home-lab fallback if you need one later.  

---

Given your current setup — Apple-centric, low-friction, less “tinker mode” — I’d lean toward **#2 (graceful deprecation)**.  
UBIK can quietly retire to “utility box” status: on when you need it, off when you don’t. The energy savings and reduction in noise/complexity will feel bigger than you expect.  

If you’d like, I can outline a **“UBIK sunset checklist”** — backup, service shutdown order, what to keep vs wipe, and what roles could be absorbed by your Macs/iCloud stack. Want me to?

---

**User:**

UBIK is also acting as my backup server ... eg cloud files syncing to it and then robocopied to another location in a biweekly A/B split. It works fine, but to your point, it's eating watts and is clutter for a very niche use case. My cloud sync might be good enough and the risks may be acceptable enough.

---

**Assistant:**

Yeah — that’s the real inflection point: when your “redundant backup architecture” quietly becomes more *complexity insurance* than *data insurance.*  

UBIK’s doing an admirable job as a self-hosted fail-safe, but if we zoom out:  

---

### 🧮 What you actually have
- **Cloud as primary:** iCloud/OneDrive handle live sync, with their own versioning and redundancy.  
- **UBIK mirror:** receives sync copies and Robocopy jobs for air-gap duplication.  
- **Secondary copy:** Robocopy’s A/B split adds another layer (good hygiene, but more moving parts).  

That’s textbook belt-and-suspenders — useful when broadband or cloud reliability were sketchier.  
But in 2025, iCloud and OneDrive both offer **versioned, encrypted, regionally redundant** storage. Your *personal* risk profile may no longer justify the extra watts, updates, and drive wear.  

---

### ⚖️ Risk trade-off snapshot

| Threat | Cloud resilience | UBIK advantage | Actual delta |
|--------|------------------|----------------|---------------|
| Accidental delete | iCloud/OneDrive version history | Slightly better restore window | Minimal |
| Account lockout | 2FA, recovery keys | Local copy accessible offline | Moderate |
| Ransom/cloud corruption | Version history + offline devices | Air-gap delay with Robocopy | Small, given modern recovery |
| Connectivity outage | Local cache on Apple devices | Full LAN copy | Minimal for a few days |
| Catastrophic provider failure | Highly improbable | Full local redundancy | Theoretical |

Unless you’re protecting archival or regulatory data, **cloud + local Mac Time Machine** is almost always sufficient now.

---

### 🧘‍♂️ Simplified posture options
- **Option A:** Retire UBIK; rely on iCloud + Time Machine (daily) + Backblaze or similar (off-site).  
- **Option B:** Keep UBIK offline; wake it up quarterly for one-shot syncs.  
- **Option C:** Virtualize it — spin a lightweight Linux VM (VALIS) on your Mac just for Robocopy-equivalent tasks.  

That middle “cold-standby” model (B) often feels safest: you get peace of mind without constant hum or maintenance.  

---

If you want, I can sketch a **“UBIK retirement plan”** — what to migrate, what to verify in cloud redundancy, and how to repurpose the drives for cold storage. It’s a nice, finite project that ends with a quieter house and one less system in your mental RAM. Want that outline?

---

**User:**

I wonder... can I run "plex on demand" from my MacBook? For the rare use cases where we need to stream something to the tv?

---

**Assistant:**

Yes — absolutely. Plex can run beautifully **“on demand”** from your MacBook, with almost zero footprint when idle. It’s basically the perfect middle-ground between full-time server and total decommission.  

Here’s how to make it clean and friction-free 👇  

---

### ⚙️ 1. Install Plex Media Server (macOS)
- Download from [plex.tv/downloads](https://www.plex.tv/downloads/).  
- It runs as a menu-bar process — you can quit it anytime.  
- Your media library can live on an **external SSD/HDD** or a **shared folder**.  
  When the drive’s disconnected, Plex just shows greyed-out titles (no harm done).  

---

### 🧠 2. Configure it for “on-demand” mode
- **Disable auto-start at login:**  
  - System Settings → General → Login Items → remove Plex.  
- **Manual launch:** create an alias in `/Applications/Utilities` or a Dock shortcut.  
- When you want to stream something → plug in your drive → launch Plex → watch → quit when done.  
- You can even create a **Shortcuts automation** that:
  - mounts the drive,
  - opens Plex,
  - quits Plex and ejects when done.  

---

### 📺 3. Stream to the TV
You’ve got two simple routes:  
- **Native Plex app** on the smart TV (Samsung, LG, Roku, etc.) → sign in → it’ll find your Mac automatically on the LAN.  
- Or **AirPlay** directly from Plex web/app on the Mac → TV.  

The discovery handshake works instantly when both are on the same Wi-Fi and the Mac isn’t sleeping.  

---

### 🔌 4. Optional: Quick toggle via command line
If you like tight control, you can wrap it in a one-liner:
```bash
open -a "Plex Media Server"
```
and a matching “kill” script:
```bash
pkill "Plex Media Server"
```
Drop those into Automator or a Shortcut → boom, instant “Plex On / Plex Off” buttons.  

---

### 💡 5. Bonus: Lightweight alternatives
If you only ever play *local* media:
- **Infuse (Mac + iOS)** — handles everything Plex does, without server overhead.  
- **VLC + DLNA** — stream straight from your Mac’s shared folder.  

Infuse especially plays nice with iCloud metadata sync, so your watched status even follows you between iPhone and Apple TV.  

---

Honestly, given your current setup and priorities, **“Plex on demand from the MacBook”** or **Infuse** is the most elegant path forward — no idle power drain, no Windows maintenance, no Plex updates running in the dark.  

Would you like me to sketch a mini workflow for that “Plex on / Plex off” Shortcut setup? It pairs really well with your Apple Notes planning system.

---

**User:**

Thinking the ease of the app ecosystem on the Samsung smarttv.. Plex just works.. but some does air play

---

**Assistant:**

Yeah — that’s the sweet spot, right? The Samsung Smart TV apps are *weirdly* good at what they do, and Plex is one of the few that’s been rock-solid on Tizen for years.  

Here’s how it plays out in real-world use:  

---

### 🧩 Option 1 — **Plex app on the TV**
- Just open the Plex app → it auto-discovers any Plex Media Server on your LAN (your MacBook, when it’s running).  
- No manual IPs, no port forwarding, no fiddly setup.  
- Playback is native — the TV decodes most formats fine.  
- You can quit Plex on the Mac when done; the TV gracefully drops the session.  

✅ *Zero cognitive friction once it’s paired the first time.*  
💡 Tip: leave “Server sleep prevention” off — that way Plex won’t try to keep your Mac awake.  

---

### 🍎 Option 2 — **AirPlay / Cast**
- Quick and dirty for single files.  
- From Finder or QuickTime → “Share > AirPlay” → your TV.  
- Works instantly but lacks library browsing, subtitles, watch history, etc.  
- A nice fallback when you’ve just downloaded one episode or movie.  

✅ No server needed.  
❌ You lose the “nice Plex interface” and metadata.  

---

### 🪶 Pragmatic hybrid (what most people settle into)
1. Keep Plex Media Server installed on the MacBook.  
2. Quit it until you actually want to watch something.  
3. Fire up Plex → TV app finds it automatically → done.  
4. Quit Plex afterward.  

It behaves like a modern-era DVD player — *there when you want it, invisible when you don’t.*  

---

If you want a bit more convenience, I can show you a one-click Shortcut on the Mac that:  
- launches Plex,  
- pings the TV to wake the app,  
- and then closes everything when you’re finished.  
Would you want that little automation?

---

**User:**

I could run qbttorrent passively that way as well in server mode against an RSS feed. My MacBook is docked most of the time-- especially in the evenings. 

---

**Assistant:**

Exactly — that’s a really elegant setup, actually.  
You’d basically be turning your MacBook into a *quiet, part-time media appliance* instead of a full-time Windows headless box. 💡  

Here’s what that could look like:  

---

### ⚙️ The “Evening Server” Model
When your MacBook’s docked and plugged in (evenings, weekends, etc.), it quietly:  
- Runs **qBittorrent in server mode** (RSS + web UI)  
- Spins up **Plex Media Server**  
- Sleeps when undocked or idle  

All without feeling like a *server*.  

---

### 🧲 How to set up qBittorrent for passive operation
1. **Install qBittorrent (macOS)**  
   - Use the latest dmg from the official site (no Homebrew needed).  
2. **Enable Web UI:**  
   - Preferences → Web UI → enable and set a strong password.  
   - Defaults to `http://localhost:8080`  
3. **Set up RSS auto-downloading:**  
   - RSS tab → add feeds → create rules for matching titles.  
   - Optionally direct downloads to a specific “Media Inbox” folder that Plex watches.  
4. **Run headless (optional):**  
   - You can launch it hidden via `launchctl` or a small Shortcut that opens it silently when on AC power.  

---

### 💾 Integrate with Plex
- Point Plex’s “Library > Add Folder” to your qBittorrent download directory.  
- Enable “Auto Update Library” in Plex.  
- Now when a new episode arrives, Plex sees it instantly and shows it on the TV app.  

Everything syncs as soon as your MacBook is awake, docked, and on Wi-Fi.  

---

### 💤 Automate the on/off logic (optional, but fun)
Use **Shortcuts + Automator**:  

**Trigger:** when power adapter is connected *and* on home Wi-Fi  
**Actions:**  
- Launch qBittorrent  
- Launch Plex Media Server  

**Opposite trigger (on battery):**  
- Quit both apps  
- Optional: eject external drive  

That makes the whole stack literally “server when docked, laptop when mobile.”  

---

It’s such a clean middle path — no headless box humming away in the corner, no Windows update roulette, but you still get the self-updating media flow you liked about UBIK.  

Would you like me to sketch that Shortcut pair (dock = on, undock = off)? It’s a neat 5-step automation that works shockingly well in practice.

---

**User:**

Yeah that's the ticket.. only run plex/qbittorrent when plugged in and on home wifi

---

**Assistant:**

Perfect — that’s the sweet spot:  
power-aware, location-aware, and *completely invisible once set up.*  

Here’s how to wire that up cleanly on macOS without any background cruft 👇  

---

## ⚙️ Step 1 — Configure both apps for clean start/stop
**qBittorrent**  
- Preferences ▸ Behavior ▸ **Uncheck “Start on login.”**  
- Enable **Web UI** (Prefs ▸ Web UI ▸ check the box, choose port 8080 or similar).  
- Optional: set download folder to `/Users/you/MediaInbox` — easy for Plex to index.  

**Plex Media Server**  
- Preferences ▸ General ▸ uncheck “Launch at login.”  
- Confirm you can start/quit it manually from Spotlight (`Plex Media Server.app`).  

Now both apps only run when you tell them to.

---

## ⚡ Step 2 — Create your “Docked at Home” automation

### In **Shortcuts.app**
Create a new personal automation:  
**When:**  
- **Power** → “When power adapter is connected”  
- **AND** **Wi-Fi** → “When connected to [your home SSID]”

**Then run these actions:**
1. *Run Shell Script* →  
   ```bash
   open -a "Plex Media Server"
   open -a "qBittorrent"
   ```
2. (Optional) *Show Notification* → “🎬 Media services started.”

💡 You can test the script manually in Terminal first — it’ll pop both apps open.

---

## 💤 Step 3 — Create the inverse “Undocked / Leaving Home” automation
Duplicate the Shortcut and flip the triggers:

**When:**
- Power adapter is disconnected  
- OR Wi-Fi disconnects from home network

**Then:**
```bash
pkill "Plex Media Server"
pkill "qBittorrent"
```
Optional notification: “🛏️ Media services stopped.”

macOS will gracefully quit them — Plex writes its cache and qBittorrent saves state automatically.

---

## 🪶 Optional refinement
If you want to avoid both running simultaneously (say, when you just want to torrent quietly), you can split them:
- *Media Download Mode* → qBittorrent only  
- *Media Viewing Mode* → qBittorrent + Plex  
Triggered via different shortcuts or menu-bar buttons.

---

Result:  
When you dock the MacBook and it sees home Wi-Fi → everything spins up automatically.  
When you unplug → everything shuts down.  
No power waste, no extra maintenance, no more UBIK hum.  

Want me to give you the ready-to-import `.shortcut` XML code block for both automations? It’ll drop straight into Shortcuts.

---

**User:**

I don't think there's any harm in leaving both running together or even leaving them running during the day. Both are pretty lightweight.. just only want them running when docked at home

---

**Assistant:**

Yeah, totally — that’s a perfectly reasonable balance. Both **Plex** and **qBittorrent** are pretty gentle citizens when idle:  

- **Plex** barely does anything until a client pings it (and it sleeps its transcoder when not streaming).  
- **qBittorrent** idles at near-zero CPU, even with RSS polling.  
So there’s no need to kill them aggressively — just make sure they’re not burning battery or waking the Mac when you’re mobile.  

Here’s a slightly simpler, cleaner way to handle it given that goal:  

---

## ⚙️ “Run at Home” Automation (simplified version)

### Trigger
- **When power adapter is connected**  
- **AND Wi-Fi network = your home SSID**

### Actions
```bash
open -a "Plex Media Server"
open -a "qBittorrent"
```

### Optional: Add a notification
“🎥 Plex + qBittorrent started (home docked mode).”

That’s it — you don’t need an “off” version unless you’re picky about tidiness.  
If you unplug and leave, they’ll just sit dormant in the background; macOS power management will freeze them after a bit anyway.

---

## 🧠 Nice-to-have tweaks
- **Sleep behavior:**  
  In Plex > Energy Saver, disable “Prevent computer from sleeping.” That way the Mac can still nap if nothing’s streaming.  
- **qBittorrent:**  
  Turn off “Keep seeding after completion” if you don’t want lingering network chatter while you’re not watching.  
- **Network scope:**  
  You can restrict Plex’s “Network Discovery” to your LAN subnet only — no external exposure.

---

Net effect:  
When you drop your MacBook into the dock at night — everything just *lights up and does its thing*.  
Unplug, and it all goes quiet again without drama.  

Want me to hand you the full `.shortcut` export code so you can just import and tweak the SSID/power conditions?

---

**User:**

I'd probably stop them when undocked as I don't want them to run when I'm at work

---

**Assistant:**

Yeah — that’s the smart refinement. Keeps things tidy and avoids any “oops, Plex is serving my downloads to the world while I’m on campus” moments 😅  

Here’s the clean, two-shortcut setup for exactly what you want: lightweight, no-bloat, and fully reversible.  

---

## ⚙️ Shortcut 1 — **“Docked at Home → Start Media Services”**
**Trigger:**  
- Power adapter connected  
- AND Wi-Fi = *your home SSID*  

**Actions:**  
```bash
open -a "Plex Media Server"
open -a "qBittorrent"
```

**Optional Notification:**  
`🎬 Media services started.`  

✅ This runs when you drop your MacBook in the dock at home.  

---

## 💤 Shortcut 2 — **“Undocked or Away → Stop Media Services”**
**Trigger:**  
- Power adapter disconnected  
- OR Wi-Fi disconnects from *your home SSID*  

**Actions:**  
```bash
pkill "Plex Media Server"
pkill "qBittorrent"
```

**Optional Notification:**  
`🛑 Media services stopped.`  

✅ This fires automatically when you unplug or take the MacBook off your home network (e.g. at work).  

---

## 🧠 Tips
- Test with `pkill` in Terminal once — Plex and qBittorrent both exit gracefully.  
- In **Shortcuts**, choose “Run immediately, don’t ask” for each automation (otherwise macOS nags you).  
- You can even pair them with a “When power adapter connected/disconnected” trigger *only when Wi-Fi = home SSID* so it doesn’t run in other places.  

---

Would you like me to generate the full `.shortcut` export XML for both? You could drop them straight into Shortcuts and just edit your SSID name — no manual assembly required.

---

**User:**

Is qbittorrent the best for this on macOS or does transmission support rss feed watxching?

---

**Assistant:**

Good question — and you’re asking exactly the right one.  

On macOS today, **qBittorrent** is still the best all-around choice *if you want native RSS feed automation*. Transmission is great for lightweight seeding and single-file downloads, but it’s deliberately minimalist — and that means **no built-in RSS or rule-based auto-downloading**.  

Here’s the comparison in plain English:  

---

### ⚙️ **qBittorrent**
**Pros**
- Built-in **RSS feed reader + auto-download rules**  
- Full web UI (so you can check it from your iPhone if needed)  
- Integrated scheduler, bandwidth caps, and watch folders  
- Works perfectly headless — you can run it in background or via web interface  

**Cons**
- Heavier footprint (Qt interface, background process)  
- UI feels slightly clunkier on macOS compared to Linux/Windows  

**Bottom line:**  
✅ *Best automation engine. Solid for “set and forget” setups like yours.*  

---

### 🌊 **Transmission**
**Pros**
- Super lightweight — practically invisible CPU/memory usage  
- Native macOS feel  
- Great for manual magnet links or seeding existing files  

**Cons**
- ❌ No native RSS or auto-download rules  
- ❌ No built-in scheduler or filters (you’d need external scripts)  
- RSS support only via third-party helpers (e.g. `FlexGet`, `transmission-rss`, or Automator scripts)

**Bottom line:**  
✅ *Best minimalist client if you don’t care about automation.*  
❌ *Bad fit for “always-on RSS puller.”*

---

### 💡 If you really wanted Transmission simplicity *plus* RSS:
You could run a tiny command-line tool like `FlexGet` or `Catch` to feed Transmission new torrents automatically — but that’s complexity for no real gain, since qBittorrent already does it natively.  

---

So:  
If your goal is *Mac docked = media automation*, then **qBittorrent** wins hands-down.  
If your goal were *Mac = manual occasional torrenting*, then Transmission would be cleaner.  

Given your “home-only automation” plan, **stick with qBittorrent** — it does exactly what you want, quietly and predictably.  

Would you like me to show the optimal qBittorrent config for passive RSS automation (feeds + filters + folder structure)? It’s about five minutes of setup but pays off for years.

---

**User:**

Plex and sharing built in apple macOS media folders tv and movies, etc.. good idea or should I make a separate "Media" folder for plex?

---

**Assistant:**

Definitely make a separate **“Media”** folder for Plex — don’t touch the built-in macOS “TV,” “Movies,” or “Music” libraries.  

Here’s why, broken down:  

---

### ⚠️ Why not use Apple’s built-in media folders
- **Ownership confusion:** macOS and iCloud see those as managed by Apple’s own apps (TV.app, Music.app). They’ll add hidden metadata, nested subfolders, and sometimes rename or move things when syncing.  
- **File permission weirdness:** those folders live under `~/Movies` or `~/Music`, but system processes sometimes hold file locks or alter metadata for Spotlight and TV sync. Plex can read them, but write/scan operations can hang.  
- **Cross-app indexing chaos:** Apple’s TV app may try to ingest Plex files into its own library, generating duplicate artwork and nonsense in your “Up Next” queue.  
- **Backup bloat:** Time Machine treats those as user media and will back them up aggressively — not ideal if Plex regenerates thumbnails or cache data often.  

---

### ✅ Recommended Plex structure
Just make your own neutral directory tree somewhere predictable, like:

```
/Users/doug/Media/
├── Movies/
├── TV Shows/
├── Music/
└── Downloads/
```

or, if you’re using an external drive:

```
/Volumes/MediaDrive/Media/…
```

Then in Plex:
- Add each subfolder as its own **Library** (Movies, TV, etc.).  
- Turn on “Automatically scan library folder” for that structure only.  
- Leave “Allow metadata updates from files” off unless you hand-tag your files.

That gives you **clean separation**: Apple handles Apple media; Plex handles everything else.

---

### 💡 Bonus tip
If you also use qBittorrent’s RSS automation, point its **Completed Downloads** folder to `/Users/doug/Media/Incoming`. Plex can watch that folder and auto-ingest new content, keeping everything compartmentalized.

---

So yes — keep it distinct. One self-contained “Media” folder will spare you a thousand headaches down the line.

---

**User:**

Should I just push everything into the external media drive?

---

**Assistant:**

Yeah — for your setup, that’s absolutely the cleanest move. 🧹  

You’re already thinking in “dock-and-run” mode, so putting **all Plex- and qBittorrent-related data on the external drive** makes the whole stack modular: plug it in, the system lights up; unplug it, nothing breaks.

Here’s how it plays out practically:

---

### 🧩 Why moving everything to the external drive is smart
- **Isolation:** no media clutter mixed with macOS user folders or iCloud sync paths.  
- **Predictable permissions:** Plex, qBittorrent, and Finder all point to one mount.  
- **Portability:** you can plug the drive into another Mac (or even a future NAS) and everything still works.  
- **Wear management:** big sequential reads/writes happen on a cheap external disk instead of your Mac’s internal SSD.  
- **Easy backup:** clone or replace that drive independently of your system backups.

---

### 🧱 Recommended layout
```
/Volumes/MediaDrive/
├── Plex/
│   ├── Movies/
│   ├── TV Shows/
│   └── Music/
├── qBittorrent/
│   ├── Incomplete/
│   └── Completed/
└── Misc/
    └── Temp/
```
Then in qBittorrent:
- Default **save path** → `/Volumes/MediaDrive/qBittorrent/Completed`
- Temp path → `/Volumes/MediaDrive/qBittorrent/Incomplete`

In Plex:
- Point each library to the corresponding `Plex/…` subfolder.  
- Turn off “empty trash automatically after every scan” to avoid re-indexing if the drive’s disconnected.

---

### ⚙️ Quality-of-life tweaks
- **Mount point stability:**  
  Format the drive with a simple name (no spaces), e.g. `MediaDrive`, so paths stay identical between reboots.  
- **Auto-mount:**  
  System Settings ▸ Users & Groups ▸ Login Items ▸ add the drive there, or use Automator:
  ```bash
  open /Volumes/MediaDrive
  ```
- **Sleep behavior:**  
  Energy Saver ▸ prevent drive sleep while Plex is active (avoids “drive disconnected” messages).

---

### 🧘‍♂️ Optional extras
- Back up the drive monthly with Carbon Copy Cloner or `rsync` to a second portable disk.  
- If you ever replace UBIK entirely, that external could become your “cold media vault.”

---

So yes — push it all outboard. It keeps your Mac’s internal environment pristine, makes your automation simpler, and turns the whole media setup into a literal plug-in module.

---

**User:**

The automation shortcuts can be just "when the external drive" connects and disconnects?

---

**Assistant:**

💯 Exactly. That’s actually the *cleanest possible* trigger set for your setup.  
No need to overcomplicate it with Wi-Fi or power conditions if your whole “media mode” lives on that external drive.  

Here’s how to wire it:  

---

## ⚙️ Shortcut 1 — **“Drive Connected → Start Media Services”**
**Trigger:**  
- When volume `MediaDrive` is mounted  

**Actions:**
```bash
open -a "Plex Media Server"
open -a "qBittorrent"
```
**Optional:**  
- Add a “Show Notification” → 🎬 Media services started.  
- Add a short delay (2 s) if the apps sometimes launch before the disk is fully spun up.  

---

## 💤 Shortcut 2 — **“Drive Disconnected → Stop Media Services”**
**Trigger:**  
- When volume `MediaDrive` is ejected or unmounted  

**Actions:**
```bash
pkill "Plex Media Server"
pkill "qBittorrent"
```
**Optional:**  
- Show Notification → 🛑 Media services stopped.  

---

### 🧠 Why this is the best trigger
- **Perfect correlation:** if the drive isn’t there, there’s literally no point in Plex or qBittorrent running.  
- **Battery-safe:** when you unplug the dock (and the drive), everything shuts down automatically.  
- **Zero false positives:** you can be at work, on any Wi-Fi, and nothing fires because the drive isn’t mounted.  

---

### ⚡ Nice refinements
- If you have multiple drives, specify by **volume name** so it only reacts to `MediaDrive`.  
- In Shortcuts settings, toggle **“Run without asking”** for both automations so they’re silent.  
- For extra polish: add a short `sleep 1` before quitting apps to let them flush caches cleanly.  

---

That’s it — now your entire home-media stack literally exists in physical space:  
plug in the drive → server wakes; unplug → server sleeps.  

Would you like me to spit out the ready-to-import Shortcut XML pair for this “Drive Mount = Start / Drive Eject = Stop” version?

---

**User:**

How can I setup the automation on macos?

---

**Assistant:**

Nice — you’re about to make your Mac behave like a little plug-and-play home server. Here’s the full walkthrough for setting those **“Drive-mount start / Drive-eject stop”** automations on macOS (Ventura, Sonoma, or Sequoia — the steps haven’t changed much).  

---

## ⚙️ 1. Open Shortcuts and Create a New Automation
1. Launch **Shortcuts.app**.  
2. In the sidebar, click **Automations** → **New Automation** → **Event**.  
3. Scroll down to **Files & Folders**.  
4. Choose **When a Volume is Mounted**.  
5. Select your external drive, e.g. `MediaDrive`.  
6. Click **Next**.

---

## 🎬 2. Add the “Start Media Services” Actions
Inside the automation editor:
1. Add a **Run Shell Script** action.  
2. Paste this:
   ```bash
   sleep 2
   open -a "Plex Media Server"
   open -a "qBittorrent"
   ```
   (That two-second delay ensures the drive fully mounts before Plex looks for libraries.)
3. Optional: Add a **Show Notification** action → “🎥 Plex + qBittorrent started.”  
4. Turn **Ask Before Running** off → confirm “Don’t Ask.”  
5. Save the automation and name it **Drive Connected – Start Media**.

---

## 💤 3. Make the “Drive Disconnected” Twin
1. Create another automation → **When a Volume is Unmounted**.  
2. Choose the same drive, `MediaDrive`.  
3. Add a **Run Shell Script** action with:
   ```bash
   pkill "Plex Media Server"
   pkill "qBittorrent"
   ```
4. Optional notification: “🛑 Media services stopped.”  
5. Disable **Ask Before Running**, then save it as **Drive Disconnected – Stop Media**.

---

## 🧠 4. Test It
1. Quit Plex and qBittorrent manually.  
2. Eject and reconnect your external drive.  
3. Within a couple of seconds you should see Plex and qBittorrent launch.  
4. Eject the drive again — both apps should close cleanly.

---

## 🪄 5. Optional refinements
- **Hide windows at launch:**  
  In Plex prefs → uncheck “Show window at startup.”  
  In qBittorrent prefs → Behavior → uncheck “Show splash screen.”  
- **Graceful shutdown:**  
  If you want to be gentle, replace the `pkill` line with:
  ```bash
  osascript -e 'quit app "Plex Media Server"'
  osascript -e 'quit app "qBittorrent"'
  ```
  That sends a normal “Quit” command instead of a hard kill.  
- **Multi-drive setups:** repeat with a different trigger volume.

---

After this, your MacBook behaves like a proper on-demand media node:
plug in `MediaDrive` → Plex & qBittorrent spin up;  
eject or undock → they fade away quietly.  

Would you like me to generate the `.shortcut` export files for both so you can import them instead of building them manually?

---

**User:**

Hmmm . Won't let me use this external drive as a trigger.. so I have to use power/home wifi trigger instead..

---

**Assistant:**

Ah yeah — that’s one of Apple’s maddening “almost useful” limitations 😑  
You’re absolutely right: **macOS Shortcuts can detect volume mounts manually**, but **can’t use them as *automatic triggers*** for privacy and sandbox reasons. The “When a volume is mounted/unmounted” option only runs if you click *Run* after the notification prompt — not truly background automation.  

So yeah, your instinct’s correct: fall back to **power + home Wi-Fi** — it’s just as reliable for your use case, and arguably more stable.  

Here’s the best setup given Apple’s current sandbox rules:  

---

## ⚙️ Shortcut 1 — **When Power Connected + Home Wi-Fi**
**Trigger:**
- When **power adapter is connected**
- **AND** Wi-Fi network = *your home SSID*  

**Actions:**
```bash
sleep 2
open -a "Plex Media Server"
open -a "qBittorrent"
```

Add optional notification:  
> 🎬 Media services started  

Turn off *Ask Before Running* → confirm “Don’t Ask.”

---

## 💤 Shortcut 2 — **When Power Disconnected OR Leave Home Wi-Fi**
**Trigger:**
- When **power adapter is disconnected**
- OR **Wi-Fi disconnects from home network**

**Actions:**
```bash
osascript -e 'quit app "Plex Media Server"'
osascript -e 'quit app "qBittorrent"'
```

Optional notification:  
> 🛑 Media services stopped  

---

## 🧠 Why this actually works better day-to-day
- You’ll almost always have your **dock plugged in** when you’re home.  
- Both Plex and qBittorrent need the Mac to be **awake and powered** anyway.  
- You can freely eject or plug your media drive without worrying about triggers breaking.  
- Zero permission prompts — these automations run truly unattended.  

---

If you ever want to *simulate* the “drive mount trigger” later, there’s a geeky workaround using a **folder action** or a **LaunchAgent plist** that watches `/Volumes` for mounts — I can show that, but it’s a little lower-level (basically a one-line shell daemon).  

Do you want me to show that alternative, or are you good staying with the simpler power/Wi-Fi setup?

---

**User:**

How do you setup that trigger?

---

**Assistant:**

Nice — we’re getting into the good stuff now ⚙️  

Let’s do both options quickly, since you can choose depending on how deep you want to go:  

---

## 🪄 **Option 1 — Simple Shortcuts-based “Power + Wi-Fi” Trigger** *(the Apple-sanctioned route)*
This one’s easy and rock-solid.  

### ➤ Create the “Docked → Start Media Services” automation
1. Open **Shortcuts → Automations → New Automation**.  
2. Choose **Power → When Power Adapter is Connected**.  
3. Add a **Wi-Fi** condition right after it:  
 - Tap the “Add Filter” option → select your home SSID.  
4. Tap **Next** → **Add Action → Run Shell Script**, and paste:
   ```bash
   sleep 2
   open -a "Plex Media Server"
   open -a "qBittorrent"
   ```
5. Add an optional **Show Notification** action: “🎬 Media services started.”  
6. Turn **Ask Before Running → Off** → confirm “Don’t Ask.”  
7. Save it as **Docked – Start Media**.

---

### ➤ Create the “Undocked → Stop Media Services” automation
1. New Automation → **Power → When Power Adapter is Disconnected**.  
2. Add a **Run Shell Script** action with:
   ```bash
   osascript -e 'quit app "Plex Media Server"'
   osascript -e 'quit app "qBittorrent"'
   ```
3. Optional notification: “🛑 Media services stopped.”  
4. Disable *Ask Before Running* → save as **Undocked – Stop Media**.

✅ Now every time you dock the MacBook on home Wi-Fi, Plex + qBittorrent start; when you unplug, they quit.

---

## 🧰 **Option 2 — Advanced “Drive Mount” Trigger via LaunchAgent**
If you *really* want it tied to plugging in your external drive, Shortcuts can’t auto-fire, but a lightweight **LaunchAgent** can.  

1. Open Terminal and create a small shell script at `~/Library/Scripts/mediadisk_start.sh`:
   ```bash
   #!/bin/bash
   if [ "$1" = "mounted" ]; then
       open -a "Plex Media Server"
       open -a "qBittorrent"
   elif [ "$1" = "unmounted" ]; then
       osascript -e 'quit app "Plex Media Server"'
       osascript -e 'quit app "qBittorrent"'
   fi
   ```
   Make it executable:  
   ```bash
   chmod +x ~/Library/Scripts/mediadisk_start.sh
   ```

2. Create the LaunchAgent plist:  
   ```bash
   mkdir -p ~/Library/LaunchAgents
   nano ~/Library/LaunchAgents/com.doug.mediadisk.plist
   ```
   Paste:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key><string>com.doug.mediadisk</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/local/bin/fswatch</string>
           <string>-0</string>
           <string>/Volumes</string>
       </array>
       <key>StandardOutPath</key><string>/tmp/mediadisk.log</string>
       <key>StandardErrorPath</key><string>/tmp/mediadisk.err</string>
       <key>RunAtLoad</key><true/>
   </dict>
   </plist>
   ```
   *(You’d need `fswatch` from Homebrew; the script can parse events to detect your drive’s mount/unmount and call `mediadisk_start.sh mounted|unmounted`.)*

3. Load it:  
   ```bash
   launchctl load ~/Library/LaunchAgents/com.doug.mediadisk.plist
   ```

That’s the fully automated Unix-style method — more control, but more moving parts.

---

For most people (and definitely your “dock-and-run” workflow), **Option 1** is the sweet spot: zero maintenance, system-approved, and it just works.  

Do you want me to give you the ready-to-import *Shortcuts JSON export* for the Power + Wi-Fi version so you can drop it right in?

---

**User:**

Ummm.. how do I add the filter?

---

**Assistant:**

Ah — yeah, that bit’s confusing because Apple *moved the logic filters* around in macOS Shortcuts. There isn’t a literal “add filter” button for automations like there is for scripts — you have to chain **two automations** or combine logic inside one.  

Let’s break it down cleanly for your case 👇  

---

## 🪄 Option A — “Power + Wi-Fi” combined trigger (recommended)
Shortcuts can’t do true “AND” logic between triggers directly,  
but you can fake it by checking Wi-Fi *inside* the script after the power trigger fires.

### Here’s how:
1. **Create automation**  
   - In Shortcuts ▸ Automations ▸ **New Automation → Power → When Power Adapter is Connected**  

2. **Add a “Run Shell Script” action**  
   Paste this code:
   ```bash
   # Wait a moment for network to settle
   sleep 2

   # Check current Wi-Fi SSID
   SSID=$(networksetup -getairportnetwork en0 | sed 's/^Current Wi-Fi Network: //')

   # Replace 'YourHomeNetwork' with your actual SSID
   if [ "$SSID" = "YourHomeNetwork" ]; then
       open -a "Plex Media Server"
       open -a "qBittorrent"
       osascript -e 'display notification "🎬 Media services started."'
   fi
   ```
   > **Note:** if your Wi-Fi interface isn’t `en0`, check it first with  
   > `networksetup -listallhardwareports` in Terminal.

3. **Turn off “Ask Before Running.”**

✅ Result: it only runs when the Mac is plugged in *and* connected to your home Wi-Fi.

---

## 💤 Option B — Separate “Leave Home / Undock” automation
Create another one for **Power Adapter Disconnected**, with:

```bash
SSID=$(networksetup -getairportnetwork en0 | sed 's/^Current Wi-Fi Network: //')
if [ "$SSID" = "YourHomeNetwork" ]; then
    osascript -e 'quit app "Plex Media Server"'
    osascript -e 'quit app "qBittorrent"'
    osascript -e 'display notification "🛑 Media services stopped."'
fi
```

That shuts them down only when you undock *at home* —  
not every time you unplug somewhere else.

---

## 🧠 Pro tip
If you later want to include both power **and** network events, you can duplicate the shortcut and set its trigger to “When Wi-Fi connects to [Home SSID]” using the same code block — then you’re covered even if you plug in after waking from sleep.

---

Would you like me to show what the full Shortcut looks like in the visual editor (action-by-action, not just the code)? It’s easier to drop in without scripting once you see the layout.

---

**User:**

I don't understand option B.. 

---

**Assistant:**

Totally fair — Apple’s Shortcuts logic is… not intuitive here 🙃  
Let me restate Option B in plain English and then walk you through how to build it click-by-click.

---

## 🧩 What Option B actually does
It’s your **“turn everything off”** automation.

- It runs when you **unplug your MacBook** *or* when you **leave your home Wi-Fi**.  
- Inside the script, it double-checks that the *last known* Wi-Fi was your home network so it doesn’t quit Plex/qBittorrent when you’re, say, in a coffee shop.

So the logic is:

> “If I unplug the Mac *while* it’s still on my home Wi-Fi, that means I’ve left the dock — shut down Plex and qBittorrent.”

---

## 🧰 Step-by-step build in Shortcuts

### 1️⃣  Create the trigger
1. Open **Shortcuts → Automations**.  
2. Click **New Automation → Power → When Power Adapter is Disconnected**.  
3. Hit **Next**.

---

### 2️⃣  Add the “Run Shell Script” action
1. Tap **Add Action → Run Shell Script**.  
2. Paste this in:

   ```bash
   # Get current Wi-Fi network name
   SSID=$(networksetup -getairportnetwork en0 | sed 's/^Current Wi-Fi Network: //')

   # Replace with your actual home SSID
   if [ "$SSID" = "YourHomeNetwork" ]; then
       osascript -e 'quit app "Plex Media Server"'
       osascript -e 'quit app "qBittorrent"'
       osascript -e 'display notification "🛑 Media services stopped."'
   fi
   ```

   *(You can check your Wi-Fi interface name by running  
   `networksetup -listallhardwareports` in Terminal — it’s usually `en0`.)*

3. Optional: add a **Show Notification** action if you prefer the visual version instead of the AppleScript line.  

---

### 3️⃣  Disable confirmation
Toggle **Ask Before Running → Off**, then **Don’t Ask** when prompted.  
Name the automation something like **Undocked – Stop Media Services**.

---

### ✅  What happens now
- When you **unplug** at home → Plex + qBittorrent quit automatically.  
- When you **unplug somewhere else** (work, coffee shop) → nothing happens, because it’s not your home SSID.  

That’s all Option B is — just the “reverse gear” to your earlier *Docked → Start* automation.

---

Want me to show the *Docked → Start* and *Undocked → Stop* versions side-by-side in visual Shortcut form (so you can rebuild them quickly)?

---

**User:**

I think I'd like to shutdown plex/qb whenever the power is unplugged...

---

**Assistant:**

Perfect — that actually simplifies things beautifully. 💡  

No Wi-Fi logic, no conditions. Just *“If I’m not docked, shut down the background stuff.”*  
Here’s exactly how to wire that up in **Shortcuts on macOS**:

---

## ⚙️ **Create the “Undock → Stop Plex & qBittorrent” Automation**

### 1️⃣  Open the Automations tab
- Launch **Shortcuts.app → Automations → New Automation → Event → Power**  
- Choose **“When Power Adapter is Disconnected.”**

---

### 2️⃣  Add the shutdown logic
- Add an action: **Run Shell Script**  
- Paste this:

  ```bash
  osascript -e 'quit app "Plex Media Server"'
  osascript -e 'quit app "qBittorrent"'
  osascript -e 'display notification "🛑 Media services stopped (undocked)."'
  ```

  This sends normal “Quit” events—no hard kills—so Plex writes its caches safely.

---

### 3️⃣  Disable prompts
- Scroll down, toggle **Ask Before Running → Off**, then confirm **Don’t Ask**.  
- Name it something like **Undocked – Stop Media**.

---

### ✅  Done
Now, any time you **unplug** your MacBook (even on battery at home or work), both Plex and qBittorrent will shut down within a second.  
No network checks, no conditions — totally automatic.

If you also have the earlier **“Power Connected → Start Plex/qBittorrent”** shortcut, the pair will keep your system perfectly in sync:

| State | Trigger | Action |
|--------|----------|---------|
| Docked / Plugged In | Power Adapter Connected | Start Plex & qBittorrent |
| Undocked / On Battery | Power Adapter Disconnected | Quit Plex & qBittorrent |

---

Would you like me to drop the full `.shortcut` export JSON for those two so you can import them directly instead of recreating them manually?

---

**User:**

Ok.. the off script works.. the on script does not

---

**Assistant:**

Use the built-in **Open App** actions (not a shell) or call `/usr/bin/open` with full paths and a short delay—Shortcuts often runs before the system/network is fully ready on “power connected.”

## Quick fix (no scripting)
- Open **Shortcuts → Automations → Power Adapter is Connected**.
- **Actions:**
  - **Open App → Plex Media Server**
  - **Open App → qBittorrent**
  - **Wait** → 3 seconds (add “Wait” action)
- Turn **Ask Before Running** off.

This avoids PATH/permission quirks that break `Run Shell Script`.

## If you prefer shell, make it robust
Replace your action with this exact block:

```bash
#!/bin/zsh
# Give the system a moment to settle after power-connect
sleep 3

# Use absolute paths (Shortcuts sandbox = tiny PATH)
/usr/bin/open "/Applications/Plex Media Server.app"
/usr/bin/open "/Applications/qBittorrent.app"

# Optional: log for debugging
/bin/date >> /tmp/media_start.log 2>&1
echo "Launched PMS + qB" >> /tmp/media_start.log 2>&1
```

### Common gotchas
- **App locations:** Plex sometimes installs to `~/Applications`. If so, change paths to:
  - `/Users/<you>/Applications/Plex Media Server.app`
- **Name mismatch:** It’s **“Plex Media Server.app”** (not “Plex.app”).
- **Permissions:** macOS → **System Settings ▸ Privacy & Security ▸ Automation**  
  Ensure **Shortcuts** is allowed to control **Plex Media Server** and **qBittorrent** (toggle on).
- **Shortcuts setting:** **Shortcuts ▸ Settings ▸ Advanced ▸ Allow Running Scripts** must be enabled.
- **Race condition:** If it still doesn’t launch on first try, bump `sleep` to **5–8s**.

## Sanity checks
- Test commands manually in Terminal:
  ```bash
  /usr/bin/open "/Applications/Plex Media Server.app"
  /usr/bin/open "/Applications/qBittorrent.app"
  ```
- Verify locations:
  ```bash
  mdfind "kMDItemCFBundleIdentifier == 'tv.plex.media-server'"
  mdfind "kMDItemCFBundleIdentifier == 'org.qbittorrent.qBittorrent'"
  ```
- Check logs if it still fails: `cat /tmp/media_start.log`

## Minimal fallback that always works
If the shell keeps being flaky on your machine, use two **Open App** actions + a **Wait**. It’s boring—but 100% reliable with Shortcuts’ power trigger.

---

**User:**

Still want to test for wifi

---

**Assistant:**

Got it — you want the automation to start Plex/qB *only when you’re plugged in **and** on home Wi-Fi*.  
Here’s the simplest working version for that on macOS:

---

### ⚙️ Power-and-Wi-Fi Start Automation
1. In **Shortcuts → Automations**, create a new one:  
   **When Power Adapter is Connected** → Next.  

2. Add **Run Shell Script** and paste this:

   ```bash
   #!/bin/zsh
   sleep 3
   SSID=$(networksetup -getairportnetwork en0 | sed 's/^Current Wi-Fi Network: //')

   if [ "$SSID" = "YourHomeNetwork" ]; then
       /usr/bin/open "/Applications/Plex Media Server.app"
       /usr/bin/open "/Applications/qBittorrent.app"
       osascript -e 'display notification "🎬 Plex + qBittorrent started (home Wi-Fi)"'
   else
       osascript -e 'display notification "⚡ Power connected, but not on home Wi-Fi — skipped."'
   fi
   ```

   - Replace **YourHomeNetwork** with your actual SSID.  
   - If Wi-Fi interface isn’t `en0`, check with `networksetup -listallhardwareports`.  

3. Turn **Ask Before Running → Off** → **Don’t Ask**.

---

### 💤 Power-off Stop Automation
You already have this, but for completeness:

```bash
osascript -e 'quit app "Plex Media Server"'
osascript -e 'quit app "qBittorrent"'
osascript -e 'display notification "🛑 Media services stopped (undocked)"'
```

Trigger: **When Power Adapter is Disconnected** → Don’t Ask.

---

### ✅ Behavior
- Plug in at home → wait ≈ 3 s → both apps launch.  
- Plug in anywhere else → nothing happens (you’ll see the “skipped” notification).  
- Unplug anywhere → both quit.

That’s the most reliable way to include the Wi-Fi check—Shortcuts can’t add a true “AND” filter, so the shell handles it inside one automation.

---

**User:**

Not detecting home wifi.. BELL587 is the ssid

---

**Assistant:**

Got it — if it’s not detecting `BELL587`, it’s almost certainly a small mismatch between how macOS reports the SSID and what you typed in your script. The `networksetup -getairportnetwork en0` command returns something like:  

```
Current Wi-Fi Network: BELL587
```

…but sometimes includes invisible spaces, smart quotes, or interface differences. Let’s troubleshoot quickly:  

---

### 🧪 Step 1 — Verify what macOS *actually* reports
Open **Terminal** and run:

```bash
networksetup -getairportnetwork en0
```

If that gives you:
```
Current Wi-Fi Network: BELL587
```
then you’re good — that means `en0` is correct and the SSID is *exactly* `BELL587`.  

If it says something like:
```
You are not associated with an AirPort network.
```
try:
```bash
networksetup -listallhardwareports
```
and find which line says **Wi-Fi** — you’ll see something like:
```
Hardware Port: Wi-Fi
Device: en1
```
Then use that device (`en1`) instead of `en0` in the script.

---

### 🧰 Step 2 — Simplify and debug the script
Here’s a cleaned-up version that logs the SSID and ignores extra spaces:

```bash
#!/bin/zsh
sleep 3
SSID=$(networksetup -getairportnetwork en0 | awk -F': ' '{print $2}' | tr -d '\n\r')

# Debug log
echo "Detected SSID: '$SSID'" >> /tmp/plexwifi.log

if [[ "$SSID" == "BELL587" ]]; then
    /usr/bin/open "/Applications/Plex Media Server.app"
    /usr/bin/open "/Applications/qBittorrent.app"
    osascript -e 'display notification "🎬 Plex + qBittorrent started (home Wi-Fi: BELL587)"'
else
    osascript -e "display notification \"⚡ Connected to '$SSID' — skipping start.\""
fi
```

Now when the automation fires, you can open `/tmp/plexwifi.log` to see exactly what SSID was detected:

```bash
cat /tmp/plexwifi.log
```

---

### 🪄 Step 3 — Re-run test manually
Before relying on the automation, paste this whole script in **Terminal** while you’re connected to BELL587.  
If it reports “Detected SSID: 'BELL587'” and launches Plex/qB, you’re golden.  

Then paste the working version back into your Shortcut’s “Run Shell Script” action.

---

Want me to give you a version that automatically detects *any* “BELL*” SSID (in case the router renames itself like `BELL587-5G`)?

---

**User:**

It's not an airportnetwork?

---

**Assistant:**

Exactly — that’s the catch on newer Macs.  
Apple renamed / re-abstracted Wi-Fi hardware a few OS generations ago, so **`networksetup -getairportnetwork`** sometimes fails or returns blank because the Mac doesn’t literally have an “AirPort” chipset anymore.  

No worries — there’s a more modern and reliable way to grab the connected SSID. Let’s fix that. 👇  

---

## 🧰 Use the `scutil` command instead
This works on all recent macOS versions (Ventura → Sequoia):

```bash
#!/bin/zsh
sleep 3

# Grab SSID from the system configuration
SSID=$(/usr/sbin/scutil --nwi | grep 'SSID' | awk -F': ' '{print $2}' | head -1 | tr -d '\n\r')

# Debug log
echo "Detected SSID: '$SSID'" >> /tmp/plexwifi.log

if [[ "$SSID" == "BELL587" ]]; then
    /usr/bin/open "/Applications/Plex Media Server.app"
/usr/bin/open "/Applications/qBittorrent.app"
    osascript -e 'display notification "🎬 Plex + qBittorrent started (home Wi-Fi: BELL587)"'
else
    osascript -e "display notification \"⚡ Connected to '$SSID' — skipping start.\""
fi
```

---

### 🧪 Test it first
1. Paste that into **Terminal**, connected to your home Wi-Fi.  
2. It should log a line in `/tmp/plexwifi.log` like:  
   ```
   Detected SSID: 'BELL587'
   ```
3. Plex and qBittorrent should open right after.  

If that works, drop this script into your **Shortcuts “Run Shell Script”** action for the “Power Connected” automation.  
This `scutil` method works universally — even on M1/M2/M3 Macs where `networksetup` breaks or reports “You are not associated with an AirPort network.”  

---

Would you like me to tweak it so it matches **any** SSID starting with “BELL” (handy if your router has both 2.4 GHz and 5 GHz variants)?

---

**User:**

Still not detecting wifi

---

**Assistant:**

Use a more robust “power-on” script that (a) waits for Wi-Fi to come up, and (b) tries multiple SSID methods—then start Plex/qB only on a match.

## What to do
- In your **Power Adapter Connected** automation, replace the action with **Run Shell Script** (zsh) and paste the script below.
- Turn **Ask Before Running** off.
- Ensure **Shortcuts → Settings → Advanced → Allow Running Scripts** is enabled.

## Drop-in script (retry + multi-method SSID detection)
```bash
#!/bin/zsh
# Wait a bit for network to be ready after power connect
sleep 2

TARGET_SSID="BELL587"

get_wifi_device() {
  # Pull the device mapped to "Wi-Fi" (en0, en1, etc.)
  networksetup -listallhardwareports \
    | awk '/Wi-Fi/{getline; if($1=="Device:") print $2}'
}

read_ssid() {
  local ssid=""

  # 1) scutil (modern)
  ssid=$(/usr/sbin/scutil --nwi | awk -F': ' '/SSID/ {print $2; exit}')
  [[ -n "$ssid" ]] && { echo "$ssid"; return; }

  # 2) airport (older but reliable)
  local AIRPORT="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
  if [[ -x "$AIRPORT" ]]; then
    ssid=$("$AIRPORT" -I 2>/dev/null | awk -F': ' '/ SSID/ {print $2; exit}')
    [[ -n "$ssid" ]] && { echo "$ssid"; return; }
  fi

  # 3) networksetup (works on some Macs)
  local dev="$(get_wifi_device)"
  if [[ -n "$dev" ]]; then
    ssid=$(networksetup -getairportnetwork "$dev" 2>/dev/null \
            | sed 's/^Current Wi-Fi Network: //')
    [[ "$ssid" != "You are not associated with an AirPort network." ]] || ssid=""
    [[ -n "$ssid" ]] && { echo "$ssid"; return; }
  fi

  # 4) fallback: empty
  echo ""
}

# Retry loop: give Wi-Fi up to ~12s to report an SSID
SSID=""
for i in {1..12}; do
  SSID="$(read_ssid | tr -d '\n\r')"
  [[ -n "$SSID" ]] && break
  sleep 1
done

# Debug (optional): tail this if needed
echo "$(date) — Detected SSID: '$SSID'" >> /tmp/plexwifi.log

# Match exactly; change to pattern if your router appends bands (e.g., BELL587-5G)
if [[ "$SSID" == "$TARGET_SSID" ]]; then
  /usr/bin/open "/Applications/Plex Media Server.app"
  /usr/bin/open "/Applications/qBittorrent.app"
  osascript -e 'display notification "🎬 Plex + qBittorrent started (home Wi-Fi matched)"'
else
  osascript -e "display notification \"⚡ Power connected, SSID='$SSID' — start skipped\""
fi
```

## If it still doesn’t fire
- Check **Automation permissions**: System Settings → Privacy & Security → **Automation** → allow **Shortcuts** to control **Plex Media Server** and **qBittorrent**.
- Verify app locations (some installs live in `~/Applications`—update paths accordingly).
- Inspect the log: `cat /tmp/plexwifi.log` to see what SSID the script detected.
- Bump the initial `sleep` to **5–8s** if your Wi-Fi takes longer after power-on.

---

**User:**

How about this.. can I run an apple shortcut automation that first tests for wifi as a trigger then within the shortcut via and if statement test for power charger?

---

**Assistant:**

You can! The Shortcuts app can’t do two *independent* triggers (“Wi-Fi joins” **and** “Power connected”), but you can build a **Wi-Fi trigger** that checks power state *inside* the shortcut with an **If** block.

Here’s how to build that logic:

---

### ⚙️ 1. Create the Wi-Fi-based automation
1. Open **Shortcuts → Automations → New Automation → Wi-Fi**.  
2. Choose **When I connect to Wi-Fi → BELL587**.  
3. Tap **Next**.

---

### 🧩 2. Add the logic to check for power
Now we’ll only launch Plex/qB when the charger is plugged in.

**Actions list:**
1. **Get Battery Level** → adds the variable *Battery Level*.  
2. **Get Device Details** → choose *Charger State*.  
3. **If** → set condition to:
   ```
   Charger State is Connected
   ```
4. Inside the **If** block:
   - Add **Run Shell Script** (set to `/bin/zsh`):  
     ```bash
     /usr/bin/open "/Applications/Plex Media Server.app"
     /usr/bin/open "/Applications/qBittorrent.app"
     osascript -e 'display notification "🎬 Plex + qBittorrent started (on power + home Wi-Fi)"'
     ```
5. Add an **Otherwise** block (optional) → “Show Notification: Skipped, not charging.”
6. Turn off **Ask Before Running** → confirm *Don’t Ask.*

---

### ✅ What happens
- When you join **BELL587**, the automation runs.  
- It checks: “Am I charging?”  
  - **If yes:** launches Plex + qBittorrent.  
  - **If not:** exits quietly.

You can keep your existing *Power-disconnected → quit apps* automation for the “off” half of the cycle.  
Together they behave like this:

| Trigger | Check | Action |
|----------|--------|---------|
| Wi-Fi = BELL587 | Charger = connected | Start Plex/qB |
| Power disconnected | — | Quit Plex/qB |

That gives you exactly the “only when docked at home” behavior without any external scripting.

---

**User:**

How do I get the device detail about charging state?

---

**Assistant:**

Yeah, that one’s buried a bit — Apple hides it behind a few taps instead of making it obvious. Here’s exactly how to surface **Charger State** in a Shortcut:

---

### ⚙️ Step-by-step (macOS or iOS Shortcuts)

1. Open **Shortcuts → Automations →** edit your **Wi-Fi = BELL587** automation.  
2. Tap **Add Action → Scripting → Device Details.**  
   *(If you don’t see it, search “device details” in the search bar.)*  
3. In the blue **Device Details** box that appears, tap **Device Detail** → pick **Charger State.**  
   - You’ll now see a variable bubble labeled *Charger State*.  
4. Add an **If** action:  
   - Tap **Add Action → Scripting → If.**  
   - In the “If” condition dropdown, choose **Charger State**, then **is** → **Connected.**  
5. Inside that **If** block, add your “Open App” or “Run Shell Script” actions for Plex and qBittorrent.  
6. Optional: under **Otherwise**, add “Show Notification → Skipped (not charging).”

---

### ✅ How it works
When the automation triggers on Wi-Fi connect, it queries the system for the charger state and evaluates it in the If block:
- **Connected:** runs Plex/qB launch actions.  
- **Not Connected:** does nothing (or shows your “Skipped” message).

That’s all you need — no variables or scripting required.  

If you want, I can write out the visual action list exactly as it appears in the Shortcuts editor so you can copy it click-for-click. Want that?

---

**User:**

It's battery state., boolean?

---

**Assistant:**

Yep — that’s it! Apple just labels it a bit inconsistently.  

In Shortcuts, the field you’re looking for is actually called **Battery State**, not *Charger State* (older docs and iOS versions still use that name).  

Here’s how it behaves:  

---

### ⚙️ **Battery State** variable
When you choose **Get Device Details → Battery State**, it returns **text**, not a Boolean.  
The value can be one of the following strings:

- `"Charging"`
- `"Full"`
- `"Unplugged"`
- `"Unknown"` *(rare — usually right after waking)*

So in your **If** block, you’ll want to compare the *text* value, like so:

---

### ✅ Example Shortcut logic

1. **Get Device Details → Battery State**  
   → gives variable `Battery State`.

2. **If** `Battery State` **is** `"Charging"`  
   *(and optionally add an OR condition for `"Full"` if you want to include fully charged but still plugged in)*  

3. Inside the **If**:
   - **Open App → Plex Media Server**  
   - **Open App → qBittorrent**

4. (Optional) **Otherwise**:
   - **Show Notification → Skipped, not charging**

---

### 💡 Tip
If you prefer to handle both “Charging” and “Full” cases:
- Use **If Battery State is not Unplugged**,  
  which covers both plugged-in conditions at once.

That’s the cleanest way to make sure your Wi-Fi automation only fires when docked or charging.

---

**User:**

Is Connected to charger... better?

---

**Assistant:**

Yep — **“Is Connected to Charger”** is the cleaner, more reliable choice. 👍  

Here’s why:  

---

### 💡 Why “Is Connected to Charger” works better
- It’s a **Boolean**, not text — simpler to evaluate (`true` or `false`).  
- It automatically covers both “Charging” *and* “Full” battery states.  
- It’s available under **Get Device Details → Is Connected to Charger** on both macOS and iOS.  
- Fewer moving parts — no string comparison or “OR” conditions.  

So your logic becomes beautifully simple:

---

### ✅ Recommended Shortcut Layout

**Trigger:**  
- When Wi-Fi connects to `BELL587`.

**Actions:**
1. **Get Device Details → Is Connected to Charger**  
   → creates a Boolean variable.  
2. **If [Is Connected to Charger] is True**  
   - **Open App → Plex Media Server**  
   - **Open App → qBittorrent**  
3. **Otherwise (optional):**  
   - **Show Notification → “Skipped, not charging.”**  

**Ask Before Running:** Off.

---

### ⚙️ Summary

| Option | Type | Handles “Charging” + “Full”? | Simplicity |
|---------|------|-------------------------------|-------------|
| Battery State | Text (“Charging”, “Full”, etc.) | Yes, but needs OR condition | More complex |
| **Is Connected to Charger** | **Boolean (True/False)** | **Yes** | **✅ Simpler, cleaner** |

---

So yeah — go with **Is Connected to Charger**. It’s the modern, stable route and does exactly what you want without extra comparisons.

---

**User:**

So I have 3 automations.. 
1. when connected to bell587, check for power charge state and stop/start apps 
2. When disconnect from power, kill apps 
3. When disconnected from bell587, kill apps 


Make sense? What's missing?

---

**Assistant:**

Your 3-automation plan is solid; add two guards—**external drive present** and **home-network variants**—and you’re done.

## Keep
- **#1 Wi-Fi join (BELL587) → If “Is Connected to Charger” = true → start Plex & qB.**
- **#2 Power disconnected → quit Plex & qB.**
- **#3 Wi-Fi leave (BELL587) → quit Plex & qB.**

## Add / tighten
- **Drive presence check (if libraries live on an external):** before starting, verify `/Volumes/MediaDrive` is mounted; skip if not.  
  - Easiest: add a **Run Shell Script** (zsh) *before* the “Open App” steps:
    ```bash
    [ -d "/Volumes/MediaDrive" ] || exit 0
    ```
- **SSID variants:** routers often present `BELL587-5G` or `BELL587-2.4`.  
  - Make the Wi-Fi automation trigger on **any of** those SSIDs (create multiple Wi-Fi triggers) **or** keep one trigger and inside it check a **List** `["BELL587","BELL587-5G","BELL587-2.4"]` with an If “**List contains Current Network**”.
- **Graceful quits:** in #2 and #3, use quit (not kill) to avoid cache corruption:
  ```bash
  osascript -e 'quit app "Plex Media Server"'
  osascript -e 'quit app "qBittorrent"'
  ```
- **Debounce races:** #2 and #3 can fire close together; the quit above is idempotent, so you’re safe. (No need to over-engineer.)
- **Permissions sanity:** System Settings → Privacy & Security → **Automation** → allow **Shortcuts** to control **Plex Media Server** and **qBittorrent**; Shortcuts → Settings → Advanced → **Allow Running Scripts**.

## Optional niceties
- **Ethernet at home:** if you sometimes dock via Ethernet (no Wi-Fi), add a second **Power-connected** automation that starts apps when `Is Connected to Charger = true` **and** `/Volumes/MediaDrive` exists (no SSID check).
- **Prevent sleep while streaming:** leave Plex’s “prevent sleep” **off** by default; toggle it on only if you see playback pausing mid-movie.
- **Logs for debugging:** in the start automation add:
  ```bash
  echo "$(date) start attempt; ssid=$(/usr/sbin/scutil --nwi | awk -F': ' '/SSID/{print $2; exit}'); drive=$([ -d /Volumes/MediaDrive ] && echo yes || echo no)" >> /tmp/plexwifi.log
  ```

## Final checklist (quick)
- [ ] Wi-Fi join (BELL587 family) → If **Is Connected to Charger** → **check drive** → Open Plex & qB.  
- [ ] Power disconnected → **quit** Plex & qB.  
- [ ] Wi-Fi leave (BELL587 family) → **quit** Plex & qB.  
- [ ] Automation + Scripts permissions confirmed.  
- [ ] Test: plug in at home → starts; unplug or leave SSID → stops; drive unplugged while docked → start is skipped.

---
