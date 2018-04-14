import pandas as pd
import talib as ta


def extract_for_fx_by_m1(df):
    df['1_1_M1_range'] = df['2_high'] - df['3_low']
    df['1_2_M1_upper_beard'] = df['2_high'] - df['1_open']
    df['1_3_M1_lower_beard'] = df['4_close'] - df['3_low']
    df['1_4_M1_trend'] = df['1_open'] - df['4_close']

    return df


def get_bb(ohlc):
    upperband, middleband, lowerband = ta.BBANDS(ohlc['4_close'], timeperiod=40)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['upperband'] = upperband
    df['middleband'] = middleband
    df['lowerband'] = lowerband
    print(df)
    return df


def get_dema(ohlc):
    dema = ta.DEMA(ohlc['4_close'], timeperiod=30)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['dema'] = dema
    print(df)
    return df


def get_ema(ohlc):
    ema = ta.EMA(ohlc['4_close'], timeperiod=30)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['ema'] = ema
    print(df)
    return df


def get_ht(ohlc):
    ht = ta.HT_TRENDLINE(ohlc['4_close'])

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['ht'] = ht
    print(df)
    return df


def get_kama(ohlc):
    kama = ta.KAMA(ohlc['4_close'], timeperiod=30)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['kama'] = kama
    print(df)
    return df


def get_ma(ohlc):
    ma = ta.MA(ohlc['4_close'], timeperiod=30, matype=0)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['ma'] = ma
    print(df)
    return df


def get_ma(ohlc):
    mama, fama = ta.MAMA(ohlc['4_close'], fastlimit=0, slowlimit=0)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['mama'] = mama
    df['fama'] = fama
    print(df)
    return df


def get_midpoint(ohlc):
    midpoint = ta.MIDPOINT(ohlc['4_close'], timeperiod=14)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['midpoint'] = midpoint
    print(df)
    return df


def get_midprice(ohlc):
    midprice = ta.MIDPRICE(ohlc['2_high'], ohlc['3_low'], timeperiod=14)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['midprice'] = midprice
    print(df)
    return df


def get_sar(ohlc):
    sar = ta.SAR(ohlc['2_high'], ohlc['3_low'], acceleration=0, maximum=0)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['sar'] = sar
    print(df)
    return df


def get_sarext(ohlc):
    sarext = ta.SAREXT(ohlc['2_high'], ohlc['3_low'], startvalue=0, offsetonreverse=0, accelerationinitlong=0,
                       accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0,
                       accelerationmaxshort=0)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['sarext'] = sarext
    print(df)
    return df


def get_sma(ohlc):
    sma = ta.SMA(ohlc['4_close'], timeperiod=30)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['sma'] = sma
    print(df)
    return df


def get_t3(ohlc):
    t3 = ta.T3(ohlc['4_close'], timeperiod=5, vfactor=0)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['t3'] = t3
    print(df)
    return df


def get_tema(ohlc):
    tema = ta.TEMA(ohlc['4_close'], timeperiod=30)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['tema'] = tema
    print(df)
    return df


def get_trima(ohlc):
    trima = ta.TRIMA(ohlc['4_close'], timeperiod=30)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['trima'] = trima
    print(df)
    return df


def get_wma(ohlc):
    wma = ta.WMA(ohlc['4_close'], timeperiod=30)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['wma'] = wma
    print(df)
    return df


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

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']
    df['rsi'] = rsi
    print(df)
    return df


def get_MAVP(ohlc):
    return ta.MAVP(ohlc['4_close'], fastlimit=0, slowlimit=0)


def get_bb(ohlc):
    return ta.BBANDS(ohlc['4_close'], timeperiod=40)


def get_bb(ohlc):
    return ta.BBANDS(ohlc['4_close'], timeperiod=40)
