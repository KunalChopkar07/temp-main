import numpy as np

def calculate_rci(candles: np.ndarray, period: int) -> dict:
    """
    Calculate Rank Correlation Index (RCI).
    
    :param candles: np.ndarray - OHLCV candles
    :param period: int - lookback period
    :return: dict with indicator name and values
    """
    close_prices = candles[:, 4]
    length = len(close_prices)

    if length < period:
        return {
            "indicator": "rci",
            "values": []
        }

    rci_values = []

    for i in range(period - 1, length):
        close_slice = close_prices[i - period + 1:i + 1]
        price_ranks = close_slice.argsort().argsort() + 1  # 1-based ranks
        time_ranks = np.arange(1, period + 1)

        d = price_ranks - time_ranks
        d_squared_sum = np.sum(d ** 2)

        rci = (1 - (6 * d_squared_sum) / (period * (period**2 - 1))) * 100
        rci_values.append(rci)

    # pad the beginning with NaNs for consistent array length
    full_rci = [np.nan] * (period - 1) + rci_values

    return {
        "indicator": "rci",
        "values": full_rci
    }
