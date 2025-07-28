import numpy as np

def calculate_rob_intraday_pivot(candles: np.ndarray) -> dict:
    """
    Calculates Rob Booker's Intraday Pivot Points.
    Typically based on the previous day's OHLC data.

    :param candles: np.ndarray with shape (n, 6)
    :return: dict with pivot, support, and resistance levels
    """
    previous_day = candles[:-1]  # all but the most recent candle
    high = np.max(previous_day[:, 2])
    low = np.min(previous_day[:, 3])
    close = previous_day[-1, 4]

    pivot = (high + low + close) / 3
    r1 = (2 * pivot) - low
    s1 = (2 * pivot) - high
    r2 = pivot + (high - low)
    s2 = pivot - (high - low)

    return {
        "indicator": "rob_intraday_pivot",
        "pivot": pivot,
        "resistance1": r1,
        "support1": s1,
        "resistance2": r2,
        "support2": s2
    }
