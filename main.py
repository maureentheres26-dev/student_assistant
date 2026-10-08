from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent


# Load API key
load_dotenv()


# -----------------------------
# Student Database
# -----------------------------

students = {
    "Arun": {
        "department": "CSE",
        "attendance": 82
    },
    "Priya": {
        "department": "AI",
        "attendance": 91
    }
}


# -----------------------------
# Calculator Tool
# -----------------------------

@tool
def calculator(a: float, b: float, operation: str) -> str:
    """Perform basic mathematical calculations."""

    if operation == "add":
        return str(a + b)

    elif operation == "subtract":
        return str(a - b)

    elif operation == "multiply":
        return str(a * b)

    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero."

        return str(a / b)

    elif operation == "percentage":
        return str((a * b) / 100)

    else:
        return "Invalid operation."


# -----------------------------
# Student Information Tool
# -----------------------------

@tool
def get_student_info(name: str) -> str:
    """Get the department of a student."""

    name = name.strip().title()

    if name in students:
        return f"{name} is from the {students[name]['department']} department."

    return f"Student {name} was not found."


# -----------------------------
# Attendance Tool
# -----------------------------

@tool
def get_attendance(name: str) -> str:
    """Get the attendance percentage of a student."""

    if name in students:
        return f"{name}'s attendance is {students[name]['attendance']}%."

    return f"Student {name} was not found."


# -----------------------------
# Create LLM
# -----------------------------

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


# -----------------------------
# Give tools to the Agent
# -----------------------------

tools = [
    calculator,
    get_student_info,
    get_attendance
]


# -----------------------------
# Create Agent
# -----------------------------

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a helpful Student Assistant.

Decide which tool to use based on the user's question.

Use:
- calculator for mathematical calculations
- get_student_info for student department questions
- get_attendance for student attendance questions

If the question does not require any of these tools,
answer normally using your knowledge.

Always give a clear and simple final answer.
"""
)


# -----------------------------
# Interactive Student Assistant
# -----------------------------

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })

    print("Assistant:", response["messages"][-1].content)





