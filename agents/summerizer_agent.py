from tools.file_tool import read_file, write_file


def summarizer_node(state):
    article1 = read_file("article1.txt")

    summary = f"""
Combined Summary:

{article1}
"""

    write_file("summary.txt", summary)

    state["files"]["summary.txt"] = summary
    state["completed_tasks"].append("Summarization completed")

    return state