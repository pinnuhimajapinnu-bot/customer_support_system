from langgraph.graph import StateGraph, END

from state import CustomerState

from router import intent_classification, route_decision
from agents import sales_agent, technical_agent, billing_agent, account_agent
from rag import rag_node
from memory import save_memory, get_last_issue
from human_approval import human_approval
from supervisor import supervisor


graph = StateGraph(CustomerState)

# --------------------
# MEMORY CHECK NODE
# --------------------
def memory_check(state):
    query = state["query"].lower()

    if "previous" in query or "earlier" in query:
        issue = get_last_issue(state["customer_name"])

        if issue:
            state["response"] = f"Your previous issue was: {issue}"
        else:
            state["response"] = "No previous issue found."

        state["finished"] = True

    return state
from memory import save_memory

def save_memory_node(state):
    save_memory(state["customer_name"], state["query"])
    return state

graph.add_node("memory_check", memory_check)
graph.add_node("intent_classification", intent_classification)

graph.add_node("routing_node", intent_classification)

graph.add_node("sales_agent", sales_agent)
graph.add_node("technical_agent", technical_agent)
graph.add_node("billing_agent", billing_agent)
graph.add_node("account_agent", account_agent)

graph.add_node("rag_node", rag_node)
graph.add_node("human_approval", human_approval)
graph.add_node("supervisor", supervisor)
graph.add_node("save_memory", save_memory_node)

# --------------------
# FLOW
# --------------------
graph.set_entry_point("memory_check")

def memory_router(state):
    if state.get("finished", False):
        return "end"
    return "intent_classification"

graph.add_conditional_edges(
    "memory_check",
    memory_router,
    {
        "end": END,
        "intent_classification": "intent_classification"
    }
)

graph.add_edge("intent_classification", "routing_node")

# --------------------
# ROUTING
# --------------------
graph.add_conditional_edges(
    "routing_node",
    route_decision,
    {
        "sales": "sales_agent",
        "technical": "technical_agent",
        "billing": "billing_agent",
        "account": "account_agent",
    },
)

# --------------------
# PIPELINE
# --------------------
graph.add_edge("sales_agent", "rag_node")
graph.add_edge("technical_agent", "rag_node")
graph.add_edge("billing_agent", "rag_node")
graph.add_edge("account_agent", "rag_node")

graph.add_edge("rag_node", "human_approval")
graph.add_edge("human_approval", "supervisor")
graph.add_edge("supervisor", "save_memory")
graph.add_edge("save_memory", END)

app = graph.compile()