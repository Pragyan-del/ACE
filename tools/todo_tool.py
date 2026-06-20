from models.llm import llm

def write_todos(user_task):
    if llm is None:
        return ["ERROR: LLM not initialized"]

    prompt = f"""
    Break this task into 3-5 actionable TODO steps.
    Task: {user_task}
    Return only bullet points.
    """

    try:
        response = llm.invoke(prompt)
        todos = response.content.split("\n")
        return todos

    except Exception as e:
        return [f"Groq API Error: {str(e)}"]