from models.llm import llm

def write_todos(user_task):
    prompt = f"""
Break this task into TODO steps.

Task: {user_task}

Return one task per line only.
No explanation.
"""

    response = llm.invoke(prompt)

    raw = response.content
    print("RAW TODO RESPONSE:", raw)

    todos = [
        line.strip("-•1234567890. ").strip()
        for line in raw.split("\n")
        if line.strip()
    ]

    print("PARSED TODOS:", todos)

    return todos