import numpy as np

def calculate_rob_reversal(candles: np.ndarray) -> dict:
    """
    Simple reversal logic using engulfing pattern.

    :param candles: np.ndarray
    """
    if len(candles) < 2:
        return {"indicator": "rob_reversal", "signal": "insufficient data"}

    prev = candles[-2]
    curr = candles[-1]

    # Bullish engulfing
    if curr[1] < curr[4] and curr[1] < prev[1] and curr[4] > prev[4]:
        signal = "bullish"
    elif curr[1] > curr[4] and curr[1] > prev[1] and curr[4] < prev[4]:
        signal = "bearish"
    else:
        signal = "none"

    return {
        "indicator": "rob_reversal",
        "signal": signal
    }
