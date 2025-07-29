import numpy as np

def calculate_pivot(candles: np.ndarray) -> dict:
    """
    Calculates Pivot Points (Standard).

    Pivot = (High + Low + Close) / 3
    Resistance and Support levels:
    R1 = (2 * Pivot) - Low
    S1 = (2 * Pivot) - High
    R2 = Pivot + (High - Low)
    S2 = Pivot - (High - Low)

    :param candles: np.ndarray with shape (N, 6) as [timestamp, open, high, low, close, volume]
    :return: dict with latest Pivot, R1, S1, R2, S2
    """
    highs = candles[:, 2]
    lows = candles[:, 3]
    closes = candles[:, 4]

    pivot = (highs + lows + closes) / 3
    r1 = (2 * pivot) - lows
    s1 = (2 * pivot) - highs
    r2 = pivot + (highs - lows)
    s2 = pivot - (highs - lows)

    return {
        "indicator": "pivot_points",
        "pivot": pivot[-1],
        "resistance1": r1[-1],
        "support1": s1[-1],
        "resistance2": r2[-1],
        "support2": s2[-1]
    }
