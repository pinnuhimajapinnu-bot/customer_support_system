from state import CustomerState


def intent_classification(state: CustomerState):
    query = state["query"].lower()

    intent = "technical"

    if any(x in query for x in ["price", "plan", "cost", "buy"]):
        intent = "sales"

    elif any(x in query for x in ["error", "bug", "crash", "issue"]):
        intent = "technical"

    elif any(x in query for x in ["refund", "payment", "invoice"]):
        intent = "billing"

    elif any(x in query for x in ["login", "password", "account"]):
        intent = "account"

    state["intent"] = intent
    return state


# MUST return STRING ONLY (IMPORTANT)
def route_decision(state: CustomerState):
    intent = state.get("intent", "technical")

    if intent not in ["sales", "technical", "billing", "account"]:
        intent = "technical"

    return intent