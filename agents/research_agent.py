from models.llm import llm
from tools.file_tool import write_file


def research_node(state):
    task = state["user_input"]

    prompt = f"""
Research this topic in detail:

Topic: {task}

Include:
1. Introduction
2. Key Concepts
3. Examples
4. Advantages
5. Challenges
"""

    response = llm.invoke(prompt)
    research_notes = response.content

    print("=== RESEARCH NOTES ===")
    print(research_notes)

    write_file("article1.txt", research_notes)

    state["files"]["article1.txt"] = research_notes
    state["completed_tasks"].append("Research completed")

    return state