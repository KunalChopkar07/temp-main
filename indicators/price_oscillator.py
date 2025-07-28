import numpy as np
from jesse.indicators import apo

def calculate_price_oscillator(candles: np.ndarray) -> dict:
    result = apo(candles, sequential=True)
    clean = result[~np.isnan(result)]
    
    return {
        "indicator": "price_oscillator",
        "values": clean.tolist()
    }
