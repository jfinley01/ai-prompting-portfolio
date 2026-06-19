# Prompt Library

Annotated examples across twelve common use cases. Each entry shows a weak version, a strong version, and explains the difference.

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

## 7. Feedback and critique

### ❌ Weak prompt
```
Give me feedback on this presentation.
```

### ✅ Strong prompt
```
You are a communications coach reviewing a 10-minute executive presentation. The presenter is a first-time VP presenting to a board of directors for the first time.

Review the slide deck below and give feedback in three tiers:
- **Must fix before presenting** (2–3 items max): issues that would undermine credibility
- **Worth improving if time allows** (3–5 items): things that would lift the quality noticeably
- **Leave alone**: anything you'd be tempted to change but shouldn't — explain why

Be specific. Reference the actual slide content, not generic presentation advice.
Do not comment on visual design — that's handled separately.

[SLIDE CONTENT HERE]
```

**Why this works:**
Tiered feedback forces prioritization — the most common failure of AI feedback is treating everything as equally important. "Leave alone" is an underused instruction that prevents over-editing and builds the presenter's confidence. Excluding visual design keeps the feedback focused and avoids scope creep.

---

## 8. Decision support

### ❌ Weak prompt
```
Should I take this job offer?
```

### ✅ Strong prompt
```
I need help thinking through a job decision, not a recommendation. Help me structure my thinking.

Current role: Senior Marketing Manager at a 400-person SaaS company. Stable, good team, limited upward mobility.
New offer: Head of Marketing at a 30-person startup. 20% salary increase, equity, but pre-Series B with real risk.
Personal context: Two kids in middle school, mortgage, spouse works full-time. I can absorb some financial risk but not a lot.
What matters most to me: career growth, stability, and meaningful work — roughly in that order.

Do not tell me what to do. Instead:
1. Identify the 3 questions I should be able to answer before deciding
2. Point out any assumptions I seem to be making that I should pressure-test
3. Name what I'd be giving up in each direction that I might be underweighting
```

**Why this works:**
Asking an AI "should I do X?" produces a hedged non-answer. Asking it to structure your thinking produces something actually useful. The "do not tell me what to do" instruction is essential — it prevents the model from defaulting to false confidence. Naming personal context and priorities gives the model something real to work with.

---

## 9. Learning and explanation

### ❌ Weak prompt
```
Explain machine learning to me.
```

### ✅ Strong prompt
```
Explain how machine learning models are trained, for someone who understands spreadsheets and basic statistics but has no programming background.

Use one concrete analogy that isn't about teaching a child or training a dog — those are overused.
Cover: what "training data" means, what the model is actually optimizing for, and why more data isn't always better.

Keep it under 300 words. End with one question I should be able to answer if I understood this correctly.
```

**Why this works:**
"Explain X to me" without an audience produces textbook output. The analogy constraint ("not the child/dog one") forces creativity and avoids clichés. Specifying what to cover prevents the model from front-loading irrelevant background. The closing question is a smart trick — it lets the reader self-check comprehension without needing a quiz.

---

## 10. Content creation

### ❌ Weak prompt
```
Write a LinkedIn post about our product launch.
```

### ✅ Strong prompt
```
Write a LinkedIn post announcing the launch of a new AI-powered scheduling tool for healthcare clinics.

Audience: clinic administrators and practice managers (not clinicians or patients).
Tone: confident and direct, not hype-y. This audience is skeptical of vendor marketing.
Length: 150–200 words. No hashtag spam — two relevant hashtags maximum.

Structure:
- Open with the problem, not the product
- Introduce the product in one sentence in the middle
- Close with a specific call to action (book a demo, not "learn more")

Do not use the phrases "game-changer," "revolutionary," or "excited to announce."
```

**Why this works:**
LinkedIn posts written without audience context default to generic enthusiasm that performs poorly. Leading with the problem (not the product) is a copywriting principle the model won't apply unless instructed. The banned phrases list prevents the most common AI content clichés. A specific CTA ("book a demo") outperforms vague ones in every channel.

---

## 11. Meeting and workshop design

### ❌ Weak prompt
```
Help me plan a team meeting about our strategy.
```

### ✅ Strong prompt
```
Design a 90-minute working session for a leadership team of 8 people (VP level) to align on priorities for Q3.

Context:
- The team has not agreed on priorities in two previous meetings
- The disagreement is partly about resources (who gets budget) and partly about strategic direction
- One VP is known for dominating discussions; two others rarely speak up in groups

Design the session so that:
- All voices are heard, not just the loudest
- The output is a ranked list of 3–5 priorities with owners assigned
- We leave with a decision, not just more discussion

Include: agenda with timing, facilitation notes for the tricky moments, and one technique for handling the dominant participant without embarrassing them.
```

**Why this works:**
Meeting design prompts fail when they ignore the human dynamics in the room. Naming the specific dysfunction (one dominator, two quiet voices, two failed prior meetings) lets the model address the real problem. "A decision, not just more discussion" is an outcome instruction that changes the entire shape of the agenda.

---

## 12. Coaching and performance conversations

### ❌ Weak prompt
```
Help me give feedback to an underperforming employee.
```

### ✅ Strong prompt
```
Help me prepare for a performance conversation with a direct report.

Context:
- She is a 3-year employee who was strong in her first two years but has missed three consecutive deadlines in Q2
- I suspect the issue is personal (she mentioned family stress in passing) but I don't know for sure
- She tends to shut down when she feels criticized — previous feedback has not landed well
- My goal: understand what's going on, be honest about the impact, and agree on a path forward together

Do not write a script. Instead, give me:
1. The opening 2–3 sentences I should use to set the right tone
2. The one question I should ask early and genuinely listen to before saying anything evaluative
3. Two phrases to avoid and what to say instead
4. How to close the conversation so we both leave with clarity, not anxiety
```

**Why this works:**
"Help me give feedback" produces a generic feedback framework. This prompt names the specific person, history, and dynamic — so the output is actually usable in the room. Asking for phrases to avoid (and replacements) is more actionable than asking for "tips." The closing instruction addresses a gap most feedback advice ignores: how the conversation ends determines whether it sticks.

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
| Asking "should I do X?" | Ask it to structure your thinking instead |
| Treating all feedback as equal | Ask for tiered feedback (must fix / worth improving / leave alone) |
| Ignoring human dynamics | Name the specific people and patterns in the room |
