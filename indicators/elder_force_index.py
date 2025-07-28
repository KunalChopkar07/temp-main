import numpy as np
from jesse.indicators.efi import efi

def calculate_elder_force_index(candles: np.ndarray, period: int) -> dict:
    """
    Calculates the Elder Force Index (EFI).

    :param candles: np.ndarray with shape [N, 6] in OHLCV format
    :param period: Lookback period
    :return: dict containing the EFI values
    """
    values = efi(candles, period=period, sequential=True)
    return {
        "indicator": "elder_force_index",
        "values": values[~np.isnan(values)].tolist()
    }
