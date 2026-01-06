# Excel Demo Scenarios - Three Real-World Examples

These three scenarios represent actual problems academic chairs face when working with PeopleSoft query exports. Each tab demonstrates a different Excel challenge and the type of prompt you'd use with Copilot to get help.

---

## Scenario 1: At-Risk Student Identification (Pivot Table)

**Tab Name:** `Scenario-1-AtRisk`

**Data Structure:**
```
Student Name | Course Code | Final Grade | Attendance %
---|---|---|---
Alex Johnson | BUS101 | 58% | 65%
Briana Chen | BUS101 | 72% | 88%
Chris Rodriguez | BUS101 | 45% | 52%
Diana Park | MATH201 | 81% | 92%
Evan Smith | MATH201 | 35% | 45%
Fatima Hassan | MATH201 | 76% | 88%
Gabriel Torres | ENG150 | 42% | 61%
Hannah Lee | ENG150 | 88% | 95%
Isabel Martinez | ENG150 | 51% | 70%
Jason Williams | BUS102 | 65% | 75%
Kayla Johnson | BUS102 | 38% | 48%
Liam Brown | BUS102 | 77% | 89%
Maya Patel | CHEM101 | 52% | 68%
Noah Davis | CHEM101 | 44% | 58%
Olivia Jackson | CHEM101 | 89% | 98%
```

**The Pain Point:**
Academic chair needs to identify students who are failing (grade < 60%) AND have poor attendance (< 70%) so they can intervene. With hundreds of rows, manual filtering is slow and error-prone.

**Copilot Prompt:**
```
I have an Excel file with columns for Student Name, Course Code, Final Grade, and Attendance Percentage. I need to create a pivot table that shows me how many students in each course have grades below 60% AND attendance below 70%. Walk me through how to set this up.
```

**What Copilot Will Help With:**
- How to select the data range
- Where to find the Pivot Table feature
- How to drag fields into rows/columns/values
- How to add filters to show only failing grades and low attendance

**Why This Matters:**
Instead of sorting, filtering, and counting manually, the chair gets a quick visual of which courses have the most at-risk students - critical for intervention planning.

---

## Scenario 2: Identify & Filter At-Risk Students (Formula/Conditional Formatting)

**Tab Name:** `Scenario-2-Filter`

**Data Structure:**
Same data as Scenario 1

**The Pain Point:**
Chair wants to highlight at-risk students in the original data (not create a pivot table) so they can see names, get contact info, and reach out directly.

**Copilot Prompt:**
```
I have student data with columns: Student Name, Course Code, Grade (%), Attendance (%). I need to identify all students who have BOTH a grade below 60% AND attendance below 75%. What's the best way to filter or highlight these students in Excel?
```

**What Copilot Will Help With:**
- Using AutoFilter to show only matching records
- Using conditional formatting to highlight cells meeting criteria
- Using a helper column with an IF formula to mark at-risk students
- Trade-offs between each approach

**Why This Matters:**
The chair can work directly with the student list, which may feed into outreach systems or integration with their CRM.

---

## Scenario 3: Combine Student Data from Two Sources (VLOOKUP/INDEX-MATCH)

**Tab Name:** `Scenario-3-Lookup`

**Data Structure - Sheet A (Contact Info):**
```
Student Name | Email | Phone
---|---|---
Alex Johnson | alex.j@student.edu | 902-555-0101
Briana Chen | b.chen@student.edu | 902-555-0102
Chris Rodriguez | c.rodriguez@student.edu | 902-555-0103
Diana Park | d.park@student.edu | 902-555-0104
Evan Smith | e.smith@student.edu | 902-555-0105
```

**Data Structure - Sheet B (Grades from PeopleSoft):**
```
Student Name | Course | Final Grade
---|---|---
Alex Johnson | BUS101 | 58%
Briana Chen | BUS101 | 72%
Chris Rodriguez | BUS101 | 45%
Diana Park | MATH201 | 81%
Evan Smith | MATH201 | 35%
```

**The Pain Point:**
Grades come from PeopleSoft, contact info is in a different system. Chair needs to match student names across both lists to send targeted emails to students who are failing.

**Copilot Prompt:**
```
I have two Excel sheets: one with student names and email addresses, another with student names and their current grades. How do I use a formula to pull the email address into the grades sheet so I can email students who are failing?
```

**What Copilot Will Help With:**
- VLOOKUP syntax and how it works
- INDEX-MATCH as an alternative (more flexible)
- Handling duplicate names or mismatched data
- Common errors and how to fix them
- How to structure the formula

**Why This Matters:**
Once the email addresses are matched to grades, the chair can sort/filter to get all failing students' contact info, then bulk email or import to their communication system.

---

## How to Use These in Your Demo

**Timing:** 5 minutes for this section

**Approach:**
1. "Here's what a real PeopleSoft export looks like - lots of data, lots of rows"
2. Show the three scenarios briefly
3. Pick ONE that resonates most with your audience
4. Say: "Let me ask Copilot how to solve this..."
5. Read your prompt into Copilot Chat
6. Show what it responds with
7. "This is what you'd do: follow these steps, try it, and if you get stuck, Copilot can help you troubleshoot"

**Don't try to:**
- Actually build the pivot table live (too time-consuming)
- Show every detail of the formula
- Expect them to become Excel experts

**Do show them:**
- That specific, clear prompts get useful answers
- That Copilot understands Excel concepts
- That this saves them from googling or calling IT

---

## Demo Notes

- These three scenarios represent the main types of Excel help ACs need
- Scenario 1 (Pivot Table) is probably most impactful for finding patterns
- Scenario 2 (Filter) is quickest to execute
- Scenario 3 (Lookup) is most technical but solves real integration problems
- All three can be solved in minutes with Copilot instead of hours of trial-and-error
