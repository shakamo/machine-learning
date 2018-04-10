import os

import pandas as pd



def extract_for_fx_by_m1(df):

    df['1_1_M1_range'] = df['2_high'] - df['3_low']
    df['1_2_M1_upper_beard'] = df['2_high'] - df['1_open']
    df['1_3_M1_lower_beard'] = df['4_close'] - df['3_low']
    df['1_4_M1_trend'] = df['1_open'] - df['4_close']

    df['2_1_M2_range'] = df.apply(func=lambda x: range(x, df, 2), axis=1)
    df['2_2_M2_upper_beard'] = df.apply(func=lambda x: upper_beard(x, df, 2), axis=1)
    df['2_3_M2_lower_beard'] = df.apply(func=lambda x: lower_beard(x, df, 2), axis=1)
    df['2_4_M2_trend'] = df.apply(func=lambda x: trend(x, df, 2), axis=1)

    df['3_1_M3_range'] = df.apply(func=lambda x: range(x, df, 3), axis=1)
    df['3_2_M3_upper_beard'] = df.apply(func=lambda x: upper_beard(x, df, 3), axis=1)
    df['3_3_M3_lower_beard'] = df.apply(func=lambda x: lower_beard(x, df, 3), axis=1)
    df['3_4_M3_trend'] = df.apply(func=lambda x: trend(x, df, 3), axis=1)

    df['5_1_M5_range'] = df.apply(func=lambda x: range(x, df, 5), axis=1)
    df['5_2_M5_upper_beard'] = df.apply(func=lambda x: upper_beard(x, df, 5), axis=1)
    df['5_3_M5_lower_beard'] = df.apply(func=lambda x: lower_beard(x, df, 5), axis=1)
    df['5_4_M5_trend'] = df.apply(func=lambda x: trend(x, df, 5), axis=1)

    df['15_1_M15_range'] = df.apply(func=lambda x: range(x, df, 15), axis=1)
    df['15_2_M15_upper_beard'] = df.apply(func=lambda x: upper_beard(x, df, 15), axis=1)
    df['15_3_M15_lower_beard'] = df.apply(func=lambda x: lower_beard(x, df, 15), axis=1)
    df['15_4_M15_trend'] = df.apply(func=lambda x: trend(x, df, 15), axis=1)

    df['30_1_M30_range'] = df.apply(func=lambda x: range(x, df, 30), axis=1)
    df['30_2_M30_upper_beard'] = df.apply(func=lambda x: upper_beard(x, df, 30), axis=1)
    df['30_3_M30_lower_beard'] = df.apply(func=lambda x: lower_beard(x, df, 30), axis=1)
    df['30_4_M30_trend'] = df.apply(func=lambda x: trend(x, df, 30), axis=1)

    df['60_1_M60_range'] = df.apply(func=lambda x: range(x, df, 60), axis=1)
    df['60_2_M60_upper_beard'] = df.apply(func=lambda x: upper_beard(x, df, 60), axis=1)
    df['60_3_M60_lower_beard'] = df.apply(func=lambda x: lower_beard(x, df, 60), axis=1)
    df['60_4_M60_trend'] = df.apply(func=lambda x: trend(x, df, 60), axis=1)

    df['240_1_M240_range'] = df.apply(func=lambda x: range(x, df, 240), axis=1)
    df['240_2_M240_upper_beard'] = df.apply(func=lambda x: upper_beard(x, df, 240), axis=1)
    df['240_3_M240_lower_beard'] = df.apply(func=lambda x: lower_beard(x, df, 240), axis=1)
    df['240_4_M240_trend'] = df.apply(func=lambda x: trend(x, df, 240), axis=1)

    return df


def range(x, df, m_size):
    a = df.ix[x.name - m_size:x.name, '2_high']
    b = df.ix[x.name - m_size:x.name, '3_low']
    return a.max() - b.min()


def upper_beard(x, df, m_size):
    a = df.ix[x.name - m_size:x.name, '2_high']
    b = df.ix[x.name - m_size:x.name, '1_open']
    return a.max() - b.min()


def lower_beard(x, df, m_size):
    a = df.ix[x.name - m_size:x.name, '4_close']
    b = df.ix[x.name - m_size:x.name, '3_low']
    return a.max() - b.min()


def trend(x, df, m_size):
    a = df.ix[x.name - m_size:x.name, '1_open']
    b = df.ix[x.name - m_size:x.name, '4_close']
    return a.max() - b.min()



def extract_for_fx_by_m1_vectorize(df):

    df['1_1_M1_range'] = df['2_high'] - df['3_low']
    df['1_2_M1_upper_beard'] = df['2_high'] - df['1_open']
    df['1_3_M1_lower_beard'] = df['4_close'] - df['3_low']
    df['1_4_M1_trend'] = df['1_open'] - df['4_close']

    f_range_vectorize = lambda x: range(x, df['2_high'], df['3_low'], 2)
    func_range_vectorize = numpy.vectorize(f_range_vectorize)
    func_range_vectorize.excluded.add(1)
    func_range_vectorize.excluded.add(2)
    df['2_1_M2_range'] = pd.Series(np.vectorize(func_range_vectorize)(df.index), index=df.index)

    return df

def range_vectorize(x, high, low, m_size):
    a = high.ix[x - m_size:x] # '2_high'
    b = low.ix[x - m_size:x] # '3_low'
    return a.max() - b.min()


def upper_beard(x, df, m_size):
    a = df.ix[x.name - m_size:x.name, '2_high']
    b = df.ix[x.name - m_size:x.name, '1_open']
    return a.max() - b.min()


def lower_beard(x, df, m_size):
    a = df.ix[x.name - m_size:x.name, '4_close']
    b = df.ix[x.name - m_size:x.name, '3_low']
    return a.max() - b.min()


def trend(x, df, m_size):
    a = df.ix[x.name - m_size:x.name, '1_open']
    b = df.ix[x.name - m_size:x.name, '4_close']
    return a.max() - b.min()

