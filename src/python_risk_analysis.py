# ----------------------------------------------------------------------
# PYTHON CODE NODE: Gold Market Risk Scorer
# This script analyzes the 24-hour gold price percentage change (chp)
# and assigns a risk score (1-5) based on volatility.
# ----------------------------------------------------------------------

# 1. Access the Data
# Gold data is the second item (index 1) in the merged list from the Merge node.
# NOTE: We use the $input.all() method for robust access within the n8n environment.
input_items = $input.all()
gold_data = input_items[1].json
change_percent = gold_data.get('chp', 0.0) # Get the change percentage, default to 0.0 if missing

# 2. Define the Risk Scoring Logic
def calculate_risk_score(chp):
    """Calculates a risk score (1-5) based on volatility (absolute change %)."""
    # Use absolute value to measure volatility regardless of gain or loss
    abs_chp = abs(chp)
    
    if abs_chp >= 1.5:
        # High volatility - movement of 1.5% or more in 24h
        return 5, "EXTREME VOLATILITY. Potential major market shift."
    elif abs_chp >= 1.0:
        # Significant volatility
        return 4, "High volatility detected. Watch closely."
    elif abs_chp >= 0.5:
        # Moderate volatility (normal trading day)
        return 3, "Moderate volatility. Standard market movement."
    elif abs_chp >= 0.2:
        # Low volatility
        return 2, "Low volatility. Consolidation period."
    else:
        # Very low volatility / flat market
        return 1, "Very low volatility. Market currently flat."

# 3. Execute Analysis and Structure Output
risk_score, summary = calculate_risk_score(change_percent)

# Attach the new analysis data to the first existing item (index 0 - Weather data)
# This allows all original data and new analysis to flow to the next node.
input_items[0].json['gold_risk_score'] = risk_score
input_items[0].json['gold_risk_summary'] = summary
input_items[0].json['gold_change_percent'] = change_percent

return input_items
