from state import CustomerState


def human_approval(state: CustomerState):
    query = state["query"].lower()

    if any(x in query for x in ["refund", "cancel", "closure", "compensation"]):
        state["approval_required"] = True
        state["approval_status"] = "pending"
    else:
        state["approval_required"] = False
        state["approval_status"] = "auto-approved"

    return state