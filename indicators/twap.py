import numpy as np

def calculate_twap(candles: np.ndarray) -> dict:
    """
    Calculates the Time Weighted Average Price (TWAP).

    Each candle must be of the format: [timestamp, open, high, low, close, volume]

    TWAP = sum(close prices) / number of periods

    :param candles: np.ndarray of candles
    :return: dict with TWAP value
    """
    close_prices = candles[:, 4]  # close is at index 4
    twap_value = np.nanmean(close_prices)

    return {
        "indicator": "twap",
        "twap": float(twap_value)
    }
