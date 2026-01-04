# iPhone ad blocking options

**Created:** 2025-12-06 16:38:11
**Updated:** 2025-12-07 22:30:59
**Turns:** 11

---

**User:**

IPhone in December 2025. Ad blocking is a mess. What are my options? Adguard seems fine but it’s probably gonna run into the v3 wall. Ublock origin lite seems promising. Stack these any any of the other options. Also— not willing to pay for ad blocking.  

---

**Assistant:**

Good questions — and you’re right: ad-blocking on iPhone in late 2025 remains a bit messy. There’s no perfect zero-cost solution that works everywhere, but you *can* stack a few free tools to get fairly solid results. Here’s how I’d break down your options (and caveats), based on the current landscape + what people on iOS are actually using.  

---

## ✅ What works reasonably well on iPhone now

### • entity["software","AdGuard",0] for iOS  
- AdGuard remains one of the more robust content-blockers for Safari — blocks banners, pop-ups, video ads, trackers. citeturn0search2turn0search9  
- The free version works fine for basic blocking; paid gets you extras (custom filters, DNS-level blocking, etc.) but core ad-blocking doesn’t require payment. citeturn0search2turn0search4  
- Note: As of recent months some users report that AdGuard no longer blocks ads in *all* apps — mainly works in Safari, less reliably system-wide. citeturn0reddit29turn0reddit31

### • entity["software","uBlock Origin Lite",0] (on Safari / iOS browsers)  
- uBlock Origin Lite surfaced in 2025 for Safari / iOS. It’s lighter than some blockers and popular for those wanting a free, minimal footprint blocker. citeturn0reddit37turn0reddit39  
- People on Reddit say it's worth trying — some report noticeably fewer ads with uBlock Lite + another blocker or DNS filter backing it. Example:  
  > “I’m using Wipr 2 and it works well. If you don’t want to pay for it then ublock origin lite.” citeturn0reddit39  
- But, because of the evidence of limitations under modern iOS (see below), you probably shouldn’t rely on it as a sole solution.

### • Combine Safari content-blocker + DNS- or system-wide blocker  
- iOS Safari content blockers only work in Safari (third-party browsers, apps, embedded webviews often skip them). That’s a well-known limitation. citeturn0search10turn0search13  
- A DNS-level blocker (or equivalent) can extend ad-blocking beyond Safari — though effectiveness depends heavily on the ad networks, how ads are embedded, and whether ads come from same domains as content. citeturn0search4turn0search10  
- Real-world iOS users report using something like AdGuard + DNS-blocking (via its DNS profile, or another free DNS service) to catch many ads across apps and Safari. citeturn0reddit35turn0reddit43  

### • entity["software","1Blocker",0] (free-tier), or similar Safari-only blockers  
- 1Blocker offers a free tier that gives you a decent ad/tracker-blocking list for Safari. citeturn0search1  
- Not perfect — some ads (especially in apps or sites using creative or obfuscated delivery) may slip through — but for a free/simple setup, it’s often “good enough.”  

---

## ⚠️ Key caveats & what’s broken (or going to break)

- iOS content blockers can only block in **Safari**. Ads inside native iOS apps or embedded webviews often don’t get blocked. citeturn0search10turn0reddit43  
- Some recent complaints from users: after updates, ad-blocking effectiveness dipped (e.g. on search ads, banners) even with AdGuard. citeturn0reddit40turn0reddit29  
- Because ad-blockers and ad networks are in a constant “arms race,” what works today might degrade — filters go stale, sites change ad delivery methods, and iOS restrictions tighten.  
- If you rely *only* on something like uBlock Origin Lite — result likely “some, but not all” ads blocked. Users on Reddit say it's lighter but often doesn't catch everything. citeturn0reddit35turn0reddit37  

---

## 🔧 What I’d do if I were you (free & pragmatic stack)

If I had your constraints (no payment, want best possible blocking), I’d:

1. Install **AdGuard** for iOS — enable it in Safari as content blocker.  
2. Also install **uBlock Origin Lite** (or another free Safari blocker like 1Blocker) — sometimes overlapping filters catch things one misses.  
3. Add a free ad-blocking DNS (e.g. via AdGuard DNS or other free public blocklist DNS) to Wi-Fi and mobile (or use a free DNS-blocking VPN profile) to catch ads/tracking across all apps — where possible.  
4. Accept that you’ll still see ads inside many native apps, or dynamic ads/serving methods that slip past filters. Maybe whitelist sites you support, to keep them sustainable and avoid breakage.  

---

If you like — I can **pull up a current (Dec 2025) list of ~5 fully free tools or combos** that seem to have the best real-world success on iPhone + what the tradeoffs are (ad coverage, privacy, battery, etc.).  
Takeaway: no silver bullet — layering helps.

---

**User:**

I have CIRA DNS configured on my router to trim some malware. It’s also Canadian. 

I have a pihole dns server. I suppose I can upstream it to adguard dns. Adguard is non-US… based out of Cyprus?

Ublock origin lite seems sensible to have on device

That full stack only works at home. 

Ublock would be my only defense on mobile. 

Should I install Adguard app on the phone or is that just adding overhead for little gain?

---

**Assistant:**

You’re basically at the point where adding AdGuard *on-device* only helps if you need one of two very specific things: extra Safari filter sets **or** a DNS/VPN profile when you’re **off-Wi-Fi**. Otherwise, yes — it’s overhead with diminishing returns.

Here’s the quick take:

**One sentence:** Installing AdGuard on iPhone is only worth it if you want its DNS/VPN layer active on mobile data or you want deeper Safari filters than uBlock Lite can provide.

---

## Your current stack (at home)
- **CIRA DNS on router** → baseline malware filtering (good, light, Canadian jurisdiction).  
- **Pi-hole upstream to AdGuard DNS** → solid ad + tracker trimming before it even hits devices.  
- **Safari-level blocking with uBlock Origin Lite** → front-line page cleanup.

That’s actually a strong three-layer model, and the home network part is already doing most of the heavy lifting.

---

## Off-network reality
When you leave home:
- CIRA + Pi-hole vanish.
- AdGuard DNS (if configured via Pi-hole only) also disappears.
- You’re left with **uBlock Origin Lite**, which is Safari-only.

This is the main gap.

---

## Would the AdGuard iOS app improve mobile coverage?

### **Worth it IF:**
1. **You want DNS-level blocking on mobile data.**  
   AdGuard app can install a VPN-based DNS profile to keep ad/malware filtering active anywhere.  
   (The free tier gives you basic AdGuard DNS, which is enough to mimic part of your home setup.)

2. **You want extra Safari filtering beyond uBlock Lite.**  
   uBlock Lite is intentionally minimal (MV3-style constraints) — AdGuard adds full rule sets that sometimes catch cosmetic or script-based ads that Lite doesn’t.

### **Not worth it IF:**
- You don’t care about system-wide blocking outside Safari.  
- You’re fine relying on uBlock Lite alone when mobile.  
- Battery overhead bothers you — a DNS/VPN tunnel adds a small but real cost.  
- You don’t want one more background extension/process.

### **How much does it actually block in apps?**
DNS/VPN blocking on iOS:
- Works on many apps.  
- Fails on apps that hardcode ad servers or use blended content domains.  
- Still chops a *lot* of telemetry.

It’s not as powerful as Android system blockers, but it’s better than nothing.

---

## Net recommendation based on your setup + priorities
**Yes, install AdGuard on the phone** *only* if you want mobile-data DNS blocking and don’t mind the minor overhead.

**If your mobile browsing is mostly in Safari and you don’t care about in-app ads, stick with uBlock Lite alone.**

A clean middle option is:
- **AdGuard iOS app installed but *DNS/VPN turned on only when you leave home*** (one tap toggle in Control Centre).  
- **uBlock Origin Lite always on.**

That gives you:
- Full stack at home (router + Pi-hole + uBlock).  
- Partial stack on mobile (AdGuard DNS + uBlock).

Lean, free, consistent.

If you want, I can sketch the simplest low-friction workflow for switching between “Home stack” and “Mobile stack” with the fewest moving parts.

---

**User:**

Ok. I’ll just keep the Ublock on device and point my dns for my home WiFi profile to my pihole. That should be a decent blend. 

I could swap Cira for Adguard on the router I suppose to help all my devices. 

Is that sensible or should I stick with cira?

---

**Assistant:**

Stick with CIRA unless you specifically want **more ad/tracker filtering at the network layer**, not just malware protection.

Here’s the quick decision rule:

**One sentence:** CIRA gives you clean, stable, low-false-positive security; AdGuard DNS adds heavier blocking but at the cost of occasional breakage and less “Canadian-quiet” governance.

---

## When to stay with CIRA (your case right now)
- You’ve already got **Pi-hole providing ad/tracker filtering** upstream.  
- CIRA gives you **malware, phishing, botnet** filtering without touching legitimate content.  
- It’s **Canadian-operated**, predictable, and very low maintenance.  
- The combo CIRA → Pi-hole → device blockers is stable and rarely breaks sites.

This keeps your router setup clean and leaves Pi-hole as the place where filtering logic lives.

---

## When to switch your router to AdGuard DNS
Only if you want to:
- Apply **network-wide ad blocking** to *everything* before Pi-hole even sees it.  
- Catch more trackers across IoT or TV devices you don’t care to micro-manage.  
- Accept that occasionally a domain gets overblocked and requires whitelisting.

But note:  
If you already run Pi-hole with decent blocklists, AdGuard DNS on the router becomes **overlapping**, not additive — Pi-hole will block most of the same things already.

---

## Best blended architecture for your goals
If you want:  
- **Zero subscription**,  
- **Minimal overhead**,  
- **Consistent behaviour**,  
- **Canadian jurisdiction**,  
- **No accidental breakage**,  

then:

**Router → CIRA DNS → Pi-hole (custom lists) → devices like iPhone running uBlock Lite**  
…is balanced and quiet.

If you want me to tune your Pi-hole lists for a “low-breakage but high-value” set, I can give you a three-list stack that performs well without the usual Pi-hole chaos.

---

**User:**

Hmm. My dhcp runs on my router so the cira dns is what gets pushed around my network. My wife’s phone, etc. 

I have to manually point devices to my pihole DNS

---

**Assistant:**

You’ve got three clean options, and one of them is clearly the lowest-friction for your household.

**One sentence:** The simplest fix is to make your router hand out Pi-hole’s IP as the primary DNS via DHCP, while Pi-hole itself uses CIRA upstream — that way *all* devices automatically benefit without per-device hand-tuning.

---

## The three viable patterns

### **1) Best balance: router → Pi-hole → CIRA**
**How it works:**
- DHCP hands out Pi-hole as the DNS server (one setting on the router).  
- Pi-hole uses CIRA as *its* upstream.  
- Every device on your network (your wife’s phone included) immediately benefits from Pi-hole + CIRA without manual config.

**Why it’s ideal:**
- Lowest friction on devices.  
- Household doesn’t need tech literacy.  
- Pi-hole gives you ad/tracker filtering; CIRA handles malware/phishing.  
- Clean, reliable, and easy to maintain.

This is the pattern most Pi-hole users eventually settle on.

---

### **2) Keep router on CIRA and manually point only your devices to Pi-hole**
This is what you’re doing now.

**Pros:**  
- No disruption for family; they run CIRA-only.  
- You get extra filtering.

**Cons:**  
- Not scalable as you add devices.  
- You forget the config on new phones/laptops.  
- Mixed behaviour around the house.

This is fine short-term but annoying long-term.

---

### **3) Router on AdGuard DNS → Pi-hole**
You could do this, but it’s overkill:

- Double ad-blocking sometimes increases breakage.  
- AdGuard DNS upstream adds extra complexity with little gain if your Pi-hole is already carrying the load.  
- Doesn’t line up with your goal of “light, safe, and not-US-based but non-annoying.”

This usually makes sense only when you want *maximal* blocking on IoT/TVs with no effort.

---

## The recommendation
**Change your router’s DHCP setting to hand out Pi-hole’s IP as the DNS server.  
Set Pi-hole’s upstream to CIRA DNS.**

Done.  
All devices benefit, no per-device config, and CIRA still provides the safety net.

If you want, I can give you the exact “two-field” DNS values for CIRA’s protected service (IPv4 + IPv6) or a quick step-by-step for pushing Pi-hole through DHCP on common router brands.

---

**User:**

If #3, I wouldn’t bother with pihole. 

---

**Assistant:**

Right — if you go with **#3 (router → AdGuard DNS)**, then Pi-hole becomes redundant for your purposes.

**One sentence:** If you switch your router to AdGuard DNS, you can safely retire Pi-hole unless you want the extra visibility, control, or custom lists.

---

Here’s the direct comparison so you can see if #3 actually fits your goals:

## If you replace Pi-hole with router-level AdGuard DNS
### **Pros**
- Zero local hardware to maintain.  
- Automatically applies to every device (DHCP hands out the router).  
- AdGuard DNS blocks ads, trackers, and malware in one step.  
- Works well for non-tech family members.  
- No per-device settings.

### **Cons**
- Less granular control (no per-domain whitelisting dashboard).  
- No local query logs or analytics.  
- AdGuard DNS blocklists are global → occasional false positives you can’t fix locally without reconfig.  
- Slightly less predictable for troubleshooting.  
- Harder to tune for “low breakage” mode compared to Pi-hole’s local list tuning.

---

## When #3 is genuinely the right answer
Choose router-level AdGuard DNS **only** if:
- You want *hands-off* ad/malware blocking for your whole household.  
- You don’t care about analytics or custom blocklists.  
- You want zero tinkering going forward.  
- You want something stronger than CIRA with no local infrastructure.

This setup is lightweight and good enough for 90% of families.

---

## When to stay with Pi-hole + CIRA
Stay with your current plan if you want:
- Local control over what breaks.  
- Ability to whitelist/blacklist quickly.  
- Fine-grained visibility into which apps leak telemetry.  
- A “quiet” Canadian upstream (CIRA) instead of AdGuard’s Cyprus jurisdiction.

---

If you want your network to “just work” without talking about DNS again for a year, **router → AdGuard DNS** is the simplest.  
If you want control, **Pi-hole → CIRA** is stronger and cleaner.

---

**User:**

I have a bell home hub 4000. 

So I’d have to configure Adguard dns globally. 

---

**Assistant:**

Given the **HH4000’s locked-down DHCP/DNS behaviour**, switching to AdGuard DNS at the router level means *every single device* — yours, your wife’s, guests’, IoT — would automatically and unavoidably use AdGuard DNS.

**One sentence:** Yes, on the Home Hub 4000 you’d have to set AdGuard DNS globally, because Bell doesn’t let you push Pi-hole or per-client DNS via DHCP.

---

## What this means in practice

### **1) HH4000 limitations**
- You **cannot** tell the HH4000’s DHCP server to hand out a custom DNS server like Pi-hole.  
- You **cannot** implement conditional DNS, split DNS, or per-device DNS.  
- If you set a DNS on the router, it becomes **the DNS for the entire LAN**.

### **2) So your only router-level options are:**
- **CIRA for all devices**  
- **AdGuard DNS for all devices**  
- **Bell’s defaults (avoid)**

That’s it.

---

## Is going “AdGuard DNS for *everything*” sensible with an HH4000?

### **It’s sensible IF:**
- You want a one-shot change that improves the whole household’s privacy/ad-blocking.  
- You don’t mind the occasional false-positive blocking from AdGuard.  
- You’re fine with Cyprus/EU jurisdiction.  
- You don't want to maintain Pi-hole.

### **It’s *not* sensible IF:**
- You want fine control over what gets blocked.  
- Your wife gets annoyed when one app suddenly stops loading images or login pages (AdGuard does occasionally overblock).  
- You rely on Pi-hole for analytics or targeted whitelisting.  
- You want to keep a “quiet,” Canada-based DNS service (CIRA).

**With an HH4000, household acceptance is the real constraint** — if something breaks, you can’t tell her device to bypass it.

---

## Your actual best-fit choices

### **Option A — Keep things as they are (your current path)**
- Router: **CIRA DNS** for the whole home  
- Your devices: manually pointed to Pi-hole  
- Your wife’s devices: clean, stable CIRA  
- Minimal breakage  
- More control for you, no surprises for her  

This is stable and quiet.  
The only downside: per-device DNS config for *your* gadgets.

---

### **Option B — Flip router to AdGuard DNS and retire Pi-hole**
- One change → network-wide ad/malware blocking  
- Easier operationally  
- Occasional breakage can’t be scoped to just your device  
- You lose all local control and visibility  
- Everything relies on remote filter tuning  

This is simplest, but least adjustable.

---

### **Option C — Put HH4000 into “passthrough” mode and run your own router**
(Only if you're ever willing to upgrade your network.)  
- Your router handles DHCP → Pi-hole can be DNS for everyone  
- Pi-hole → CIRA upstream  
- Full control, no per-device config, no HH4000 restrictions  
- Most flexible and reliable long-term  

This is the “best network,” but more gear.

---

## Recommendation for now
**Stay with your current setup (CIRA router-level + Pi-hole for your devices).**  
Given the HH4000 limitations, switching the whole household to AdGuard DNS is more risk than reward unless simplicity is your top priority.

If you ever want, I can map out the cleanest HH4000 → “own router” migration path that preserves TV/Internet functionality.

---

**User:**

Option C is a non starter. While I can technically do this work. I don’t want to be the sysadmin for my house. 

Option b give me pause because, while it simplifies everything and lets me spin down pihole, my wife’s iPhone and iPad games might get broken. Probably shouldn’t do that. Happy wife happy life. 

Option a is the status quo. 

---

**Assistant:**

Option A is the right call — it hits the balance you actually care about: low friction for you, zero friction for your wife, no household breakage risk, and no new sysadmin burden quietly creeping in.

---

**User:**

So here’s the thing. Is cira dns and Ublock origin lite enough? Or should I use pihole? Or install Adguard app?

---

**Assistant:**

Here’s the crisp answer: **CIRA DNS + uBlock Origin Lite is enough for a smooth, low-maintenance experience; Pi-hole adds power but also overhead, and the AdGuard app only makes sense if you want DNS-level blocking on mobile data.**

---

## The simplest way to think about it
**One sentence:** If you want “good enough everywhere with zero hassle,” stay with CIRA + uBlock; add Pi-hole only if you want more control, and add AdGuard iOS only if you want protection off-Wi-Fi.

---

## 1) **CIRA DNS + uBlock Origin Lite** (your baseline)  
**What it gives you:**  
- Malware + phishing filtering (CIRA)  
- Tracker + ad blocking in Safari (uBlock Lite)  
- No breakage for your wife’s apps  
- No system-wide surprises  
- No maintenance  

**This is the most “hands-off” setup.**  
For most households, this is *already enough*.

**Where it falls short:**  
- No blocking inside apps (YouTube, games, etc.).  
- No visibility into device traffic.  
- You rely entirely on uBlock Lite inside Safari and CIRA for everything else.

If you’re okay with that, you’re done.

---

## 2) **Add Pi-hole** (more control, more filtering, more responsibility)  
Use Pi-hole **only** if you want the benefits:  
- Local control over what’s blocked  
- Analytics (who’s querying what)  
- Ability to selectively whitelist when something breaks  
- Catch extra telemetry from smart TVs, IoT, random apps

**Cost:** you become the sysadmin for that box.  
If running it already feels like overhead, you’re not getting enough value out of it.

Given what you’ve said, Pi-hole is “nice to have,” not “must have.”

---

## 3) **Install AdGuard App on iPhone** (optional, targeted benefit)  
Only worth it if you want **DNS filtering while on mobile data**.

Because:
- uBlock Lite only covers Safari  
- CIRA only protects you on Wi-Fi  
- Pi-hole only protects you on your home network  
- Off-Wi-Fi, you’re naked unless Safari catches it

The free AdGuard app gives you:  
- DNS filtering anywhere (via a local VPN profile)  
- Slight battery overhead  
- Slight chance of breakage  
- No payment required

If you want consistent behaviour *outside the house*, this is the only low-effort way.

---

## The recommendation tailored to your constraints
Given:
- You want **no sysadmin role**  
- You want **zero risk of breaking your wife’s iPad/iPhone apps**  
- You want **enough blocking to feel clean**  
- You don’t want to pay  
- You want **predictability**  

Here’s the sensible stack:

### **At home:**  
- Router: **CIRA DNS**  
- Your devices: **uBlock Origin Lite**

### **Optional for you only:**  
- **AdGuard iOS app** with DNS mode **ON only when you’re off Wi-Fi**

### **Skip Pi-hole** unless you enjoy tinkering (you don’t right now).

---

If you want, I can give you a one-line setup that triggers AdGuard DNS automatically only when you leave home (Shortcuts → Automation → “When Wi-Fi disconnects”).

---

**User:**

Hmmm. The VM I’m running pihole on is also where I run an openvpn server. I use it to access my windows machine when offsite— which I never really do. 

My host windows server which is my legacy plex/torrent box (largely unused since I resubsxribed to cable)

I have a intune managed windows VM on this host for work—- but I rarely use it. I could probably spin it down. 

Most of my training/demo work is in a browser. 

---

**Assistant:**

Sounds like you’re circling a bigger truth: **your homelab stack is doing way more than you actually need today**, and Pi-hole/OpenVPN/extra VMs may now be legacy inertia rather than live value.

**One sentence:** If Pi-hole and your VPN server are only running because they “used to be useful,” you can safely simplify and reclaim mental space without losing anything important.

---

## Let’s look at your actual components through a “does this still earn its keep?” lens

### **Pi-hole VM**  
**Value today:**  
- Mild ad/tracker filtering *only when you manually point devices to it*.  
- Occasional insight into local traffic.  
- Requires care, updates, and a dedicated VM.

**Reality:**  
- CIRA DNS + uBlock Lite already covers your practical needs.  
- You explicitly don’t want to be the house sysadmin.  
- It’s not providing value to anyone else in the household.

**Verdict:**  
**Low ROI. Absolutely safe to spin down.**

---

### **OpenVPN Server on that VM**  
**Value today:**  
- Lets you reach your Windows box remotely.  
- But you said you *never do that anymore*.

**Reality:**  
- That’s a “just in case” service.  
- Rarely-used VPN endpoints are just maintenance and attack surface.  
- If you ever need something, ZeroTier or Tailscale is lighter, faster, and more modern.

**Verdict:**  
**Shut it down. If you ever need remote access again, use Tailscale for 4 minutes and be done.**

---

### **Host Windows Server (Plex/torrent legacy box)**  
**Value today:**  
- Barely used; Plex and torrents aren’t part of your workflow.  
- Hosting your VMs, but they’re barely used.  
- Consumes power and contributes to the “home sysadmin tax.”

**Reality:**  
- Intune VM could move or be paused indefinitely.  
- You don’t need a home hypervisor if your work is browser-driven.

**Verdict:**  
You can move toward the **“Single clean host only when needed”** model:
- Keep the physical server if you like owning your data,  
- or retire it gracefully and migrate anything essential to lighter solutions.

---

## So what’s the simplest DNS/convenience posture going forward?

Given all this:

### **At home:**  
- Router → **CIRA DNS**  
- Devices → **uBlock Origin Lite**  
- No Pi-hole. No OpenVPN. No maintenance. No breakage.

### **Off home Wi-Fi (optional):**  
- Install **AdGuard iOS** and toggle DNS-only mode *when you feel like it.*  
- Or automate via a Shortcut that enables it only when Wi-Fi disconnects.

This gives you:
- Zero sysadmin burden  
- Zero breakage for your wife  
- Clean, predictable behaviour  
- No new hardware or VMs  
- No ongoing maintenance  
- And you’re not paying for anything

---

## Your stack is evolving from “homelab mode” → “minimal, intentional, and stable”

Nothing in your current needs requires Pi-hole, OpenVPN, or a heavy always-on Windows host.  
You’re basically using modern cloud workflows + iPhone browsing + occasional media.  
That’s a lifestyle that thrives on **less**, not more.

If you want, I can give you a one-step plan to sunset the Pi-hole/VM/OpenVPN stack cleanly so nothing breaks unexpectedly.

---

**User:**

The only household risk is in keeping/deleting the plex/torrent function. It’s been months since we watched anything on it. I’ll probably keep it live for another 3 months and reevaluate. But i suspect it’s surplus. I could always torrent individual shows from my Mac and plug the removable drive directly into the tv. Or plug the drive into the router do that matter. 

---

**Assistant:**

That’s a clean, rational way to wind it down — and a 3-month “cooling-off” period is exactly how you confirm that something is truly surplus without risking household friction.

**One sentence:** Keep Plex/torrent running quietly for 90 days, monitor whether anyone actually *reaches* for it, and if the answer is “no,” you can retire it with zero impact.

---

## Why your 3-month plan is solid
- It gives your household (and your own habits) time to surface any hidden dependencies.  
- If nobody uses it in that window, that’s the strongest possible signal it’s dead weight.  
- It removes the emotional “what if we need it once” decision — the data answers it for you.  
- It means you can shut it down with confidence and no guilt.

---

## If/when you retire it, your fallback options are easy
### **1) Occasional Mac torrent → plug drive into the TV**  
- Zero network complexity  
- Works even if the server is gone  
- [Modern TVs read USB drives just fine]

### **2) Plug the drive into the router**  
- Router-as-NAS mode is fine for infrequent use  
- Low power and no maintenance  
- Removes the whole Windows Server footprint

### **3) Quick Plex alternative if you ever miss it**  
- Jellyfin or Infuse on your Apple devices  
- Works off a simple shared directory  
- No VM, no Windows box, no background services

---

## The big picture
You’ve already shifted to cable TV and browser-based media.  
That means the heavy Plex/torrent host is no longer a “media backbone”—it’s just legacy infrastructure running out the clock.

Your plan to keep it alive for one more quarter, then reassess, is the lowest-risk and lowest-effort move.

---

**User:**

I can probably spin down pihole, openvpn and the work windows VM. Reduce the attack surface and sysadmin. 

---

**Assistant:**

Good call — simplifying here meaningfully lowers risk without losing anything essential.

Here’s the crisp view:

You’ve already got strong coverage with **CIRA DNS + uBlock Origin Lite**, so the incremental protection from Pi-hole, OpenVPN, and the Windows VM is small compared to the maintenance and exposure they introduce. The Plex/torrent stack is the only real outlier, and if you’re barely using it, parking it for a 3-month sunset is a clean approach.

If you truly only need occasional torrents, pulling them on your Mac and dropping them onto a USB drive or a router-attached drive is safer, simpler, and removes a huge chunk of moving parts.

Big picture: shutting down Pi-hole, OpenVPN, and the Win VM meaningfully reduces your external attack surface with almost no lifestyle penalty.

---
