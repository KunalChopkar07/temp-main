import numpy as np
from jesse.indicators.medprice import medprice

def calculate_medprice(candles: np.ndarray) -> dict:
    """
    Calculates the Median Price for each candle.

    Median Price = (High + Low) / 2

    :param candles: np.ndarray of OHLCV candles
    :return: dict with Median Price values
    """
    values = medprice(candles, sequential=True)
    clean = values[~np.isnan(values)]

    return {
        "indicator": "medprice",
        "values": clean.tolist()
    }
