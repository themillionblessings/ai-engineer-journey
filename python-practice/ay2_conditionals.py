def calculate_grade(score):
    """Convert numerical score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test it
print(f"95 Score: {calculate_grade(95)}")  # Should print A
print(f"75 Score: {calculate_grade(75)}")  # Should print C

