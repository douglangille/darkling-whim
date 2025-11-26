Perfect. Here’s a **one-page GPT-5 Prompting Framework** tuned for your ZORA vault. It’s designed to be **durable, simple, and system-ready**—not a grab-bag of YouTube gimmicks.
### **BLUF**

Stop chasing “magic words.” Treat prompting as a system: **Role → Task → Constraints → Format → Iteration.** This anchors GPT-5’s routing and reasoning while staying reusable.

---

## **1. Core Prompt Skeleton**

  

Use this structure (adapt to task):

```
<Role>
You are [expert persona] with [perspective/constraints].

<Task>
Your goal: [clear statement of outcome].

<Constraints>
- [Scope/budget/time/length limits]
- [Tone or style]
- [Critical details, non-negotiables]

<Format>
Respond in [table / list / JSON / prose / script].

<Process>
Step 1: [what to consider]
Step 2: [how to evaluate]
Step 3: [final action]

<Iteration>
Critique your first pass against [rubric]. Revise once. Return final only.
```

---

## **2. Key Levers to Pull**

- **Role/Persona:** Stronger than “trigger words.” Sets lens + routing.
    
- **Task Clarity:** “Do X for Y purpose” beats “be creative.”
    
- **Constraints:** Anchor scope (budget, time, audience). Prevents drift.
    
- **Format:** Controls verbosity + usability.
    
- **Process Steps:** Forces reasoning without gimmicks.
    
- **Iteration:** Self-reflection, capped (1–2 cycles for speed, 3+ only if high stakes).
    

---

## **3. When to Flex**

- **Need precision →** add detail, constraints, or XML/JSON scaffolding.
    
- **Need creativity →** loosen constraints, but keep role and format.
    
- **Need brevity →** specify word/section limits.
    
- **Need rigor →** add rubric + self-critique loop.
    

---

## **4. Common Pitfalls**

- **Vagueness:** “Make it good” = wasted cycles.
    
- **Contradictions:** Confuses routing (“fun but not too crazy”).
    
- **Over-engineering:** Don’t bury GPT under 20 constraints. Aim for 4–6 anchors.
    
- **Endless loops:** Cap self-reflection cycles or you’ll get slow + bloated answers.
    

---

## **5. Quick Prompts (Copy-Paste Ready)**

- **Deep reasoning:** “Think step by step. Explain trade-offs before final.”
    
- **Critique:** “Evaluate against [criteria]. Suggest 2 fixes.”
    
- **Rewrite:** “Restructure into [format]. Keep tone [X].”
    
- **Summarize:** “Condense to 3 bullets for [audience].”
    

---

## **6. ZORA Integration**

- Store this as a **template note** in your vault.
    
- For fiction/worldbuilding: swap in narrative roles (“wry navigator,” “historian of Greyharbor”) instead of policy experts.
    
- For work: keep stock personas (analyst, strategist, coach) as modular inserts.
    
- Build a **prompt library** with tested role+constraint combos—reuse, don’t reinvent.
    
