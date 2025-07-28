from fastapi import FastAPI, HTTPException

from models.indicator_request import IndicatorRequest
from models.indicator_request import NoPeriodIndicatorRequest
from models.indicator_request import ADOSCRequest
from indicators.cksp import cksp
from indicators.chop import chop
from indicators.correl import correl

from services.binance_service import fetch_candles
from indicators.sma import calculate_sma
from indicators.rsi import calculate_rsi
from indicators.ema import calculate_ema
from indicators.macd import calculate_macd
from indicators.bollinger import calculate_bollinger
from indicators.atr import calculate_atr
from indicators.supertrend import calculate_supertrend
from indicators.vwap import calculate_vwap
from indicators.adx import calculate_adx
from indicators.cci import calculate_cci
from indicators.williams import calculate_williams_r
from indicators.roc import calculate_roc
from indicators.cmo import calculate_cmo
from indicators.apo import calculate_apo
from indicators.ppo import calculate_ppo
from indicators.mfi import calculate_mfi
from indicators.coppock import calculate_coppock
from indicators.donchian import calculate_donchian
from indicators.obv import calculate_obv
from indicators.efi import calculate_efi

from indicators.volume24h import calculate_volume24h
from indicators.zig_zag import calculate_zigzag
from indicators.woodies_cci import calculate_woodies_cci
from indicators.williams_r import calculate_williams_r
from indicators.williams_fractals import calculate_williams_fractals
from indicators.williams_alligator import calculate_williams_alligator
from indicators.vwap_auto_anchored import calculate_vwap_auto_anchored
from indicators.vortex import calculate_vortex
from indicators.vwma import calculate_vwma
from indicators.volume_oscillator import calculate_volume_oscillator
from indicators.volume_delta import calculate_volume_delta
from indicators.volatility_stop import calculate_volatility_stop
from indicators.visible_average_price import calculate_visible_average_price
from indicators.up_down_volume import calculate_up_down_volume
from indicators.ultimate_oscillator import calculate_ultimate_oscillator
from indicators.tsi import calculate_tsi
from indicators.trix import calculate_trix
from indicators.trading_sessions import calculate_trading_sessions
from indicators.twap import calculate_twap
from indicators.technical_ratings import calculate_technical_rating
from indicators.stoch_rsi import calculate_stoch_rsi
from indicators.smi import calculate_smi
from indicators.smi_ergodic_oscillator import calculate_smi_ergodic_oscillator
from indicators.smi_ergodic import calculate_smi_ergodic
from indicators.seasonality import calculate_seasonality
from indicators.rci import calculate_rci
from indicators.rci_ribbon import calculate_rci_ribbon
from indicators.rvi_volatility import calculate_rvi_volatility
from indicators.relative_volume_time import calculate_relative_volume_at_time
from indicators.rob_intraday_pivot import calculate_rob_intraday_pivot
from indicators.rob_knoxville_divergence import calculate_rob_knoxville_divergence
from indicators.rob_missed_pivots import calculate_rob_missed_pivots
from indicators.rob_reversal import calculate_rob_reversal
from indicators.rob_ziv_ghost import calculate_rob_ziv_ghost
from indicators.parabolic_sar import calculate_parabolic_sar
from indicators.performance import calculate_performance
from indicators.pivot_points_high_low import calculate_pivot_points_high_low
from indicators.pivot_points_standard import calculate_pivot_points_standard
from indicators.price_oscillator import calculate_price_oscillator
from indicators.price_target import calculate_price_target
from indicators.price_volume_trend import calculate_price_volume_trend
from indicators.open_interest import calculate_open_interest
from indicators.net_volume import calculate_net_volume
from indicators.ma_cross import calculate_ma_cross
from indicators.ma_index import calculate_ma_index
from indicators.mcginley_dynamic import calculate_mcginley_dynamic
from indicators.median import calculate_median
from indicators.momentum import calculate_momentum
from indicators.moon_phases import calculate_moon_phase
from indicators.ma_ribbon import calculate_ma_ribbon
from indicators.multi_time_period_chart import calculate_multi_timeframe_sma
from indicators.least_squares_moving_average import calculate_least_squares_moving_average
from indicators.linear_regression_channel import calculate_linear_regression_channel
from indicators.klinger_oscillator import calculate_klinger_oscillator
from indicators.hull_moving_average import calculate_hma
from indicators.historical_volatility import calculate_historical_volatility
from indicators.gaps import calculate_gaps
from indicators.fisher_transform import calculate_fisher_transform
from indicators.elder_force_index import calculate_elder_force_index



from indicators.aroon import aroon
from indicators.ao import ao
from indicators.bop import bop
from indicators.ad import ad
from indicators.bollinger_bands_width import bollinger_bands_width
from indicators.cfo import cfo
from indicators.adosc import adosc
from models.indicator_request import CKSPRequest
from models.indicator_request import CHOPRequest
from models.indicator_request import CorrelRequest
from models.indicator_request import VolumeOscillatorRequest
from models.indicator_request import VolatilityStopRequest
from models.indicator_request import NoPeriodIndicatorRequest
from models.indicator_request import MACrossRequest
from models.indicator_request import MultiTimeframeRequest



import numpy as np
from fastapi.responses import JSONResponse
from services.binance_service import fetch_candles
from models.indicator_request import IndicatorRequest


app = FastAPI()


@app.post("/sma")
async def get_sma(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        sma_values = calculate_sma(candles, data.period)

        # remove NaN if any (precaution)
        sma_clean = np.array(sma_values)
        sma_clean = sma_clean[~np.isnan(sma_clean)]

        return {
            "indicator": "sma",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
            "values": sma_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rsi")
async def get_rsi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        print("✅ Raw candles shape:", candles.shape)
        print("✅ First row:", candles[0])

        rsi_values = calculate_rsi(candles, data.period)

        # remove NaNs for JSON response
        rsi_clean = np.array(rsi_values)
        rsi_clean = rsi_clean[~np.isnan(rsi_clean)]

        return {
            "indicator": "rsi",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
            "values": rsi_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ema")
async def get_ema(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        ema_values = calculate_ema(candles, data.period)
        ema_clean = ema_values[~np.isnan(ema_values)]

        return {
            "indicator": "ema",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
            "values": ema_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/macd")
async def get_macd(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_macd(candles)

        # Clean NaNs from each MACD component
        macd_clean = result["macd"][~np.isnan(result["macd"])]
        signal_clean = result["signal"][~np.isnan(result["signal"])]
        hist_clean = result["hist"][~np.isnan(result["hist"])]

        return {
            "indicator": "macd",
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "fast_period": 12,
            "slow_period": 26,
            "signal_period": 9,
            "macd": macd_clean.tolist(),
            "signal": signal_clean.tolist(),
            "histogram": hist_clean.tolist()
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/bollinger")
async def get_bollinger(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_bollinger(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/atr")
async def get_atr(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_atr(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/supertrend")
async def get_supertrend(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_supertrend(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/vwap")
async def get_vwap(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_vwap(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/adx")
async def get_adx(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_adx(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/cci")
async def get_cci(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_cci(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/williams_r")
async def get_williams_r(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_williams_r(candles, data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})    


@app.post("/roc")
async def get_roc(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_roc(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/cmo")
async def get_cmo(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_cmo(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/apo")
async def get_apo(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_apo(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})    


@app.post("/ppo")
async def get_ppo(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_ppo(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/mfi")
async def get_mfi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_mfi(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/coppock")
async def get_coppock(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_coppock(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/donchian")
async def get_donchian(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_donchian(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/obv")
async def get_obv(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_obv(candles)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/efi")
async def get_efi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_efi(candles, period=data.period)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@app.post("/aroon")
async def get_aroon(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = aroon(candles, data.period)

    return {
        "indicator": "aroon",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "aroon_down": result.down.tolist() if isinstance(result.down, np.ndarray) else result.down,
        "aroon_up": result.up.tolist() if isinstance(result.up, np.ndarray) else result.up
    }


@app.post("/ao")
async def get_ao(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = ao(candles)

    return {
        "indicator": "ao",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "ao_osc": result.osc.tolist() if isinstance(result.osc, np.ndarray) else result.osc,
        "ao_change": result.change.tolist() if isinstance(result.change, np.ndarray) else result.change
    }


@app.post("/bop")
async def get_bop(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = bop(candles)

    return {
        "indicator": "bop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/ad")
async def get_ad(data: NoPeriodIndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = ad(candles)

    return {
        "indicator": "ad",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/bollinger_bands_width")
async def get_bbw(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = bollinger_bands_width(candles, data.period)

    return {
        "indicator": "bollinger_bands_width",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/cfo")
async def get_cfo(data: IndicatorRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = cfo(candles, period=data.period)

    return {
        "indicator": "cfo",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/adosc")
async def get_adosc(data: ADOSCRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = adosc(
        candles,
        fast_period=data.fast_period,
        slow_period=data.slow_period
    )

    return {
        "indicator": "adosc",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "fast_period": data.fast_period,
        "slow_period": data.slow_period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/cksp")
async def get_cksp(data: CKSPRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = cksp(candles, p=data.p, x=data.x, q=data.q)

    return {
        "indicator": "cksp",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "p": data.p,
        "x": data.x,
        "q": data.q,
        "long_stop": result.long.tolist() if isinstance(result.long, np.ndarray) else result.long,
        "short_stop": result.short.tolist() if isinstance(result.short, np.ndarray) else result.short
    }


@app.post("/chop")
async def get_chop(data: CHOPRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = chop(
        candles,
        period=data.period,
        scalar=data.scalar,
        drift=data.drift
    )

    return {
        "indicator": "chop",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "scalar": data.scalar,
        "drift": data.drift,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }


@app.post("/correl")
async def get_correl(data: CorrelRequest):
    candles = await fetch_candles(data.symbol, data.interval, data.limit)
    result = correl(candles, period=data.period)

    return {
        "indicator": "correl",
        "symbol": data.symbol.upper(),
        "interval": data.interval,
        "period": data.period,
        "values": result.tolist() if isinstance(result, np.ndarray) else result
    }

from models.indicator_request import NoPeriodIndicatorRequest  # ✅

@app.post("/volume24h")
async def get_volume24h(data: NoPeriodIndicatorRequest):  # ✅ This one!
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_volume24h(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/zig_zag")
async def get_zigzag(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_zigzag(candles, change=data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/woodies_cci")
async def get_woodies_cci(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_woodies_cci(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/williams_r")
async def get_williams_r(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_williams_r(candles, period=data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/williams_fractals")
async def get_williams_fractals(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_williams_fractals(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/williams_alligator")
async def get_williams_alligator(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_williams_alligator(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/vwap_auto_anchored")
async def get_vwap_auto_anchored(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_vwap_auto_anchored(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/vortex")
async def get_vortex(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_vortex(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/vwma")
async def get_vwma(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_vwma(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/volume_oscillator")
async def get_volume_oscillator(data: VolumeOscillatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_volume_oscillator(candles, data.short_period, data.long_period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/volume_delta")
async def get_volume_delta(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_volume_delta(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/volatility_stop")
async def get_volatility_stop(data: VolatilityStopRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_volatility_stop(candles, period=data.period, multiplier=data.multiplier)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/visible_average_price")
async def get_visible_average_price(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_visible_average_price(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/up_down_volume")
async def get_up_down_volume(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_up_down_volume(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ultimate_oscillator")
async def get_ultimate_oscillator(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_ultimate_oscillator(candles, short=7, medium=14, long=data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/tsi")
async def get_tsi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_tsi(candles, long=data.period, short=13)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/trix")
async def get_trix(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_trix(candles, period=data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/trading_sessions")
async def get_trading_sessions(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_trading_sessions(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/twap")
async def get_twap(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_twap(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "limit": data.limit
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/technical_ratings")
async def get_technical_ratings(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_technical_rating(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/stoch_rsi")
async def get_stoch_rsi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_stoch_rsi(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/smi")
async def get_smi(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_smi(candles, period=data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/smi_ergodic_oscillator")
async def get_smi_ergodic_oscillator(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_smi_ergodic_oscillator(candles, long_period=25, short_period=data.period, signal_period=9)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/smi_ergodic")
async def get_smi_ergodic(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_smi_ergodic(candles, long_period=25, short_period=data.period, signal_period=9)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/seasonality")
async def get_seasonality(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_seasonality(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rci")
async def get_rci(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rci(candles, data.period)

        # remove NaNs before returning
        result["values"] = [v for v in result["values"] if not np.isnan(v)]

        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/rci_ribbon")
async def get_rci_ribbon(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rci_ribbon(candles)

        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/relative_volatility_index")
async def get_relative_volatility_index(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rvi_volatility(candles, data.period)

        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/relative_volume_at_time")
async def get_relative_volume_at_time(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)

        result = calculate_relative_volume_at_time(candles, data.interval)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/rob_intraday_pivot")
async def get_rob_intraday_pivot(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rob_intraday_pivot(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rob_knoxville_divergence")
async def get_rob_knoxville_divergence(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rob_knoxville_divergence(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/rob_missed_pivots")
async def get_rob_missed_pivots(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rob_missed_pivots(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/rob_reversal")
async def get_rob_reversal(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rob_reversal(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/rob_ziv_ghost")
async def get_rob_ziv_ghost(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_rob_ziv_ghost(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/parabolic_sar")
async def get_parabolic_sar(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_parabolic_sar(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/performance")
async def get_performance(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_performance(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/pivot_points_high_low")
async def get_pivot_points_high_low(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_pivot_points_high_low(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/pivot_points_standard")
async def get_pivot_points_standard(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_pivot_points_standard(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/price_oscillator")
async def get_price_oscillator(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_price_oscillator(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/price_target")
async def get_price_target(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_price_target(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/price_volume_trend")
async def get_price_volume_trend(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_price_volume_trend(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/open_interest")
async def get_open_interest(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_open_interest(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/net_volume")
async def get_net_volume(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_net_volume(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ma_cross")
async def get_ma_cross(data: MACrossRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_ma_cross(candles, data.fast_period, data.slow_period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "fast_period": data.fast_period,
            "slow_period": data.slow_period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ma_index")
async def get_ma_index(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_ma_index(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/mcginley_dynamic")
async def get_mcginley_dynamic(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_mcginley_dynamic(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/median")
async def get_median(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_median(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/momentum")
async def get_momentum(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_momentum(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/moon_phases")
async def get_moon_phases():
    try:
        result = calculate_moon_phase()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/ma_ribbon")
async def get_ma_ribbon(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_ma_ribbon(candles, base_period=data.period)  # using `data.period` as base

        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "base_period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/multi_timeframe_sma")
async def get_multi_timeframe_sma(data: MultiTimeframeRequest):
    try:
        result = await calculate_multi_timeframe_sma(
            data.symbol,
            data.interval,
            data.limit,
            data.higher_interval,
            data.period
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/least_squares_moving_average")
async def get_lsma(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_least_squares_moving_average(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/linear_regression_channel")
async def get_linear_regression_channel(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_linear_regression_channel(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/klinger_oscillator")
async def get_klinger_oscillator(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_klinger_oscillator(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/hma")
async def get_hma(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_hma(candles, period=data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/historical_volatility")
async def get_historical_volatility(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_historical_volatility(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/gaps")
async def get_gaps(data: NoPeriodIndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_gaps(candles)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/fisher_transform")
async def get_fisher_transform(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_fisher_transform(candles, period=data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/elder_force_index")
async def get_elder_force_index(data: IndicatorRequest):
    try:
        candles = await fetch_candles(data.symbol, data.interval, data.limit)
        result = calculate_elder_force_index(candles, data.period)
        result.update({
            "symbol": data.symbol.upper(),
            "interval": data.interval,
            "period": data.period
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




