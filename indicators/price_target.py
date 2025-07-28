import numpy as np

def calculate_price_target(candles: np.ndarray) -> dict:
    close = candles[:, 2]  # Close price
    target_up = close[-1] * 1.05  # +5%
    target_down = close[-1] * 0.95  # -5%

    return {
        "indicator": "price_target",
        "current_price": float(close[-1]),
        "target_up": round(float(target_up), 2),
        "target_down": round(float(target_down), 2)
    }
