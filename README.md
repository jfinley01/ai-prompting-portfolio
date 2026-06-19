# AI Prompting Portfolio

A practical reference for writing effective prompts across common professional and creative use cases.
This repo is designed as a coaching resource — each example shows not just *what* to write, but *why* it works.

---

## What's in here

| File | What it covers |
|------|----------------|
| [`examples/prompt-library.md`](examples/prompt-library.md) | Annotated prompt examples across 6 categories |
| [`frameworks/prompt-evaluation.md`](frameworks/prompt-evaluation.md) | A repeatable rubric for judging prompt quality |
| [`frameworks/the-five-levers.md`](frameworks/the-five-levers.md) | The five dimensions you can tune in any prompt |
| [`prompt_grader.py`](prompt_grader.py) | Python tool that scores any prompt using the rubric |

---

## Core philosophy

Most people treat prompting like a Google search — a few keywords and hope for the best.
Effective prompting is closer to briefing a smart colleague: the more context, role clarity, and output specification you provide, the better the result.

Three principles run through everything in this repo:

**1. Role before task.**
Tell the model who it's being before you tell it what to do. A model asked to "write a summary" and a model asked to "act as a senior analyst writing a summary for a board audience" produce very different outputs.

**2. Format is part of the instruction.**
If you don't specify format, the model guesses. Specify length, structure, tone, and what to exclude — not just what to include.

**3. Show, don't just tell.**
One example in a prompt is worth ten lines of description. Whenever you want a specific style or structure, include a short sample.

---

## How to use this as a coaching resource

- Use the **prompt library** as a starting deck for workshops — each example has a "why this works" annotation you can walk through with a group
- Use the **evaluation rubric** to review prompts your team is already using — it surfaces gaps fast
- Use the **five levers** framework as a diagnostic when a prompt isn't performing — it helps people identify *which* dimension to adjust rather than just rewriting from scratch

---

## Prompt Grader — try it yourself

`prompt_grader.py` is a command-line tool that scores any prompt using the Five Levers framework. Paste in a prompt, and it returns a score out of 15 with a one-line explanation for each dimension and a top suggestion for improvement.

**Example output:**

ROLE: 1/3 — No role is defined for the model to adopt.

TASK: 2/3 — Summarization is named but purpose, length, and scope are undefined.

CONTEXT: 1/3 — No background information is given.

FORMAT: 1/3 — No guidance on structure, length, tone, or exclusions.

TONE: 1/3 — No tone guidance whatsoever is provided.
TOTAL: 6/15

VERDICT: Rewrite needed (below 7)

TOP SUGGESTION: Specify the article, desired format, and audience — without these,

the prompt cannot be acted on at all.

The same task written as a strong prompt scores 14/15. That gap is what this tool is designed to make visible.

### Setup

You'll need Python 3 and an Anthropic API key.

```bash
# Create and activate a virtual environment
python3 -m venv prompt-grader-env
source prompt-grader-env/bin/activate

# Install the Anthropic library
pip install anthropic

# Add your API key (replace with your actual key)
echo 'export ANTHROPIC_API_KEY="sk-ant-your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### Running it

```bash
python3 prompt_grader.py
```

Paste any prompt at the input, press Enter twice, and get your score.

---

## Background

Built as a working reference for AI coaching engagements. Prompting is a skill, not a knack —
it can be taught, practiced, and measured. This repo is a starting point for that work.

