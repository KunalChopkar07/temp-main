import numpy as np
from jesse.helpers import get_candle_source, same_length

def cc(candles: np.ndarray, period: int = 20, source_type: str = "close", sequential: bool = False) -> np.ndarray:
    """
    Correlation Coefficient (CC)

    :param candles: np.ndarray
    :param period: int - default: 20
    :param source_type: str - default: "close"
    :param sequential: bool - default: False

    :return: np.ndarray
    """
    source = get_candle_source(candles, source_type)
    t = np.arange(1, period + 1)
    t_mean = np.mean(t)

    def calc_corr(i):
        y = source[i - period + 1:i + 1]
        y_mean = np.mean(y)
        num = np.sum((t - t_mean) * (y - y_mean))
        den = np.sqrt(np.sum((t - t_mean) ** 2) * np.sum((y - y_mean) ** 2))
        return num / den if den != 0 else 0

    result = np.full_like(source, fill_value=np.nan)
    for i in range(period - 1, source.shape[0]):
        result[i] = calc_corr(i)

    return result if sequential else result[-1]
