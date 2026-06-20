from graph.builder import graph


def main():
    user_task = input("Enter your task: ")

    initial_state = {
        "user_input": user_task,
        "todos": [],
        "completed_tasks": [],
        "files": {},
        "next_agent": ""
    }

    result = graph.invoke(initial_state)

    print("\n" + "=" * 50)
    print("FINAL REPORT")
    print("=" * 50)

    print(
        result["files"].get(
            "final_report.txt",
            "No final report generated."
        )
    )

    print("\nCOMPLETED TASKS:")
    for task in result["completed_tasks"]:
        print(f"- {task}")


if __name__ == "__main__":
    main()