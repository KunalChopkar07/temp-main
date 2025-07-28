import numpy as np

def calculate_gaps(candles: np.ndarray) -> dict:
    """
    Detects price gaps between consecutive candles.
    A gap is considered when the open of current candle is greater than the previous high
    or lower than the previous low.

    :param candles: np.ndarray with shape [N, 6] in OHLCV format
    :return: dict with gap_up and gap_down positions
    """
    highs = candles[:, 2]
    lows = candles[:, 3]
    opens = candles[:, 1]

    gap_up = []
    gap_down = []

    for i in range(1, len(candles)):
        if opens[i] > highs[i - 1]:
            gap_up.append(i)
        elif opens[i] < lows[i - 1]:
            gap_down.append(i)

    return {
        "indicator": "gaps",
        "gap_up_indices": gap_up,
        "gap_down_indices": gap_down
    }
