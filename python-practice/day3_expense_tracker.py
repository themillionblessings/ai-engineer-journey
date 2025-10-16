import csv
import json
import os
import time

# --- File Paths ---
# We store the data in two different formats to practice both I/O methods.
CSV_FILE = 'transactions.csv'
JSON_FILE = 'transactions.json'

# Global variable to hold the transaction data (list of dictionaries)
transactions = []

# ====================================================================
# I/O Functions (Persistence)
# ====================================================================

def load_data():
    """Attempts to load transaction data from the JSON file first."""
    global transactions
    
    # os.path.exists checks if the file is there
    if os.path.exists(JSON_FILE):
        try:
            # 'r' mode means read
            with open(JSON_FILE, 'r') as f:
                # json.load converts the JSON text back into a Python list/dict
                transactions = json.load(f)
            print(f"💾 Data loaded successfully from {JSON_FILE} ({len(transactions)} records).")
            return

        except json.JSONDecodeError:
            print(f"⚠️ Error reading JSON file. Starting with empty data.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred while loading JSON: {e}")

    # Fallback/First Run: Initialize with empty list
    transactions = []
    print("✅ Initializing new transaction list.")


def save_data():
    """Saves the current transactions list to both JSON and CSV files."""
    try:
        # 1. Save to JSON (Best for complex data structures)
        # 'w' mode means write (or overwrite)
        with open(JSON_FILE, 'w') as f:
            # json.dump converts the Python list/dict into JSON text, indent=4 makes it readable
            json.dump(transactions, f, indent=4)

        # 2. Save to CSV (Best for simple, tabular data)
        if transactions:
            # We need the keys of the dictionary to be the column headers
            fieldnames = transactions[0].keys()
            with open(CSV_FILE, 'w', newline='') as f:
                # DictWriter knows how to map dictionary keys to CSV columns
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader() # Writes the column headers
                writer.writerows(transactions) # Writes all transaction rows
        
        print(f"\n💾 Data saved successfully to {JSON_FILE} and {CSV_FILE}.")

    except Exception as e:
        print(f"❌ Error during saving: {e}")

# ====================================================================
# Core Tracker Logic
# ====================================================================

def add_transaction():
    """Prompts user for transaction details and adds it to the list."""
    
    print("\n--- Add New Transaction ---")
    
    while True:
        try:
            vendor = input("Vendor Name (e.g., G42 Office Cafe): ").strip()
            amount = float(input("Amount (AED): "))
            category = input("Category (e.g., Food, Learning, Transport): ").strip()
            
            if not vendor or not category or amount <= 0:
                raise ValueError("All fields must be filled and amount must be positive.")

            # Create a unique ID based on timestamp
            new_id = int(time.time() * 1000)
            
            new_transaction = {
                "id": new_id,
                "vendor": vendor,
                "amount": amount,
                "category": category,
                "date": time.strftime("%Y-%m-%d")
            }
            
            transactions.append(new_transaction)
            print(f"✅ Added {vendor} for AED {amount:.2f}.")
            save_data() # Save immediately after adding
            break
            
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def show_summary():
    """Displays the total spending, number of transactions, and a category breakdown."""
    
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    total_spent = 0.0
    category_totals = {}
    
    # 1. Loop and Aggregate
    for t in transactions:
        try:
            amount = float(t['amount']) 
            category = t['category']
            
            total_spent += amount
            
            # Use .get() to aggregate category totals—a key dictionary skill
            category_totals[category] = category_totals.get(category, 0.0) + amount
        except ValueError:
            print(f"Skipping record with invalid amount: {t}")
        
    print("\n" + "="*50)
    print(f"PERSONAL FINANCE SUMMARY ({len(transactions)} Records)")
    print("="*50)
    print(f"TOTAL SPENT: AED {total_spent:.2f}")
    
    print("\n--- Breakdown by Category ---")
    # Sort categories by total spent (highest first)
    for category, total in sorted(category_totals.items(), key=lambda item: item[1], reverse=True):
        print(f"  • {category:<15}: AED {total:.2f}")
        
    print("="*50)


def main_menu():
    """Main application loop."""
    load_data() # Load data at startup

    while True:
        print("\n--- Finance Tracker Menu ---")
        print("1. Add New Transaction")
        print("2. View Summary")
        print("3. Exit and Save")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            save_data()
            print("\nExiting tracker. Happy learning!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# ====================================================================
# Application Entry Point
# ====================================================================

if __name__ == "__main__":
    main_menu()
