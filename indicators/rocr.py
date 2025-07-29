import numpy as np

def calculate_rocr(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates Rate of Change Ratio (ROCR).
    
    Formula:
        ROCR = Close / Close_n

    :param candles: np.ndarray with shape (N, 6)
    :param period: lookback period
    :return: dict containing ROCR values
    """
    closes = candles[:, 4]
    prev_closes = np.roll(closes, period)
    rocr = closes / prev_closes
    rocr[:period] = np.nan

    return {
        "indicator": "rocr",
        "period": period,
        "values": rocr[~np.isnan(rocr)].tolist()
    }
