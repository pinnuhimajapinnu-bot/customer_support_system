from graph import app

if __name__ == "__main__":
    query = input("Enter your query: ")

    input_state = {
        "customer_name": "User",
        "query": query,
        "intent": "",
        "response": "",
    }
    from memory import init_db
    init_db()


    

    result = app.invoke(input_state)
    

    print("\nFINAL OUTPUT:\n")
    print(result["response"])