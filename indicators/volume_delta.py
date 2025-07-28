import numpy as np

def calculate_volume_delta(candles: np.ndarray) -> dict:
    """
    Calculates Volume Delta = Buy Volume - Sell Volume approximation.
    Assumes green candle (close > open) = buy volume, red candle = sell volume.

    :param candles: np.ndarray of candles: [timestamp, open, high, low, close, volume]
    :return: dict with volume delta series
    """
    close = candles[:, 4]
    open_ = candles[:, 1]
    volume = candles[:, 5]

    # Approximate buy/sell volume based on candle color
    delta = np.where(close > open_, volume, -volume)
    clean_delta = delta[~np.isnan(delta)]

    return {
        "indicator": "volume_delta",
        "values": clean_delta.tolist()
    }
