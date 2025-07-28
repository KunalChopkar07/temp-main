import numpy as np

def calculate_least_squares_moving_average(candles: np.ndarray, period: int) -> dict:
    """
    Calculates Least Squares Moving Average (LSMA) of the closing prices.
    
    :param candles: np.ndarray with shape (N, 6), where column 4 = close price
    :param period: Period over which LSMA is calculated
    :return: dict with indicator name and values
    """
    close = candles[:, 4]
    lsma_values = []

    for i in range(len(close)):
        if i + 1 < period:
            lsma_values.append(np.nan)
            continue

        y = close[i + 1 - period:i + 1]
        x = np.arange(1, period + 1)

        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        lsma = m * period + c
        lsma_values.append(lsma)

    return {
        "indicator": "least_squares_moving_average",
        "values": lsma_values
    }
