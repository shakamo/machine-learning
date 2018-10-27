import talib as ta


def get_bb2(ohlc):
    upperband, middleband, lowerband = ta.BBANDS(ohlc['4_close'], timeperiod=40, nbdevup=2, nbdevdn=2)

    ohlc['upperband2'] = upperband
    ohlc['middleband2'] = middleband
    ohlc['lowerband2'] = lowerband

    return ohlc


def get_bb3(ohlc):
    upperband, middleband, lowerband = ta.BBANDS(ohlc['4_close'], timeperiod=40, nbdevup=3, nbdevdn=3)

    ohlc['upperband3'] = upperband
    ohlc['middleband3'] = middleband
    ohlc['lowerband3'] = lowerband

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
    return ohlc


def get_ma(ohlc):
    ma = ta.MA(ohlc['4_close'], timeperiod=30, matype=0)

    ohlc['ma'] = ma
    return ohlc


def get_mama(ohlc):
    mama, fama = ta.MAMA(ohlc['4_close'])

    ohlc['mama'] = mama
    ohlc['fama'] = fama
    return ohlc


def get_midpoint(ohlc):
    midpoint = ta.MIDPOINT(ohlc['4_close'], timeperiod=14)

    ohlc['midpoint'] = midpoint
    return ohlc


def get_midprice(ohlc):
    midprice = ta.MIDPRICE(ohlc['2_high'], ohlc['3_low'], timeperiod=14)

    ohlc['midprice'] = midprice
    return ohlc


def get_sar(ohlc):
    sar = ta.SAR(ohlc['2_high'], ohlc['3_low'], acceleration=0, maximum=0)

    ohlc['sar'] = sar
    return ohlc


def get_sarext(ohlc):
    sarext = ta.SAREXT(ohlc['2_high'], ohlc['3_low'], startvalue=0, offsetonreverse=0, accelerationinitlong=0,
                       accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0,
                       accelerationmaxshort=0)

    ohlc['sarext'] = sarext
    return ohlc


def get_sma(ohlc):
    sma = ta.SMA(ohlc['4_close'], timeperiod=30)

    ohlc['sma'] = sma
    return ohlc


def get_t3(ohlc):
    t3 = ta.T3(ohlc['4_close'], timeperiod=5, vfactor=0)

    ohlc['t3'] = t3
    return ohlc


def get_tema(ohlc):
    tema = ta.TEMA(ohlc['4_close'], timeperiod=30)

    ohlc['tema'] = tema
    return ohlc


def get_trima(ohlc):
    trima = ta.TRIMA(ohlc['4_close'], timeperiod=30)

    ohlc['trima'] = trima
    return ohlc


def get_wma(ohlc):
    wma = ta.WMA(ohlc['4_close'], timeperiod=30)

    ohlc['wma'] = wma
    return ohlc
