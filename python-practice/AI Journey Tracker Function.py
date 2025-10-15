# --- AI Journey Tracker Function ---

def ai_journey_tracker():
    """Track your AI learning journey by setting goals and calculating commitment."""
    
    # Automatically set info based on user's progress and goals
    name = "Gaber"
    current_skill = "Beginner"
    target_salary = "20000"
    
    # The program will still ask for the timeline in months
    months_input = input("Timeline (months, e.g., 6): ") 
    
    # Convert the months input from string to integer for calculation
    try:
        months = int(months_input)
    except ValueError:
        print("Error: Timeline must be a whole number. Setting to 6 months.")
        months = 6
        
    # Calculate total time commitment
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

# Call the function to start the journey tracker
ai_journey_tracker()
