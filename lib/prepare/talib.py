from .momentum_indicator import *
from .overlap_studies import *
from .volume_indicators import *
from .volatility_indicators import *
from .cycle_indicators import *
from .pattern_recognition import *
from .statistic_functions import *


def extract(ohlc):
    # Overlap Studies Functions
    ohlc = get_bb2(ohlc)
    ohlc = get_bb3(ohlc)
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
    ohlc = get_macd_1440(ohlc)
    ohlc = get_macdext(ohlc)
    ohlc = get_macdfix(ohlc)
    ohlc = get_mfi(ohlc)
    ohlc = get_minus_di(ohlc)
    ohlc = get_minus_dm(ohlc)
    ohlc = get_mom(ohlc)
    ohlc = get_plus_di(ohlc)
    ohlc = get_plus_dm(ohlc)
    ohlc = get_ppo(ohlc)
    ohlc = get_roc(ohlc)
    ohlc = get_rocp(ohlc)
    ohlc = get_rocr(ohlc)
    ohlc = get_rocr100(ohlc)
    ohlc = get_rsi(ohlc)
    ohlc = get_stoch(ohlc)
    ohlc = get_stochf(ohlc)
    ohlc = get_stochrsi(ohlc)
    ohlc = get_trix(ohlc)
    ohlc = get_ultosc(ohlc)
    ohlc = get_willr(ohlc)

    # Volume Indicator Functions
    ohlc = get_ad(ohlc)
    ohlc = get_adosc(ohlc)
    ohlc = get_obv(ohlc)

    # Volatility Indicator Functions
    ohlc = get_atr(ohlc)
    ohlc = get_natr(ohlc)
    ohlc = get_trange(ohlc)

    # Cycle Indicator Functions
    ohlc = get_ht_dcperiod(ohlc)
    ohlc = get_ht_dcphase(ohlc)
    ohlc = get_ht_phasor(ohlc)
    ohlc = get_ht_sine(ohlc)
    ohlc = get_ht_trendmode(ohlc)

    # Pattern Recognition Functions
    ohlc = get_cdl2crows(ohlc)

    # Statistic Functions
    ohlc = get_beta(ohlc)
    ohlc = get_correl(ohlc)
    ohlc = get_linearreg(ohlc)
    ohlc = get_linearreg_angle(ohlc)
    ohlc = get_linearreg_intercept(ohlc)
    ohlc = get_linearreg_slope(ohlc)
    ohlc = get_stddev(ohlc)
    ohlc = get_tsf(ohlc)
    ohlc = get_var(ohlc)


    print(ohlc.describe())
    print(ohlc.info())

    ohlc = ohlc.dropna(how='any')
    return ohlc
