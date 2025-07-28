import numpy as np
from datetime import datetime, timezone

def calculate_trading_sessions(candles: np.ndarray) -> dict:
    """
    Identifies the trading session for each candle (Asian, London, New York)

    :param candles: np.ndarray with each row like [timestamp, open, high, low, close, volume]
    :return: dict mapping timestamps to sessions
    """
    session_mapping = []

    for candle in candles:
        timestamp = int(candle[0])
        dt = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)
        hour = dt.hour

        if 0 <= hour < 8:
            session = "Asian"
        elif 8 <= hour < 16:
            session = "London"
        else:
            session = "New York"

        session_mapping.append({
            "timestamp": timestamp,
            "datetime_utc": dt.isoformat(),
            "session": session
        })

    return {
        "indicator": "trading_sessions",
        "sessions": session_mapping
    }
