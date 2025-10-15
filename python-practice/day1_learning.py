# --- New AI Journey Tracker Function ---

def ai_journey_tracker():
    """Track your AI learning journey"""
    
    # Get info from user using the input() function
    # NOTE: The input() function always returns text (a string)!
    name = input("Gaber")
    current_skill = input("Beginner")
    target_salary = input("20,000 AED")
    
    # Ask for timeline in months
    months_input = input("6 Months") 
    
    # CRITICAL: Convert the months input from string to integer for calculation
    # If we didn't do this, Python would raise an error when multiplying
    try:
        months = int(months_input)
    except ValueError:
        print("Error: Timeline must be a whole number. Setting to 6 months.")
        months = 6
        
    # Calculate
    days = months * 30
    daily_hours = 4 
    total_hours = days * daily_hours 
    
    # Display summary
    print("\n" + "="*50)
    print("YOUR AI ENGINEER JOURNEY PLAN")
    print("="*50)
    print(f"Name: {name}")
    print(f"Starting Level: {current_skill}")
    print(f"Target Salary: AED {target_salary}")
    print(f"Timeline: {months} months ({days} days)")
    print(f"Daily Commitment: {daily_hours} hours")
    print(f"Total Learning Hours: {total_hours}")
    print("="*50)
    print(f"\n🚀 Let's do this, {name}! Day 1 of {days}!")
    print("="*50)

# Call the new function to start the user input prompts
ai_journey_tracker()

