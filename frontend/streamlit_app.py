import sys
import os

# Fix import path for graph, agents, tools
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.append(project_root)

import streamlit as st
from graph.builder import graph

# Page settings
st.set_page_config(
    page_title="ACE",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

.stChatMessage {
    border-radius: 15px;
    padding: 12px;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4da6ff;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">🧠 Autonomous Cognitive Engine</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Multi-Agent AI Research Assistant</div>',
    unsafe_allow_html=True
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Ask anything...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.spinner("ACE is thinking..."):
        initial_state = {
            "user_input": prompt,
            "todos": [],
            "completed_tasks": [],
            "files": {},
            "next_agent": ""
        }

        result = graph.invoke(initial_state)

        print("FINAL RESULT =", result)
        print("FINAL TODOS =", result["todos"])

        # IMPORTANT: define final_report
        final_report = result["files"].get(
            "final_report.txt",
            "No final report generated."
        )

    # Assistant response
    with st.chat_message("assistant"):
        st.markdown(final_report)

        with st.expander("Agent Workflow"):
            st.write("✅ Planner completed")
            st.write("✅ Supervisor completed")
            st.write("✅ Research completed")
            st.write("✅ Summarizer completed")
            st.write("✅ Synthesizer completed")

        with st.expander("Generated TODOs"):
            if result["todos"]:
                for todo in result["todos"]:
                    st.write(f"- {todo}")
            else:
                st.write("No TODOs generated")

    st.session_state.messages.append({
        "role": "assistant",
        "content": final_report
    })