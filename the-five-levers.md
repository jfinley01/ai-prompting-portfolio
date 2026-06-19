# The Five Levers

When a prompt isn't working, most people rewrite it from scratch. That's slow and imprecise.

A better approach: identify *which dimension* of the prompt is underspecified, and adjust that lever specifically. This framework names the five dimensions you can tune in any prompt, and describes what each one actually does.

---

## The levers

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   ROLE       →  who the model is being              │
│   TASK       →  what output you want                │
│   CONTEXT    →  what the model needs to know        │
│   FORMAT     →  what the output should look like    │
│   TONE       →  how it should sound                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

### Lever 1: Role

**What it is:** The persona or professional identity you assign to the model.

**What it does:** Role calibrates default assumptions about depth, vocabulary, and perspective. A "staff attorney" and a "product manager" asked the same question will emphasize different things — and both will differ from no role at all.

**How to use it:**
- Be specific about seniority: "junior copywriter" vs. "senior brand strategist" produces different output
- Include the audience relationship: "a consultant advising a CEO" is different from "a consultant writing for a general audience"
- Roles work best when they're realistic — don't assign a role the model can't credibly play (e.g., "You are the world's foremost expert on X" adds nothing useful)

**Signs this lever needs adjusting:** Output is too shallow, too technical, or pitched at the wrong audience.

---

### Lever 2: Task

**What it is:** The specific output you're asking for.

**What it does:** Task precision determines whether the model produces what you actually need or what it thinks you want. Vague tasks produce vague outputs.

**How to use it:**
- Name the *output type* explicitly: summary, draft, analysis, list, comparison, script, table
- Specify *scope*: "three bullet points" vs. "a comprehensive overview"
- Include the *purpose*: "for internal review" vs. "for publication" vs. "to help me make a decision"

**Signs this lever needs adjusting:** You got output, but it's not the thing you needed. The model answered a different question than the one you were actually asking.

---

### Lever 3: Context

**What it is:** Background information the model needs to avoid producing generic output.

**What it does:** Context is what makes the output specific to your situation rather than applicable to any situation. It's the difference between advice and a brief.

**How to use it:**
- Include the situation: industry, company type/size, decision being made
- Include constraints that aren't obvious: budget, timeline, what's already been tried
- Include what the model *shouldn't* assume: if there are common misconceptions about your situation, name them

**Signs this lever needs adjusting:** Output is technically correct but not actually useful for your specific case. The model is answering the general question when you needed the specific one.

---

### Lever 4: Format

**What it is:** Instructions for the structure, length, and presentation of the output.

**What it does:** Format determines whether the output is immediately usable or requires significant cleanup. Most prompts under-specify format, which means the model guesses — and often guesses wrong.

**How to use it:**
- Specify *structure*: headers, bullets, numbered list, table, flowing prose
- Specify *length*: word count, number of bullets, number of sections
- Specify *exclusions*: what to leave out is often more useful than what to include
- Use one-line examples: "Structure it like this: [header] / [2-3 bullet points] / [one-sentence so-what]"

**Signs this lever needs adjusting:** The content is right but the format is wrong. You spend more time reformatting the output than you do on the underlying task.

---

### Lever 5: Tone

**What it is:** The voice, register, and emotional quality of the output.

**What it does:** Tone is what makes the output sound like *you* (or like your intended audience) rather than like a generic AI assistant.

**How to use it:**
- Describe tone through relationships and analogies, not just adjectives: "direct, like a peer who won't waste your time" is more useful than "professional"
- Name what to avoid: "no corporate filler," "don't hedge," "don't apologize before delivering bad news"
- One strong example beats a paragraph of tone description

**Signs this lever needs adjusting:** The content is right and the format is right, but it sounds off — too formal, too casual, too diplomatic, too flat. When people say "it sounds like an AI wrote it," this is usually the lever to pull.

---

## Diagnostic workflow

When output disappoints, ask:

1. **Is the task clear?** Could someone describe in one sentence exactly what the finished output should look like? → Lever 2
2. **Is the role right?** Is the model calibrated to the right level of expertise and audience? → Lever 1
3. **Is there enough context?** Is the output generic when you needed specific? → Lever 3
4. **Is the format specified?** Are you reformatting the output more than using it? → Lever 4
5. **Does the tone fit?** Does it sound right for the situation and audience? → Lever 5

Adjust one lever at a time. If you change everything at once, you can't learn which change fixed the problem.

---

## Example: applying the framework

**Starting prompt:**
> "Write a proposal for a new HR policy."

| Lever | Current state | Improvement |
|-------|--------------|-------------|
| Role | Not set | "You are an HR business partner at a 500-person tech company" |
| Task | Vague | "Draft a one-page policy proposal for manager approval" |
| Context | None | "We're addressing a pattern of inconsistent remote work decisions across teams" |
| Format | Unspecified | "Problem / Proposed policy / Implementation steps / Expected outcome — one paragraph each" |
| Tone | Not set | "Clear and direct; this is an internal document, not a legal filing" |

**Revised prompt:**
> You are an HR business partner at a 500-person tech company. Draft a one-page policy proposal for manager approval addressing a pattern of inconsistent remote work decisions across teams. Structure it as: Problem / Proposed policy / Implementation steps / Expected outcome — one paragraph each. Clear and direct tone; this is an internal document, not a legal filing.

Same task. Dramatically different output.
