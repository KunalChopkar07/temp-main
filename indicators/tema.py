import numpy as np
from jesse.indicators.ema import ema

def calculate_tema(candles: np.ndarray, period: int) -> dict:
    """
    Triple Exponential Moving Average (TEMA)

    :param candles: np.ndarray with shape (n, 6)
    :param period: int - lookback period
    :return: dict with TEMA values
    """
    close = candles[:, 4]

    ema1 = ema(candles, period=period, source_type="close", sequential=True)
    ema2 = ema(np.column_stack([candles[:, 0], ema1, ema1, ema1, ema1, candles[:, 5]]), period=period, source_type="close", sequential=True)
    ema3 = ema(np.column_stack([candles[:, 0], ema2, ema2, ema2, ema2, candles[:, 5]]), period=period, source_type="close", sequential=True)

    tema = 3 * (ema1 - ema2) + ema3
    clean_tema = tema[~np.isnan(tema)]

    return {
        "indicator": "tema",
        "period": period,
        "values": clean_tema.tolist()
    }
