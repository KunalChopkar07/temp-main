import numpy as np

def calculate_smi(candles: np.ndarray, period: int = 14, smoothing_period: int = 3) -> dict:
    """
    Calculate Stochastic Momentum Index (SMI)
    Formula source: common trading logic
    Each candle: [timestamp, open, high, low, close, volume]

    :param candles: np.ndarray
    :param period: int - SMI calculation period
    :param smoothing_period: int - smoothing factor
    :return: dict with SMI and signal values
    """
    high = candles[:, 2]
    low = candles[:, 3]
    close = candles[:, 4]

    center = (high + low) / 2
    h_l = high - low
    diff = close - center

    def ema(x, length):
        alpha = 2 / (length + 1)
        ema = np.full_like(x, np.nan)
        ema[length] = np.mean(x[:length])
        for i in range(length + 1, len(x)):
            ema[i] = alpha * x[i] + (1 - alpha) * ema[i - 1]
        return ema

    avg_diff = ema(diff, smoothing_period)
    avg_range = ema(h_l, smoothing_period)

    smi = np.full_like(avg_diff, np.nan)
    for i in range(len(avg_diff)):
        if avg_range[i] != 0:
            smi[i] = 100 * (avg_diff[i] / (avg_range[i] / 2))

    # Signal line (3-period EMA of SMI)
    signal = ema(smi, 3)

    clean_smi = smi[~np.isnan(smi)]
    clean_signal = signal[~np.isnan(signal)]

    return {
        "indicator": "stochastic_momentum_index",
        "smi": clean_smi.tolist(),
        "signal": clean_signal.tolist()
    }

