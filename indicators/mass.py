import numpy as np
from jesse.indicators.mass import mass

def calculate_mass(candles: np.ndarray, period: int = 9) -> dict:
    """
    Calculates the Mass Index.

    :param candles: np.ndarray of OHLCV candles
    :param period: Period used to calculate Mass Index (default: 9)
    :return: dict with Mass Index values
    """
    values = mass(candles, period=period, sequential=True)
    clean = values[~np.isnan(values)]

    return {
        "indicator": "mass_index",
        "period": period,
        "values": clean.tolist()
    }
