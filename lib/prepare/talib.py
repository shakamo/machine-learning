from .momentum_indicator import *
from .overlap_studies import *


def extract(ohlc):
    # Overlap Studies Functions
    ohlc = get_bb2(ohlc)
    ohlc = get_bb3(ohlc)
    # ohlc = get_dema(ohlc)
    ohlc = get_ema(ohlc)
    # ohlc = get_ht(ohlc)
    # ohlc = get_kama(ohlc)
    ohlc = get_ma(ohlc)
    # ohlc = get_mama(ohlc)
    # ohlc = get_midpoint(ohlc)
    # ohlc = get_midprice(ohlc)
    ohlc = get_sar(ohlc)
    # ohlc = get_sarext(ohlc)
    ohlc = get_sma(ohlc)
    # ohlc = get_t3(ohlc)
    # ohlc = get_tema(ohlc)
    # ohlc = get_trima(ohlc)
    ohlc = get_wma(ohlc)

    # Momentum Indicator Functions
    ohlc = get_adx(ohlc)
    ohlc = get_adxr(ohlc)
    ohlc = get_apo(ohlc)
    ohlc = get_aroon(ohlc)
    ohlc = get_aroonosc(ohlc)
    ohlc = get_bop(ohlc)
    ohlc = get_cci(ohlc)
    ohlc = get_cmo(ohlc)
    ohlc = get_dx(ohlc)
    ohlc = get_macd(ohlc)
    ohlc = get_macdext(ohlc)
    ohlc = get_macdfix(ohlc)
    ohlc = get_rsi(ohlc)

    ohlc = ohlc.dropna(how='any')
    return ohlc
