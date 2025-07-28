import numpy as np

def calculate_performance(candles: np.ndarray) -> dict:
    close = candles[:, 2]  # assuming close price at index 2
    pct_change = (close[-1] - close[0]) / close[0] * 100

    return {
        "indicator": "performance",
        "percentage_change": round(pct_change, 2)
    }
