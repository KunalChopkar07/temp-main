import numpy as np

def calculate_mcginley_dynamic(candles: np.ndarray, period: int) -> dict:
    """
    McGinley Dynamic Indicator.
    Formula: MD[i] = MD[i-1] + (price[i] - MD[i-1]) / (k * (price[i] / MD[i-1])^4)
    """
    close = candles[:, 2]  # you may change to close price if needed ([:, 4])
    md = np.empty_like(close)
    md[:] = np.nan

    k = 1  # Smoothing constant; you may tune this

    md[period] = np.mean(close[:period])  # initialize first value

    for i in range(period + 1, len(close)):
        md[i] = md[i - 1] + (close[i] - md[i - 1]) / (k * ((close[i] / md[i - 1]) ** 4))

    clean_md = md[~np.isnan(md)]

    return {
        "indicator": "mcginley_dynamic",
        "values": clean_md.tolist()
    }
