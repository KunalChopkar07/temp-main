import numpy as np

def calculate_vpwma(candles: np.ndarray, period: int) -> dict:
    """
    Volume Price Weighted Moving Average (VPWMA)

    Formula:
        VPWMA = SUM(close * volume, period) / SUM(volume, period)

    :param candles: np.ndarray of shape (n, 6)
    :param period: int
    :return: dict containing VPWMA values
    """
    close = candles[:, 4]
    volume = candles[:, 5]
    
    vp = close * volume
    vpwma = np.full_like(close, fill_value=np.nan)

    for i in range(period - 1, len(close)):
        sum_vp = np.sum(vp[i - period + 1:i + 1])
        sum_vol = np.sum(volume[i - period + 1:i + 1])
        vpwma[i] = sum_vp / sum_vol if sum_vol != 0 else np.nan

    clean_vpwma = vpwma[~np.isnan(vpwma)]

    return {
        "indicator": "vpwma",
        "values": clean_vpwma.tolist()
    }
