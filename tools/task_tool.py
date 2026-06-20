def delegate_task(agent_name):
    available_agents = {
        "research": "research",
        "summarizer": "summarizer"
    }

    return available_agents.get(agent_name, None)
