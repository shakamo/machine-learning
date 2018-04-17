import pandas as pd
import talib as ta


def extract_for_fx_by_m1(ohlc):
    ohlc = get_bb(ohlc)
    ohlc = get_dema(ohlc)
    ohlc = get_ema(ohlc)
    ohlc = get_ht(ohlc)
    ohlc = get_kama(ohlc)
    ohlc = get_ma(ohlc)
    ohlc = get_mama(ohlc)
    ohlc = get_midpoint(ohlc)
    ohlc = get_midprice(ohlc)
    ohlc = get_sar(ohlc)
    ohlc = get_sarext(ohlc)
    ohlc = get_sma(ohlc)
    ohlc = get_t3(ohlc)
    ohlc = get_tema(ohlc)
    ohlc = get_trima(ohlc)
    ohlc = get_wma(ohlc)

    return ohlc


def get_bb(ohlc):
    upperband, middleband, lowerband = ta.BBANDS(ohlc['4_close'], timeperiod=40)

    ohlc['upperband'] = upperband
    ohlc['middleband'] = middleband
    ohlc['lowerband'] = lowerband

    return ohlc


def get_dema(ohlc):
    dema = ta.DEMA(ohlc['4_close'], timeperiod=30)

    ohlc['dema'] = dema
    return ohlc


def get_ema(ohlc):
    ema = ta.EMA(ohlc['4_close'], timeperiod=30)

    ohlc['ema'] = ema
    return ohlc


def get_ht(ohlc):
    ht = ta.HT_TRENDLINE(ohlc['4_close'])

    ohlc['ht'] = ht
    return ohlc


def get_kama(ohlc):
    kama = ta.KAMA(ohlc['4_close'], timeperiod=30)

    ohlc['kama'] = kama
    print(ohlc)
    return ohlc


def get_ma(ohlc):
    ma = ta.MA(ohlc['4_close'], timeperiod=30, matype=0)

    ohlc['ma'] = ma
    print(ohlc)
    return ohlc


def get_mama(ohlc):
    mama, fama = ta.MAMA(ohlc['4_close'])

    ohlc['mama'] = mama
    ohlc['fama'] = fama
    print(ohlc)
    return ohlc


def get_midpoint(ohlc):
    midpoint = ta.MIDPOINT(ohlc['4_close'], timeperiod=14)

    ohlc['midpoint'] = midpoint
    print(ohlc)
    return ohlc


def get_midprice(ohlc):
    midprice = ta.MIDPRICE(ohlc['2_high'], ohlc['3_low'], timeperiod=14)

    ohlc['midprice'] = midprice
    print(ohlc)
    return ohlc


def get_sar(ohlc):
    sar = ta.SAR(ohlc['2_high'], ohlc['3_low'], acceleration=0, maximum=0)

    ohlc['sar'] = sar
    print(ohlc)
    return ohlc


def get_sarext(ohlc):
    sarext = ta.SAREXT(ohlc['2_high'], ohlc['3_low'], startvalue=0, offsetonreverse=0, accelerationinitlong=0,
                       accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0,
                       accelerationmaxshort=0)

    ohlc['sarext'] = sarext
    print(ohlc)
    return ohlc


def get_sma(ohlc):
    sma = ta.SMA(ohlc['4_close'], timeperiod=30)

    ohlc['sma'] = sma
    print(ohlc)
    return ohlc


def get_t3(ohlc):
    t3 = ta.T3(ohlc['4_close'], timeperiod=5, vfactor=0)

    ohlc['t3'] = t3
    print(ohlc)
    return ohlc


def get_tema(ohlc):
    tema = ta.TEMA(ohlc['4_close'], timeperiod=30)

    ohlc['tema'] = tema
    print(ohlc)
    return ohlc


def get_trima(ohlc):
    trima = ta.TRIMA(ohlc['4_close'], timeperiod=30)

    ohlc['trima'] = trima
    print(ohlc)
    return ohlc


def get_wma(ohlc):
    wma = ta.WMA(ohlc['4_close'], timeperiod=30)

    ohlc['wma'] = wma
    print(ohlc)
    return ohlc


def get_macd(ohlc):
    # MACD (先行 12 日移動平均、遅行 26 日移動平均、 9 日シグナル線) を求める
    macd, macdsignal, macdhist = ta.MACD(ohlc['4_close'], fastperiod=12, slowperiod=26, signalperiod=9)

    ohlc = ohlc.assign(
        macd=macd
        , macdsignal=macdsignal
        , macdhist=macdhist
    )

    print(ohlc.head())
    return ohlc


def get_rsi(ohlc):
    rsi = ta.RSI(ohlc['4_close'], timeperiod=40)

    ohlc['rsi'] = rsi
    print(ohlc)
    return ohlc


def get_MAVP(ohlc):
    mavp = ta.MAVP(ohlc['4_close'], fastlimit=0, slowlimit=0)

    ohlc['mavp'] = mavp
    print(ohlc)
    return ohlc
