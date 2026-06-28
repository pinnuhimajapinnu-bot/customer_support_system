# rag.py

def rag_node(state):
    query = state["query"].lower()

    context = ""

    # Load documents
    with open("documents/CompanyPolicy.txt", "r", encoding="utf-8") as f:
        policy = f.read()

    with open("documents/PricingGuide.txt", "r", encoding="utf-8") as f:
        pricing = f.read()

    with open("documents/TechnicalManual.txt", "r", encoding="utf-8") as f:
        technical = f.read()

    with open("documents/FAQ.txt", "r", encoding="utf-8") as f:
        faq = f.read()

    # ----------------------------
    # SIMPLE RAG LOGIC (KEYWORD-BASED)
    # ----------------------------

    if any(word in query for word in ["price", "pricing", "plan", "subscription", "cost"]):
        context = pricing

    elif any(word in query for word in ["crash", "error", "issue", "bug", "upload", "login"]):
        context = technical

    elif any(word in query for word in ["refund", "cancel", "policy", "compensation"]):
        context = policy

    elif "password" in query or "reset" in query:
        context = faq

    else:
        context = faq

    # ----------------------------
    # STORE IN STATE
    # ----------------------------
    state["retrieved_context"] = context[:500]  # limit for output

    # Add RAG info to response
    if "response" not in state or state["response"] is None:
        state["response"] = ""

    state["response"] += "\n[RAG Applied]\n" + context[:300]

    return state