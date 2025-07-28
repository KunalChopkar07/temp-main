import numpy as np

def calculate_smi_ergodic_oscillator(candles: np.ndarray, long_period: int = 25, short_period: int = 13, signal_period: int = 9) -> dict:
    """
    Calculates SMI Ergodic Oscillator.
    This is a version of the True Strength Index with a signal line.
    Each candle format: [timestamp, open, high, low, close, volume]

    :param candles: np.ndarray
    :param long_period: long EMA period
    :param short_period: short EMA period
    :param signal_period: signal line EMA period
    :return: dict with oscillator and signal line
    """
    close = candles[:, 4]
    momentum = np.diff(close, prepend=close[0])

    def ema(series, length):
        alpha = 2 / (length + 1)
        result = np.full_like(series, np.nan)
        result[length] = np.mean(series[:length])
        for i in range(length + 1, len(series)):
            result[i] = alpha * series[i] + (1 - alpha) * result[i - 1]
        return result

    ema1 = ema(momentum, short_period)
    ema2 = ema(ema1, long_period)

    abs_mom = np.abs(momentum)
    ema1_abs = ema(abs_mom, short_period)
    ema2_abs = ema(ema1_abs, long_period)

    tsi = np.where(ema2_abs != 0, 100 * ema2 / ema2_abs, 0)
    signal = ema(tsi, signal_period)

    clean_tsi = tsi[~np.isnan(tsi)]
    clean_signal = signal[~np.isnan(signal)]

    return {
        "indicator": "smi_ergodic_oscillator",
        "oscillator": clean_tsi.tolist(),
        "signal": clean_signal.tolist()
    }
