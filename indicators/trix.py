import numpy as np

def calculate_trix(candles: np.ndarray, period: int = 15) -> dict:
    """
    Calculates the TRIX (Triple Exponential Average) indicator.

    :param candles: np.ndarray of OHLCV data
    :param period: period for smoothing
    :return: dict with TRIX values
    """
    close = candles[:, 4]

    def ema(series, p):
        alpha = 2 / (p + 1)
        result = np.zeros_like(series)
        result[0] = series[0]
        for i in range(1, len(series)):
            result[i] = alpha * series[i] + (1 - alpha) * result[i - 1]
        return result

    ema1 = ema(close, period)
    ema2 = ema(ema1, period)
    ema3 = ema(ema2, period)

    trix = np.zeros_like(ema3)
    trix[1:] = (ema3[1:] - ema3[:-1]) / ema3[:-1] * 100

    return {
        "indicator": "trix",
        "values": trix.tolist()
    }
