from state import CustomerState


def supervisor(state: CustomerState):
    state["response"] += "\n[Supervisor Approved]"
    state["finished"] = True
    return state