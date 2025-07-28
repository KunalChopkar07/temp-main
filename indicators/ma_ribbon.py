import numpy as np
from jesse.indicators.sma import sma

def calculate_ma_ribbon(candles: np.ndarray, base_period: int = 10, ribbons: int = 6, step: int = 5) -> dict:
    """
    Generates a Moving Average Ribbon consisting of multiple SMAs with increasing periods.

    :param candles: np.ndarray OHLCV data
    :param base_period: the starting period for the first SMA
    :param ribbons: number of SMAs in the ribbon
    :param step: how much to increment each subsequent SMA
    :return: dict with each SMA ribbon
    """
    result = {}
    for i in range(ribbons):
        period = base_period + i * step
        ma = sma(candles, period=period, sequential=True)
        result[f"sma_{period}"] = ma[~np.isnan(ma)].tolist()

    return {
        "indicator": "ma_ribbon",
        "ribbons": result
    }
