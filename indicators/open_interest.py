import numpy as np

def calculate_open_interest(candles: np.ndarray) -> dict:
    """
    Assumes open interest is at index 6 of the candles (if available).
    If not available, this will be a placeholder returning zeros.
    """
    if candles.shape[1] <= 6:
        raise ValueError("Open Interest data not available in candles.")

    open_interest = candles[:, 6]
    clean_oi = open_interest[~np.isnan(open_interest)]

    return {
        "indicator": "open_interest",
        "values": clean_oi.tolist()
    }
