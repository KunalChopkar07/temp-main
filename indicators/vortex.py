import numpy as np
from jesse.helpers import slice_candles
from jesse.indicators import vi  # Jesse already includes vortex indicator

def calculate_vortex(candles: np.ndarray, period: int) -> dict:
    """
    Calculate Vortex Indicator (VI+ and VI−) for the given candles.
    :param candles: np.ndarray of shape (N, 6)
    :param period: int
    :return: dict with VI+ and VI− arrays
    """
    candles = slice_candles(candles, sequential=True)
    vi_plus, vi_minus = vi(candles, period=period, sequential=True)

    clean_vi_plus = vi_plus[~np.isnan(vi_plus)]
    clean_vi_minus = vi_minus[~np.isnan(vi_minus)]

    return {
        "indicator": "vortex",
        "vi_plus": clean_vi_plus.tolist(),
        "vi_minus": clean_vi_minus.tolist()
    }
