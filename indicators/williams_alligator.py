import numpy as np
from jesse.indicators.smma import smma

def calculate_williams_alligator(candles: np.ndarray) -> dict:
    """
    Calculates the Williams Alligator indicator: Jaw, Teeth, Lips.

    :param candles: OHLCV np.ndarray
    :return: dict with jaw, teeth, lips
    """
    close = candles[:, 2]  # Use HIGH for more sensitivity or close for basic calc

    jaw = smma(close, period=13, sequential=True)
    teeth = smma(close, period=8, sequential=True)
    lips = smma(close, period=5, sequential=True)

    # Replace NaNs and shift
    jaw_shifted = np.roll(jaw, 8)
    teeth_shifted = np.roll(teeth, 5)
    lips_shifted = np.roll(lips, 3)

    return {
        "indicator": "williams_alligator",
        "jaw": jaw_shifted[~np.isnan(jaw_shifted)].tolist(),
        "teeth": teeth_shifted[~np.isnan(teeth_shifted)].tolist(),
        "lips": lips_shifted[~np.isnan(lips_shifted)].tolist()
    }
