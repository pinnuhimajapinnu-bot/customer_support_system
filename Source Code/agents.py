from state import CustomerState
from memory import save_memory


def sales_agent(state: CustomerState):
    state["response"] = f"[SALES] Info for: {state['query']}"

    save_memory(state["customer_name"], state["query"])
    return state


def technical_agent(state: CustomerState):
    state["response"] = f"[TECHNICAL] Help for: {state['query']}"

    save_memory(state["customer_name"], state["query"])
    return state


def billing_agent(state: CustomerState):
    state["response"] = f"[BILLING] Help for: {state['query']}"

    save_memory(state["customer_name"], state["query"])
    return state


def account_agent(state: CustomerState):
    state["response"] = f"[ACCOUNT] Help for: {state['query']}"

    save_memory(state["customer_name"], state["query"])
    return state