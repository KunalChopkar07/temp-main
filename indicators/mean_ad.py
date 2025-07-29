import numpy as np
from jesse.indicators.mean_ad import mean_ad

def calculate_mean_ad(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates the Mean Absolute Deviation (Mean AD).

    :param candles: np.ndarray of OHLCV candles
    :param period: Period over which to calculate Mean AD (default: 14)
    :return: dict with Mean AD values
    """
    values = mean_ad(candles, period=period, sequential=True)
    clean = values[~np.isnan(values)]

    return {
        "indicator": "mean_ad",
        "period": period,
        "values": clean.tolist()
    }
