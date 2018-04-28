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


def get_macd_1440(ohlc):
    span = 1440
    # MACD (先行 12 日移動平均、遅行 26 日移動平均、 9 日シグナル線) を求める
    macd, macdsignal, macdhist = ta.MACD(ohlc['4_close'], fastperiod=12 * span, slowperiod=26 * span,
                                         signalperiod=9 * span)

    ohlc = ohlc.assign(
        macd_1440=macd
        , macdsignal_1440=macdsignal
        , macdhist_1440=macdhist
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


def get_mfi(ohlc):
    mfi = ta.MFI(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], ohlc['5_volume'], timeperiod=14)

    ohlc['mfi'] = mfi
    return ohlc


def get_minus_di(ohlc):
    minus_di = ta.MINUS_DI(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['minus_di'] = minus_di
    return ohlc


def get_minus_dm(ohlc):
    minus_dm = ta.MINUS_DM(ohlc['2_high'], ohlc['3_low'], timeperiod=14)

    ohlc['minus_dm'] = minus_dm
    return ohlc


def get_mom(ohlc):
    mom = ta.MOM(ohlc['4_close'], timeperiod=10)

    ohlc['mom'] = mom
    return ohlc


def get_plus_di(ohlc):
    plus_di = ta.PLUS_DI(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['plus_di'] = plus_di
    return ohlc


def get_plus_dm(ohlc):
    plus_dm = ta.PLUS_DM(ohlc['2_high'], ohlc['3_low'], timeperiod=14)

    ohlc['plus_dm'] = plus_dm
    return ohlc


def get_ppo(ohlc):
    ppo = ta.PPO(ohlc['4_close'], fastperiod=12, slowperiod=26, matype=0)

    ohlc['ppo'] = ppo
    return ohlc


def get_roc(ohlc):
    roc = ta.ROC(ohlc['4_close'], timeperiod=10)

    ohlc['roc'] = roc
    return ohlc


def get_rocp(ohlc):
    rocp = ta.ROCP(ohlc['4_close'], timeperiod=10)

    ohlc['rocp'] = rocp
    return ohlc


def get_rocr(ohlc):
    rocr = ta.ROCR(ohlc['4_close'], timeperiod=10)

    ohlc['rocr'] = rocr
    return ohlc


def get_rocr100(ohlc):
    rocr100 = ta.ROCR100(ohlc['4_close'], timeperiod=10)

    ohlc['rocr100'] = rocr100
    return ohlc


def get_rsi(ohlc):
    rsi = ta.RSI(ohlc['4_close'], timeperiod=14)

    ohlc['rsi'] = rsi
    return ohlc


def get_stoch(ohlc):
    slowk, slowd = ta.STOCH(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], fastk_period=5, slowk_period=3, slowk_matype=0,
                     slowd_period=3, slowd_matype=0)

    ohlc['stoch_slowk'] = slowk
    ohlc['stoch_slowd'] = slowd
    return ohlc


def get_stochf(ohlc):
    fastk, fastd = ta.STOCHF(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], fastk_period=5, fastd_period=3, fastd_matype=0)

    ohlc['stochf_fastk'] = fastk
    ohlc['stochf_fastd'] = fastd
    return ohlc


def get_stochrsi(ohlc):
    stochrsi_fastk, stochrsi_fastd = ta.STOCHRSI(ohlc['4_close'], timeperiod=14, fastk_period=5, fastd_period=3,
                                                 fastd_matype=0)

    ohlc = ohlc.assign(
        stochrsi_fastk=stochrsi_fastk
        , stochrsi_fastd=stochrsi_fastd
    )
    return ohlc


def get_trix(ohlc):
    trix = ta.TRIX(ohlc['4_close'], timeperiod=30)

    ohlc['trix'] = trix
    return ohlc


def get_ultosc(ohlc):
    ultosc = ta.ULTOSC(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)

    ohlc['ultosc'] = ultosc
    return ohlc


def get_willr(ohlc):
    willr = ta.WILLR(ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], timeperiod=14)

    ohlc['willr'] = willr
    return ohlc
