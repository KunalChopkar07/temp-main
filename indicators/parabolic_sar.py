import numpy as np
from jesse.indicators import sar

def calculate_parabolic_sar(candles: np.ndarray) -> dict:
    sar_values = sar(candles, sequential=True)
    clean_sar = sar_values[~np.isnan(sar_values)]
    
    return {
        "indicator": "parabolic_sar",
        "values": clean_sar.tolist()
    }
