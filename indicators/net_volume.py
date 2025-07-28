import numpy as np

def calculate_net_volume(candles: np.ndarray) -> dict:
    """
    Net Volume = Volume on Up Days - Volume on Down Days
    Based on closing price comparison to previous candle.
    """
    close = candles[:, 4]
    volume = candles[:, 5]

    net_volumes = np.zeros_like(volume)

    for i in range(1, len(candles)):
        if close[i] > close[i - 1]:
            net_volumes[i] = volume[i]
        elif close[i] < close[i - 1]:
            net_volumes[i] = -volume[i]
        else:
            net_volumes[i] = 0

    net_volumes_clean = net_volumes[~np.isnan(net_volumes)]

    return {
        "indicator": "net_volume",
        "values": net_volumes_clean.tolist()
    }
