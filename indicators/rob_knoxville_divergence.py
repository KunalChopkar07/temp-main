import numpy as np
from jesse.indicators.rsi import rsi
from jesse.indicators.macd import macd

def calculate_rob_knoxville_divergence(candles: np.ndarray) -> dict:
    """
    Simulated Knoxville Divergence using MACD histogram and RSI.

    :param candles: np.ndarray
    """
    macd_result = macd(candles, fast_period=12, slow_period=26, signal_period=9, sequential=True)
    rsi_values = rsi(candles, period=14, sequential=True)

    # Simple divergence condition (mock logic)
    divergence = np.where((macd_result.hist > 0) & (rsi_values > 70), 1,
                          np.where((macd_result.hist < 0) & (rsi_values < 30), -1, 0))

    return {
        "indicator": "rob_knoxville_divergence",
        "divergence_signal": divergence.tolist()
    }

