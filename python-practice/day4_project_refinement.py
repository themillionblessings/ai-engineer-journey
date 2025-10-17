import sqlite3
import csv
from datetime import datetime
import sys
import os

# --- Configuration ---
DB_NAME = "expenses.db"
EXPORT_FILE = "expenses_export.csv"

def get_db_connection():
    """Connects to the SQLite database and returns the connection."""
    try:
        conn = sqlite3.connect(DB_NAME)
        # Set row factory to sqlite3.Row to access columns by name (like a dictionary)
        conn.row_factory = sqlite3.Row 
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        # Use sys.exit(1) for a graceful exit on critical failure
        sys.exit(1) 

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

# --- CRUD Functions (Inherited from Phase 2) ---

def add_expense(amount: float, category: str, description: str):
    """Inserts a new expense record into the database."""
    conn = get_db_connection()
    if conn:
        try:
            current_time = datetime.now().isoformat()
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
                date_part = exp['timestamp'].split('T')[0]
                print(f"{exp['id']:<4} | ${exp['amount']:<7.2f} | {exp['category']:<15} | {exp['description']:<30} | {date_part:<15}")

        except sqlite3.Error as e:
            print(f"Error viewing expenses: {e}")
        finally:
            conn.close()

def view_summary():
    """Calculates and prints total expenses grouped by category using SQL aggregation."""
    conn = get_db_connection()
    if conn:
        try:
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

            print("\n--- Summary by Category (SQL Aggregation) ---")
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

# --- New Refinement Functions (Phase 3) ---

def export_to_csv():
    """Exports all expenses from the database to a CSV file."""
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.execute("SELECT id, amount, category, description, timestamp FROM expenses ORDER BY timestamp ASC;")
            expenses = cursor.fetchall()

            if not expenses:
                print("No expenses to export.")
                return

            # Get the column names (headers)
            header = [description[0] for description in cursor.description]
            
            with open(EXPORT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write header row
                writer.writerow(header)
                
                # Write data rows
                for row in expenses:
                    # 'row' is a sqlite3.Row object, treat it like a dictionary
                    writer.writerow(list(row)) 
            
            print(f"✅ Successfully exported {len(expenses)} records to '{EXPORT_FILE}'.")

        except sqlite3.Error as e:
            print(f"Error exporting to CSV: {e}")
        except IOError as e:
            print(f"Error writing to file {EXPORT_FILE}: {e}")
        finally:
            conn.close()


def summarize_from_csv():
    """Loads expenses from the CSV file and summarizes them using Python logic."""
    if not os.path.exists(EXPORT_FILE):
        print(f"❌ Error: CSV file '{EXPORT_FILE}' not found. Please run option 5 (Export to CSV) first.")
        return

    summary = {}
    total_all = 0.0
    
    try:
        with open(EXPORT_FILE, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # Use DictReader to access columns by header name
            
            for row in reader:
                try:
                    category = row['category']
                    # Convert amount from string (in CSV) back to float
                    amount = float(row['amount']) 
                    
                    # Python Aggregation: Use a dictionary to sum totals by category
                    summary[category] = summary.get(category, 0.0) + amount
                    total_all += amount
                except ValueError:
                    print(f"⚠️ Skipping row due to invalid amount: {row['amount']}")
                except KeyError as e:
                    print(f"⚠️ Skipping row: Missing column {e}")

        if not summary:
            print("No valid data found in CSV to summarize.")
            return

        print("\n--- Summary by Category (Python Aggregation from CSV) ---")
        print(f"{'Category':<15} | {'Total Spent':<12}")
        print("-" * 28)

        # Sort the summary by total spent (highest first)
        sorted_summary = sorted(summary.items(), key=lambda item: item[1], reverse=True)
        
        for category, total in sorted_summary:
            print(f"{category:<15} | ${total:<11.2f}")
            
        print("-" * 28)
        print(f"{'TOTAL':<15} | ${total_all:<11.2f}")

    except IOError as e:
        print(f"Error reading file {EXPORT_FILE}: {e}")

def db_health_check():
    """Runs database maintenance (VACUUM) and verifies primary key integrity."""
    conn = get_db_connection()
    if conn:
        try:
            print("\n--- Running Database Health Check ---")
            
            # 1. VACUUM: Reclaims space from deleted rows and rebuilds the database file.
            print("Running VACUUM to reclaim space and optimize file structure...")
            conn.execute("VACUUM;")
            print("✅ VACUUM complete.")

            # 2. Integrity Check: Check for proper sequence of the ID column
            # Note: After VACUUM, the physical ROWID might reset, but the key integrity should be fine.
            # We check the max ID vs count to ensure no obvious gaps.
            cursor_max = conn.execute("SELECT MAX(id) FROM expenses;").fetchone()[0]
            cursor_count = conn.execute("SELECT COUNT(id) FROM expenses;").fetchone()[0]
            
            if cursor_max is None or cursor_max == cursor_count:
                 print("✅ ID Integrity Check: All sequential IDs seem present (or DB is empty/freshly compacted).")
            else:
                 print(f"⚠️ ID Integrity Warning: Max ID is {cursor_max}, but total count is {cursor_count}. This is expected after deletions and prior to VACUUM.")

            conn.commit()
            print("--- Health Check Complete ---")

        except sqlite3.Error as e:
            print(f"Error during health check: {e}")
        finally:
            conn.close()


def main():
    """The main command-line interface loop for the expense tracker."""
    initialize_db()

    while True:
        print("\n--- Expense Tracker Menu (Refined) ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Summary (SQL Aggregation)")
        print("4. Delete Expense by ID")
        print("-----------------------------------")
        print("5. **Export All Data to CSV** (New Feature 1)")
        print("6. **View Summary (Python/CSV)** (New Feature 2)")
        print("7. **Run DB Health Check** (New Feature 3)")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ").strip()

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
            export_to_csv()
            
        elif choice == '6':
            summarize_from_csv()

        elif choice == '7':
            db_health_check()
            
        elif choice == '8':
            print("Exiting Expense Tracker. Data is saved to 'expenses.db'.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
