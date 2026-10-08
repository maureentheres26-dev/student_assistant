# Agentic AI Student Assistant

A simple Agentic AI Student Assistant built using Python, LangChain, and Groq.

## Features

- 🧮 Calculator tool for basic mathematical calculations
- 🎓 Student information tool to find a student's department
- 📊 Attendance tool to find a student's attendance percentage
- 🤖 LLM-based answers for general questions
- ❌ Handles students who are not found
- 💬 Interactive conversation through the terminal

## How It Works

The user enters a question, and the AI agent decides which tool should be used.

```text
User
  ↓
LLM / Agent
  ↓
Decides which tool to use
  ↓
Calculator / Student Information / Attendance
  ↓
Tool Result
  ↓
LLM
  ↓
Final Answer
