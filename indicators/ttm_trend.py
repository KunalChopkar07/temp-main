import numpy as np
from jesse.helpers import slice_candles
from jesse.indicators.sma import sma

def calculate_ttm_trend(candles: np.ndarray, period: int = 20) -> dict:
    """
    TTM Trend indicator shows trend direction (bullish or bearish) based on candle closes and moving average.
    If the close is above the SMA, trend is bullish; otherwise, bearish.

    :param candles: np.ndarray with shape (n, 6)
    :param period: int - moving average period
    :return: dict with trend values as 1 (bullish) or -1 (bearish)
    """
    close = candles[:, 4]
    ma = sma(candles, period=period, source_type="close", sequential=True)

    trend = np.where(close > ma, 1, -1)
    trend_clean = trend[~np.isnan(ma)]  # Filter for valid moving average values

    return {
        "indicator": "ttm_trend",
        "period": period,
        "trend": trend_clean.tolist()
    }
