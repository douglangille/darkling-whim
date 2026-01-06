# Demo Testing Notes - January 6, 2026

## Testing Environment
- **Primary Account**: Doug's account with Copilot add-on (Work + Web tabs available)
- **Demo Account**: Half-borked demo account with basic licensing (closer to audience experience)
- **Audience Experience**: Web-grounded Copilot Chat only, no licensed add-ons

---

## Demo 1: Research & Brainstorming - Academic Chair Challenges

### Status: ✅ TESTED & WORKING PERFECTLY

### Prompt Used:
```
Find recent articles about administrative challenges for academic chairs in community colleges
```

### What Happened:
- Retrieved 3 relevant Inside Higher Ed articles from Aug 2025, Feb 2025, and 2022
- Articles directly addressed audience pain points:
  - "Being Chair at a Time of Existential Challenge" (Aug 2025)
  - "Chairs Can Be the Changemakers Colleges Need" (Feb 2025)
  - "Department chair leadership: Exploring the role's demands and tensions" (2022)
- Key themes resonated: role ambiguity, limited authority, crisis management, lack of training
- Copilot provided structured summary with Crisis Management, Equity Leadership Gaps, Emerging Solutions
- **BONUS**: Offered follow-up actions: "Create a summary report", "Generate a slide deck", "Compare with four-year colleges"

### Follow-Up Test: "Create a summary report"
**Result**: Generated a full structured summary with:
- Conflict resolution and performance evaluation
- Equity and inclusion leadership
- Crisis Management section
- Equity Leadership Gaps
- Emerging Solutions (Professional Development Programs, Collaborative Budgeting, Equity-Focused Leadership Training)
- Bottom Line with actionable insights
- Additional follow-up options: Format into PDF, Create PowerPoint deck, Draft executive summary (1-page)

### Why This Works:
- Web-grounded Copilot pulls from current, relevant sources
- Articles are from August 2025 and February 2025 - very recent
- Language matches academic administrator experience
- Shows immediate practical value for research and staying current

### Demo Strategy:
- Use this as opening demo to establish credibility
- Show how web-grounding pulls current higher ed literature
- Emphasize the "I see my challenges reflected here" factor
- Consider clicking "Create a summary report" to show follow-up capability

---

## Demo 2: Email Clarity - Grade 8 Reading Level

### Status: ✅ TESTED & WORKING BEAUTIFULLY

### Original Email (Academic-ese):
```
Subject: Program Planning Documentation Requirements

Dear Students,

This correspondence is to inform you that all students must complete and submit their Program Planning Forms (PPF) to the Academic Advising Office no later than Friday, January 10th, 2026, at 4:00 PM AST.

Failure to comply with this deadline will result in a registration hold being placed on your student account, thereby preventing you from accessing the course registration system for the upcoming semester. Students who do not submit their PPF in a timely manner will be required to meet with their academic advisor to discuss their academic trajectory and program requirements prior to the hold being removed.

The PPF can be accessed via the Student Portal under the "Academic Planning" tab. Should you encounter any technical difficulties or have questions regarding the completion of this form, please contact the Academic Advising Office during regular business hours (Monday-Friday, 8:30 AM - 4:30 PM).

Your prompt attention to this matter is appreciated.

Sincerely,
Academic Advising Office
```

### Prompt Used:
```
Rewrite this email for grade 8 reading level while keeping all important information and deadlines. Make it clear and friendly.
```

### Result:
```
Subject: Program Planning Form – Due January 10

Dear Students,

Please make sure to complete and submit your Program Planning Form (PPF) by Friday, January 10, 2026, at 4:00 PM AST.

If you miss this deadline:
• A registration hold will be placed on your account.
• You will not be able to register for next semester's courses until the hold is removed.
• To remove the hold, you'll need to meet with your academic advisor to review your program plan.

You can find the PPF in the Student Portal under the "Academic Planning" tab.

If you have any questions or run into technical problems, please contact the Academic Advising Office during business hours:
Monday–Friday, 8:30 AM – 4:30 PM.

Thank you for taking care of this on time!

Academic Advising Office
```

### What Changed:
- Subject line: Clear, concise, deadline-focused
- Opening: "This correspondence is to inform you" → "Please make sure to"
- Structure: Dense paragraphs → Bullet points for consequences
- Language: "Failure to comply", "thereby preventing", "academic trajectory" → Plain language
- Tone: Formal/bureaucratic → Clear and friendly
- Formatting: Better use of whitespace and bullets

### Follow-Up Offered by Copilot:
- "Add bold highlights for key dates"
- "Create a version for SMS reminders"
- "Simplify the tone further"

### Why This Works:
- Dramatic, visible improvement that's immediately obvious
- Addresses real accessibility and literacy concerns
- No confidential data in the demo
- Shows practical time-saving (no need to manually rewrite)
- Demonstrates understanding of audience reading levels

### Demo Strategy:
- Show original email first - let them cringe at their own writing
- Paste prompt, get result
- Do side-by-side comparison
- Emphasize: "This is humbling every single time"
- Remind about privacy: draft generic, then customize with student names afterward

---

## Demo 3: Excel Help - PeopleSoft Data Analysis

### Status: ✅ TESTED & WORKING EXCELLENTLY

### ⚠️ CRITICAL DISTINCTION - MUST EMPHASIZE IN DEMO:
**Copilot teaches you HOW to do the Excel analysis. It does NOT do the transforms for you.**
- Demo 1 (Research): Copilot DOES the research and summarizing
- Demo 2 (Email): Copilot DOES the rewriting  
- Demo 3 (Excel): Copilot TEACHES you the steps - you still have to execute them yourself

**Why this matters for your audience:**
- They can't paste their actual Excel file into web-grounded Copilot
- Even if they could, it won't manipulate their data
- The value is in learning the technique (helper columns, pivot tables, formulas)
- They save time by not googling or trial-and-error, but they still do the work

**How to frame this:**
- "The first two demos, Copilot did the work. This one? It's your Excel tutor."
- "You're learning to fish, not getting a fish delivered."
- "It won't touch your data - but it'll teach you exactly what to do with it."

### Prompt Used:
```
I have an Excel file with columns for Student Name, Course Code, Final Grade, and Attendance Percentage. I need to create a pivot table that shows me how many students in each course have grades below 60% AND attendance below 70%. Walk me through how to set this up.
```

### Copilot Response:

**Step 1: Prepare Your Data**
- Ensure columns are clearly labeled: Student Name | Course Code | Final Grade | Attendance %
- Confirm Final Grade and Attendance % are numeric (remove % signs if needed)

**Step 2: Add a Helper Column**
- Insert new column called "At Risk"
- Formula example (assuming Final Grade in C and Attendance in D):
  `=IF(AND(C2<60,D2<70),"Yes","No")`
- This marks students who meet both conditions

**Step 3: Create the Pivot Table**
- Select entire data range (including the new "At Risk" column)
- Go to Insert → PivotTable
- Place the Pivot Table in a new worksheet

**Step 4: Configure the Pivot Table**
- Rows: Drag Course Code
- Filters: Drag At Risk
- Values: Drag Student Name (set to Count)

**Step 5: Apply Filter**
- In the At Risk filter, select "Yes"
- This will show the count of students per course who have Final Grade < 60% AND Attendance < 70%

**Result Example (Based on Your Data):**
```
Course Code | Count of Students
BUS101      | 2
MATH201     | 1
ENG150      | 1
BUS102      | 1
CHEM101     | 2
```

### Follow-Up Offered by Copilot:
- "Create this pivot table in your uploaded file and send it back" (won't work with web-grounded)
- "Generate a quick chart (bar graph) showing these counts" (theoretical, not actual data manipulation)

### Why This Works:
- Clear, numbered steps anyone can follow
- Teaches the helper column technique (valuable Excel skill most people don't know)
- Explains WHY each step is needed
- Provides example result so you know what success looks like
- No actual student data needed - teaches the concept
- Saves time vs. googling or YouTube tutorials

### Demo Strategy:
- **SET EXPECTATIONS FIRST**: "This demo is different - Copilot won't do it for you, it'll teach you how"
- Show the prompt clearly
- Scroll through the response highlighting key steps
- **Emphasize Step 2** (helper column): "This is the trick most people don't know - Copilot just taught you that"
- Point out the example result table: "This is what you'd get if you follow these steps"
- **Be explicit**: "Now you have to go open your actual Excel file and follow these instructions. Copilot didn't manipulate your data - it can't with web-grounded access. But you just saved 30 minutes of googling and trial-and-error."
- Acknowledge: "Taking an Excel course would be better long-term, but when you need an answer today and students are waiting..."

### Alternative Scenarios (Not Tested, But Available if Needed):

#### Scenario 2: Filter/Highlight
```
I have student data with columns: Student Name, Course Code, Grade (%), Attendance (%). I need to identify all students who have BOTH a grade below 60% AND attendance below 75%. What's the best way to filter or highlight these students in Excel?
```

#### Scenario 3: VLOOKUP
```
I have two Excel sheets: one with student names and email addresses, another with student names and their current grades. How do I use a formula to pull the email address into the grades sheet so I can email students who are failing?
```

**Recommendation**: Stick with Scenario 1 (Pivot Table) - it's the most impactful and best-tested.

---

## Demo 4: Effective Brainstorming/Prompting

### Status: DECISION MADE - Use Option B

### Approach: Integrate Prompting Lessons Into All Three Demos

Rather than a standalone fourth demo, weave prompting lessons throughout:

**During Demo 1 (Research):**
- "Notice I said 'community colleges' not just 'higher education' - specificity matters"

**During Demo 2 (Email):**
- "I told it grade 8 reading level, keep all info, make it friendly - three specific instructions"

**During Demo 3 (Excel):**
- "I described my exact column names and the exact conditions I needed - that specificity gets better help"

**In Wrap-Up (Minute 21-25):**
- "Notice the pattern? Vague prompts get vague answers. Specific prompts get useful help."
- Quick comparison if time:
  - Bad: "Give me PD ideas" 
  - Good: "I'm presenting to community college academic chairs in Nova Scotia who are overwhelmed with admin tasks. Three practical strategies they can implement this week?"

### Why This Approach:
- Teaches prompting without taking extra demo time
- Makes the connection explicit as you go
- More impactful than standalone examples
- Keeps focus on practical outcomes

---

## Technical Observations

### What's Available in Web-Grounded Copilot:
✅ Web search and article retrieval
✅ Text rewriting and simplification  
✅ Excel formula help and step-by-step instructions
✅ Helper column technique teaching
✅ Summary generation
✅ Follow-up action suggestions
✅ Example results/visualizations
✅ Chat history (visible in sidebar)
✅ Library, Create, Teach, Agents features (visible but may require licensing)

### What's NOT Available:
❌ Direct document upload/analysis (no internal files)
❌ Access to OneDrive/SharePoint documents
❌ Integration with Outlook/Word/Excel apps (requires licensed add-on)
❌ **Actually creating/modifying Excel files (can only teach you how)**

### Privacy Reminders:
⚠️ Never paste student names, IDs, grades, or personal information
⚠️ Never paste confidential internal documents
⚠️ Draft generic versions, then add specific details manually afterward
⚠️ Rule of thumb: "Would I post this on Twitter?" - if not, don't put it in Copilot

---

## Final Session Flow (30 Minutes)

### Minute 0-5: Setup & Expectations
- Show of hands: Who's seen Copilot button? Who's used it?
- Set expectation: "We're using web-grounded Copilot - no licensed add-ons, playing it safe with privacy"
- Positioning: "I'm 5 minutes ahead, not an expert. I'm just experimenting."
- "We're going to look at three practical uses you can try this week"

### Minute 5-10: Demo 1 - Research
- "Let's start by seeing what's current about YOUR challenges"
- Show prompt, emphasize specificity: "community colleges, not just higher ed"
- Show results - Inside Higher Ed articles
- Point out themes: "This is you, right? Role ambiguity, limited training?"
- Optional: Click "Create a summary report"
- Transition: "Finding info is one thing. Creating content?"

### Minute 10-15: Demo 2 - Email Clarity
- "Who writes emails that could be clearer?" (expect laughs/nods)
- Show original academic email
- Point out prompt: "grade 8 level, keep info, make friendly - three specific asks"
- Show result
- Let them react to the difference
- Privacy reminder: "Generic email. Don't paste student names."
- "This is humbling every time"

### Minute 15-21: Demo 3 - Excel
- "PeopleSoft dumps - who loves them?" (expect groans)
- **SET EXPECTATIONS**: "This demo is different. The first two, Copilot did the work. This one? Copilot is your Excel tutor."
- Context: "Can't paste real data, and even if you could, it won't manipulate it. But it WILL teach you how."
- Show prompt - note column specificity
- Scroll through response:
  - Helper column is the key technique
  - Step-by-step approach anyone can follow
  - Example result shows what you'd get
- **Be explicit**: "You still have to go do this in your actual Excel file. But you just saved 30 minutes of googling."
- "You're learning to fish, not getting a fish delivered."
- Acknowledge: "Excel course would be better long-term, but when you need help today and students are waiting..."

### Minute 21-25: Wrap-Up & Pattern Recognition
- "See the pattern in all three?"
- **Specificity**: Vague prompts = vague answers
- **Different value propositions**:
  - Research: Copilot does it
  - Email: Copilot does it
  - Excel: Copilot teaches you
- **Current info**: Web-grounded strength
- "This is table stakes, not advanced AI tricks"

### Minute 25-30: Q&A & Challenge
- "Questions?"
- Honest about limitations: "Web-grounded = privacy-safe but limited"
- "More advanced stuff needs licensed tools"
- "But research, writing, learning Excel - that's real value TODAY"
- **The challenge**: "Pick ONE. Try it ONCE this week."
- "I'm five minutes ahead because I'm experimenting. You can too."
- Share email for follow-up

---

## Pre-Session Checklist

- [x] Test academic chair research prompt ✅
- [x] Test email rewrite prompt ✅
- [x] Test Excel pivot table prompt ✅
- [x] Create Excel file with sample data ✅
- [x] Decide on Demo 4 approach ✅ (integrated)
- [x] Clarify Excel teaching vs. doing distinction ✅
- [ ] Practice full run-through with timing
- [ ] Screenshot key results as backup
- [ ] Final test in demo account morning of session
- [ ] Have prompts ready to copy/paste (use cheat sheet)
- [ ] Prepare to share email in chat at end

---

## Key Talking Points to Weave In

- "Notice how specific the prompt was..."
- "This is web-grounded, so no confidential data..."
- "First two demos, Copilot did the work. This one, Copilot teaches you."
- "You're learning to fish, not getting a fish..."
- "This is table stakes, not advanced AI..."
- "I'm five minutes ahead, experimenting..."
- "This is humbling every time..."
- "When you need an answer today and students are waiting..."

---

## Emergency Backup Plan

**If Copilot is slow/broken:**
- Have screenshots of successful results ready
- Walk through what you tested: "Here's what it gave me yesterday..."
- The conversation about possibilities is still valuable

**If running long:**
- Skip "Create summary report" follow-up in Demo 1
- Don't show Excel file, just describe it
- Shorten wrap-up, extend Q&A

**If running short:**
- Show "Create summary report" in Demo 1
- Do bad vs. good prompt comparison in wrap-up
- Deeper dive on helper column technique in Excel

**Lean into authenticity:**
- If something breaks: "This is why I say I'm experimenting - let's try again"
- The "5 minutes ahead" positioning gives you permission to not be perfect
