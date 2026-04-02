# E&R Tool - AI Code Explainer CLI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-AI-orange?logo=groq)](https://groq.com/)

## Overview

E&R Tool (Explain & Review Tool) is a simple command-line interface (CLI) tool that uses the Groq API to provide **beginner-friendly explanations** of a code file. 

## Features

- **AI-Powered Explanations**: Uses Groq's `openai/gpt-oss-120b` model for accurate, concise breakdowns.
- **Easy CLI**: Single command to explain any file.
- **Local File Support**: Reads any Python file path you provide.

## Requirements

- Python 3.8+
- Groq API key (free tier available)
- Dependencies: See [requirement.txt](requirement.txt)

## Installation

1. Clone or download this project.

2. Install dependencies:
   ```
   pip install -r requirement.txt
   ```

3. Get a free Groq API key from [console.groq.com](https://console.groq.com/keys).

4. Create a `.env` file in the directory:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Navigate to the project directory in the terminal:
```
cd "/Users/E&R tool"
```

Explain a code file:
```
python E&R_tool.py explain example.py
```

### Commands
- `python E&R_tool.py explain <filename>`: Explain the code in the given file.

## Project Structure
```
├── E&R_tool.py      # Main CLI tool
├── example.py        # Sample file to explain
├── requirement.txt   # Dependencies
├── README.md
└── .env              # Your API key (create this)
```