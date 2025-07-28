import numpy as np

def calculate_historical_volatility(candles: np.ndarray, period: int = 14) -> dict:
    """
    Calculates Historical Volatility (annualized standard deviation of log returns).

    :param candles: np.ndarray with OHLCV format
    :param period: period to calculate HV
    :return: dict with historical volatility values
    """
    close_prices = candles[:, 4]
    log_returns = np.diff(np.log(close_prices))

    # rolling std of log returns
    hv = np.full_like(close_prices, fill_value=np.nan)
    for i in range(period, len(log_returns)):
        std = np.std(log_returns[i - period:i], ddof=1)
        hv[i + 1] = std * np.sqrt(252) * 100  # Annualized (%)

    return {
        "indicator": "historical_volatility",
        "period": period,
        "values": hv.tolist()
    }


