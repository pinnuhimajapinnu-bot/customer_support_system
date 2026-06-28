import sqlite3

DB_PATH = "memory.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            issue TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_memory(customer, issue):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO memory (customer, issue) VALUES (?, ?)",
        (customer, issue)
    )

    conn.commit()
    conn.close()


def get_last_issue(customer):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT issue FROM memory
        WHERE customer = ?
        ORDER BY id DESC LIMIT 1
    """, (customer,))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None