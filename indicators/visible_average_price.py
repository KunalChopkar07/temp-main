import numpy as np

def calculate_visible_average_price(candles: np.ndarray) -> dict:
    """
    Calculates the Visible Average Price (VAP) as the average of close prices over the visible range.

    :param candles: np.ndarray of shape (N, 6) — [timestamp, open, high, low, close, volume]
    :return: dict with the average price
    """
    close_prices = candles[:, 4]
    avg_price = np.nanmean(close_prices)

    return {
        "indicator": "visible_average_price",
        "average_price": float(avg_price)
    }
