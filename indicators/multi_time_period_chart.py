import numpy as np
from jesse.indicators import sma
from services.binance_service import fetch_candles

async def calculate_multi_timeframe_sma(symbol: str, interval: str, limit: int, higher_interval: str, period: int) -> dict:
    """
    Calculate SMA from a higher timeframe and map it for a lower timeframe chart.
    """
    # Fetch candles from higher timeframe
    higher_candles = await fetch_candles(symbol, higher_interval, limit)
    sma_values = sma(higher_candles, period=period, sequential=True)

    clean = sma_values[~np.isnan(sma_values)]

    return {
        "indicator": "multi_timeframe_sma",
        "symbol": symbol.upper(),
        "interval": interval,
        "mapped_from": higher_interval,
        "period": period,
        "values": clean.tolist()
    }
