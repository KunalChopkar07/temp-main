import numpy as np

def calculate_zigzag(candles: np.ndarray, change: float = 5.0) -> dict:
    """
    Simple Zig Zag implementation based on close price and percentage change.
    """
    closes = candles[:, 4]
    length = len(closes)

    pivots = [np.nan] * length
    direction = None
    last_pivot = closes[0]

    for i in range(1, length):
        pct_change = ((closes[i] - last_pivot) / last_pivot) * 100

        if direction is None:
            if abs(pct_change) >= change:
                direction = "up" if pct_change > 0 else "down"
                pivots[i] = closes[i]
                last_pivot = closes[i]
        elif direction == "up":
            if closes[i] > last_pivot:
                pivots[i - 1] = np.nan  # remove previous pivot
                pivots[i] = closes[i]
                last_pivot = closes[i]
            elif pct_change <= -change:
                direction = "down"
                pivots[i] = closes[i]
                last_pivot = closes[i]
        elif direction == "down":
            if closes[i] < last_pivot:
                pivots[i - 1] = np.nan
                pivots[i] = closes[i]
                last_pivot = closes[i]
            elif pct_change >= change:
                direction = "up"
                pivots[i] = closes[i]
                last_pivot = closes[i]

    # Clean NaNs
    clean_zigzag = [p for p in pivots if not np.isnan(p)]

    return {
        "indicator": "zig_zag",
        "change": change,
        "values": clean_zigzag
    }
