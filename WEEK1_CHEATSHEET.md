# **Week 1 Quick Reference \- My Python & API Cheat Sheet**

Personal reference for concepts I use most often.

## **🐍 Python Essentials**

### **Variables & Types**

\# Basic types  
name \= "Mahdi"            \# String  
age \= 25                  \# Integer  
salary \= 300000.50        \# Float  
is\_learning \= True        \# Boolean

\# Type conversion  
age\_str \= str(age)        \# Convert to string  
price\_float \= float("2640") \# Convert to float  
count\_int \= int("10")     \# Convert to integer

### **String Formatting**

\# f-strings (my favorite\!)  
print(f"Hello {name}, you're {age} years old")  
print(f"Price: ${salary:.2f}")  \# 2 decimal places

### **Lists (Ordered Collections)**

skills \= \["Python", "SQL", "APIs"\]

\# Access  
first \= skills\[0\]           \# "Python"  
last \= skills\[-1\]           \# "APIs"

\# Add/Remove  
skills.append("FastAPI")    \# Add to end  
skills.insert(1, "Git")     \# Insert at position  
skills.remove("SQL")        \# Remove by value  
popped \= skills.pop()       \# Remove and return last

\# Loop  
for skill in skills:  
    print(skill)

\# List comprehension  
doubled \= \[x \* 2 for x in \[1, 2, 3\]\]  \# \[2, 4, 6\]

### **Dictionaries (Key-Value Pairs)**

person \= {  
    "name": "Mahdi",  
    "age": 25,  
    "city": "Abu Dhabi"  
}

\# Access  
name \= person\["name"\]  
age \= person.get("age")     \# Safer (returns None if missing)

\# Add/Update  
person\["email"\] \= "mahdi@example.com"

\# Loop  
for key, value in person.items():  
    print(f"{key}: {value}")

### **Conditionals**

score \= 85 \# Example value  
if score \>= 90:  
    grade \= "A"  
elif score \>= 80:  
    grade \= "B"  
else:  
    grade \= "C"

\# Boolean logic  
age \= 25 \# Example value  
has\_license \= True \# Example value  
if age \>= 18 and has\_license:  
    print("Can drive")

category \= "Food" \# Example value  
if category \== "Food" or category \== "Dining":  
    print("Eating expense")

### **Loops**

items \= \["a", "b", "c"\] \# Example list

\# For loop with range  
for i in range(5):          \# 0, 1, 2, 3, 4  
    print(i)

\# While loop  
count \= 0  
while count \< 5:  
    print(count)  
    count \+= 1

\# Loop with index  
for i, item in enumerate(items):  
    print(f"{i}: {item}")

### **Functions**

def greet(name, greeting="Hello"):  
    """Function with default parameter"""  
    return f"{greeting}, {name}\!"

\# Call it  
message\_1 \= greet("Mahdi")            \# "Hello, Mahdi\!"  
message\_2 \= greet("Mahdi", "Hi")        \# "Hi, Mahdi\!"

## **🗄️ Database (SQLite)**

### **Connect to Database**

import sqlite3

\# Better way (auto-closes)  
with sqlite3.connect("database.db") as conn:  
    cursor \= conn.cursor()  
    \# Do work here  
\# conn.close() is called automatically outside the block

### **Common SQL Queries**

\-- Create table  
CREATE TABLE expenses (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    date TEXT NOT NULL,  
    category TEXT NOT NULL,  
    amount REAL NOT NULL  
);

\-- Insert data  
INSERT INTO expenses (date, category, amount)  
VALUES ('2025-10-18', 'Food', 45.50);

\-- Select all  
SELECT \* FROM expenses;

\-- Select with filter  
SELECT \* FROM expenses WHERE category \= 'Food';

\-- Select with aggregation  
SELECT category, SUM(amount) as total  
FROM expenses  
GROUP BY category  
ORDER BY total DESC;

\-- Update  
UPDATE expenses SET amount \= 50.00 WHERE id \= 1;

\-- Delete  
DELETE FROM expenses WHERE id \= 5;

### **Python \+ SQL**

\# Assuming 'conn' and 'cursor' are active  
\# Execute query  
cursor.execute("SELECT \* FROM expenses")  
rows \= cursor.fetchall()

\# Insert with parameters (SAFE from SQL injection)  
date \= "2025-10-18" \# Example  
category \= "Travel" \# Example  
amount \= 120.00 \# Example  
cursor.execute(  
    "INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)",  
    (date, category, amount)  
)  
conn.commit()  \# Don't forget\!

## **🌐 FastAPI Essentials**

### **Basic API Setup**

from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel

app \= FastAPI()

\# Root endpoint  
@app.get("/")  
def read\_root():  
    return {"message": "Hello World"}

\# GET with path parameter  
@app.get("/items/{item\_id}")  
def get\_item(item\_id: int):  
    return {"item\_id": item\_id}

\# POST with body  
class Item(BaseModel):  
    name: str  
    price: float

@app.post("/items")  
def create\_item(item: Item):  
    return {"created": item.name}

### **Run API**

uvicorn filename:app \--reload

### **Access Documentation**

http://localhost:8000/docs        \# Swagger UI  
http://localhost:8000/redoc       \# ReDoc

## **📁 File Handling**

### **Read File**

\# Read entire file  
with open("file.txt", "r") as file:  
    content \= file.read()

\# Read lines  
with open("file.txt", "r") as file:  
    lines \= file.readlines()

\# Read line by line  
with open("file.txt", "r") as file:  
    for line in file:  
        print(line.strip())

### **Write File**

\# Write (overwrites)  
with open("file.txt", "w") as file:  
    file.write("Hello\\n")  
    file.write("World\\n")

\# Append  
with open("file.txt", "a") as file:  
    file.write("New line\\n")

### **JSON**

import json

\# Load JSON  
with open("data.json", "r") as file:  
    data \= json.load(file)

\# Save JSON  
data\_to\_save \= {"name": "Mahdi", "age": 25}  
with open("data.json", "w") as file:  
    json.dump(data\_to\_save, file, indent=2)

\# String to dict  
data \= json.loads('{"key": "value"}')

\# Dict to string  
json\_str \= json.dumps({"key": "value"})

### **CSV**

import csv

\# Read CSV  
with open("data.csv", "r") as file:  
    reader \= csv.DictReader(file)  
    for row in reader:  
        print(row\["column\_name"\])

\# Write CSV  
with open("data.csv", "w", newline='') as file:  
    writer \= csv.DictWriter(file, fieldnames=\["name", "age"\])  
    writer.writeheader()  
    writer.writerow({"name": "Mahdi", "age": 25})

## **🔧 Git Commands I Use**

\# Daily workflow  
git status                      \# Check what changed  
git add .                       \# Stage all changes  
git commit \-m "Message"         \# Commit with message  
git push origin main            \# Push to GitHub

\# Branch management  
git branch \-M main              \# Rename branch to main  
git branch                      \# List branches

\# First time setup  
git init                        \# Initialize repo  
git remote add origin URL       \# Link to GitHub  
git push \-u origin main         \# First push

\# Useful commands  
git log                         \# See commit history  
git diff                        \# See changes

## **🐛 Common Errors & Fixes**

### **Python**

\# NameError: name 'x' is not defined  
\# → You forgot to define variable x

\# IndentationError  
\# → Check your spaces/tabs are consistent

\# TypeError: unsupported operand type(s)  
\# → Trying to add string \+ number  
\#   Fix: convert types first

\# KeyError: 'key'  
\# → Dictionary key doesn't exist  
\#   Fix: use .get() method instead

### **SQL**

\-- Syntax error near 'X'  
\-- → Check your SQL syntax carefully

\-- No such table: table\_name  
\-- → Table doesn't exist, create it first

\-- UNIQUE constraint failed  
\-- → Trying to insert duplicate in UNIQUE field

### **FastAPI**

\# 404 Not Found  
\# → Check your endpoint URL matches exactly

\# 422 Unprocessable Entity  
\# → Request body doesn't match Pydantic model

\# Module not found  
\# → pip install \<module-name\>

## **💡 Pro Tips I Learned**

1. **Always use with for files** \- Auto-closes them.  
2. **Use f-strings** \- Cleaner than .format() or %.  
3. **.get() for dictionaries** \- Safer than \[\].  
4. **enumerate() when you need index** \- Better than range(len()).  
5. **SQL parameters ?** \- Prevents SQL injection.  
6. **Git commit often** \- Small commits easier to track.  
7. **Test in small pieces** \- Don't write 100 lines then test.  
8. **Read error messages carefully** \- They usually tell you exactly what's wrong.

## **🎯 My Go-To Debugging Process**

1. **Read the error message** (seriously, read it\!)  
2. **Check the line number** it mentions.  
3. **Print variables** to see their values.  
4. **Google the exact error** (someone else hit it\!).  
5. **Comment out code** to isolate the problem.  
6. **Ask AI** (Claude/ChatGPT) with full error message.

## **📚 Resources I Actually Use**

**Official Docs:**

* Python: https://docs.python.org/3/  
* FastAPI: https://fastapi.tiangolo.com/  
* SQLite: https://www.sqlite.org/docs.html

**Learning:**

* CS50P: https://cs50.harvard.edu/python/  
* Real Python: https://realpython.com/

**Quick Reference:**

* Python Cheat Sheet: https://www.pythoncheatsheet.org/  
* SQL Cheat Sheet: https://www.sqltutorial.org/sql-cheat-sheet/

Created: October 18, 2025  
Last Updated: October 18, 2025  
Status: Living document (I add to this as I learn\!)