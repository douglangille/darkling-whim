# Health Tech Stack - Current Implementation

**Last Updated:** January 13, 2026  
**Status:** Active - Revised after HealthKit integration discovery

---

## Current Stack (Validated)

### 🏥 Devices & Apps
- **Fitbit Inspire 3** — Activity tracking (steps, heart rate, sleep duration)
- **ResMed CPAP + myAir web** — Sleep apnea management (AHI, mask seal, usage hours)
- **OneTouch Reveal app** — Glucose monitoring (standalone, minimal use)
- **Apple Reminders** — Medication adherence (testosterone injections, daily medications)
- **iPhone 13** — Apple Health (data consolidation layer)
- **Sync Fitbit to Health** (by Yoshifumi Kanno) — Middleware for Fitbit → Apple Health sync

### 📊 What Each Tool Provides

| Function | Tool | Why It Works |
|----------|------|--------------|
| **Activity & movement** | Fitbit app | Native interface, reliable tracking |
| **Sleep apnea adherence** | myAir web app | Direct feedback, drives behavior change |
| **Glucose tracking** | OneTouch Reveal | Standalone, minimal UI friction |
| **CPAP pressure trends** | myAir web | Built-in analytics, clinical context |
| **Medication reminders** | Apple Reminders | Native iOS, recurring notifications, completion tracking |
| **Step targets** | Fitbit dashboard | Motivation, trend view |
| **Data consolidation** | Apple Health | Passive repository, potential for future AI analysis |
| **Data sync** | Sync Fitbit to Health | One-tap manual sync, no subscription |

---

## Recent Stack Evolution (January 13, 2026)

### What Changed

**Perplexity HealthKit Integration Investigation**
- Discovered HealthKit integration exists in Perplexity's toolkit
- Testing revealed **feature is non-functional** across all platforms
- Platform detection bug: appears on macOS (where it can't work), absent on iOS (where it should work)
- No authorization flow or official documentation
- **Decision:** Keep on hold until proper release

**Apple Health Reinstatement (Completed)**
- Previously deleted due to lack of actionable value
- **Current rationale:** Serves as data consolidation layer for potential future AI analysis
- **NOT used as dashboard** — Fitbit remains primary interface for daily checks
- Manual sync from Fitbit established (morning coffee ritual)

**Current Data Pipeline**
```
Fitbit → Sync App → Apple Health (passive storage)
↓
Workbench Repo (manual markdown notes)
```

### Why This Stack Works

**✅ ADHD-Friendly Design**
- **Cognitive load:** 3 primary contexts (myAir web, Fitbit app, Apple Reminders)
- **Apple Health is invisible:** Used as passive data store, not a dashboard to check
- **Task-switching cost:** Minimized by maintaining Fitbit as primary interface
- **Maintenance burden:** Minimal (one-tap daily sync)

**✅ Clinical Value Preserved**
- **CPAP adherence:** myAir's daily scores remain the primary feedback mechanism
- **Activity awareness:** Fitbit dashboard unchanged
- **Medication compliance:** Apple Reminders unchanged
- **Data preservation:** Apple Health maintains historical record for future use

**✅ Cost & Maintenance**
- **Spending:** $0 (Sync Fitbit to Health has no subscription fees)
- **Time:** <1 minute daily for manual sync
- **Privacy:** All data stays within Apple ecosystem

---

## What Was Rejected (And Why)

### ❌ Apple Health as Hub (Previous Decision - Still Valid)
**Problem:** Creates infrastructure to solve a problem that doesn't exist.
- Unified dashboards improve outcomes *only* when paired with professional coaching or real-time feedback
- Self-guided data consolidation without clinical support does NOT improve health metrics

**CURRENT CONTEXT:** Apple Health now serves as **passive data repository** for potential future AI analysis.
- Still don't check Apple Health app as primary interface
- Fitbit remains the daily dashboard
- Data preserved for when AI analysis tools become properly available

### ❌ Perplexity HealthKit Integration (January 2026)
**Problem:** Feature doesn't actually work yet.
- Platform detection bug (backwards availability)
- No authorization flow exists
- No official documentation
- Would add cognitive load to troubleshoot non-functional feature

**Decision:** Revisit quarterly. Don't build workflow around vapor features.

### ❌ Third-Party Sync Apps (PowerSync, Sync Solver, etc.)
**Problem:** Maintenance burden > benefit.
- Require repeated reconnection when APIs throttle or update
- Cost ($10-60) for feature that doesn't improve outcomes

**CURRENT SOLUTION:** "Sync Fitbit to Health" (Yoshifumi Kanno)
- $0 subscription cost
- One-tap manual sync (intentional, not automatic)
- 10+ health categories supported
- Aligns with "workbench, not warehouse" philosophy

### ❌ Fitbit Premium
**Problem:** "Pretty charts for data you already have."
- You don't need guided workouts or Daily Readiness score
- You already hit your 10k steps/day target
- Sleep stage data is unreliable with CPAP mask interference

**Decision:** Remain on free tier indefinitely.

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

### Biweekly (2 min)
- Respond to **testosterone injection reminder** in Apple Reminders
- Complete injection
- Mark reminder as complete

### Monthly (10 min)
- Review **Fitbit activity trends**
  - Check step averages vs 10k target
  - Acknowledge sleep trend data (but don't over-interpret due to CPAP mask interference)
  - Use for motivation, not clinical decisions

### Quarterly (During doctor appointments)
- Share **myAir AHI export** with Dr. Sharma if requested
- Discuss **A1C blood work results**
- Review **blood pressure readings** (from home checks or clinic)
- Confirm **testosterone therapy effectiveness** with Dr. Massaro
- Update **patient_summary_jan2026.md** with new lab values
- **Check Perplexity HealthKit status** (is it working yet?)

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

---

## Review Schedule

### 3-Month Check-In (April 2026)
1. Is daily Fitbit → Health sync routine sustainable? (If no, reassess)
2. Has Perplexity HealthKit integration launched properly? (Check iOS availability)
3. Am I checking Apple Health as a dashboard? (If yes, delete app and reassess)
4. Has CPAP adherence maintained or improved?
5. Have I missed testosterone injections? (If yes, adjust reminder time)

### 6-Month Check-In (July 2026)
1. Has CPAP adherence improved, maintained, or declined?
2. Has activity level (steps) improved, maintained, or declined?
3. Is Apple Health data sync adding value or cognitive load?
4. Are Workbench health notes being referenced for clinical discussions?
5. Any new devices or apps tempting you back to unnecessary complexity? (Resist.)

### Annual Check-In (January 2027)
1. Review A1C trends over the year
2. Review CPAP adherence patterns
3. Review activity/weight trends
4. Assess whether Apple Health data preservation was valuable
5. Assess whether tech stack needs adjustments based on changing health needs

---

## Key Insights

**You were building infrastructure to solve a problem that doesn't exist.**

For healthspan optimization at 53 with Type 2 diabetes + sleep apnea + ADHD:
- **CPAP adherence matters infinitely more than sleep staging precision**
- **myAir's feedback loops drive behavior change, not data integration**
- **Fitbit alone provides sufficient activity context**
- **Complexity costs more than it gains**

**UPDATED INSIGHT (January 13, 2026):**

**Don't build workflows around features that don't exist yet.**

- Perplexity HealthKit integration looked promising but isn't functional
- Apple Health now serves as passive data repository only
- Fitbit remains primary dashboard for daily monitoring
- Manual markdown health notes continue in Workbench
- Revisit AI analysis tools quarterly as they mature

**Key principle:** Maintain working stack until better option *actually* exists and is proven to work.

---

## Future Possibilities (On Hold)

### AI-Powered Health Analysis
**When Perplexity HealthKit works properly:**
- Natural language queries about health trends
- Automated weekly/monthly markdown reports
- Correlation detection (activity vs sleep, steps vs energy)
- Integration with Workbench workflow

**Status:** Check quarterly (next: April 2026)

### Custom Fitbit → HealthKit Sync Tool
**If needed in future:**
- Python script with Fitbit API + HealthKit integration
- Direct Perplexity integration when available
- Automated markdown report generation
- Auto-commit health reports to Workbench repo

**Status:** Vibe coding project idea, very low priority

---

**Keep this simple. Trust the stack. Revisit only when proven AI capabilities emerge.**