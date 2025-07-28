import numpy as np
from jesse.indicators.atr import atr

def calculate_volatility_stop(candles: np.ndarray, period: int = 14, multiplier: float = 2.0) -> dict:
    """
    Calculates a simplified version of Volatility Stop using ATR.

    :param candles: np.ndarray of candles [timestamp, open, high, low, close, volume]
    :param period: ATR period
    :param multiplier: multiplier applied to ATR
    :return: dict with upper/lower volatility stop lines
    """
    close = candles[:, 4]
    atr_values = atr(candles, period=period, sequential=True)

    upper = close + multiplier * atr_values
    lower = close - multiplier * atr_values

    # Clean NaNs
    clean_upper = upper[~np.isnan(upper)]
    clean_lower = lower[~np.isnan(lower)]

    return {
        "indicator": "volatility_stop",
        "period": period,
        "multiplier": multiplier,
        "upper": clean_upper.tolist(),
        "lower": clean_lower.tolist()
    }
