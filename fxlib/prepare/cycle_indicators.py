import talib as ta


def get_ht_dcperiod(ohlc):
    ht_dcperiod = ta.HT_DCPERIOD(ohlc['4_close'])

    ohlc['ht_dcperiod'] = ht_dcperiod

    return ohlc


def get_ht_dcphase(ohlc):
    ht_dcphase = ta.HT_DCPHASE(ohlc['4_close'])

    ohlc['ht_dcphase'] = ht_dcphase

    return ohlc


def get_ht_phasor(ohlc):
    inphase, quadrature = ta.HT_PHASOR(ohlc['4_close'])

    ohlc['ht_phasor_inphase'] = inphase
    ohlc['ht_phasor_quadrature'] = quadrature

    return ohlc


def get_ht_sine(ohlc):
    sine, leadsine = ta.HT_SINE(ohlc['4_close'])

    ohlc['ht_sine_sine'] = sine
    ohlc['ht_sine_leadsine'] = leadsine

    return ohlc


def get_ht_trendmode(ohlc):
    ht_trendmode = ta.HT_TRENDMODE(ohlc['4_close'])

    ohlc['ht_trendmode'] = ht_trendmode

    return ohlc
