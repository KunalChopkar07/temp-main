import numpy as np
from jesse.indicators.willr import willr

def calculate_williams_r(candles: np.ndarray, period: int) -> dict:
    """
    Calculates Williams %R indicator.

    :param candles: np.ndarray of shape (N, 6) -> [timestamp, open, high, low, close, volume]
    :param period: Lookback period
    :return: Dictionary with cleaned Williams %R values
    """
    wr_values = willr(candles, period=period, sequential=True)
    clean_wr = wr_values[~np.isnan(wr_values)]

    return {
        "indicator": "williams_r",
        "period": period,
        "values": clean_wr.tolist()
    }
