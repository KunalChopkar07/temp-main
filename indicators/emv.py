import numpy as np
from jesse.indicators.emv import emv

def calculate_emv(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates the Ease of Movement (EMV) indicator.

    :param candles: np.ndarray containing OHLCV candles.
    :param period: The smoothing period (default 14).
    :return: A dictionary containing cleaned EMV values.
    """
    values = emv(candles, period=period, sequential=True)
    clean_values = values[~np.isnan(values)]

    return {
        "indicator": "emv",
        "period": period,
        "values": clean_values.tolist()
    }
