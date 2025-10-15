# DAY 2: Python Loops Practice

# ═══════════════════════════════════════════════════
# EXERCISE 1: Learning Journey Countdown
# ═══════════════════════════════════════════════════

def countdown_to_job():
    """Count down days to job-ready, using current progress (Day 2)"""
    total_days = 180
    
    # Start the loop from the current day (Day 2) and show the next 10 days
    # Note: range(2, 12) will run for days 2, 3, 4, ..., 11 (10 iterations)
    print("\n--- Next 10 Days of Progress ---\n")
    for day in range(2, 12):
        days_left = total_days - day
        progress = (day / total_days) * 100
        print(f"Day {day}: {days_left} days left ({progress:.1f}% complete)")

countdown_to_job()

# ═══════════════════════════════════════════════════
# EXERCISE 2: Skill Accumulation Tracker
# ═══════════════════════════════════════════════════

def track_skills():
    """Track skills learned over time (Pre-populated with Day 2 skills)"""
    # Using your actual Day 1 and Day 2 core skills:
    skills = [
        "Python Functions/Variables",
        "Python Conditionals (if/elif/else)",
        "Python Loops (for/while)",
        "API Fundamentals (GET/POST)",
        "n8n Automation",
        "Gemini AI Integration",
        "Git/GitHub Basics"
    ]
    
    print("\n" + "="*50)
    print("YOUR SKILL INVENTORY:")
    print("="*50)
    
    # Display the current skills
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")
        
    print(f"\nTotal skills learned so far: {len(skills)}")
    print("="*50)
    
    # Loop for adding new skills (commented out to avoid stopping execution)
    # while True:
    #     skill = input("Enter a skill you learned (or 'done' to finish): ")
        
    #     if skill.lower() == 'done':
    #         break
        
    #     skills.append(skill)
    #     print(f"Added: {skill}")
    #     print(f"Total skills: {len(skills)}")


# Uncomment the line below to run the pre-populated function
track_skills()

# ═══════════════════════════════════════════════════
# EXERCISE 3: Gold Price History Analyzer
# ═══════════════════════════════════════════════════

def analyze_gold_trends():
    """Analyze gold price history (simulated data based on current $4200/oz price)"""
    
    # Simulated gold prices for last 10 days (showing realistic volatility around $4200)
    prices = [4185, 4210, 4205, 4225, 4200, 4235, 4230, 4250, 4240, 4260] # Latest price: $4260
    
    print("\nGOLD PRICE TREND ANALYSIS")
    print("="*50)
    
    # Calculate statistics using built-in functions
    highest = max(prices)
    lowest = min(prices)
    average = sum(prices) / len(prices)
    
    # Count up days vs down days using a loop
    up_days = 0
    down_days = 0
    
    # The loop runs 9 times to compare each day (prices[i]) to the previous day (prices[i-1])
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            up_days += 1
        elif prices[i] < prices[i-1]:
            down_days += 1
    
    # Display results
    print(f"Period: Last {len(prices)} days")
    print(f"Highest Price: ${highest}")
    print(f"Lowest Price: ${lowest}")
    print(f"Average Price: ${average:.2f}")
    print(f"Up Days: {up_days}")
    print(f"Down Days: {down_days}")
    # Use conditionals to determine the overall trend
    print(f"Trend: {'Bullish' if up_days > down_days else 'Bearish' if down_days > up_days else 'Neutral'}")
    print("="*50)
    
    # Show daily changes using a loop
    print("\nDAILY PRICE MOVEMENTS:")
    for i, price in enumerate(prices, 1):
        if i == 1:
            print(f"Day {i}: ${price} (Starting price)")
        else:
            # prices[i-2] is the price from the previous day's index.
            # (i-1 in the loop, but using 1-based day count)
            change = price - prices[i-2]
            symbol = "📈" if change > 0 else "📉" if change < 0 else "➡️"
            print(f"Day {i}: ${price} ({symbol} {change:+.0f})")

analyze_gold_trends()

# ═══════════════════════════════════════════════════
# YOUR CHALLENGE: find_best_trade
# ═══════════════════════════════════════════════════

def find_best_trade(prices):
    """Find best buy and sell days for maximum profit using nested loops"""
    # Initialize variables to track maximum profit
    max_profit = 0
    best_buy_day = 0
    best_sell_day = 0
    
    # Outer loop: Iterate through all possible buy days (i)
    for i in range(len(prices)):
        buy_price = prices[i]
        
        # Inner loop: Iterate through all possible sell days (j) after the buy day (i + 1)
        for j in range(i + 1, len(prices)):
            sell_price = prices[j]
            current_profit = sell_price - buy_price
            
            # Use conditional logic to check if this trade is better
            if current_profit > max_profit:
                max_profit = current_profit
                best_buy_day = i + 1  # Use 1-based indexing for display
                best_sell_day = j + 1
                
    if max_profit > 0:
        print(f"\n--- Best Trade Analysis ---")
        print(f"Max Profit: ${max_profit}")
        print(f"Buy Day: {best_buy_day} (${prices[best_buy_day-1]})")
        print(f"Sell Day: {best_sell_day} (${prices[best_sell_day-1]})")
        print("---------------------------\n")
    else:
        print("\n--- Best Trade Analysis ---\nNo profit opportunity found.\n---------------------------\n")

# Test with new, realistic gold price data
find_best_trade([4185, 4210, 4205, 4225, 4200, 4235, 4230, 4250, 4240, 4260])

# Expected: Buy Day 1 ($4185), Sell Day 10 ($4260), Profit $75
