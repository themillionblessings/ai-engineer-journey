import sqlite3
from datetime import datetime
import sys

# --- Configuration ---
DB_NAME = "expenses.db"

def get_db_connection():
    """Connects to the SQLite database and returns the connection."""
    try:
        conn = sqlite3.connect(DB_NAME)
        # Set row factory to sqlite3.Row to access columns by name (like a dictionary)
        conn.row_factory = sqlite3.Row 
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        sys.exit(1) # Exit if we can't connect to the DB

def initialize_db():
    """Initializes the database by creating the 'expenses' table if it doesn't exist."""
    conn = get_db_connection()
    if conn:
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    timestamp TEXT NOT NULL
                );
            """)
            conn.commit()
            print(f"✅ Database initialized: '{DB_NAME}' is ready.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

# --- CRUD Functions ---

def add_expense(amount: float, category: str, description: str):
    """Inserts a new expense record into the database."""
    conn = get_db_connection()
    if conn:
        try:
            # Get current timestamp for the record
            current_time = datetime.now().isoformat()
            
            # Use a parameterized query for safe insertion
            conn.execute("""
                INSERT INTO expenses (amount, category, description, timestamp)
                VALUES (?, ?, ?, ?);
            """, (amount, category, description, current_time))
            
            conn.commit()
            print(f"✅ Expense of ${amount:.2f} added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding expense: {e}")
        finally:
            conn.close()

def view_expenses():
    """Retrieves and prints all expenses from the database."""
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.execute("SELECT id, amount, category, description, timestamp FROM expenses ORDER BY timestamp DESC;")
            expenses = cursor.fetchall()

            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n--- All Expenses ---")
            print(f"{'ID':<4} | {'Amount':<8} | {'Category':<15} | {'Description':<30} | {'Date':<15}")
            print("-" * 75)
            
            for exp in expenses:
                # Format the date for cleaner display
                date_part = exp['timestamp'].split('T')[0]
                print(f"{exp['id']:<4} | ${exp['amount']:<7.2f} | {exp['category']:<15} | {exp['description']:<30} | {date_part:<15}")

        except sqlite3.Error as e:
            print(f"Error viewing expenses: {e}")
        finally:
            conn.close()

def view_summary():
    """Calculates and prints total expenses grouped by category."""
    conn = get_db_connection()
    if conn:
        try:
            # Aggregation Query: SUM the amounts and GROUP BY category.
            # This is significantly faster than doing the math in Python.
            cursor = conn.execute("""
                SELECT category, SUM(amount) AS total_spent 
                FROM expenses 
                GROUP BY category 
                ORDER BY total_spent DESC;
            """)
            summary = cursor.fetchall()

            if not summary:
                print("No expenses to summarize.")
                return

            print("\n--- Summary by Category ---")
            print(f"{'Category':<15} | {'Total Spent':<12}")
            print("-" * 28)
            
            total_all = 0.0
            for row in summary:
                total_all += row['total_spent']
                print(f"{row['category']:<15} | ${row['total_spent']:<11.2f}")
                
            print("-" * 28)
            print(f"{'TOTAL':<15} | ${total_all:<11.2f}")


        except sqlite3.Error as e:
            print(f"Error viewing summary: {e}")
        finally:
            conn.close()

def delete_expense(expense_id: int):
    """Deletes a specific expense record by ID."""
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            if cursor.rowcount > 0:
                conn.commit()
                print(f"✅ Expense ID {expense_id} deleted successfully.")
            else:
                print(f"❌ Error: Expense ID {expense_id} not found.")
        except sqlite3.Error as e:
            print(f"Error deleting expense: {e}")
        finally:
            conn.close()


def main():
    """The main command-line interface loop for the expense tracker."""
    initialize_db()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add New Expense (C)")
        print("2. View All Expenses (R)")
        print("3. View Summary by Category (R - Aggregation)")
        print("4. Delete Expense by ID (D)")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter amount spent (e.g., 25.50): "))
                category = input("Enter category (e.g., Groceries, Rent, Entertainment): ").strip()
                description = input("Enter description (optional): ").strip()
                if amount > 0 and category:
                    add_expense(amount, category, description)
                else:
                    print("❌ Amount must be positive and Category cannot be empty.")
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
                
        elif choice == '2':
            view_expenses()

        elif choice == '3':
            view_summary()

        elif choice == '4':
            try:
                exp_id = int(input("Enter the ID of the expense to delete: "))
                delete_expense(exp_id)
            except ValueError:
                print("❌ Invalid ID. Please enter an integer.")

        elif choice == '5':
            print("Exiting Expense Tracker. Data is saved to 'expenses.db'.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
