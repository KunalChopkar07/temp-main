import numpy as np
from jesse.indicators.median_ad import median_ad

def calculate_median_ad(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates the Median Absolute Deviation (Median AD).

    :param candles: np.ndarray of OHLCV candles
    :param period: Period over which to calculate Median AD (default: 14)
    :return: dict with Median AD values
    """
    values = median_ad(candles, period=period, sequential=True)
    clean = values[~np.isnan(values)]

    return {
        "indicator": "median_ad",
        "period": period,
        "values": clean.tolist()
    }
