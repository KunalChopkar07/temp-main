import numpy as np
import datetime

def calculate_seasonality(candles: np.ndarray) -> dict:
    """
    Calculate average % return by weekday (Monday-Sunday) for seasonality analysis.

    :param candles: np.ndarray - OHLCV candles
    :return: dict - average return grouped by weekday
    """
    timestamps = candles[:, 0].astype(np.int64)  # milliseconds
    closes = candles[:, 4].astype(np.float64)

    returns_by_day = {i: [] for i in range(7)}  # 0=Monday ... 6=Sunday

    for i in range(1, len(candles)):
        prev_close = closes[i - 1]
        current_close = closes[i]

        if prev_close == 0:
            continue

        ret = (current_close - prev_close) / prev_close * 100  # % return
        day = datetime.datetime.utcfromtimestamp(timestamps[i] / 1000).weekday()
        returns_by_day[day].append(ret)

    average_returns = {
        "Monday": np.mean(returns_by_day[0]) if returns_by_day[0] else 0,
        "Tuesday": np.mean(returns_by_day[1]) if returns_by_day[1] else 0,
        "Wednesday": np.mean(returns_by_day[2]) if returns_by_day[2] else 0,
        "Thursday": np.mean(returns_by_day[3]) if returns_by_day[3] else 0,
        "Friday": np.mean(returns_by_day[4]) if returns_by_day[4] else 0,
        "Saturday": np.mean(returns_by_day[5]) if returns_by_day[5] else 0,
        "Sunday": np.mean(returns_by_day[6]) if returns_by_day[6] else 0,
    }

    return {
        "indicator": "seasonality",
        "average_weekday_returns": average_returns
    }
