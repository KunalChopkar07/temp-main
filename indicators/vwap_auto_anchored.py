import numpy as np
import pandas as pd

def calculate_vwap_auto_anchored(candles: np.ndarray) -> dict:
    """
    VWAP anchored from start of day (auto reset when date changes).

    :param candles: np.ndarray of shape (N, 6) - [timestamp, open, high, low, close, volume]
    :return: dict with auto-anchored VWAP values
    """
    timestamps = candles[:, 0]
    high = candles[:, 2]
    low = candles[:, 3]
    close = candles[:, 4]
    volume = candles[:, 5]

    # Convert timestamps to pandas datetime
    datetimes = pd.to_datetime(timestamps, unit='ms')
    dates = datetimes.date

    typical_price = (high + low + close) / 3
    tpv = typical_price * volume

    df = pd.DataFrame({
        "date": dates,
        "tpv": tpv,
        "volume": volume
    })

    # Compute cumulative sums grouped by day (auto anchoring)
    df["cum_tpv"] = df.groupby("date")["tpv"].cumsum()
    df["cum_volume"] = df.groupby("date")["volume"].cumsum()
    df["vwap"] = df["cum_tpv"] / df["cum_volume"]

    return {
        "indicator": "vwap_auto_anchored",
        "vwap": df["vwap"].fillna(0).tolist()
    }
