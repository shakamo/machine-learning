import talib as ta


def get_ad(ohlc):
    ad = ta.AD(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], ohlc['5_volume'])

    ohlc['ad'] = ad

    return ohlc


def get_adosc(ohlc):
    adosc = ta.ADOSC(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], ohlc['5_volume'], fastperiod=3, slowperiod=10)

    ohlc['adosc'] = adosc

    return ohlc


def get_obv(ohlc):
    obv = ta.OBV(ohlc['4_close'], ohlc['5_volume'])

    ohlc['obv'] = obv

    return ohlc
