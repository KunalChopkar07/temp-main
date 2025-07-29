import numpy as np
from jesse.indicators.mom import mom

def calculate_momentum(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Momentum indicator.

    Momentum = Close - Close[n-period]

    :param candles: np.ndarray of OHLCV candles
    :param period: Number of periods
    :return: dict with Momentum values
    """
    values = mom(candles, period=period, sequential=True)
    clean = values[~np.isnan(values)]

    return {
        "indicator": "momentum",
        "period": period,
        "values": clean.tolist()
    }
