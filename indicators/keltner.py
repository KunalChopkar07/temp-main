import numpy as np
from jesse.indicators.keltner import keltner

def calculate_keltner(candles: np.ndarray, period: int = 20) -> dict:
    """
    Calculates the Keltner Channels (upper, middle, lower bands).

    :param candles: np.ndarray of OHLCV candles.
    :param period: Period for the Keltner calculation.
    :return: Dictionary with band values.
    """
    upper, middle, lower = keltner(candles, period=period, sequential=True)

    return {
        "indicator": "keltner_channels",
        "period": period,
        "upper_band": upper[~np.isnan(upper)].tolist(),
        "middle_band": middle[~np.isnan(middle)].tolist(),
        "lower_band": lower[~np.isnan(lower)].tolist()
    }
