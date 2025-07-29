import numpy as np
from jesse.indicators.di import di

def calculate_di(candles: np.ndarray, period: int) -> dict:
    """
    Calculate Directional Indicator (+DI and -DI)

    :param candles: np.ndarray -> [timestamp, open, high, low, close, volume]
    :param period: int
    :return: dict with +DI and -DI
    """
    plus_di, minus_di = di(candles, period=period, sequential=True)

    clean_plus_di = plus_di[~np.isnan(plus_di)]
    clean_minus_di = minus_di[~np.isnan(minus_di)]

    return {
        "indicator": "di",
        "period": period,
        "plus_di": clean_plus_di.tolist(),
        "minus_di": clean_minus_di.tolist()
    }
