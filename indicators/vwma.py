import numpy as np
from jesse.indicators import vwma

def calculate_vwma(candles: np.ndarray, period: int) -> dict:
    """
    Calculate Volume Weighted Moving Average (VWMA)
    :param candles: np.ndarray with shape (N, 6)
    :param period: int
    :return: dict with VWMA values
    """
    values = vwma(candles, period=period, sequential=True)
    clean_values = values[~np.isnan(values)]

    return {
        "indicator": "vwma",
        "values": clean_values.tolist()
    }
