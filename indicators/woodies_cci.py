import numpy as np
from jesse.indicators.cci import cci

def calculate_woodies_cci(candles: np.ndarray, period: int = 14) -> dict:
    """
    Woodies CCI is a variation of Commodity Channel Index.
    This function returns both the CCI and a 'Turbo CCI' (shorter period) for plotting histogram.
    """
    normal_cci = cci(candles, period=period, sequential=True)
    turbo_cci = cci(candles, period=6, sequential=True)  # Turbo CCI typically uses 6-period

    # Clean NaNs
    clean_cci = normal_cci[~np.isnan(normal_cci)]
    clean_turbo = turbo_cci[~np.isnan(turbo_cci)]

    return {
        "indicator": "woodies_cci",
        "period": period,
        "cci": clean_cci.tolist(),
        "turbo_cci": clean_turbo.tolist()
    }
