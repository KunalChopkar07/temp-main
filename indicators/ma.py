import numpy as np
from jesse.indicators.ma import ma

def calculate_ma(candles: np.ndarray, period: int, ma_type: str = 'sma') -> dict:
    """
    Calculates Moving Average of specified type (sma, ema, wma, etc.).

    :param candles: np.ndarray of OHLCV candles.
    :param period: Number of periods.
    :param ma_type: Type of MA: 'sma', 'ema', 'wma', etc.
    :return: dict with MA values.
    """
    values = ma(candles, period=period, ma_type=ma_type, sequential=True)

    return {
        "indicator": f"{ma_type}_ma",
        "period": period,
        "values": values[~np.isnan(values)].tolist()
    }
