import talib as ta


def get_cdl2crows(ohlc):
    cdl2crows = ta.CDL2CROWS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdl2crows'] = cdl2crows

    return ohlc


def get_cdl3blackcrows(ohlc):
    cdl3blackcrows = ta.CDL3BLACKCROWS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdl3blackcrows'] = cdl3blackcrows

    return ohlc



def get_CDL3INSIDE(ohlc):
    cdl3inside = ta.CDL3INSIDE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdl3inside'] = cdl3inside

    return ohlc



def get_cdl3linestrike(ohlc):
    cdl3linestrike = ta.CDL3LINESTRIKE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdl3linestrike'] = cdl3linestrike

    return ohlc



def get_cdl3outside(ohlc):
    cdl3outside = ta.CDL3OUTSIDE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdl3outside'] = cdl3outside

    return ohlc



def get_cdl3starsinsouth(ohlc):
    cdl3starsinsouth = ta.CDL3STARSINSOUTH(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdl3starsinsouth'] = cdl3starsinsouth

    return ohlc



def get_cdl3whitesoldiers(ohlc):
    cdl3whitesoldiers = ta.CDL3WHITESOLDIERS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdl3whitesoldiers'] = cdl3whitesoldiers

    return ohlc



def get_cdlabandonedbaby(ohlc):
    cdlabandonedbaby = ta.CDLABANDONEDBABY(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlabandonedbaby'] = cdlabandonedbaby

    return ohlc



def get_cdladvanceblock(ohlc):
    cdladvanceblock = ta.CDLADVANCEBLOCK(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdladvanceblock'] = cdladvanceblock

    return ohlc



def get_cdlbelthold(ohlc):
    cdlbelthold = ta.CDLBELTHOLD(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlbelthold'] = cdlbelthold

    return ohlc



def get_cdlbreakaway(ohlc):
    cdlbreakaway = ta.CDLBREAKAWAY(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlbreakaway'] = cdlbreakaway

    return ohlc



def get_cdlclosingmarubozu(ohlc):
    cdlclosingmarubozu = ta.CDLCLOSINGMARUBOZU(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlclosingmarubozu'] = cdlclosingmarubozu

    return ohlc



def get_cdlconcealbabyswall(ohlc):
    cdlconcealbabyswall = ta.CDLCONCEALBABYSWALL(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlconcealbabyswall'] = cdlconcealbabyswall

    return ohlc



def get_cdlcounterattack(ohlc):
    cdlcounterattack = ta.CDLCOUNTERATTACK(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlcounterattack'] = cdlcounterattack

    return ohlc



def get_cdldarkcloudcover(ohlc):
    cdldarkcloudcover = ta.CDLDARKCLOUDCOVER(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], penetration=0)

    ohlc['cdldarkcloudcover'] = cdldarkcloudcover

    return ohlc



def get_cdldoji(ohlc):
    cdldoji = ta.CDLDOJI(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdldoji'] = cdldoji

    return ohlc



def get_cdldojistar(ohlc):
    cdldojistar = ta.CDLDOJISTAR(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdldojistar'] = cdldojistar

    return ohlc



def get_cdldragonflydoji(ohlc):
    cdldragonflydoji = ta.CDLDRAGONFLYDOJI(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdldragonflydoji'] = cdldragonflydoji

    return ohlc



def get_cdlengulfing(ohlc):
    cdlengulfing = ta.CDLENGULFING(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlengulfing'] = cdlengulfing

    return ohlc



def get_cdleveningdojistar(ohlc):
    cdleveningdojistar = ta.CDLEVENINGDOJISTAR(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], penetration=0)

    ohlc['cdleveningdojistar'] = cdleveningdojistar

    return ohlc



def get_cdleveningstar(ohlc):
    cdleveningstar = ta.CDLEVENINGSTAR(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], penetration=0)

    ohlc['cdleveningstar'] = cdleveningstar

    return ohlc



def get_cdlgapsidesidewhite(ohlc):
    cdlgapsidesidewhite = ta.CDLGAPSIDESIDEWHITE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlgapsidesidewhite'] = cdlgapsidesidewhite

    return ohlc



def get_cdlgravestonedoji(ohlc):
    cdlgravestonedoji = ta.CDLGRAVESTONEDOJI(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlgravestonedoji'] = cdlgravestonedoji

    return ohlc



def get_cdlhammer(ohlc):
    cdlhammer = ta.CDLHAMMER(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlhammer'] = cdlhammer

    return ohlc



def get_cdlhangingman(ohlc):
    cdlhangingman = ta.CDLHANGINGMAN(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlhangingman'] = cdlhangingman

    return ohlc



def get_cdlharami(ohlc):
    cdlharami = ta.CDLHARAMI(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlharami'] = cdlharami

    return ohlc



def get_cdlharamicross(ohlc):
    cdlharamicross = ta.CDLHARAMICROSS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlharamicross'] = cdlharamicross

    return ohlc



def get_cdlhighwave(ohlc):
    cdlhighwave = ta.CDLHIGHWAVE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlhighwave'] = cdlhighwave

    return ohlc



def get_cdlhikkake(ohlc):
    cdlhikkake = ta.CDLHIKKAKE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlhikkake'] = cdlhikkake

    return ohlc



def get_cdlhikkakemod(ohlc):
    cdlhikkakemod = ta.CDLHIKKAKEMOD(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlhikkakemod'] = cdlhikkakemod

    return ohlc



def get_cdlhomingpigeon(ohlc):
    cdlhomingpigeon = ta.CDLHOMINGPIGEON(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlhomingpigeon'] = cdlhomingpigeon

    return ohlc



def get_cdlidentical3crows(ohlc):
    cdlidentical3crows = ta.CDLIDENTICAL3CROWS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlidentical3crows'] = cdlidentical3crows

    return ohlc



def get_cdlinneck(ohlc):
    cdlinneck = ta.CDLINNECK(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlinneck'] = cdlinneck

    return ohlc



def get_cdlinvertedhammer(ohlc):
    cdlinvertedhammer = ta.CDLINVERTEDHAMMER(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlinvertedhammer'] = cdlinvertedhammer

    return ohlc



def get_cdlkicking(ohlc):
    cdlkicking = ta.CDLKICKING(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlkicking'] = cdlkicking

    return ohlc



def get_cdlkickingbylength(ohlc):
    cdlkickingbylength = ta.CDLKICKINGBYLENGTH(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlkickingbylength'] = cdlkickingbylength

    return ohlc


def get_cdlladderbottom(ohlc):
    cdlladderbottom = ta.CDLLADDERBOTTOM(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlladderbottom'] = cdlladderbottom

    return ohlc


def get_cdllongleggeddoji(ohlc):
    cdllongleggeddoji = ta.CDLLONGLEGGEDDOJI(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdllongleggeddoji'] = cdllongleggeddoji

    return ohlc


def get_cdllongline(ohlc):
    cdllongline = ta.CDLLONGLINE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdllongline'] = cdllongline

    return ohlc


def get_cdlmarubozu(ohlc):
    cdlmarubozu = ta.CDLMARUBOZU(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlmarubozu'] = cdlmarubozu

    return ohlc


def get_cdlmatchinglow(ohlc):
    cdlmatchinglow = ta.CDLMATCHINGLOW(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlmatchinglow'] = cdlmatchinglow

    return ohlc


def get_cdlmathold(ohlc):
    cdlmathold = ta.CDLMATHOLD(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], penetration=0)

    ohlc['cdlmathold'] = cdlmathold

    return ohlc


def get_cdlmorningdojistar(ohlc):
    cdlmorningdojistar = ta.CDLMORNINGDOJISTAR(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], penetration=0)

    ohlc['cdlmorningdojistar'] = cdlmorningdojistar

    return ohlc


def get_cdlmorningstar(ohlc):
    cdlmorningstar = ta.CDLMORNINGSTAR(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'], penetration=0)

    ohlc['cdlmorningstar'] = cdlmorningstar

    return ohlc


def get_cdlonneck(ohlc):
    cdlonneck = ta.CDLONNECK(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlonneck'] = cdlonneck

    return ohlc


def get_cdlpiercing(ohlc):
    cdlpiercing = ta.CDLPIERCING(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlpiercing'] = cdlpiercing

    return ohlc


def get_cdlrickshawman(ohlc):
    cdlrickshawman = ta.CDLRICKSHAWMAN(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlrickshawman'] = cdlrickshawman

    return ohlc


def get_cdlrisefall3methods(ohlc):
    cdlrisefall3methods = ta.CDLRISEFALL3METHODS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlrisefall3methods'] = cdlrisefall3methods

    return ohlc


def get_cdlseparatinglines(ohlc):
    cdlseparatinglines = ta.CDLSEPARATINGLINES(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlseparatinglines'] = cdlseparatinglines

    return ohlc


def get_cdlshootingstar(ohlc):
    cdlshootingstar = ta.CDLSHOOTINGSTAR(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlshootingstar'] = cdlshootingstar

    return ohlc


def get_cdlshortline(ohlc):
    cdlshortline = ta.CDLSHORTLINE(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlshortline'] = cdlshortline

    return ohlc


def get_cdlspinningtop(ohlc):
    cdlspinningtop = ta.CDLSPINNINGTOP(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlspinningtop'] = cdlspinningtop

    return ohlc


def get_cdlstalledpattern(ohlc):
    cdlstalledpattern = ta.CDLSTALLEDPATTERN(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlstalledpattern'] = cdlstalledpattern

    return ohlc


def get_cdlsticksandwich(ohlc):
    cdlsticksandwich = ta.CDLSTICKSANDWICH(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlsticksandwich'] = cdlsticksandwich

    return ohlc


def get_cdltakuri(ohlc):
    cdltakuri = ta.CDLTAKURI(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdltakuri'] = cdltakuri

    return ohlc


def get_cdltasukigap(ohlc):
    cdltasukigap = ta.CDLTASUKIGAP(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdltasukigap'] = cdltasukigap

    return ohlc


def get_cdlthrusting(ohlc):
    cdlthrusting = ta.CDLTHRUSTING(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlthrusting'] = cdlthrusting

    return ohlc


def get_cdltristar(ohlc):
    cdltristar = ta.CDLTRISTAR(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdltristar'] = cdltristar

    return ohlc



def get_cdlunique3river(ohlc):
    cdlunique3river = ta.CDLUNIQUE3RIVER(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlunique3river'] = cdlunique3river

    return ohlc



def get_cdlupsidegap2crows(ohlc):
    cdlupsidegap2crows = ta.CDLUPSIDEGAP2CROWS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlupsidegap2crows'] = cdlupsidegap2crows

    return ohlc



def get_cdlxsidegap3methods(ohlc):
    cdlxsidegap3methods = ta.CDLXSIDEGAP3METHODS(ohlc['1_open'], ohlc['2_high'], ohlc['3_low'], ohlc['4_close'])

    ohlc['cdlxsidegap3methods'] = cdlxsidegap3methods

    return ohlc

