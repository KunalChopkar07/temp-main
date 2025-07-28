import numpy as np

def calculate_volume24h(candles: np.ndarray) -> dict:
    """
    Calculates the total 24-hour volume from 1-minute candles.

    Each candle must be of the format: [timestamp, open, high, low, close, volume]

    :param candles: np.ndarray of 1440 1-minute candles
    :return: dict containing the total volume
    """
    volumes = candles[:, 5]  # volume is at index 5
    total_volume = np.nansum(volumes)

    return {
        "indicator": "volume24h",
        "volume": float(total_volume)
    }
