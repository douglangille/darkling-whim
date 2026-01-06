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

### Status: ⚠️ NOT FULLY TESTED YET (Prompts prepared, need to test in Copilot)

### Three Scenarios Prepared:

#### Scenario 1: Pivot Table for At-Risk Students
**Prompt**:
```
I have an Excel file with columns for Student Name, Course Code, Final Grade, and Attendance Percentage. I need to create a pivot table that shows me how many students in each course have grades below 60% AND attendance below 70%. Walk me through how to set this up.
```

**Sample Data**: 15 students across BUS101, MATH201, ENG150, BUS102, CHEM101
- At-risk students included: Chris Rodriguez (45%, 52%), Evan Smith (35%, 45%), Gabriel Torres (42%, 61%), Kayla Johnson (38%, 48%), Noah Davis (44%, 58%)

#### Scenario 2: Filter/Highlight At-Risk Students
**Prompt**:
```
I have student data with columns: Student Name, Course Code, Grade (%), Attendance (%). I need to identify all students who have BOTH a grade below 60% AND attendance below 75%. What's the best way to filter or highlight these students in Excel?
```

**Same data as Scenario 1**

#### Scenario 3: VLOOKUP for Email Matching
**Prompt**:
```
I have two Excel sheets: one with student names and email addresses, another with student names and their current grades. How do I use a formula to pull the email address into the grades sheet so I can email students who are failing?
```

**Sample Data**:
- Contact Info sheet: 10 students with emails (alex.j@student.edu, etc.) and phone numbers
- Grades sheet: Same 10 students with courses and final grades

### Expected Copilot Response:
- Step-by-step instructions for each technique
- Explanation of Excel functions (PIVOT, FILTER, IF, VLOOKUP, INDEX-MATCH)
- Common errors and how to avoid them
- Alternative approaches

### Why This Works:
- No actual student data goes into Copilot (web-grounded limitation respected)
- Shows how to get help with Excel concepts and formulas
- Addresses real PeopleSoft query export pain points
- Teaches fishing, doesn't just give fish

### Demo Strategy:
- Show the Excel file with sample data (brief glance)
- Pick ONE scenario based on time and audience engagement
- Read the prompt to Copilot
- Show the response
- Emphasize: "This isn't analyzing your data - it's teaching you how to analyze it yourself"
- Acknowledge: "Yes, learning Excel properly would be better long-term, but when you need an answer today..."

---

## Demo 4: Effective Brainstorming/Prompting

### Status: ⚠️ NOT TESTED - NEEDS DEFINITION

### Options:

**Option A: Bad vs. Good Prompt Comparison**
- Bad: "Give me professional development ideas for faculty"
- Good: "I'm presenting to community college academic chairs in Nova Scotia. They're overwhelmed with administrative tasks. What are three current best practices from higher education for helping chairs manage their workload? Focus on practical, implementable strategies."

**Option B: Integrate into other demos**
- Show how specificity in prompts led to better results in demos 1-3
- Make it a teaching moment rather than standalone demo

**Option C: Skip entirely**
- Use time for deeper Q&A on demos 1-3
- Address brainstorming in closing remarks

### Decision needed: Which approach fits best in 30-minute timeframe?

---

## Technical Observations

### What's Available in Web-Grounded Copilot:
✅ Web search and article retrieval
✅ Text rewriting and simplification
✅ Excel formula help and explanations
✅ Summary generation
✅ Follow-up action suggestions
✅ Chat history (visible in sidebar)
✅ Library, Create, Teach, Agents features (visible but may require licensing)

### What's NOT Available:
❌ Direct document upload/analysis (no internal files)
❌ Access to OneDrive/SharePoint documents
❌ Integration with Outlook/Word/Excel apps (requires licensed add-on)
❌ Custom agent creation (visible but may not work)

### Privacy Reminders:
⚠️ Never paste student names, IDs, grades, or personal information
⚠️ Never paste confidential internal documents
⚠️ Draft generic versions, then add specific details manually afterward
⚠️ Rule of thumb: "Would I post this on Twitter?" - if not, don't put it in Copilot

---

## Session Flow Recommendations

### Minute 0-5: Setup & Expectations
- Show of hands: Who's seen Copilot button? Who's used it?
- Set expectation: Web-grounded version, no licensed add-ons
- Positioning: "I'm 5 minutes ahead, not an expert"

### Minute 5-10: Demo 1 - Academic Chair Research
- "Let's start by seeing what's current about your challenges"
- Show prompt, show results
- Click "Create a summary report" to show follow-up
- Transition: "This is about finding current information. But what about creating content?"

### Minute 10-15: Demo 2 - Email Clarity
- "How many of you write emails that could be clearer?"
- Show original academic-ese email
- Show prompt and result
- Side-by-side comparison
- Privacy reminder

### Minute 15-20: Demo 3 - Excel Help
- "PeopleSoft dumps - who loves them?"
- Quick glimpse of sample data
- Pick ONE scenario based on engagement
- Show prompt and Copilot's teaching response
- Emphasize: Teaching vs. doing

### Minute 20-25: Demo 4 (if time) OR Deeper Q&A
- Decision point based on how previous demos went
- If running long: Skip demo 4, go straight to Q&A

### Minute 25-30: Q&A, Challenge, Close
- Address limitations honestly
- "Pick one thing to try this week"
- "I'm 5 minutes ahead, experimenting within our boundaries"
- Share follow-up resources

---

## Outstanding Items to Test

- [ ] Actually test Excel prompts in Copilot (all three scenarios)
- [ ] Test brainstorming bad vs. good prompt comparison
- [ ] Verify all follow-up action buttons work in demo account
- [ ] Create backup prompts in case primary ones fail
- [ ] Screenshot key results for reference during live demo
- [ ] Test in demo account one more time before session

---

## Notes for Tomorrow Morning

**What worked really well:**
- Academic chair research prompt - perfect audience connection
- Email rewrite demo - dramatic, visible improvement
- Follow-up action buttons add bonus value

**What needs attention:**
- Excel prompts need live testing
- Decision on Demo 4 approach
- Timing practice (30 minutes goes fast)

**Emergency backup plan:**
- If demos fail: Talk through what you would have shown
- Have screenshots ready as fallback
- Lean into "experimenting together" if things break
