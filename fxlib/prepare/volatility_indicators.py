import talib as ta


def get_atr(ohlc):
    atr = ta.ATR(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['atr'] = atr

    return ohlc


def get_natr(ohlc):
    natr = ta.NATR(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['natr'] = natr

    return ohlc


def get_trange(ohlc):
    trange = ta.TRANGE(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['trange'] = trange

    return ohlc
