import numpy as np

def calculate_williams_fractals(candles: np.ndarray) -> dict:
    """
    Detects Williams Fractals (Bullish & Bearish)

    :param candles: np.ndarray with OHLCV candles [timestamp, open, high, low, close, volume]
    :return: dict with bullish and bearish fractal indices
    """
    highs = candles[:, 2]
    lows = candles[:, 3]

    bullish = []
    bearish = []

    for i in range(2, len(candles) - 2):
        if lows[i] < lows[i - 1] and lows[i] < lows[i - 2] and lows[i] < lows[i + 1] and lows[i] < lows[i + 2]:
            bullish.append(i)

        if highs[i] > highs[i - 1] and highs[i] > highs[i - 2] and highs[i] > highs[i + 1] and highs[i] > highs[i + 2]:
            bearish.append(i)

    return {
        "indicator": "williams_fractals",
        "bullish_indices": bullish,
        "bearish_indices": bearish
    }
