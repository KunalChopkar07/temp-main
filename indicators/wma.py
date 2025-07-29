import numpy as np

def calculate_wma(candles: np.ndarray, period: int) -> dict:
    """
    Weighted Moving Average (WMA)

    :param candles: np.ndarray with OHLCV format
    :param period: int - number of periods
    :return: dict with WMA values
    """
    close = candles[:, 4]
    wma = np.full_like(close, fill_value=np.nan)

    weights = np.arange(1, period + 1)

    for i in range(period - 1, len(close)):
        window = close[i - period + 1:i + 1]
        wma[i] = np.dot(window, weights) / weights.sum()

    clean_wma = wma[~np.isnan(wma)]

    return {
        "indicator": "wma",
        "values": clean_wma.tolist()
    }
