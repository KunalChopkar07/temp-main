import numpy as np
from jesse.indicators.fisher import fisher

def calculate_fisher(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Fisher Transform indicator.

    :param candles: np.ndarray with shape (n, 6)
    :param period: Lookback period for the Fisher calculation
    :return: dict with indicator name and values
    """
    fisher_values = fisher(candles, period=period, sequential=True)
    clean_fisher = fisher_values[~np.isnan(fisher_values)]

    return {
        "indicator": "fisher_transform",
        "values": clean_fisher.tolist()
    }
