import numpy as np
from jesse.indicators.dpo import dpo

def calculate_dpo(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Detrended Price Oscillator (DPO).

    :param candles: np.ndarray -> [timestamp, open, high, low, close, volume]
    :param period: int
    :return: dict with DPO values
    """
    values = dpo(candles, period=period, sequential=True)
    clean = values[~np.isnan(values)]

    return {
        "indicator": "dpo",
        "period": period,
        "values": clean.tolist()
    }
