import numpy as np
from jesse.indicators.dm import dm

def calculate_dm(candles: np.ndarray, period: int) -> dict:
    """
    Calculate Directional Movement (+DM and -DM)

    :param candles: np.ndarray -> [timestamp, open, high, low, close, volume]
    :param period: int
    :return: dict with +DM and -DM
    """
    plus_dm, minus_dm = dm(candles, period=period, sequential=True)

    clean_plus_dm = plus_dm[~np.isnan(plus_dm)]
    clean_minus_dm = minus_dm[~np.isnan(minus_dm)]

    return {
        "indicator": "dm",
        "period": period,
        "plus_dm": clean_plus_dm.tolist(),
        "minus_dm": clean_minus_dm.tolist()
    }
