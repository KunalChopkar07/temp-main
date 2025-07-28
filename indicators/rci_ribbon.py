import numpy as np
from indicators.rci import calculate_rci  # reuse your RCI logic

def calculate_rci_ribbon(candles: np.ndarray, short_period=9, mid_period=26, long_period=52) -> dict:
    """
    RCI Ribbon with short, mid, and long-term RCI calculations.

    :param candles: np.ndarray - OHLCV candles
    :param short_period: int
    :param mid_period: int
    :param long_period: int
    :return: dict with RCI ribbon values
    """
    short_rci = calculate_rci(candles, short_period)["values"]
    mid_rci = calculate_rci(candles, mid_period)["values"]
    long_rci = calculate_rci(candles, long_period)["values"]

    return {
        "indicator": "rci_ribbon",
        "short_period": short_period,
        "mid_period": mid_period,
        "long_period": long_period,
        "short_rci": [v for v in short_rci if not np.isnan(v)],
        "mid_rci": [v for v in mid_rci if not np.isnan(v)],
        "long_rci": [v for v in long_rci if not np.isnan(v)],
    }
