import talib as ta


def get_adx(ohlc):
    adx = ta.ADX(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['adx'] = adx
    return ohlc


def get_adxr(ohlc):
    adxr = ta.ADXR(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['adxr'] = adxr
    return ohlc


def get_apo(ohlc):
    apo = ta.APO(ohlc['4_close'], fastperiod=12, slowperiod=26, matype=0)

    ohlc['apo'] = apo
    return ohlc


def get_aroon(ohlc):
    aroondown, aroonup = ta.AROON(ohlc['2_high'], ohlc['3_low'], timeperiod=14)

    ohlc['aroondown'] = aroondown
    ohlc['aroonup'] = aroonup
    return ohlc


def get_aroonosc(ohlc):
    aroonosc = ta.AROONOSC(ohlc['2_high'], ohlc['3_low'], timeperiod=14)

    ohlc['aroonosc'] = aroonosc
    return ohlc


def get_bop(ohlc):
    bop = ta.BOP(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['bop'] = bop
    return ohlc


def get_cci(ohlc):
    cci = ta.CCI(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['cci'] = cci
    return ohlc


def get_cmo(ohlc):
    cmo = ta.CMO(ohlc['4_close'], timeperiod=14)

    ohlc['cmo'] = cmo
    return ohlc


def get_dx(ohlc):
    dx = ta.DX(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['dx'] = dx
    return ohlc


def get_macd(ohlc):
    # MACD (先行 12 日移動平均、遅行 26 日移動平均、 9 日シグナル線) を求める
    macd, macdsignal, macdhist = ta.MACD(ohlc['4_close'], fastperiod=12, slowperiod=26, signalperiod=9)

    ohlc = ohlc.assign(
        macd=macd
        , macdsignal=macdsignal
        , macdhist=macdhist
    )
    return ohlc


def get_macdext(ohlc):
    # MACD (先行 12 日移動平均、遅行 26 日移動平均、 9 日シグナル線) を求める
    macdext, macdsignalext, macdhistext = ta.MACDEXT(ohlc['4_close'], fastperiod=12, fastmatype=0, slowperiod=26,
                                                     slowmatype=0, signalperiod=9, signalmatype=0)

    ohlc = ohlc.assign(
        macdext=macdext
        , macdsignalext=macdsignalext
        , macdhistext=macdhistext
    )
    return ohlc


def get_macdfix(ohlc):
    # MACD (先行 12 日移動平均、遅行 26 日移動平均、 9 日シグナル線) を求める
    macd, macdsignal, macdhist = ta.MACDFIX(ohlc['4_close'], signalperiod=9)

    ohlc = ohlc.assign(
        macdfix=macd
        , macdsignalfix=macdsignal
        , macdhistfix=macdhist
    )
    return ohlc


def get_rsi(ohlc):
    rsi = ta.RSI(ohlc['4_close'], timeperiod=40)

    ohlc['rsi'] = rsi
    return ohlc
