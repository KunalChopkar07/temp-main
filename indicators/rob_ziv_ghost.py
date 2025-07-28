import numpy as np

def calculate_rob_ziv_ghost(candles: np.ndarray) -> dict:
    """
    Mocked Ziv Ghost Pivot – gap-based reversal signal.

    :param candles: np.ndarray
    """
    if len(candles) < 2:
        return {"indicator": "rob_ziv_ghost", "signal": "insufficient data"}

    prev_close = candles[-2, 4]
    open_price = candles[-1, 1]

    gap = (open_price - prev_close) / prev_close * 100

    if abs(gap) > 1:
        signal = "ghost_pivot_possible"
    else:
        signal = "none"

    return {
        "indicator": "rob_ziv_ghost",
        "gap_percent": round(gap, 2),
        "signal": signal
    }
