# Prompt Library

Annotated examples across six common use cases. Each entry shows a weak version, a strong version, and explains the difference.

---

## 1. Summarization

### ❌ Weak prompt
```
Summarize this article.
```

### ✅ Strong prompt
```
You are a research assistant preparing briefings for a senior executive who has 5 minutes to read.

Summarize the article below using this format:
- **Bottom line** (1 sentence): the single most important takeaway
- **Key points** (3 bullets max): supporting facts worth knowing
- **What to watch** (1 sentence): what happens next that matters

Exclude background context the executive already knows. Avoid jargon.

[ARTICLE TEXT HERE]
```

**Why this works:**
The role ("research assistant") sets expectations for tone and depth. The named audience ("senior executive, 5 minutes") gives the model a target to calibrate against. The explicit format means the output is immediately usable — no reformatting needed. The "exclude" instruction is just as important as the "include" instructions.

---

## 2. Writing assistance

### ❌ Weak prompt
```
Make this email sound more professional.
```

### ✅ Strong prompt
```
Edit the email below for professional tone. Keep these constraints:
- Preserve the sender's core message exactly — do not add or remove information
- Keep it under 150 words
- The relationship is warm but not casual (long-term client, not a friend)
- Do not use the word "utilize" or corporate filler phrases like "moving forward" or "touch base"

Return only the revised email, no commentary.

[EMAIL TEXT HERE]
```

**Why this works:**
"More professional" is subjective. This prompt defines professional through constraints (length, relationship type, banned phrases) rather than adjectives. The "preserve core message" instruction prevents the model from hallucinating new content. "Return only the revised email" eliminates the preamble most models add by default.

---

## 3. Analysis and reasoning

### ❌ Weak prompt
```
What are the pros and cons of remote work?
```

### ✅ Strong prompt
```
You are an organizational psychologist advising a 200-person B2B software company that is deciding whether to move from hybrid to fully remote.

Analyze the tradeoffs of full remote for this specific context. Consider:
- Impact on collaboration for knowledge workers (not customer-facing roles)
- Retention implications in a competitive hiring market
- The research evidence for and against remote productivity (cite the strongest studies)

Structure your response as: Strengths / Risks / What the evidence actually says / My recommendation.

Be direct. If the evidence is mixed, say so rather than hedging.
```

**Why this works:**
The generic "pros and cons" prompt gets generic output. Anchoring to a specific company type, size, and decision context forces relevant analysis. The "cite studies" instruction prompts the model to ground claims in evidence. "Be direct / say so rather than hedging" counters the model's tendency toward false balance.

---

## 4. Ideation and brainstorming

### ❌ Weak prompt
```
Give me some ideas for team building activities.
```

### ✅ Strong prompt
```
Generate 10 team-building activity ideas for the following context:
- Team: 14 people, fully remote, spread across US and Europe time zones
- Budget: under $50 per person
- Constraint: must work async OR in a 60-minute sync window
- Goal: strengthen relationships between people who have never met in person
- What we've already tried: virtual trivia, coffee chats, Donut app pairings

For each idea, include: name, format (sync/async), estimated time, why it builds relationships (not just entertainment).

Push beyond obvious options. If you include something like "virtual happy hour," explain specifically how to make it less forgettable than the average one.
```

**Why this works:**
The constraints (budget, timezone, already-tried list) eliminate most generic suggestions immediately. Asking *why it builds relationships* forces the model to think about mechanism, not just activity. The last line explicitly pushes back against the model's default toward safe, obvious suggestions.

---

## 5. Data interpretation

### ❌ Weak prompt
```
What does this data tell me?
```

### ✅ Strong prompt
```
You are a data analyst helping a non-technical marketing manager understand survey results.

Below is a summary of responses from a customer satisfaction survey (N=312). Your job is to:
1. Identify the 2–3 most meaningful patterns — not just the highest or lowest scores
2. Flag any results that seem contradictory or surprising
3. Suggest one follow-up question we should have asked but didn't

Use plain language. Avoid statistical jargon. If a finding could have multiple explanations, name them.

[DATA HERE]
```

**Why this works:**
"What does this tell me?" produces a description. This prompt asks for patterns, contradictions, and gaps — three distinct analytical moves. The audience definition ("non-technical marketing manager") calibrates language. "Could have multiple explanations, name them" prevents false confidence in interpretation.

---

## 6. Role-play and simulation

### ❌ Weak prompt
```
Pretend you're a difficult customer and I'll practice handling you.
```

### ✅ Strong prompt
```
You are playing the role of a customer named Sandra who:
- Has been a loyal client for 4 years but is frustrated about a billing error she's reported twice
- Is professional but direct — she doesn't yell, but she's firm and expects resolution
- Loses patience quickly with scripted-sounding responses
- Her goal: get a clear answer on whether she'll be refunded, and by when

Start the conversation by saying what she'd realistically say when the rep picks up.
Stay in character throughout. If the rep gives a vague answer, push back the way Sandra would.

After I say "debrief," step out of character and give me honest feedback on where I could have handled it better.
```

**Why this works:**
"Difficult customer" is too vague to practice against usefully. A named character with specific history, communication style, and concrete goal creates a realistic simulation. The debrief instruction turns a role-play into a coaching session — the model becomes both the challenge and the coach.

---

## Quick reference: the most common prompt mistakes

| Mistake | Fix |
|---------|-----|
| Vague task ("help me with this") | Name the specific output you want |
| No audience defined | Say who will read or use the output |
| No format specified | Describe structure, length, and what to exclude |
| Asking for "pros and cons" generically | Anchor to a specific situation and decision |
| No example provided | Add one short example of the style you want |
| Accepting the first output | Treat the first response as a draft; iterate with specific edits |
