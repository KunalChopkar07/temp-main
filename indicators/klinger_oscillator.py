import numpy as np

def calculate_klinger_oscillator(candles: np.ndarray, short_period: int = 34, long_period: int = 55, signal_period: int = 13) -> dict:
    """
    Calculates the Klinger Oscillator and its signal line.

    :param candles: np.ndarray with columns [timestamp, open, high, low, close, volume]
    :param short_period: short EMA period
    :param long_period: long EMA period
    :param signal_period: signal EMA period
    :return: dict with oscillator and signal
    """
    high = candles[:, 2]
    low = candles[:, 3]
    close = candles[:, 4]
    volume = candles[:, 5]

    typical_price = (high + low + close) / 3
    dm = high - low
    trend = np.where(typical_price > np.roll(typical_price, 1), 1, -1)
    trend[0] = 1  # first value default

    vf = volume * trend * dm

    def ema(values, period):
        result = np.empty_like(values)
        alpha = 2 / (period + 1)
        result[0] = values[0]
        for i in range(1, len(values)):
            result[i] = alpha * values[i] + (1 - alpha) * result[i - 1]
        return result

    kvo = ema(vf, short_period) - ema(vf, long_period)
    signal = ema(kvo, signal_period)

    return {
        "indicator": "klinger_oscillator",
        "kvo": kvo.tolist(),
        "signal": signal.tolist()
    }
