# Prompt Evaluation Rubric

A repeatable framework for auditing and improving prompts — useful for coaching individuals, reviewing team workflows, or building a shared standard.

---

## How to use this

Run any prompt through the five dimensions below. Score each 1–3. A prompt scoring 12–15 is production-ready. A prompt scoring below 8 needs a rewrite before you rely on it.

This rubric is also useful as a *diagnostic* — if output is disappointing, the dimension with the lowest score is usually where to focus first.

---

## The five dimensions

### 1. Task clarity
*Does the prompt name a specific output, or does it describe a vague activity?*

| Score | What it looks like |
|-------|-------------------|
| 1 | Task is undefined ("help me with this," "what do you think?") |
| 2 | Task is named but ambiguous ("write something about X," "analyze this") |
| 3 | Task is specific: output type, purpose, and scope are all named |

**Test:** Can you describe in one sentence exactly what the finished output looks like? If not, score 1 or 2.

---

### 2. Audience and role
*Does the prompt establish who the model is and who it's writing for?*

| Score | What it looks like |
|-------|-------------------|
| 1 | No role or audience mentioned |
| 2 | Either role or audience is named, but not both |
| 3 | Both role (who the model is being) and audience (who will read/use the output) are specified with enough detail to matter |

**Test:** If you swapped the audience from "a CFO" to "a first-year intern," would the output change significantly? If yes, the audience specification is doing useful work. If the prompt doesn't include audience at all, it should.

---

### 3. Format and constraints
*Does the prompt specify what the output should look like and what to leave out?*

| Score | What it looks like |
|-------|-------------------|
| 1 | No format guidance; length, structure, and tone are all unspecified |
| 2 | Some guidance present (e.g., "keep it short") but incomplete |
| 3 | Format is fully specified: structure, length, tone, and at least one "do not include" instruction |

**Common omissions:** people specify what to include but rarely what to *exclude*. Exclusions are often more useful — they prevent padding, hedging, and off-topic content.

---

### 4. Context and grounding
*Does the prompt give the model enough background to avoid generic output?*

| Score | What it looks like |
|-------|-------------------|
| 1 | No context — the model has to guess at situation, stakes, or relevant background |
| 2 | Some context but key details are missing (company type, decision at stake, etc.) |
| 3 | Enough context that a smart human seeing this prompt could produce useful output without needing to ask clarifying questions |

**Rule of thumb:** If you were briefing a smart new hire, what would you tell them before they started? That's the context the model also needs.

---

### 5. Iteration readiness
*Is the prompt written as a starting point for refinement, or as a one-shot throw?*

| Score | What it looks like |
|-------|-------------------|
| 1 | Written as if the first output will be final; no thought given to follow-up |
| 2 | User plans to iterate but prompt doesn't make iteration easy |
| 3 | Prompt is structured so that the output can be cleanly evaluated and refined — either through follow-up prompts or built-in feedback instructions |

**Signs of iteration readiness:** the prompt asks for a draft (not "the final version"), or it includes an instruction like "after generating, ask me if I want to adjust tone or length."

---

## Scoring guide

| Total | What it means |
|-------|--------------|
| 13–15 | Production-ready. This prompt should perform well consistently. |
| 10–12 | Good foundation. One or two dimensions need strengthening before relying on it. |
| 7–9 | Functional but fragile. Will produce acceptable output sometimes; unreliable at scale. |
| Below 7 | Rewrite before using. Results will be inconsistent and hard to improve incrementally. |

---

## Using this in a coaching session

**For individual coaching:** Have the person bring three prompts they actually use. Score them together. Focus on the lowest-scoring dimension — that's where the fastest improvement is.

**For team workshops:** Collect prompts anonymously from the group before the session. Display them (without attribution) and score as a group. The discussion about *why* a dimension scored low is more valuable than the score itself.

**For workflow audits:** If a team is unhappy with AI output quality, run their existing prompts through this rubric before recommending tools or models. The problem is almost always the prompt, not the model.

---

## A note on what this rubric doesn't measure

This rubric measures *prompt quality*, not *output quality*. A well-scored prompt can still produce bad output if:
- The task requires knowledge the model doesn't have
- The model is being asked to do something it's not suited for
- The underlying task is poorly defined at a business level (no prompt fixes a bad brief)

The rubric is a floor, not a ceiling. It ensures you're not leaving obvious improvements on the table.
