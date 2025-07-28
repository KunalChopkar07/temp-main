import numpy as np

def calculate_price_volume_trend(candles: np.ndarray) -> dict:
    close = candles[:, 2]
    volume = candles[:, 5]

    pvt = np.zeros_like(close)
    for i in range(1, len(close)):
        pct_change = (close[i] - close[i - 1]) / close[i - 1]
        pvt[i] = pvt[i - 1] + volume[i] * pct_change

    return {
        "indicator": "price_volume_trend",
        "values": pvt.tolist()
    }
