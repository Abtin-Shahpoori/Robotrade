def buysell(**args):
    candles = args.get("candle")
    opening_prices , closing_prices, highest_prices = [], [], []

    for candle in candles:
        opening_prices.append(float(candle[1]))
        closing_prices.append(float(candle[2]))
        highest_prices.append(float(candle[3]))
    
    n = len(opening_prices)
    if n < 2:
        return 0
    if closing_prices[n -1] == opening_prices[n-1]:
        return 0

    if (opening_prices[n - 2] < opening_prices[n - 3]) and (closing_prices[n - 1] > opening_prices[n - 2]):
        return {"entry_price": closing_prices[n - 1], "stop_loss": closing_prices[n - 2], "take_profit": max(closing_prices[n-1] + 0.002 * closing_prices[n-1], opening_prices[n-1])}
    else:
        return 0
