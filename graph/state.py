from typing import TypedDict, List, Dict


class AgentState(TypedDict):
    user_input: str
    todos: List[str]
    completed_tasks: List[str]
    files: Dict[str, str]
    next_agent: str