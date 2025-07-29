import numpy as np

def calculate_smma(candles: np.ndarray, period: int) -> dict:
    """
    Calculate the Smoothed Moving Average (SMMA).
    
    :param candles: np.ndarray with shape (n, 6) - [timestamp, open, high, low, close, volume]
    :param period: int - period for smoothing
    :return: dict with SMMA values
    """
    close = candles[:, 4]
    smma = np.full_like(close, fill_value=np.nan)

    smma[period - 1] = np.mean(close[:period])
    for i in range(period, len(close)):
        smma[i] = (smma[i - 1] * (period - 1) + close[i]) / period

    return {
        "indicator": "smma",
        "period": period,
        "values": smma[~np.isnan(smma)].tolist()
    }
