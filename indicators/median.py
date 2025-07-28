import numpy as np

def calculate_median(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the median price over a rolling window.

    Median = (High + Low) / 2
    """
    high = candles[:, 2]
    low = candles[:, 3]
    median_price = (high + low) / 2

    result = np.full_like(median_price, np.nan)
    
    for i in range(period - 1, len(median_price)):
        result[i] = np.median(median_price[i - period + 1:i + 1])
    
    clean_median = result[~np.isnan(result)]

    return {
        "indicator": "median",
        "values": clean_median.tolist()
    }
