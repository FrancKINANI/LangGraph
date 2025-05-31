import os
from dotenv import load_dotenv
from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph
from langgraph.constants import END, START
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-3-sonnet-20240229", anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"))

class State(TypedDict):
    """
    Define the state of the graph.
    """
    messages: list

graph_builder = StateGraph(State)

def chatbot(state: State):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": messages + [{"role": "assistant", "content": response.content}]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

user_input = input("You: ")
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
while True:
    if state["messages"][-1]["role"] == "assistant":
        print(f"Assistant: {state['messages'][-1]['content']}")
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    state = graph.invoke({"messages": state["messages"] + [{"role": "user", "content": user_input}]})
    continue_chat = input("Continue to iterate? (y/n): ").lower()
    if continue_chat != 'y':
        break