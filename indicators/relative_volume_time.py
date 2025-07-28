import numpy as np

def calculate_relative_volume_at_time(candles: np.ndarray, interval: str) -> dict:
    """
    Calculates the Relative Volume at Time.
    
    :param candles: np.ndarray with shape (n, 6) - [timestamp, open, high, low, close, volume]
    :param interval: string like '1m', '5m'
    :return: dict with relative volumes
    """
    from datetime import datetime
    import pandas as pd

    if interval not in ['1m', '5m', '15m']:
        raise ValueError("Interval must be 1m, 5m, or 15m for time-based analysis.")

    # Convert to DataFrame
    df = pd.DataFrame(candles, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["time"] = df["datetime"].dt.time
    df["date"] = df["datetime"].dt.date

    # Group by time slot across days and compute average
    avg_volume_by_time = df.groupby("time")["volume"].mean()

    # Get today’s date
    today = df["date"].iloc[-1]
    today_df = df[df["date"] == today]

    # Align with average
    today_df = today_df[today_df["time"].isin(avg_volume_by_time.index)]
    relative_volume = today_df["volume"].values / avg_volume_by_time.loc[today_df["time"]].values

    return {
        "indicator": "relative_volume_at_time",
        "times": today_df["time"].astype(str).tolist(),
        "relative_volume": relative_volume.tolist()
    }
