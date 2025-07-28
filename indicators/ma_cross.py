import numpy as np
from jesse.indicators import sma

def calculate_ma_cross(candles: np.ndarray, fast_period: int, slow_period: int) -> dict:
    """
    Calculates the crossover between two simple moving averages (fast and slow).
    """
    close = candles[:, 2]  # you may also use candles[:, 4] for 'close'
    fast_ma = sma(candles, period=fast_period, source_type="close", sequential=True)
    slow_ma = sma(candles, period=slow_period, source_type="close", sequential=True)

    signals = []
    for i in range(1, len(close)):
        if np.isnan(fast_ma[i]) or np.isnan(slow_ma[i]):
            signals.append(None)
        elif fast_ma[i - 1] < slow_ma[i - 1] and fast_ma[i] > slow_ma[i]:
            signals.append("bullish_cross")
        elif fast_ma[i - 1] > slow_ma[i - 1] and fast_ma[i] < slow_ma[i]:
            signals.append("bearish_cross")
        else:
            signals.append(None)

    return {
        "indicator": "ma_cross",
        "fast_ma": fast_ma[~np.isnan(fast_ma)].tolist(),
        "slow_ma": slow_ma[~np.isnan(slow_ma)].tolist(),
        "signals": signals
    }
