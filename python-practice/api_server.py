from fastapi import FastAPI, HTTPException, Body, status, Response, Depends
from pydantic import BaseModel, Field
from datetime import date # Still need to import the 'date' type
from typing import List, Dict, Any

# IMPORTANT: This imports the database functions we just updated
from database import initialize_db, add_expense, get_all_expenses, get_summary_by_category

# --- Pydantic Schemas for Data Validation and Documentation ---

# Schema for incoming expense data (POST body)
class ExpenseCreate(BaseModel):
    # CHANGED: Renamed 'date' to 'expense_date' to avoid Pydantic conflict errors.
    expense_date: date = Field(..., description="Date of the expense (YYYY-MM-DD)")
    amount: float = Field(..., gt=0, description="Amount spent")
    category: str = Field(..., description="Category of the expense (e.g., Groceries, Rent)")
    description: str = Field(None, description="Detailed description of the expense")

# Schema for expense data returned from the GET endpoints
class Expense(ExpenseCreate):
    # Already changed in the last step
    expense_id: int = Field(..., description="Unique ID of the expense")

# Schema for the category summary data returned from the summary endpoint
class CategorySummary(BaseModel):
    category: str = Field(..., description="Category name")
    total_spent: float = Field(..., description="Total amount spent in this category")

# --- FastAPI Application Setup ---

app = FastAPI(
    title="Expense Tracker API",
    description="A simple API for tracking personal expenses using SQLite.",
    version="1.0.3" # Incrementing version after the fix
)

# --- Startup Event (Database Initialization) ---

@app.on_event("startup")
def startup_event():
    """Initializes the database when the application starts."""
    initialize_db()

# --- API Endpoints ---

@app.post("/expenses", response_model=Dict[str, Any], status_code=status.HTTP_200_OK)
def create_expense(expense: ExpenseCreate):
    """Adds a new expense to the tracker."""
    try:
        # CHANGED: Use expense.expense_date instead of expense.date
        add_expense(
            date=expense.expense_date.isoformat(), # The argument name is still 'date' for the function
            amount=expense.amount,
            category=expense.category,
            description=expense.description
        )
        return {
            "message": "Expense added successfully",
            "date": expense.expense_date.isoformat(),
            "amount": expense.amount
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to add expense: {e}"
        )

@app.get("/expenses", response_model=List[Expense], status_code=status.HTTP_200_OK)
def read_expenses():
    """Retrieves all recorded expenses."""
    try:
        expenses = get_all_expenses()

        # REMAPPING: Convert 'id' key from database output to 'expense_id' and 'date' to 'expense_date'
        remapped_expenses = []
        for exp in expenses:
            remapped_expenses.append({
                "expense_id": exp.pop("id"), # Renaming 'id' to 'expense_id'
                "expense_date": exp.pop("date"), # Renaming 'date' to 'expense_date' for the model
                **exp # Spreading the rest of the dictionary keys
            })

        return remapped_expenses
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve expenses: {e}"
        )

# NEW ENDPOINT: Category Summary
@app.get("/summary", response_model=List[CategorySummary], status_code=status.HTTP_200_OK)
def get_category_summary():
    """Calculates and returns the total spent per category."""
    try:
        summary = get_summary_by_category()
        return summary
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve category summary: {e}"
        )

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    """Simple root endpoint to confirm the API is running."""
    return {"message": "Hello World! FastAPI is running correctly!"}
