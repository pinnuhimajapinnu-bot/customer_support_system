from typing import TypedDict


class CustomerState(TypedDict):
    customer_name: str
    query: str

    intent: str
    response: str

    retrieved_context: str

    approval_required: bool
    approval_status: str

    memory_result: str
    finished: bool