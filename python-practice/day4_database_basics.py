import sqlite3
import os

# --- Configuration ---
# The database file name. SQLite will create this file if it doesn't exist.
DB_NAME = "university_records.db"

# --- Database Utility Functions ---

def get_db_connection():
    """Connects to the database and returns the connection object."""
    try:
        # Connect to the DB. If the file doesn't exist, it creates it.
        conn = sqlite3.connect(DB_NAME)
        
        # Set row_factory to sqlite3.Row. This is a best practice!
        # It allows us to access columns by name (like a dictionary) instead of by index.
        conn.row_factory = sqlite3.Row 
        print(f"Connected to database: {DB_NAME}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def main():
    """Executes the sequence of database operations."""
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    
    # -----------------------------------------------------------
    # 1. CREATE TABLE (Schema Definition)
    # -----------------------------------------------------------
    print("\n--- 1. CREATE TABLE (Defining the Schema) ---")
    try:
        # Drop the table if it exists so we start fresh every run
        cursor.execute("DROP TABLE IF EXISTS students")
        
        # Define the structure of the 'students' table
        cursor.execute("""
            CREATE TABLE students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                major TEXT NOT NULL,
                gpa REAL DEFAULT 0.0
            )
        """)
        conn.commit()
        print("Table 'students' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        conn.close()
        return

    # -----------------------------------------------------------
    # 2. INSERT (Adding Data - The 'C' in CRUD)
    # -----------------------------------------------------------
    print("\n--- 2. INSERT (Adding Data) ---")
    try:
        # Good practice: Use parameterized queries to insert data safely.
        students_data = [
            ("Alice Smith", "Computer Science", 3.9),
            ("Bob Johnson", "Mechanical Engineering", 3.2),
            ("Charlie Brown", "Business", 3.5),
        ]
        
        cursor.executemany("INSERT INTO students (name, major, gpa) VALUES (?, ?, ?)", students_data)
        conn.commit()
        print(f"Inserted {cursor.rowcount} students.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

    # -----------------------------------------------------------
    # 3. SELECT (Reading Data - The 'R' in CRUD)
    # -----------------------------------------------------------
    print("\n--- 3. SELECT (Reading all data) ---")
    cursor.execute("SELECT id, name, major, gpa FROM students")
    
    records = cursor.fetchall()
    print("Initial Records:")
    for row in records:
        # Accessing columns by name thanks to row_factory = sqlite3.Row
        print(f"ID: {row['id']} | Name: {row['name']:<15} | Major: {row['major']:<25} | GPA: {row['gpa']:.2f}")

    # -----------------------------------------------------------
    # 4. UPDATE (Modifying Data - The 'U' in CRUD)
    # -----------------------------------------------------------
    print("\n--- 4. UPDATE (Changing a record) ---")
    # Let's give Bob a higher GPA (assume his grades were updated)
    student_id_to_update = 2 # Assuming Bob is the second record
    new_gpa = 3.8
    
    cursor.execute("UPDATE students SET gpa = ? WHERE id = ?", (new_gpa, student_id_to_update))
    conn.commit()
    print(f"Updated student ID {student_id_to_update}'s GPA to {new_gpa}.")
    
    # Verify the update
    print("\nVerification after UPDATE:")
    cursor.execute("SELECT id, name, gpa FROM students WHERE id = ?", (student_id_to_update,))
    updated_row = cursor.fetchone()
    if updated_row:
        print(f"ID: {updated_row['id']} | Name: {updated_row['name']} | New GPA: {updated_row['gpa']:.2f}")

    # -----------------------------------------------------------
    # 5. DELETE (Removing Data - The 'D' in CRUD)
    # -----------------------------------------------------------
    print("\n--- 5. DELETE (Removing a record) ---")
    # Let's remove Charlie Brown (ID 3)
    student_id_to_delete = 3
    
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id_to_delete,))
    conn.commit()
    print(f"Deleted student ID {student_id_to_delete}.")

    # Final check
    print("\n--- 6. Final SELECT (Remaining Records) ---")
    cursor.execute("SELECT id, name FROM students")
    final_records = cursor.fetchall()
    
    for row in final_records:
        print(f"Remaining ID: {row['id']} | Name: {row['name']}")
    
    print(f"\nTotal records remaining: {len(final_records)}")

    # -----------------------------------------------------------
    # 7. CLOSE CONNECTION (Essential Cleanup)
    # -----------------------------------------------------------
    conn.close()
    print("\nDatabase connection closed. CRUD process complete.")


if __name__ == "__main__":
    main()
