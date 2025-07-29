import numpy as np

def calculate_rocr100(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates Rate of Change Ratio (ROCR100).

    Formula:
        ROCR100 = (Close / Close_n) * 100

    :param candles: np.ndarray with shape (N, 6)
    :param period: lookback period
    :return: dict containing ROCR100 values
    """
    closes = candles[:, 4]
    prev_closes = np.roll(closes, period)
    rocr100 = (closes / prev_closes) * 100
    rocr100[:period] = np.nan

    return {
        "indicator": "rocr100",
        "period": period,
        "values": rocr100[~np.isnan(rocr100)].tolist()
    }
