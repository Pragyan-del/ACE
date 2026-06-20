from models.llm import llm


def synthesizer_node(state):
    summary = state["files"].get("summary.txt", "Summary missing")

    prompt = f"""
    Generate a professional final report from this summary.

    Summary:
    {summary}
    """

    response = llm.invoke(prompt)
    final_report = response.content

    state["files"]["final_report.txt"] = final_report
    state["completed_tasks"].append("Synthesis completed")

    return state