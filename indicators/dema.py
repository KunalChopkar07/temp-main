import numpy as np
from jesse.indicators.ema import ema

def calculate_dema(candles: np.ndarray, period: int) -> dict:
    """
    Calculate Double Exponential Moving Average (DEMA)

    :param candles: np.ndarray -> [timestamp, open, high, low, close, volume]
    :param period: int
    :return: dict
    """
    # First EMA of close prices
    first_ema = ema(candles, period=period, source_type="close", sequential=True)
    
    # Create a temporary candle array where the close price is replaced with the first EMA
    temp_candles = candles.copy()
    temp_candles[:, 2] = first_ema  # use high column temporarily for second EMA calc
    second_ema = ema(temp_candles, period=period, source_type="high", sequential=True)

    dema_values = 2 * first_ema - second_ema
    clean_dema = dema_values[~np.isnan(dema_values)]

    return {
        "indicator": "dema",
        "values": clean_dema.tolist()
    }
