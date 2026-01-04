# Apple Reminders System

## Framework

**Now / Next / Later / Recurring**

## List Structure

### Core Lists

- **Today**: Daily execution
- **All Reminders**: Promotion/demotion lane (not for viewing regularly)
- **Now**: Current priority
- **Next**: Coming up
- **Later**: Backlog
- **Recurring**: Repeating tasks

## Smart List

### "Today + Now"

**Purpose**: Drives execution

**Logic**:
- Shows items from Today list
- Shows items from Now list
- Combined view for focused action

## System Design

- **Minimal pinned lists**: Today, All Reminders
- **All Reminders** = promotion/demotion staging area
- **Smart List** = execution driver
- Already provides ambient pressure
- No overengineering

## Friday Review Loop

### Name

"Friday Review → Clear, Promote, Reset"

### Format

**Recurring reminder** (not calendar appointment)

### Micro-Script (Embedded in Reminder Body)

```
1. Clear Today + Now
2. Promote/demote in All Reminders
3. Check Recurring
4. Stop when lineup feels good (or consciously skipped)
```

### Duration

5–10 minutes (minimally rigid)

### Compliance Definition

- Either completion **or** conscious decision not to
- Intentional skipping allowed
- No guilt

## Rationale

- Weekly review discipline gap acknowledged
- System already provides ambient pressure
- Prefer to wait until September to formalize broader routines
- Reminder > calendar appointment (less formal pressure)

## Open Loops

- Optional: compress loop into single mantra for memory (without opening reminder body)
- Visual NNL template or cross-system integration across Apple tools

## Discardables

- Calendar appointment as review trigger (superseded by reminder approach)
- Extra reflection or notes during review (kept minimal)
