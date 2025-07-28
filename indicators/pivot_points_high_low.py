import numpy as np

def calculate_pivot_points_high_low(candles: np.ndarray) -> dict:
    high = np.max(candles[:, 1])  # high
    low = np.min(candles[:, 2])   # low

    return {
        "indicator": "pivot_points_high_low",
        "pivot_high": float(high),
        "pivot_low": float(low)
    }
