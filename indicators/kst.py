import numpy as np
from jesse.indicators.kst import kst

def calculate_kst(candles: np.ndarray) -> dict:
    """
    Calculates the Know Sure Thing (KST) indicator.

    :param candles: np.ndarray of OHLCV candles.
    :return: Dictionary with KST and its signal line values.
    """
    kst_values, signal = kst(candles, sequential=True)

    return {
        "indicator": "kst",
        "kst": kst_values[~np.isnan(kst_values)].tolist(),
        "signal": signal[~np.isnan(signal)].tolist()
    }
