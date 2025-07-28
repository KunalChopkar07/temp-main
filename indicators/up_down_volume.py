import numpy as np

def calculate_up_down_volume(candles: np.ndarray) -> dict:
    """
    Calculates Up/Down Volume from OHLCV candles.
    
    :param candles: np.ndarray of shape (N, 6)
    :return: dict with up_volume and down_volume arrays
    """
    closes = candles[:, 4]
    volumes = candles[:, 5]

    up_volume = np.zeros_like(volumes)
    down_volume = np.zeros_like(volumes)

    # Calculate up/down volume based on price movement
    for i in range(1, len(closes)):
        if closes[i] > closes[i - 1]:
            up_volume[i] = volumes[i]
        elif closes[i] < closes[i - 1]:
            down_volume[i] = volumes[i]
        # equal close => neither

    return {
        "indicator": "up_down_volume",
        "up_volume": up_volume.tolist(),
        "down_volume": down_volume.tolist()
    }
