import sqlite3
from typing import List, Dict, Any

DATABASE_NAME = "expense_tracker.db"

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    # Set row_factory to sqlite3.Row so we can access columns by name
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    """Initializes the database by creating the 'expenses' table if it doesn't exist."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_expense(date: str, amount: float, category: str, description: str):
    """Inserts a new expense record into the database."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses (date, amount, category, description)
            VALUES (?, ?, ?, ?)
        """, (date, amount, category, description))
        conn.commit()
    except Exception as e:
        print(f"Error adding expense: {e}")
        raise
    finally:
        conn.close()

def get_all_expenses() -> List[Dict[str, Any]]:
    """Retrieves all expenses from the database, returned as a list of dictionaries."""
    conn = get_db_connection()
    expenses = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses ORDER BY date DESC, id DESC")
        # Convert sqlite3.Row objects to standard Python dictionaries
        expenses = [dict(row) for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error retrieving all expenses: {e}")
        raise
    finally:
        conn.close()
    return expenses

def get_summary_by_category() -> List[Dict[str, Any]]:
    """Calculates the total amount spent for each category."""
    conn = get_db_connection()
    summary = []
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                category, 
                SUM(amount) AS total_spent
            FROM expenses
            GROUP BY category
            ORDER BY total_spent DESC
        """)
        # Convert sqlite3.Row objects to standard Python dictionaries
        summary = [dict(row) for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error retrieving category summary: {e}")
        raise
    finally:
        conn.close()
    return summary
