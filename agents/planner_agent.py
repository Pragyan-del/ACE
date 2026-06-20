from tools.todo_tool import write_todos

def planner_node(state):
    user_task = state["user_input"]

    todos = write_todos(user_task)
    print("PLANNER TODOS =", todos)

    state["todos"] = todos
    return state