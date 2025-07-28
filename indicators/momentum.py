import numpy as np

def calculate_momentum(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Momentum indicator.

    Momentum = Close - Close[n-period]
    """
    close = candles[:, 4]
    momentum = np.full_like(close, np.nan)

    for i in range(period, len(close)):
        momentum[i] = close[i] - close[i - period]

    clean_momentum = momentum[~np.isnan(momentum)]

    return {
        "indicator": "momentum",
        "values": clean_momentum.tolist()
    }
