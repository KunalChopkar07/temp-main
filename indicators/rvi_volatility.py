import numpy as np

def calculate_rvi_volatility(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates the Relative Volatility Index (RVI) using standard deviation of close prices.

    :param candles: np.ndarray of OHLCV data
    :param period: lookback period
    :return: dict containing RVI values
    """
    close = candles[:, 2]  # Use high prices (some versions use close, others high/low)

    std = np.zeros_like(close)
    std[period:] = [np.std(close[i - period:i]) for i in range(period, len(close))]

    up = np.where(np.diff(close, prepend=close[0]) > 0, std, 0)
    down = np.where(np.diff(close, prepend=close[0]) < 0, std, 0)

    up_avg = np.convolve(up, np.ones(period), 'valid') / period
    down_avg = np.convolve(down, np.ones(period), 'valid') / period

    rvi = 100 * up_avg / (up_avg + down_avg + 1e-10)  # Avoid division by zero

    return {
        "indicator": "relative_volatility_index",
        "period": period,
        "values": rvi.tolist()
    }
