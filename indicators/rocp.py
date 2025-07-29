import numpy as np

def calculate_rocp(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates Rate of Change Percentage (ROCP).

    Formula:
        ROCP = (Close - Close_n) / Close_n

    :param candles: np.ndarray with shape (N, 6)
    :param period: Number of periods back to compare
    :return: dict containing ROCP values
    """
    closes = candles[:, 4]
    rocp = (closes - np.roll(closes, period)) / np.roll(closes, period)
    rocp[:period] = np.nan

    return {
        "indicator": "rocp",
        "period": period,
        "values": rocp[~np.isnan(rocp)].tolist()
    }
