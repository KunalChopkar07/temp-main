import numpy as np

def calculate_parabolic_sar(candles: np.ndarray, step: float = 0.02, max_step: float = 0.2) -> dict:
    """
    Calculate the Parabolic SAR indicator.
    
    :param candles: np.ndarray of shape (n, 6) with OHLCV format
    :param step: Acceleration factor step (default 0.02)
    :param max_step: Maximum acceleration factor (default 0.2)
    :return: dict with SAR values
    """
    high = candles[:, 2]
    low = candles[:, 3]
    close = candles[:, 4]
    length = len(close)

    sar = np.zeros(length)
    trend = 1  # 1 = uptrend, -1 = downtrend
    af = step
    ep = low[0]  # extreme point
    sar[0] = low[0] - (high[0] - low[0])

    for i in range(1, length):
        prev_sar = sar[i - 1]
        if trend == 1:
            sar[i] = prev_sar + af * (ep - prev_sar)
            if low[i] < sar[i]:
                trend = -1
                sar[i] = ep
                ep = low[i]
                af = step
            else:
                if high[i] > ep:
                    ep = high[i]
                    af = min(af + step, max_step)
        else:
            sar[i] = prev_sar + af * (ep - prev_sar)
            if high[i] > sar[i]:
                trend = 1
                sar[i] = ep
                ep = high[i]
                af = step
            else:
                if low[i] < ep:
                    ep = low[i]
                    af = min(af + step, max_step)

    return {
        "indicator": "parabolic_sar",
        "sar": sar.tolist()
    }
