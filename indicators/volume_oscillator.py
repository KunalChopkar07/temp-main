import numpy as np
from jesse.indicators import vosc

def calculate_volume_oscillator(candles: np.ndarray, short_period: int = 5, long_period: int = 20) -> dict:
    """
    Calculate the Volume Oscillator (VO)
    :param candles: np.ndarray with shape (N, 6)
    :param short_period: int
    :param long_period: int
    :return: dict with VO values
    """
    values = vosc(candles, short_period=short_period, long_period=long_period, sequential=True)
    clean_values = values[~np.isnan(values)]

    return {
        "indicator": "volume_oscillator",
        "short_period": short_period,
        "long_period": long_period,
        "values": clean_values.tolist()
    }


