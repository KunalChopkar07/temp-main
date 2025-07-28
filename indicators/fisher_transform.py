import numpy as np
from jesse.indicators.fisher import fisher

def calculate_fisher_transform(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Fisher Transform indicator.

    :param candles: np.ndarray with shape [N, 6] in OHLCV format
    :param period: Lookback period for Fisher Transform
    :return: dict with fisher and signal line values
    """
    f, signal = fisher(candles, period=period, sequential=True)

    return {
        "indicator": "fisher_transform",
        "fisher": f[~np.isnan(f)].tolist(),
        "signal": signal[~np.isnan(signal)].tolist()
    }
