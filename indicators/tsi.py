import numpy as np

def calculate_tsi(candles: np.ndarray, long: int = 25, short: int = 13) -> dict:
    """
    Calculates the True Strength Index (TSI).

    :param candles: np.ndarray of OHLCV data
    :param long: long EMA period (default 25)
    :param short: short EMA period (default 13)
    :return: dict with TSI values
    """
    close = candles[:, 4]

    momentum = np.diff(close, prepend=close[0])
    abs_momentum = np.abs(momentum)

    def ema(series, period):
        alpha = 2 / (period + 1)
        result = np.zeros_like(series)
        result[0] = series[0]
        for i in range(1, len(series)):
            result[i] = alpha * series[i] + (1 - alpha) * result[i - 1]
        return result

    # Double EMA
    ema1_mom = ema(momentum, short)
    ema2_mom = ema(ema1_mom, long)

    ema1_abs = ema(abs_momentum, short)
    ema2_abs = ema(ema1_abs, long)

    tsi = 100 * (ema2_mom / (ema2_abs + 1e-10))  # avoid division by zero

    return {
        "indicator": "true_strength_index",
        "values": tsi.tolist()
    }
