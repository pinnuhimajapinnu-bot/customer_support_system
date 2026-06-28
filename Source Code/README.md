# AI-Powered Customer Support System using LangGraph

## 📌 Project Overview
This project is an AI-powered customer support automation system built using LangGraph.  
It automatically classifies customer queries, routes them to appropriate departments, retrieves knowledge base information, applies human approval for sensitive requests, and generates final responses.

---

## 🧠 Features
- Intent Classification (Sales, Technical, Billing, Account)
- Conditional Routing using LangGraph
- Department-specific AI Agents
- RAG-based Knowledge Retrieval (simulated using text files)
- SQLite Memory System (conversation tracking)
- Human-in-the-loop approval system
- Supervisor validation layer
- Fully state-driven workflow

---

## 🏗️ Workflow Architecture
START  
→ Memory Check  
→ Intent Classification  
→ Routing Node  
→ Department Agent  
→ RAG Retrieval  
→ Human Approval (if required)  
→ Supervisor Review  
→ Save Memory  
→ END  

---

## 📁 Project Structure
customer_support_system/
├── app.py
├── graph.py
├── state.py
├── router.py
├── agents.py
├── rag.py
├── memory.py
├── human_approval.py
├── supervisor.py
├── memory.db
└── documents/
    ├── CompanyPolicy.txt
    ├── PricingGuide.txt
    ├── TechnicalManual.txt
    └── FAQ.txt

---

## 📦 Installation

### 1. Create Virtual Environment
python -m venv venv

### 2. Activate Virtual Environment
venv\Scripts\activate

### 3. Install Dependencies
pip install langgraph

---

## 🚀 How to Run the Project
python app.py

---

## 💬 Example Queries
- What are the pricing plans available?
- I forgot my account password.
- My application crashes when uploading a file.
- I need a refund for my subscription.
- What was my previous support issue?

---

## 🧠 System Components

### 🔹 RAG System
Uses 4 knowledge base documents:
- Company Policy
- Pricing Guide
- Technical Manual
- FAQ

### 🔹 Memory System
- Stores customer queries using SQLite (memory.db)
- Retrieves previous issues when requested

### 🔹 Human-in-the-loop
Sensitive requests require approval:
- Refunds
- Subscription cancellation
- Account closure
- Compensation requests

---

## 🧪 Technologies Used
- Python
- LangGraph
- SQLite
- File-based RAG system

---

## 👨‍💻 Author
Student Project – AI-Powered Customer Support System using LangGraph