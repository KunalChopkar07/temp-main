import numpy as np
from jesse.indicators import sma

def calculate_ma_index(candles: np.ndarray, period: int) -> dict:
    """
    MA Index shows the relative distance between price and its moving average.
    """
    close = candles[:, 2]  # or candles[:, 4] if you prefer 'close' prices
    ma = sma(candles, period=period, sequential=True)

    with np.errstate(divide='ignore', invalid='ignore'):
        ma_index = ((close - ma) / ma) * 100

    clean_ma_index = ma_index[~np.isnan(ma_index)]

    return {
        "indicator": "ma_index",
        "ma_index": clean_ma_index.tolist()
    }
