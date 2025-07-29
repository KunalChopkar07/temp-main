import numpy as np
from jesse.indicators.ichimoku_cloud import ichimoku_cloud

def calculate_ichimoku_cloud(candles: np.ndarray) -> dict:
    """
    Calculates the Ichimoku Cloud components.

    :param candles: np.ndarray of OHLCV candles.
    :return: Dictionary with ichimoku components.
    """
    tenkan, kijun, senkou_span_a, senkou_span_b, chikou = ichimoku_cloud(candles, sequential=True)

    return {
        "indicator": "ichimoku_cloud",
        "tenkan_sen": tenkan[~np.isnan(tenkan)].tolist(),
        "kijun_sen": kijun[~np.isnan(kijun)].tolist(),
        "senkou_span_a": senkou_span_a[~np.isnan(senkou_span_a)].tolist(),
        "senkou_span_b": senkou_span_b[~np.isnan(senkou_span_b)].tolist(),
        "chikou_span": chikou[~np.isnan(chikou)].tolist()
    }
