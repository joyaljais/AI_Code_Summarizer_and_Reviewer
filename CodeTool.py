import argparse
import os
from groq import Groq
from dotenv import load_dotenv
from rich.text import Text
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.spinner import Spinner

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
console = Console()


parser = argparse.ArgumentParser(description="Code explainer and reviewer CLI tool.")
subparsers = parser.add_subparsers(dest="command")

#explain cli command init
explain_parser = subparsers.add_parser("explain")
explain_parser.add_argument("filename", type=str)

#review command
review_parser = subparsers.add_parser("review")
review_parser.add_argument("filename", type=str)

args = parser.parse_args()
    
if args.command == "explain":
    system_prompt = ("""You are a helpful code explainer assistant. Understand and explain the provided code briefly. Make sure to explain the code to the user
    as like as they are biginner in programing. The output of this is shown in the cli so generate the output according to that.
    DO NOT use mark down output format.""")
    title, color = "Code Explanation", "cyan"

    

elif args.command == "review":
    system_prompt = ("""You are an expert code reviewer. Give concise feedback covering: bugs, security,
        style, performance, and best practices. Output is shown in CLI, no markdown.""")
    title, color = "Code Review", "magenta"
else:
    console.print("[red]Wrong Command!")
    exit()


try:
    with open(args.filename, 'r', encoding='utf-8') as file:
        content = file.read()
except(FileNotFoundError):
    console.print("[red]File not found!")


console.print(f"[dim] {args.filename}[/]")
console.print(Panel("", title=f"[bold {color}]{title}[/]", border_style=color, padding=0))
console.print()

# Loading effect

with Live(Spinner("dots", text=Text("Thinking...", style="dim")), console=console, transient=True):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": content
            }
        ],
        temperature=1,
        max_completion_tokens=6192,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )
    first = next(iter(completion))

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

    