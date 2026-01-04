# Health Data Integration

## Device Ecosystem

- **Fitbit Inspire 3**: Sleep, activity, weight tracking
- **iPhone 13**: Central hub
- **ResMed AirSense 11 CPAP**: Sleep apnea management
- **OneTouch Verio Reveal**: Glucose monitoring

## Problem Statement

Fragmented health data across multiple apps with poor integration.

## Solution Architecture

### Apple Health as Hub

- Central aggregation point
- Already using Apple Shortcuts to track "in bed" time via sleep focus + charging status

### IFTTT Integration (Free Tier)

**Current Setup**:
- 2 applets maximum on free plan
- Sleep sync: Fitbit → Apple Health
- Weight sync: Fitbit → Apple Health

**Limitation**: Fitbit API doesn't expose sleep stage data (REM, deep, light) to third parties

### ResMed MyAir

- Can read sleep data from Apple Health
- Does not directly integrate with Fitbit
- Syncs after IFTTT bridge established

### PowerSync

- Fallback option: $12.99 CAD lifetime
- Potential backdoor solution if IFTTT limitations surface
- Alternative: myFitnessSync (also supports summary data only)

### OneTouch Reveal

- Poor integration
- Lack of useful trend analysis
- Currently tolerated, no workaround pursued
- Manual CSV export/import noted but not pursued

## Decisions Made

- Selected Sleep + Weight as two high-value IFTTT applets
- Try IFTTT free plan before purchasing PowerSync
- Acknowledged glucose monitoring limitations
- No manual workarounds for Fitbit sleep stages at this time

## Open Loops

- Evaluate IFTTT sleep sync impact on ResMed MyAir after overnight test
- Consider PowerSync if IFTTT insufficient
- Trophy Room dashboard concept (visualization tied to health data)
- Narrative OS productivity system (future reactivation)
- Optional: manual entry or Shortcuts-based Fitbit sleep stage workaround

## Discarded Options

- Zapier (not viable)
- Scriptable (not viable)
- Homebridge (not viable)
- Manual CSV export/import for sleep and glucose
- Android options (focus is iPhone + Apple Health)
- Fitbit Premium (not needed for current use case)
