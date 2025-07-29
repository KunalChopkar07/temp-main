import numpy as np

def calculate_vpt(candles: np.ndarray) -> dict:
    """
    Calculate Price Volume Trend (PVT).

    PVT = Previous PVT + Volume * ((Close - Previous Close) / Previous Close)

    :param candles: np.ndarray with OHLCV data
    :return: dict with PVT values
    """
    close = candles[:, 4]
    volume = candles[:, 5]
    pvt = np.zeros_like(close)
    
    for i in range(1, len(close)):
        prev_close = close[i - 1]
        if prev_close != 0:
            pvt[i] = pvt[i - 1] + volume[i] * ((close[i] - prev_close) / prev_close)
        else:
            pvt[i] = pvt[i - 1]

    clean_pvt = pvt[~np.isnan(pvt)]

    return {
        "indicator": "vpt",
        "values": clean_pvt.tolist()
    }
