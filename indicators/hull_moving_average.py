import numpy as np

def calculate_hma(candles: np.ndarray, period: int = 21) -> dict:
    """
    Calculates the Hull Moving Average (HMA).

    :param candles: np.ndarray with shape [timestamp, open, high, low, close, volume]
    :param period: Period to calculate HMA
    :return: dict with HMA values
    """
    close = candles[:, 4]

    def wma(data, length):
        weights = np.arange(1, length + 1)
        wmas = np.convolve(data, weights[::-1], 'valid') / weights.sum()
        return np.concatenate((np.full(length - 1, np.nan), wmas))

    half_period = int(period / 2)
    sqrt_period = int(np.sqrt(period))

    wma_half = wma(close, half_period)
    wma_full = wma(close, period)

    diff = 2 * wma_half - wma_full
    hma = wma(diff[~np.isnan(diff)], sqrt_period)

    # Fill output with same shape as input
    padded_hma = np.full_like(close, np.nan)
    valid_start = len(padded_hma) - len(hma)
    padded_hma[-len(hma):] = hma

    return {
        "indicator": "hma",
        "period": period,
        "values": padded_hma.tolist()
    }

