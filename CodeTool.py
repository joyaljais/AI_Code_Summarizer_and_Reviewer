import argparse
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def explainer_tool(filename: str) -> str:
    """
    This tool explain what a set of code do.

    Args: 
        file name / file path: File containing code that needs to explain.

    Return: Summarized explaination of the file content(code).
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(type(content))
    except(FileNotFoundError):
        print("File not found!")

    system_prompt = """You are a helpful code explainer assistant. Understand and explain the provided code briefly. Make sure to explain the code to the user
    as like as they are biginner in programing. The output of this is shown in the cli so generate the output according to that.
    DO NOT use mark down output format."""

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
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")


def reviewer_tool(filename: str) -> str:
    """
    Reviews code for bugs, style issues and improvements
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(type(content))
    except(FileNotFoundError):
        print("File not found!")


    system_prompt = """You are an expert code reviewer. Carefully review the provided code and give constructive feedback. 
        Cover the following areas:
        1. Bugs or potential runtime errors
        2. Security concerns
        3. Code style and readability
        4. Performance improvements 
        5. Best-practice suggestions
        Be concise and specific. Reference line content where helpful.
        The output is shown in the CLI, so do NOT use markdown formatting."""
    
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
    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")



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
    explainer_tool(args.filename)
elif args.command == "review":
    reviewer_tool(args.filename)
