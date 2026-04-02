# E&R Tool - AI Code Explainer CLI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-AI-orange?logo=groq)](https://groq.com/)

## Overview

E&R Tool (Explain & Review Tool) is a simple command-line interface (CLI) tool that uses the Groq API to provide **beginner-friendly explanations** of Python code files. 

Simply run the tool on any Python file, and it will analyze the code and explain it step-by-step in plain English, as if you're new to programming. Explanations are streamed directly to your terminal for an interactive feel.

**Example**: Explain what a todo app does without reading the entire code!

## Features

- **AI-Powered Explanations**: Uses Groq's `openai/gpt-oss-120b` model for accurate, concise breakdowns.
- **Beginner-Friendly**: System prompt ensures simple language, no jargon.
- **Streaming Output**: Real-time explanation as the AI generates it.
- **Easy CLI**: Single command to explain any file.
- **Local File Support**: Reads any Python file path you provide.

## Requirements

- Python 3.8+
- Groq API key (free tier available)
- Dependencies: See [E&R tool/requirement.txt](E&R tool/requirement.txt)

## Installation

1. Clone or download this project.

2. Install dependencies:
   ```
   cd "E&R tool"
   pip install -r requirement.txt
   ```

3. Get a free Groq API key from [console.groq.com](https://console.groq.com/keys).

4. Create a `.env` file in the `E&R tool/` directory:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Navigate to the project:
```
cd "/Users/benet/Program Files/CLI Project/E&R tool"
```

Explain a code file:
```
python E&R_tool.py explain example.py
```

### Example Demo
Run the above command (with your API key set). It will explain `example.py` (a simple Todo CLI app):

**Sample Output**:
```
This is a simple command-line todo list application written in Python. ...

(Add AI-like explanation here - run the tool to see live!)
```

### Commands
- `explain <filename>`: Explain the code in the given file.

## Project Structure
```
CLI Project/
├── README.md
├── TODO.md
└── E&R tool/
    ├── E&R_tool.py      # Main CLI tool
    ├── example.py        # Sample file to explain (Todo CLI demo)
    ├── requirement.txt   # Dependencies
    └── .env              # Your API key (create this)
```

## Demo Command
To test:
```
cd "/Users/benet/Program Files/CLI Project/E&R tool" && python E&R_tool.py explain example.py
```

## Limitations & TODO
- Currently only 'explain' command (parser ready for 'review').
- Basic error handling (e.g., file not found).
- No code review/refactor suggestions yet.

See [TODO.md](../TODO.md) for progress.

## License
MIT License - feel free to use and modify!

---

Built with ❤️ using Groq API for fast AI inference.

