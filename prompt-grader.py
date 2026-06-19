import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are an expert AI coaching evaluator. Your job is to score prompts using a structured rubric.

Score the prompt across these five dimensions, each on a scale of 1-3:

1. ROLE (who the model is being)
   1 = No role mentioned
   2 = Role is vague or partial
   3 = Clear role with audience relationship specified

2. TASK (what output is requested)
   1 = Vague or undefined task
   2 = Task is named but ambiguous
   3 = Specific output type, purpose, and scope all named

3. CONTEXT (background information provided)
   1 = No context given
   2 = Some context but key details missing
   3 = Enough context that a smart person could act without asking clarifying questions

4. FORMAT (structure and length instructions)
   1 = No format guidance at all
   2 = Some guidance but incomplete
   3 = Structure, length, tone, and at least one exclusion specified

5. TONE (voice and register)
   1 = No tone guidance
   2 = Tone described vaguely (e.g. "professional")
   3 = Tone defined through relationship, example, or specific banned phrases

Respond in exactly this format:

ROLE: [score]/3 — [one sentence explanation]
TASK: [score]/3 — [one sentence explanation]
CONTEXT: [score]/3 — [one sentence explanation]
FORMAT: [score]/3 — [one sentence explanation]
TONE: [score]/3 — [one sentence explanation]

TOTAL: [sum]/15

VERDICT: [one of: "Production-ready (13-15)", "Nearly there (10-12)", "Needs work (7-9)", "Rewrite needed (below 7)"]

TOP SUGGESTION: [The single most impactful change this prompt needs, in 2 sentences max]"""


def grade_prompt(user_prompt):
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Please grade this prompt:\n\n{user_prompt}"}
        ]
    )
    return message.content[0].text


def main():
    print("\n" + "="*50)
    print("        AI PROMPT GRADER")
    print("  Based on the Five Levers Framework")
    print("="*50)

    while True:
        print("\nPaste your prompt below and press Enter twice when done:")
        print("(or type 'quit' to exit)\n")

        lines = []
        while True:
            line = input()
            if line.lower() == "quit":
                print("\nGoodbye!\n")
                return
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)

        user_prompt = "\n".join(lines).strip()

        if not user_prompt:
            print("No prompt entered. Please try again.")
            continue

        print("\nGrading your prompt...\n")

        result = grade_prompt(user_prompt)

        print("="*50)
        print("RESULTS")
        print("="*50)
        print(result)
        print("="*50)

        print("\nGrade another prompt? (press Enter to continue or type 'quit' to exit)")
        again = input()
        if again.lower() == "quit":
            print("\nGoodbye!\n")
            break


if __name__ == "__main__":
    main()
