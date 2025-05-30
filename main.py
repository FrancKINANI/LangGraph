from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph import StateGraph, START, END
from langgraph.graph.message import add_message
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypeDict

load_dotenv()

llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")

class State(TypeDict):
    """
    Define the state of the graph.
    """
    messages: Annotated[list, add_message]

graph_builder = StateGraph(State)

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

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
    state = graph.invoke({"messages": state["messages"] + [{"role": "user", "content": user_input}]})
    if user_input.lower() in ["exit", "quit"]:
        break