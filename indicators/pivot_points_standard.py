import numpy as np

def calculate_pivot_points_standard(candles: np.ndarray) -> dict:
    high = np.max(candles[:, 1])
    low = np.min(candles[:, 2])
    close = candles[-1][2]

    pivot = (high + low + close) / 3
    r1 = 2 * pivot - low
    s1 = 2 * pivot - high

    return {
        "indicator": "pivot_points_standard",
        "pivot": round(pivot, 2),
        "resistance_1": round(r1, 2),
        "support_1": round(s1, 2)
    }
