import numpy as np

def calculate_stochastic(candles: np.ndarray, period: int = 14, smooth_k: int = 3, smooth_d: int = 3) -> dict:
    """
    Calculate Stochastic Oscillator (%K and %D)
    
    :param candles: np.ndarray of shape (n, 6) with OHLCV data
    :param period: int - period for calculating lowest low and highest high
    :param smooth_k: int - smoothing for %K line
    :param smooth_d: int - smoothing for %D line
    :return: dict containing %K and %D
    """
    high = candles[:, 2]
    low = candles[:, 3]
    close = candles[:, 4]

    lowest_low = np.full_like(close, np.nan)
    highest_high = np.full_like(close, np.nan)

    for i in range(period - 1, len(close)):
        lowest_low[i] = np.min(low[i - period + 1:i + 1])
        highest_high[i] = np.max(high[i - period + 1:i + 1])

    percent_k_raw = 100 * (close - lowest_low) / (highest_high - lowest_low)
    percent_k = np.convolve(percent_k_raw, np.ones(smooth_k)/smooth_k, mode='same')
    percent_d = np.convolve(percent_k, np.ones(smooth_d)/smooth_d, mode='same')

    return {
        "indicator": "stochastic",
        "period": period,
        "%K": percent_k[~np.isnan(percent_k)].tolist(),
        "%D": percent_d[~np.isnan(percent_d)].tolist()
    }
