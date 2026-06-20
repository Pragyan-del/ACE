from models.llm import llm
from tools.task_tool import delegate_task


def supervisor_node(state):
    task = state["user_input"]

    prompt = f"""
    Choose the best agent for this task.

    Available agents:
    - research
    - summarizer

    Task: {task}

    Return only agent name.
    """

    response = llm.invoke(prompt)
    chosen_agent = response.content.strip().lower()

    routed_agent = delegate_task(chosen_agent)

    if routed_agent is None:
        routed_agent = "research"

    state["next_agent"] = routed_agent
    state["completed_tasks"].append("Supervisor routing completed")

    return state