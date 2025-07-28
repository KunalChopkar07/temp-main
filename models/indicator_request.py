from pydantic import BaseModel

class IndicatorRequest(BaseModel):
    symbol: str     # e.g., "BTCUSDT"
    interval: str   # e.g., "5m", "1h"
    period: int     # e.g., 20
    limit: int = 100  # default number of candles
    
class NoPeriodIndicatorRequest(BaseModel):
    symbol: str          # e.g., "BTCUSDT"
    interval: str        # e.g., "1h"
    limit: int = 100     # default candle limit

class ADOSCRequest(BaseModel):
    symbol: str
    interval: str
    fast_period: int = 3
    slow_period: int = 10
    limit: int = 100

class CKSPRequest(BaseModel):
    symbol: str
    interval: str
    p: int = 10
    x: float = 1.0
    q: int = 9
    limit: int = 100

class CHOPRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 14
    scalar: float = 100
    drift: int = 1
    limit: int = 100

class CorrelRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 5
    limit: int = 100

class NoPeriodIndicatorRequest(BaseModel):
    symbol: str
    interval: str
    limit: int

class VolumeOscillatorRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    short_period: int
    long_period: int    
    
class VolatilityStopRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    period: int
    multiplier: float
    
class NoPeriodIndicatorRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    
class NoPeriodIndicatorRequest(BaseModel):
    symbol: str
    interval: str
    limit: int


class MACrossRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    fast_period: int
    slow_period: int
    
class IndicatorRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    period: int
    
    
class MultiTimeframeRequest(BaseModel):
    symbol: str
    interval: str
    limit: int
    higher_interval: str
    period: int
    
    
    
    
class DPORequest(BaseModel):
    symbol: str
    interval: str
    period: int = 20
    limit: int = 100
class EMARequest(BaseModel):
    symbol: str
    interval: str
    period: int = 20
    limit: int = 100    
class KSTRequest(BaseModel):
    symbol: str
    interval: str
    roc1: int = 10
    roc2: int = 15
    roc3: int = 20
    roc4: int = 30
    sma1: int = 10
    sma2: int = 10
    sma3: int = 10
    sma4: int = 15
    limit: int = 100    
class MACDRequest(BaseModel):
    symbol: str
    interval: str
    fast_period: int = 12
    slow_period: int = 26
    signal_period: int = 9
    limit: int = 100
class MFIRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 14
    limit: int = 100
class NoPeriodIndicatorRequest(BaseModel):
    symbol: str
    interval: str
    limit: int = 100
class OBVRequest(BaseModel):
    symbol: str
    interval: str
    limit: int = 100
class RSIRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 14
    limit: int = 100
class StochasticRequest(BaseModel):
    symbol: str
    interval: str
    k_period: int = 14
    d_period: int = 3
    smooth_k: int = 3
    limit: int = 100
class StochasticRSIRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 14
    k_period: int = 14
    d_period: int = 3
    smooth_k: int = 3
    limit: int = 100
class TEMARequest(BaseModel):
    symbol: str
    interval: str
    period: int = 20
    limit: int = 100
class TRIXRequest(BaseModel):
    symbol: str
    interval: str
    period: int = 15
    limit: int = 100
class VWAPRequest(BaseModel):
    symbol: str
    interval: str
    limit: int = 100

