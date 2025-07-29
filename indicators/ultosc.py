import numpy as np
from jesse.indicators.ultosc import ultosc

def calculate_ultosc(candles: np.ndarray, short: int = 7, medium: int = 14, long: int = 28) -> dict:
    """
    Calculates the Ultimate Oscillator (ULTOSC) from price candles.

    :param candles: np.ndarray with OHLCV data
    :param short: short-term period (default=7)
    :param medium: medium-term period (default=14)
    :param long: long-term period (default=28)
    :return: dict containing the ultimate oscillator values
    """
    values = ultosc(candles, short=short, medium=medium, long=long, sequential=True)
    clean_values = values[~np.isnan(values)]

    return {
        "indicator": "ultosc",
        "short": short,
        "medium": medium,
        "long": long,
        "values": clean_values.tolist()
    }
