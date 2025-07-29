import numpy as np

def calculate_volume(candles: np.ndarray) -> dict:
    """
    Extracts the volume values from OHLCV candles.

    :param candles: np.ndarray with OHLCV data
    :return: dict with volume values
    """
    volumes = candles[:, 5]
    clean_volumes = volumes[~np.isnan(volumes)]

    return {
        "indicator": "volume",
        "values": clean_volumes.tolist()
    }
