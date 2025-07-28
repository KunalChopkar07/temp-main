import numpy as np
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from indicators.sma import calculate_sma

def calculate_technical_rating(candles: np.ndarray, period: int = 14) -> dict:
    """
    Combines multiple indicator signals into a simplified technical rating.

    Signals:
    - RSI > 70 → Sell
    - RSI < 30 → Buy
    - MACD line > signal line → Buy
    - MACD line < signal line → Sell
    - Price > SMA → Buy
    - Price < SMA → Sell
    """
    rsi_values = calculate_rsi(candles, period)
    macd_result = calculate_macd(candles)
    sma_values = calculate_sma(candles, period)

    rsi_latest = rsi_values[-1]
    macd_latest = macd_result['macd'][-1]
    signal_latest = macd_result['signal'][-1]
    price_latest = candles[-1][4]  # close price
    sma_latest = sma_values[-1]

    score = 0

    # RSI
    if rsi_latest < 30:
        score += 1
    elif rsi_latest > 70:
        score -= 1

    # MACD
    if macd_latest > signal_latest:
        score += 1
    elif macd_latest < signal_latest:
        score -= 1

    # SMA
    if price_latest > sma_latest:
        score += 1
    elif price_latest < sma_latest:
        score -= 1

    if score >= 2:
        rating = "Strong Buy"
    elif score == 1:
        rating = "Buy"
    elif score == 0:
        rating = "Neutral"
    elif score == -1:
        rating = "Sell"
    else:
        rating = "Strong Sell"

    return {
        "indicator": "technical_ratings",
        "rsi": float(rsi_latest),
        "macd": float(macd_latest),
        "macd_signal": float(signal_latest),
        "sma": float(sma_latest),
        "price": float(price_latest),
        "score": score,
        "rating": rating
    }
