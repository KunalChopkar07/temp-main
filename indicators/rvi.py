import numpy as np

def calculate_rvi(candles: np.ndarray, period: int = 10) -> dict:
    """
    Calculates the Relative Vigor Index (RVI).

    Formula:
        RVI = (Close - Open) / (High - Low)

    The result is then smoothed with a simple moving average (SMA).

    :param candles: np.ndarray with shape (N, 6)
    :param period: Smoothing period
    :return: dict with smoothed RVI values
    """
    close = candles[:, 4]
    open_ = candles[:, 1]
    high = candles[:, 2]
    low = candles[:, 3]

    numerator = close - open_
    denominator = high - low
    denominator[denominator == 0] = np.nan  # avoid division by zero

    rvi_raw = numerator / denominator

    # Smooth using simple moving average
    def sma(values, p):
        return np.convolve(values, np.ones(p)/p, mode='valid')

    rvi_smooth = sma(rvi_raw, period)
    rvi_final = np.concatenate([np.full(period - 1, np.nan), rvi_smooth])

    return {
        "indicator": "rvi",
        "period": period,
        "values": rvi_final[~np.isnan(rvi_final)].tolist()
    }
