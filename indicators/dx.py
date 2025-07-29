import numpy as np
from jesse.indicators.dx import dx

def calculate_dx(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Directional Movement Index (DX).

    :param candles: np.ndarray -> [timestamp, open, high, low, close, volume]
    :param period: int
    :return: dict with DX values
    """
    values = dx(candles, period=period, sequential=True)
    clean = values[~np.isnan(values)]

    return {
        "indicator": "dx",
        "period": period,
        "values": clean.tolist()
    }
