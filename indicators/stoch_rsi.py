import numpy as np
from indicators.rsi import calculate_rsi

def calculate_stoch_rsi(candles: np.ndarray, period: int = 14) -> dict:
    rsi = calculate_rsi(candles, period)
    rsi = np.array(rsi)
    stoch_rsi = np.full_like(rsi, fill_value=np.nan)

    for i in range(period, len(rsi)):
        min_rsi = np.min(rsi[i - period:i])
        max_rsi = np.max(rsi[i - period:i])
        if max_rsi - min_rsi == 0:
            stoch_rsi[i] = 0
        else:
            stoch_rsi[i] = (rsi[i] - min_rsi) / (max_rsi - min_rsi)

    clean_stoch_rsi = stoch_rsi[~np.isnan(stoch_rsi)]

    return {
        "indicator": "stoch_rsi",
        "values": clean_stoch_rsi.tolist()
    }
