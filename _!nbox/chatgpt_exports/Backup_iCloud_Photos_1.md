# Backup iCloud Photos

**Created:** 2025-09-19 07:17:22
**Updated:** 2025-12-07 22:31:12
**Turns:** 11

---

**User:**

Thinking about how to backup my iCloud Photos. The a/b robocopy thing I have going on seems to be gakking in photos, largely because iCloud app does a terrible job at marking and keeping photos offline available for the script to work. 

---

**Assistant:**

Stop trying to mirror iCloud Photos with robocopy; make one device pull full-resolution originals and back *that* up with a 3-2-1 plan (local, second device/drive, off-site). citeturn0search10turn0search3

# What’s breaking your A/B robocopy
- iCloud for Windows keeps many items online-only and swaps states in the background, so file attributes change mid-copy and robocopy “gaks.” There’s no reliable “always keep offline” for the whole library on Windows. Apple’s own docs show per-file download behavior, not a persistent offline mirror. citeturn0search9

# Three reliable setups (pick one)

## A) Mac-native “Source of Truth” (simplest, least fragile)
1. On the Mac Photos app: **Photos ▸ Settings ▸ iCloud ▸ Download Originals to this Mac**. Let it fully sync. (Verify free disk space first.) citeturn0search10  
2. Back up the **Photos Library.photoslibrary** bundle:
   - **Local:** Time Machine (hourly).  
   - **Off-site:** a cloud backup client (e.g., Backblaze) targeting the library file.  
   - **Cold copy (optional):** periodic clone to an external drive kept offline. This satisfies 3-2-1. citeturn0search3
3. (Optional export) For an independent, flat-files archive: **File ▸ Export ▸ Export Unmodified Original** (+ “Export IPTC as XMP” for captions/faces/keywords). Store by `YYYY/YYYY-MM`. citeturn0search2turn0search7

**Pros:** Fully supported path; edits/metadata preserved in Photos; robust backups.  
**Cons:** Needs enough local storage (external SSD is fine if always attached and set as System Photo Library).

## B) Headless pull on UBIK (Windows/Linux) with **icloud_photos_downloader** (hands-off, scriptable)
- Run `icloud_photos_downloader` (aka *icloudpd*) on UBIK (Docker, Python, or packaged), set it to **Copy/Sync** mode to fetch all originals to a normal NTFS folder; schedule daily. Then use your existing robocopy jobs against *that* local folder (not iCloud’s). citeturn0search1turn0search16turn0search11

**Pros:** No Photos app needed; creates a stable filesystem mirror; easy to version and de-dupe.  
**Cons:** Community tool; relies on private APIs and 2FA app passwords—rare breakage after Apple changes is possible (usually fixed by maintainers). citeturn0search6

**Tip:** Enable Live Photo downloads (it saves still + video), keep a text log, and organize by `--folder-structure {:%Y/%m}` for clean archives. citeturn0search11

## C) Periodic **official exports/transfers** (belt-and-suspenders)
- Quarterly: use **Apple’s Data & Privacy** portal to request a full iCloud Photos export or **transfer a copy to Google Photos** as a secondary archive. Store the export on UBIK/NAS and include in your normal backups. citeturn0search10turn0search5

**Pros:** First-party copy; good disaster fallback.  
**Cons:** Not continuous; exports are slow and arrive in batches.

# Guardrails & gotchas
- **Don’t back up from iCloud for Windows folders.** Download states are flaky; you’ll chase ghosts. Pull from a *fully local* source (Mac Originals library or icloudpd output). citeturn0search9  
- **Photos Library on external SSD:** keep it consistently attached when Photos is open to avoid re-index churn; let sync finish before backup. citeturn0search4  
- **Flat-file exports vs. library:** “Export Unmodified Original” preserves the original file; edits live in the Photos library. Export XMP sidecars if you need captions/keywords outside Photos. citeturn0search2turn0search7turn0search12

# Recommended for you (fast decision)
- **Primary:** Option A on the Mac (Download Originals) + Time Machine + Backblaze + quarterly cold clone.  
- **Secondary:** Option B running nightly on UBIK to a dated folder tree; keep 90 days of deltas.  
- **Safety net:** Option C once per quarter.

Want me to sketch the exact folder layout, icloudpd command, and a robocopy line for UBIK?

---

**User:**

I kinda wanted to do it all on UBIK unattended. The robo copy thing works well for iCloud Drive and OneDrive. Wish it worked for iCloud Photos

---

**Assistant:**

Right — the snag is iCloud Photos doesn’t behave like iCloud Drive or OneDrive. The Windows iCloud client doesn’t expose a true file tree with stable “always local” files, so robocopy can’t reliably touch it. That’s why it “just works” for Drive/OneDrive but not Photos.  

If you want UBIK to run this unattended, you need to bypass iCloud for Windows entirely:

### Path that works headless
- **`icloudpd` (icloud_photos_downloader)**  
  - Runs on Windows or Linux.  
  - Logs into iCloud with 2FA and pulls full-resolution originals into a normal folder tree (`YYYY/MM/DD` if you want).  
  - Scriptable and cron-friendly, so UBIK can fetch deltas daily without you touching it.  
  - Once files are local, your A/B robocopy system will handle them perfectly.

### Why this beats iCloud for Windows
- Files are guaranteed *actual* JPEG/HEIC/MP4, not online-only placeholders.  
- No flaky “download on demand.”  
- Works exactly like your OneDrive/iCloud Drive mirror: plain files on disk, versioned however you want.

### Practical setup
1. Install `icloudpd` on UBIK (Python pip or Docker).  
2. Create an app-specific password in Apple ID settings.  
3. First run:  
   ```bash
   icloudpd --directory D:\iCloudPhotos --username you@icloud.com --folder-structure {:%Y\%m\%d} --auto-delete
   ```  
   (Folder structure is flexible; omit `--auto-delete` if you want to keep deletions.)  
4. Schedule via Task Scheduler (Windows) or cron (Linux VM).  
5. Let robocopy mirror `D:\iCloudPhotos` wherever you like.

---

Do you want me to sketch you the exact `robocopy` line and a minimal scheduled-task config for Windows, so it feels like the rest of your A/B setup?

---

**User:**

Sounds kinda fiddly

---

**Assistant:**

It is a bit fiddly, yes — but only once up front. After that it runs hands-off.  

Here’s how the options stack up if your north star is *“UBIK, unattended, same vibe as iCloud Drive/OneDrive robocopy”*:  

---

### Option 1: Stick with iCloud for Windows (what you have)
- ❌ Fragile: files keep flipping online/offline, robocopy breaks.  
- ❌ No fix — Apple doesn’t offer “download all originals” on Windows.  
- ✔ Familiar, no new tools.  
**Verdict:** unreliable for photos, you’ll always chase ghosts.

---

### Option 2: `icloudpd` headless fetch (the fiddly one)
- ✔ Gets you a real file tree (JPG/HEIC/MP4) that robocopy can handle.  
- ✔ Can be set once and forgotten (scheduled task / cron).  
- ❌ Setup requires Apple app password + 2FA dance + some command-line.  
- ❌ Occasional breakage when Apple tweaks APIs (but usually patched quickly).  
**Verdict:** The only way to get the same “normal files” experience UBIK expects.

---

### Option 3: Designate a Mac as “photo vault” and back that up
- ✔ Apple-supported. Just tick “Download Originals to this Mac.”  
- ✔ Back up with Time Machine / Backblaze / robocopy from UBIK to NAS.  
- ❌ Requires keeping a Mac powered and online as source of truth.  
**Verdict:** Easiest, but it means UBIK isn’t truly self-contained.

---

### Option 4: Quarterly exports/transfers
- ✔ No setup beyond requesting export/transfer.  
- ❌ Manual, not unattended.  
- ❌ Easy to forget, leaves gaps between pulls.  
**Verdict:** Good as belt-and-suspenders, not your daily mirror.

---

**Bottom line:** if you want *UBIK to run this with zero interaction*, Option 2 (`icloudpd`) is the only one that matches how you’re already treating iCloud Drive and OneDrive. It feels fiddly only at install time — once scripted, it behaves like your current robocopy jobs.  

Want me to draft you a “minimal viable config” for `icloudpd` on UBIK that you can paste in and forget, or do you want to explore the Mac-vault path instead?

---

**User:**

Ok.. what about Google Photos? If I use the iPhone app (my only camera) and sync to both iCloud and Google. Then use Google Drive app on UBIK to offline them for robocopy?

---

**Assistant:**

That’s actually a clever detour — but the devil’s in the plumbing.  

---

### How Google Photos → UBIK actually works

- **iPhone**  
  *Google Photos app* can auto-upload every photo/video you take. Runs parallel to iCloud. No extra taps needed once set.  
  ✔ Gives you two clouds in parallel: iCloud + Google.  

- **Google Photos side**  
  Here’s the catch: Google Drive no longer directly surfaces the Photos library as a normal folder tree. The “Google Photos in Drive” toggle was killed off in 2019. So you can’t just install Drive for desktop and see your photos auto-appear.  

- **What you *can* do**  
  1. **Google Takeout / Export** – request periodic dumps; too manual for you.  
  2. **Third-party sync tools** – there are open-source and paid tools (e.g. `gphotos-sync`, rclone with `drive:`, or Google Photos API clients) that will pull full-res photos into a filesystem on UBIK. They work much like `icloudpd` — initial fiddly setup, then scheduled sync.  
  3. **Shared albums download** – clumsy, loses metadata, not unattended.  

So: Google Photos doesn’t give you a “plain folder” the way Google Drive does.

---

### Comparison with iCloudPD path

- **Google Photos API tools**  
  - Pros: More stable API than Apple’s private iCloud ones. Google doesn’t flip bits as often.  
  - Cons: Still needs OAuth setup, tokens, config. Same level of fiddly as `icloudpd`.  

- **iCloudPD**  
  - Pros: You stay inside Apple’s ecosystem (keeps edits, Live Photos intact).  
  - Cons: Uses private APIs, occasionally breaks until patched.  

Either way: you’re in “script a downloader → feed robocopy the folder” land.

---

### Realistic options for you

- **Stay in Apple lane:** Use `icloudpd` on UBIK, let it fetch iCloud Photos directly.  
- **Dual-cloud belt-and-suspenders:** Run both iCloudPD *and* a Google Photos sync job. That way if one service hiccups, you’ve got the other.  
- **If you only want one** — Google Photos may be *slightly* more stable for scripting, but you lose Apple-side metadata fidelity (edits, Live Photos nuances).  

---

Want me to sketch the equivalent unattended Google Photos sync workflow (using `gphotos-sync` or rclone with Photos API) so you can compare setup steps head-to-head with iCloudPD?

---

**User:**

Looks like icloudpd has a direct windows executable. That kinda makes it simple? I don’t have to use robo copy for photos at all. Just script this top instead?

---

**Assistant:**

Exactly — you’ve zeroed in on it.  

If you run the Windows executable of **`icloudpd`** on UBIK, you don’t need robocopy for Photos at all. `icloudpd` already:  

- Pulls down **full-res originals** (photos + videos, Live Photos included).  
- Writes them into a normal folder tree (`YYYY/MM/DD` or whatever you like).  
- Keeps them updated on each run (new files in, optionally delete files you’ve deleted in iCloud).  
- Logs what it did so you know what changed.  

So instead of:  
```
iCloud Photos app ➝ half-baked placeholders ➝ robocopy
```

You cut straight to:  
```
icloudpd ➝ real files on disk
```

Once those files are sitting in, say, `D:\iCloudPhotos`, you can:  
- Point your backup software at that folder.  
- Or (if you like the A/B mirror discipline) run robocopy *from that stable folder* to your NAS or secondary drive.  

---

### Minimal Windows script example
```bat
@echo off
REM --- Run nightly via Task Scheduler ---
set OUTDIR=D:\iCloudPhotos
icloudpd.exe ^
  --directory %OUTDIR% ^
  --username your_apple_id@icloud.com ^
  --folder-structure "{:%Y\%m\%d}" ^
  --recent 30
```

- `--recent 30` = only check last 30 days each run (faster); omit if you want full re-scan.  
- Add `--auto-delete` if you want local deletions to mirror iCloud deletions.  
- First run will take a while; afterwards it’s deltas.  

---

So yes: you can retire the robocopy hack for Photos. Keep robocopy for Drive/OneDrive (where it works beautifully), let `icloudpd` own the photo sync.  

Do you want me to lay out a “day-one checklist” (app password, 2FA, first run, Task Scheduler config) so you can set this and forget it?

---

**User:**

I don’t think I need the a/b rigour for photos as it’s always additive. Which is different from files. 

---

**Assistant:**

Right — that’s the key distinction:  

- **Drive/OneDrive:** documents come and go; versioning and deletions matter → A/B mirroring catches errors and rollbacks.  
- **Photos:** fundamentally additive. Once pulled, they don’t change (except edits in Photos, which are tracked separately in Apple’s DB, not the file itself). Deletions are rare and usually deliberate.  

So you can keep it simple:  

### Photos workflow
- Run `icloudpd` nightly → dumps any new originals into your `D:\iCloudPhotos` archive.  
- That folder just grows over time. No need for A/B rigour — a straight scheduled backup (copy or cloud backup agent) is fine.  
- Optional: keep a cold copy to external drive once a quarter in case ransomware hits UBIK.  

### Files workflow
- Keep the A/B mirroring for iCloud Drive/OneDrive. That’s where false deletes or sync bugs can actually bite you.  

---

This way UBIK is:  
- *Strict* where it needs to be (docs).  
- *Relaxed but safe* where it can be (photos).  

Do you want me to outline a “set-and-forget” Windows Task Scheduler entry for `icloudpd` so it quietly builds that photo archive every night?

---

**User:**

Just give me the command line switches. I’ll include it my my existing backup scripts 

---

**Assistant:**

Got it — here’s the lean `icloudpd` invocation you can drop into your backup script on UBIK:  

```bat
icloudpd.exe ^
  --username your_apple_id@icloud.com ^
  --directory D:\iCloudPhotos ^
  --folder-structure "{:%Y\%m\%d}" ^
  --auto-delete ^
  --log-level info
```

### Switches explained
- `--username`: your Apple ID email.  
- `--directory`: local archive root.  
- `--folder-structure "{:%Y\%m\%d}"`: organizes into `Year\Month\Day` folders (adjust to taste).  
- `--auto-delete`: mirror deletions (optional — drop if you want only additive).  
- `--log-level info`: keeps logs readable without spam.  

### Optional knobs
- `--recent N` → only fetch the last *N* days (faster incremental runs; full sync on first run).  
- `--only-print-filenames` → dry-run, good for testing.  
- `--skip-videos` → if you want just photos, not video.  

---

Would you like me to tune this for **purely additive** (never delete anything locally, even if you delete from iCloud), or do you prefer strict mirroring of the cloud?

---

**User:**

Mirror is probably fine

---

**Assistant:**

Then your working line should look like this:  

```bat
icloudpd.exe ^
  --username your_apple_id@icloud.com ^
  --directory D:\iCloudPhotos ^
  --folder-structure "{:%Y\%m\%d}" ^
  --auto-delete ^
  --log-level info
```

That gives you:  

- **Full originals** pulled down.  
- **Year\Month\Day** structure.  
- **Local deletions track iCloud deletions** (true mirror).  
- **Readable logs** for troubleshooting.  

Drop it into your existing backup script, schedule it, and you’re done.  

Want me to also add the switches to handle **Live Photos** (still + video) explicitly, or keep it stock since the default already does both?

---

**User:**

Stock is fine. Keep it fine. I’ll probably include the same command in my two a/b robocopy scripts that run alternate weekends. 

---

**Assistant:**

That’s a clean approach: let your existing A/B weekend jobs run `icloudpd` first, then roll straight into the robocopy stages. That way each archive set is “freshened” with whatever iCloud had before the mirrors are cut.  

Because `icloudpd` is additive + deletions mirrored, each A/B target will get an identical snapshot at the time of its turn — just like your file trees. No extra logic needed.  

Only note: first full run may be *big* (all your originals), so best to kick it off manually once before you fold it into the weekend jobs. After that, the deltas are small enough that it’ll fit inside your backup window.  

Want me to sketch a quick example of how the sequence would look inside your robocopy batch so it’s crystal where `icloudpd` should sit?

---

**User:**

It’ll be a single location for the a/b iPhoto backup. The robocopies will be in their respective a/b folders

---

**Assistant:**

Perfect — then the flow is dead simple:  

1. **Single source folder** (e.g. `D:\iCloudPhotos`) is always refreshed by `icloudpd`.  
2. Your **A/B robocopy jobs** treat that folder just like iCloud Drive/OneDrive sources:  

```bat
REM --- Refresh iCloud Photos ---
icloudpd.exe ^
  --username your_apple_id@icloud.com ^
  --directory D:\iCloudPhotos ^
  --folder-structure "{:%Y\%m\%d}" ^
  --auto-delete ^
  --log-level info

REM --- Then mirror to A or B target ---
robocopy D:\iCloudPhotos X:\Backups\Photos_A /MIR /R:2 /W:5 /LOG+:C:\Logs\PhotosA.log
```

…and the B weekend job just flips the robocopy target to `Photos_B`.  

That way:  
- `D:\iCloudPhotos` is your one stable “truth” folder.  
- Robocopy continues giving you the A/B rotation safety net.  
- No juggling two icloudpd runs — one source, two mirrors.  

Want me to suggest a couple of robocopy flags tuned for **photo archives** (e.g. retries, multithread, long path support), or keep it exactly how you run your Drive/OneDrive sets?

---

**User:**

Xml chatmerge?

---

**Assistant:**

```xml
<ChatMerge>
  <Topic>Backing up iCloud Photos on UBIK</Topic>

  <Canon>
    <Point>iCloud for Windows is unreliable for photo backups because it uses online-only placeholders that robocopy can’t handle.</Point>
    <Point>`icloudpd` (icloud_photos_downloader) can run natively on Windows as a direct executable, fetching full-resolution originals.</Point>
    <Point>Using `icloudpd`, you no longer need robocopy to pull photos — it creates a stable folder tree of actual files.</Point>
    <Point>UBIK can run `icloudpd` first to refresh the photo archive, then use robocopy to mirror that single source into A/B backup sets.</Point>
    <Point>Unlike files, photos are largely additive, but mirroring with `--auto-delete` keeps local deletions consistent with iCloud.</Point>
  </Canon>

  <Decisions>
    <Decision>Adopt `icloudpd` as the source of truth for iCloud Photos on UBIK, with one local folder (e.g., `D:\iCloudPhotos`).</Decision>
    <Decision>Run `icloudpd` inside existing A/B robocopy scripts so each weekend’s mirror starts from an updated source folder.</Decision>
    <Decision>Use a Year/Month/Day folder structure for simplicity and future-proofing.</Decision>
    <Decision>Keep robocopy for A/B discipline, but recognize it’s strictly additive protection since photos don’t behave like docs.</Decision>
  </Decisions>

  <OpenLoops>
    <Loop>First run of `icloudpd` may be large; should be tested manually before folding into scheduled jobs.</Loop>
    <Loop>Optional flags like `--recent` or `--skip-videos` could optimize runtime if needed later.</Loop>
    <Loop>Consider quarterly cold backup to an external drive as ransomware protection.</Loop>
  </OpenLoops>

  <Discardables>
    <Item>Attempting to use iCloud for Windows app as a reliable photo source (placeholder churn breaks robocopy).</Item>
    <Item>Google Photos → Drive sync as a replacement workflow (Drive no longer supports direct Photos integration).</Item>
  </Discardables>
</ChatMerge>
```

---
