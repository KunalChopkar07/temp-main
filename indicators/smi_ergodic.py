import numpy as np

def calculate_smi_ergodic(candles: np.ndarray, long_period: int = 25, short_period: int = 13, signal_period: int = 9) -> dict:
    """
    Calculates the SMI Ergodic Indicator.
    Similar to True Strength Index (TSI), it includes a signal line.

    :param candles: np.ndarray of candles (timestamp, open, high, low, close, volume)
    :param long_period: int, slow EMA period
    :param short_period: int, fast EMA period
    :param signal_period: int, signal EMA period
    :return: dict with SMI and signal
    """
    close = candles[:, 4]
    momentum = np.diff(close, prepend=close[0])

    def ema(series: np.ndarray, length: int) -> np.ndarray:
        alpha = 2 / (length + 1)
        result = np.full_like(series, fill_value=np.nan)
        result[length] = np.mean(series[:length])
        for i in range(length + 1, len(series)):
            result[i] = alpha * series[i] + (1 - alpha) * result[i - 1]
        return result

    ema1 = ema(momentum, short_period)
    ema2 = ema(ema1, long_period)

    abs_mom = np.abs(momentum)
    ema1_abs = ema(abs_mom, short_period)
    ema2_abs = ema(ema1_abs, long_period)

    smi = np.where(ema2_abs != 0, 100 * ema2 / ema2_abs, 0)
    signal = ema(smi, signal_period)

    return {
        "indicator": "smi_ergodic",
        "smi": smi[~np.isnan(smi)].tolist(),
        "signal": signal[~np.isnan(signal)].tolist()
    }
