import talib as ta


def get_beta(ohlc):
    beta = ta.BETA(ohlc['2_high'], ohlc['3_low'], timeperiod=5)

    ohlc['beta'] = beta

    return ohlc



def get_correl(ohlc):
    correl = ta.CORREL(ohlc['2_high'], ohlc['3_low'], timeperiod=30)

    ohlc['correl'] = correl

    return ohlc



def get_linearreg(ohlc):
    linearreg = ta.LINEARREG(ohlc['4_close'], timeperiod=14)

    ohlc['linearreg'] = linearreg

    return ohlc


def get_linearreg_angle(ohlc):
    linearreg_angle = ta.LINEARREG_ANGLE(ohlc['4_close'], timeperiod=14)

    ohlc['linearreg_angle'] = linearreg_angle

    return ohlc



def get_linearreg_intercept(ohlc):
    linearreg_intercept = ta.LINEARREG_INTERCEPT(ohlc['4_close'], timeperiod=14)

    ohlc['linearreg_intercept'] = linearreg_intercept

    return ohlc




def get_linearreg_slope(ohlc):
    linearreg_slope = ta.LINEARREG_SLOPE(ohlc['4_close'], timeperiod=14)

    ohlc['linearreg_slope'] = linearreg_slope

    return ohlc


def get_stddev(ohlc):
    stddev = ta.STDDEV(ohlc['4_close'], timeperiod=5, nbdev=1)

    ohlc['stddev'] = stddev

    return ohlc



def get_tsf(ohlc):
    tsf = ta.TSF(ohlc['4_close'], timeperiod=14)

    ohlc['tsf'] = tsf

    return ohlc


def get_var(ohlc):
    var = ta.VAR(ohlc['4_close'], timeperiod=5, nbdev=1)

    ohlc['var'] = var

    return ohlc
