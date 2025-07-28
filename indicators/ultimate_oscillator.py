import numpy as np

def calculate_ultimate_oscillator(candles: np.ndarray, short: int = 7, medium: int = 14, long: int = 28) -> dict:
    """
    Calculates the Ultimate Oscillator (UO).

    :param candles: np.ndarray of shape (N, 6) — OHLCV candles
    :param short: short period (default 7)
    :param medium: medium period (default 14)
    :param long: long period (default 28)
    :return: dict with UO values
    """
    high = candles[:, 2]
    low = candles[:, 3]
    close = candles[:, 4]

    # Previous close
    prev_close = np.roll(close, 1)
    prev_close[0] = close[0]  # avoid bad diff on first candle

    # Buying Pressure (BP) and True Range (TR)
    bp = close - np.minimum(low, prev_close)
    tr = np.maximum(high, prev_close) - np.minimum(low, prev_close)

    # Avoid division by zero
    tr = np.where(tr == 0, 1e-10, tr)

    # Rolling sums
    def avg_bp_tr(period):
        sum_bp = np.convolve(bp, np.ones(period), 'valid')
        sum_tr = np.convolve(tr, np.ones(period), 'valid')
        return sum_bp / sum_tr

    uo_short = avg_bp_tr(short)
    uo_medium = avg_bp_tr(medium)
    uo_long = avg_bp_tr(long)

    # Align lengths
    min_len = min(len(uo_short), len(uo_medium), len(uo_long))
    uo = 100 * ((4 * uo_short[-min_len:] + 2 * uo_medium[-min_len:] + uo_long[-min_len:]) / 7)

    return {
        "indicator": "ultimate_oscillator",
        "values": uo.tolist()
    }
