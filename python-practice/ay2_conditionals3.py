# ═══════════════════════════════════════════════════
# EXERCISE 3: Gold Investment Decision Logic (Standalone Updated Version)
# ═══════════════════════════════════════════════════

def gold_investment_advisor(price, price_change_24h, market_sentiment, buy_threshold, trading_volume, is_near_52w_high):
    """
    Advanced gold investment logic using Conditionals and Boolean Operators.
    
    Parameters:
    - price: Current gold price in USD
    - price_change_24h: Percentage change in last 24 hours
    - market_sentiment: "bullish", "bearish", or "neutral"
    - buy_threshold: Maximum price to consider buying (e.g., historical average)
    - trading_volume: "high" or "low"
    - is_near_52w_high: Boolean (True/False) - is the price near its historical peak?
    """
    
    print(f"\n{'='*50}")
    print("GOLD INVESTMENT ANALYSIS (Smarter Logic)")
    print(f"{'='*50}")
    print(f"Current Price: ${price}/oz")
    print(f"24h Change: {price_change_24h:+.2f}%")
    print(f"Market Sentiment: {market_sentiment.title()}")
    print(f"Buy Threshold: ${buy_threshold}/oz")
    print(f"Trading Volume: {trading_volume.title()}")
    print(f"Near 52-Week High: {is_near_52w_high}")
    print()
    
    # --- BOOLEAN LOGIC DEFINITIONS ---
    # Buy is only considered if the price is below the limit
    is_price_ok_to_buy = price < buy_threshold 
    
    # Selling is discouraged if volume is low OR the price is near the 52w high (potential breakout)
    is_safe_to_sell = trading_volume == "high" and not is_near_52w_high

    # --- DECISION PATH ---

    # 1. STRONG BUY: Highest confidence signal
    if (price_change_24h > 2 and market_sentiment == "bullish" 
        and is_price_ok_to_buy and trading_volume == "high"):
        decision = "STRONG BUY"
        reasoning = "Strong momentum, positive sentiment, high volume, and price is below threshold."
        
    # 2. BUY: Moderate confidence signal
    elif (price_change_24h > 0.5 and market_sentiment != "bearish" 
          and is_price_ok_to_buy):
        decision = "BUY"
        reasoning = "Moderate upward trend, price below threshold. (Volume not high enough for Strong Buy)."
        
    # 3. STRONG SELL: Highest certainty sell signal
    elif (price_change_24h < -2 and market_sentiment == "bearish" 
          and is_safe_to_sell):
        decision = "STRONG SELL"
        reasoning = "Significant drop with negative sentiment. Exiting while volume is high/safe."

    # 4. CONSIDER SELLING: Simple downward trend
    elif (price_change_24h < -0.5 and market_sentiment == "bearish"):
        decision = "CONSIDER SELLING"
        reasoning = "Downward trend with bearish sentiment. Check volume before selling."

    # 5. DEFAULT: HOLD
    else:
        # If any 'BUY' conditions failed because of the threshold, we HOLD.
        if not is_price_ok_to_buy and (price_change_24h > 0.5 or market_sentiment == "bullish"):
            decision = "HOLD (Price Too High)"
            reasoning = f"Momentum is positive, but price is above the target threshold of ${buy_threshold}."
        else:
            decision = "HOLD"
            reasoning = "No clear directional signal, or conditions are too risky (e.g., low volume sell-off)."
    
    print(f"RECOMMENDATION: {decision}")
    print(f"REASONING: {reasoning}")
    print(f"{'='*50}\n")
    
    return decision

# Test different scenarios using a real-world price (~$4200 per Troy Ounce)

BUY_LIMIT = 4250

# Scenario 1 (STRONG BUY - All TRUE): Strong momentum, Positive Sentiment, Price OK (4200<4250), High Volume, Not Near High
gold_investment_advisor(4200, 2.5, "bullish", BUY_LIMIT, "high", False)

# Scenario 2 (HOLD - Fails Price Check): Strong momentum, BUT Price is too high (4300>4250)
gold_investment_advisor(4300, 2.5, "bullish", BUY_LIMIT, "high", False)

# Scenario 3 (STRONG SELL - All TRUE): Big drop, Bearish, High Volume, Not Near High (Safe to sell)
gold_investment_advisor(4200, -3.0, "bearish", BUY_LIMIT, "high", False)

# Scenario 4 (CONSIDER SELLING - Fails Safe Sell): Big drop, Bearish, BUT Low Volume (Risky sell)
gold_investment_advisor(4200, -3.0, "bearish", BUY_LIMIT, "low", False)

# Scenario 5 (HOLD): Small change, price below limit, but no strong signal
gold_investment_advisor(4200, -0.2, "neutral", BUY_LIMIT, "low", False)
