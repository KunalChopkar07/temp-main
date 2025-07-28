import numpy as np

def calculate_rob_missed_pivots(candles: np.ndarray) -> dict:
    """
    Simple detection of 'missed' pivots (previous pivot not touched today).

    :param candles: np.ndarray
    """
    high = np.max(candles[:-1][:, 2])
    low = np.min(candles[:-1][:, 3])
    close = candles[-2, 4]
    pivot = (high + low + close) / 3

    today_high = candles[-1, 2]
    today_low = candles[-1, 3]

    missed = not (today_low <= pivot <= today_high)

    return {
        "indicator": "rob_missed_pivot",
        "pivot": pivot,
        "missed_today": missed
    }
