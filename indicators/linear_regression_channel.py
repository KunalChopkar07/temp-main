import numpy as np

def calculate_linear_regression_channel(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Linear Regression Channel (LRC).
    
    :param candles: np.ndarray with shape (N, 6), column 4 = close price
    :param period: Number of periods for regression
    :return: dict with upper, middle, lower bands
    """
    close = candles[:, 4]
    upper, middle, lower = [], [], []

    for i in range(len(close)):
        if i + 1 < period:
            upper.append(np.nan)
            middle.append(np.nan)
            lower.append(np.nan)
            continue

        y = close[i + 1 - period:i + 1]
        x = np.arange(period)

        A = np.vstack([x, np.ones(period)]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        reg_line = m * x + c

        middle.append(reg_line[-1])
        deviation = np.std(y - reg_line)
        upper.append(reg_line[-1] + deviation)
        lower.append(reg_line[-1] - deviation)

    return {
        "indicator": "linear_regression_channel",
        "upper": upper,
        "middle": middle,
        "lower": lower
    }

