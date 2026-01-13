# Health Tech Stack - Current Implementation

**Last Updated:** January 13, 2026  
**Status:** Active - Recent update with Perplexity HealthKit integration

---

## Current Stack (Validated)

### 🏥 Devices & Apps
- **Fitbit Inspire 3** — Activity tracking (steps, heart rate, sleep duration)
- **ResMed CPAP + myAir web** — Sleep apnea management (AHI, mask seal, usage hours)
- **OneTouch Reveal app** — Glucose monitoring (standalone, minimal use)
- **Apple Reminders** — Medication adherence (testosterone injections, daily medications)
- **iPhone 13** — Apple Health reinstated (see rationale below)
- **Perplexity Mac app** — AI-powered health data analysis via HealthKit MCP
- **Sync Fitbit to Health** (by Yoshifumi Kanno) — Middleware for Fitbit → Apple Health sync

### 📊 What Each Tool Provides

| Function | Tool | Why It Works |
|----------|------|--------------||
| **Activity & movement** | Fitbit app | Native interface, reliable tracking |
| **Sleep apnea adherence** | myAir web app | Direct feedback, drives behavior change |
| **Glucose tracking** | OneTouch Reveal | Standalone, minimal UI friction |
| **CPAP pressure trends** | myAir web | Built-in analytics, clinical context |
| **Medication reminders** | Apple Reminders | Native iOS, recurring notifications, completion tracking |
| **Step targets** | Fitbit dashboard | Motivation, trend view |
| **Data consolidation** | Apple Health | Middleware layer for AI analysis |
| **AI-powered insights** | Perplexity MCP | Conversational queries, automated markdown reports |
| **Data sync** | Sync Fitbit to Health | One-tap manual sync, no subscription |

---

## Recent Stack Evolution (January 13, 2026)

### What Changed

**Perplexity HealthKit Integration Discovery**
- Perplexity Mac app now supports HealthKit access via Local Model Context Protocol (MCP)
- Privacy-first architecture keeps health data local during processing
- Enables AI-powered analysis and automated report generation

**Apple Health Reinstatement**
- Previously deleted due to lack of actionable value
- **New rationale:** Apple Health now serves as middleware for Perplexity AI analysis, not as a dashboard to check
- Transform from passive data silo to actionable AI interface

**New Data Pipeline**
```
Fitbit → Sync App → Apple Health → Perplexity MCP → Workbench Repo (markdown reports)
```

### Why This Changes the Calculus

**✅ Adds AI Analysis Layer Without Cognitive Load**
- Don't need to check Apple Health manually (still avoid the app as dashboard)
- Perplexity generates insights via conversational queries on Mac
- Automated weekly/monthly reports in markdown format
- Data flows to Workbench repo for permanent record

**✅ Maintains Simplicity Principles**
- One-tap manual sync (morning coffee ritual)
- No background processes draining battery
- No third-party subscription fees ($0 cost)
- Fitbit remains primary interface for daily checks

**✅ Enables Workbench Integration**
- Health reports commit directly to `_life/health` folder
- Markdown-based permanent record
- AI-generated trend analysis and anomaly detection
- Complements existing patient summary and health timeline files

---

## Why This Stack Works

### ✅ ADHD-Friendly Design
- **Cognitive load:** Still 3 primary contexts (myAir web, Fitbit app, Apple Reminders)
- **Apple Health is invisible:** Used as middleware, not a dashboard to check
- **Perplexity integration:** Natural language queries when needed, not another app to monitor
- **Task-switching cost:** Minimized by maintaining Fitbit as primary interface
- **Maintenance burden:** Minimal (one-tap daily sync)

### ✅ Clinical Value Preserved
- **CPAP adherence:** myAir's daily scores remain the primary feedback mechanism
- **Activity awareness:** Fitbit dashboard unchanged
- **New capability:** AI-powered trend analysis and correlation detection via Perplexity
- **Medication compliance:** Apple Reminders unchanged

### ✅ Cost & Maintenance
- **Spending:** $0 (Sync Fitbit to Health has no subscription fees)
- **Time:** <1 minute daily for manual sync
- **Privacy:** Local MCP keeps health data on device during Perplexity analysis

---

## What Was Rejected (And Why)

### ❌ Apple Health as Hub (Previous Decision - Still Valid)
**Problem:** Creates infrastructure to solve a problem that doesn't exist.
- Unified dashboards improve outcomes *only* when paired with professional coaching or real-time feedback
- Self-guided data consolidation without clinical support does NOT improve health metrics

**NEW CONTEXT:** Apple Health now serves as **middleware for AI analysis**, not a dashboard to manually review.
- Still don't check Apple Health app as primary interface
- Fitbit remains the daily dashboard
- Apple Health enables AI-powered insights without adding cognitive load

### ❌ Third-Party Sync Apps (PowerSync, Sync Solver, etc.)
**Problem:** Maintenance burden > benefit.
- Require repeated reconnection when APIs throttle or update
- Cost ($10-60) for feature that doesn't improve outcomes

**NEW SOLUTION:** "Sync Fitbit to Health" (Yoshifumi Kanno)
- $0 subscription cost
- One-tap manual sync (intentional, not automatic)
- 10+ health categories supported
- Aligns with "workbench, not warehouse" philosophy

### ❌ Fitbit Premium
**Problem:** "Pretty charts for data you already have."
- You don't need guided workouts or Daily Readiness score
- You already hit your 10k steps/day target
- Sleep stage data is unreliable with CPAP mask interference

**Decision:** Remain on free tier indefinitely. Perplexity provides better analysis than Fitbit Premium charts.

### ❌ MyFitnessPal / Nutrition Integration
**Problem:** Clumsy UI, poor integration with your stack.
- Fitbit's food logging is adequate for your macro tracking needs

**Decision:** Use Fitbit's native food database for spot checks; don't formalize nutrition tracking in tech stack.

---

## Maintenance Schedule

### Daily (1 min)
- **Morning coffee ritual:**
  - Open "Sync Fitbit to Health" app
  - Tap sync button
  - Confirm completion

### Weekly (5 min)
- Check **myAir web dashboard**
  - Review AHI trends
  - Confirm mask seal quality
  - Verify usage hours >4h/night
  - Read any feedback/tips from myAir

- **(Optional)** Ask Perplexity for weekly health summary
  - "Generate a weekly health report from my HealthKit data"
  - Review AI-generated insights
  - Commit markdown report to Workbench if valuable

### Biweekly (2 min)
- Respond to **testosterone injection reminder** in Apple Reminders
- Complete injection
- Mark reminder as complete

### Monthly (10 min)
- Review **Fitbit activity trends**
  - Check step averages vs 10k target
  - Acknowledge sleep trend data (but don't over-interpret due to CPAP mask interference)
  - Use for motivation, not clinical decisions

- Ask Perplexity for **monthly health analysis**
  - "Analyze my HealthKit data for the past month and identify trends or anomalies"
  - Generate markdown report for `_life/health` folder
  - Commit to Workbench repo

### Quarterly (During doctor appointments)
- Share **myAir AHI export** with Dr. Sharma if requested
- Discuss **A1C blood work results**
- Review **blood pressure readings** (from home checks or clinic)
- Confirm **testosterone therapy effectiveness** with Dr. Massaro
- Update **patient_summary_jan2026.md** with new lab values
- Share Perplexity-generated health reports if relevant to care discussion

---

## Success Metrics

### CPAP Adherence
- **Target:** >4 hours/night, >70% of nights
- **Check:** myAir daily score consistently "Good" or better
- **Action if declining:** Troubleshoot mask fit/comfort (myAir provides tips)

### Activity Level
- **Target:** ~10,000 steps/day (your established habit)
- **Check:** Fitbit weekly summary
- **Action:** Use data for motivation, not intervention

### Medication Compliance
- **Target:** 100% adherence to biweekly testosterone injections
- **Check:** Respond to all Apple Reminders notifications
- **Action if missed:** Reassess reminder timing/method

### System Health
- **Target:** Zero maintenance time on health tech
- **Check:** Daily sync takes <1 minute; no troubleshooting of sync issues
- **Action if friction increases:** Review this document and recommit to simplicity

### AI Analysis Value
- **Target:** Monthly Perplexity reports provide actionable insights
- **Check:** Do AI-generated reports reveal trends not visible in daily Fitbit checks?
- **Action if low value:** Reduce frequency or eliminate feature

---

## Review Schedule

### 3-Month Check-In (April 2026)
1. Is daily Fitbit → Health sync routine sustainable? (If no, reassess)
2. Are Perplexity health reports providing value? (If no, reduce frequency)
3. Am I checking Apple Health as a dashboard? (If yes, delete app and use Perplexity only)
4. Has CPAP adherence maintained or improved?
5. Have I missed testosterone injections? (If yes, adjust reminder time)

### 6-Month Check-In (July 2026)
1. Has CPAP adherence improved, maintained, or declined?
2. Has activity level (steps) improved, maintained, or declined?
3. Has AI analysis layer added cognitive load or reduced it?
4. Are Workbench health reports being referenced for clinical discussions?
5. Any new devices or apps tempting you back to unnecessary complexity? (Resist.)

### Annual Check-In (January 2027)
1. Review A1C trends over the year
2. Review CPAP adherence patterns
3. Review activity/weight trends
4. Assess whether Perplexity HealthKit integration improved health outcomes
5. Assess whether tech stack needs adjustments based on changing health needs

---

## Key Insights

**You were building infrastructure to solve a problem that doesn't exist.**

For healthspan optimization at 53 with Type 2 diabetes + sleep apnea + ADHD:
- **CPAP adherence matters infinitely more than sleep staging precision**
- **myAir's feedback loops drive behavior change, not data integration**
- **Fitbit alone provides sufficient activity context**
- **Complexity costs more than it gains**

**NEW INSIGHT (January 13, 2026):**

**AI analysis transforms passive data into actionable intelligence—IF it doesn't add cognitive load.**

- Perplexity HealthKit integration provides analysis layer without requiring dashboard monitoring
- Apple Health becomes invisible middleware, not another app to check
- AI-generated markdown reports integrate naturally with Workbench workflow
- One-tap daily sync maintains intentionality (not automatic background process)

**Keep this simple. Trust the stack. Revisit only when new AI capabilities emerge that align with "workbench, not warehouse" philosophy.**

---

## Future Project Idea (Pinned)

**Custom Fitbit → HealthKit Sync Tool**
- Eliminate third-party "Sync Fitbit to Health" app
- Build Python script with Fitbit API + HealthKit integration
- Direct Perplexity integration and automated markdown report generation
- Auto-commit health reports to Workbench repo
- See: `_tech/projects/2026-01-13-fitbit-healthkit-sync-project.md`

**Status:** Vibe coding project idea for future development
