# DAY 3, PART B: Hands-On Data Structures Practice
# Focus: Nested Data (Lists of Dictionaries) & Advanced Manipulation

# ═══════════════════════════════════════════════════
# EXERCISE 1: AI Engineer Project Tracker
# Goal: Model complex, nested data and calculate simple metrics.
# ═══════════════════════════════════════════════════

def track_ai_projects():
    """Uses a list of dictionaries to track the portfolio of AI projects."""

    # This is a LIST (main structure) where each element is a DICTIONARY (the project record)
    project_portfolio = [
        {
            "id": 1,
            "name": "Daily Motivation System (n8n)",
            "status": "Completed",
            "day_finished": 1,
            "tech_stack": ["n8n", "Gemini API", "Gmail"],
            "complexity": "Beginner",
            "priority": "High"
        },
        {
            "id": 2,
            "name": "Abu Dhabi Morning Brief (n8n)",
            "status": "Completed",
            "day_finished": 2,
            "tech_stack": ["n8n", "News API", "Gold API", "Gemini API"],
            "complexity": "Intermediate",
            "priority": "High"
        },
        {
            "id": 3,
            "name": "Personal Finance Tracker (Python CLI)",
            "status": "In Progress",
            "day_finished": None,
            "tech_stack": ["Python", "CSV I/O", "JSON"],
            "complexity": "Intermediate",
            "priority": "Medium"
        },
        {
            "id": 4,
            "name": "RAG System Prototype",
            "status": "Planned",
            "day_finished": None,
            "tech_stack": ["Python", "LangChain", "VectorDB", "Gemini API"],
            "complexity": "Advanced",
            "priority": "Critical"
        }
    ]

    print("\n" + "="*70)
    print("EXERCISE 1: AI PROJECT PORTFOLIO STATUS")
    print("="*70)

    # 1. Basic Looping and Nested Access
    print("Current Project List:")
    for project in project_portfolio:
        # Accessing nested list inside dictionary
        tech_str = ", ".join(project["tech_stack"])
        print(f"  • {project['name']} | Status: {project['status']} | Tech: {tech_str}")

    # 2. Calculating Metrics
    completed_count = 0
    in_progress_count = 0

    for project in project_portfolio:
        if project["status"] == "Completed":
            completed_count += 1
        elif project["status"] == "In Progress":
            in_progress_count += 1

    print("\n--- Metrics ---")
    print(f"Total Projects: {len(project_portfolio)}")
    print(f"Completed: {completed_count}")
    print(f"In Progress: {in_progress_count}")

    # 3. Simple Modification (Updating Status)
    # The Finance Tracker is being built today, let's update its complexity based on the work required.
    for project in project_portfolio:
        if project["id"] == 3:
            project["complexity"] = "Intermediate/Advanced"
            print(f"\nUpdate: Complexity for '{project['name']}' updated to: {project['complexity']}")
            break # Exit loop once found

    print("="*70 + "\n")

    return project_portfolio

# Store the result for use in the next exercise
current_portfolio = track_ai_projects()

# ═══════════════════════════════════════════════════
# EXERCISE 2: Financial Transaction Aggregator & Analysis
# Goal: Introduce List Comprehensions and lambda for filtering/summarization.
# ═══════════════════════════════════════════════════

def analyze_transactions():
    """Simulates financial data and analyzes it using advanced Python techniques."""

    # Simulating API data (list of expense dictionaries)
    transactions = [
        {"id": "t1", "vendor": "G42 Office Cafe", "amount": 15.50, "category": "Food", "date": "2025-10-14"},
        {"id": "t2", "vendor": "Python Academy", "amount": 99.00, "category": "Learning", "date": "2025-10-14"},
        {"id": "t3", "vendor": "ADNOC Petrol", "amount": 80.00, "category": "Transport", "date": "2025-10-15"},
        {"id": "t4", "vendor": "Amazon AWS", "amount": 5.25, "category": "Learning", "date": "2025-10-15"},
        {"id": "t5", "vendor": "Talabat", "amount": 42.00, "category": "Food", "date": "2025-10-16"},
        {"id": "t6", "vendor": "Bus Pass", "amount": 120.00, "category": "Transport", "date": "2025-10-16"},
        {"id": "t7", "vendor": "Presight Conference", "amount": 350.00, "category": "Networking", "date": "2025-10-16"}
    ]

    print("\n" + "="*70)
    print("EXERCISE 2: TRANSACTION ANALYSIS (LIST COMPREHENSIONS)")
    print("="*70)

    # --- 1. List Comprehension: Extracting Data ---
    # Create a new list containing only the amounts. (Faster and cleaner than a for loop)
    all_amounts = [t["amount"] for t in transactions]
    print(f"Total Transactions: {len(all_amounts)}")
    print(f"All Amounts Extracted: {all_amounts}")
    print(f"Overall Total Spent: AED {sum(all_amounts):.2f}")


    # --- 2. List Comprehension: Filtering Data ---
    # Create a new list containing only transactions where category is "Learning".
    learning_expenses = [t for t in transactions if t["category"] == "Learning"]
    learning_total = sum([t["amount"] for t in learning_expenses]) # Sum the filtered amounts

    print("\n--- Learning Expenses ---")
    for expense in learning_expenses:
        print(f"  • {expense['vendor']}: AED {expense['amount']:.2f}")
    print(f"Total Learning Spend: AED {learning_total:.2f}")


    # --- 3. Filtering using a lambda function (Advanced Filtering/Sorting) ---
    # Find the single most expensive transaction, useful for anomaly detection.
    # The max() function uses a 'key' argument which takes a lambda function.
    # A lambda function is a small, anonymous function: lambda x: expression
    
    # max() iterates through 'transactions' and uses the lambda to compare the 'amount'
    most_expensive = max(transactions, key=lambda t: t["amount"])

    print("\n--- Most Expensive Transaction ---")
    print(f"Vendor: {most_expensive['vendor']}")
    print(f"Amount: AED {most_expensive['amount']:.2f} (Category: {most_expensive['category']})")

    # --- 4. Modifying Data (Applying a Tax or Fee) ---
    # Use a list comprehension to create a NEW list with a 5% "Admin Fee" applied to all amounts.
    transactions_with_fee = [
        {**t, "amount": t["amount"] * 1.05}
        for t in transactions
    ]

    print("\n--- Total Spent with 5% Admin Fee ---")
    # Sum the new amounts from the modified list
    new_total = sum([t["amount"] for t in transactions_with_fee])
    print(f"New Total (with fee): AED {new_total:.2f}")

    print("="*70 + "\n")

# Run the analysis
analyze_transactions()
