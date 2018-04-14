import numpy as np


def extract_for_fx_by_m1_vectorize(df):
    df = df.assign(X1_1_M1_range=lambda df: df.apply(lambda row: row['2_high'] - row['3_low'], axis=1))
    df = df.assign(X1_2_M1_upper_beard=lambda df: df.apply(lambda row: row['2_high'] - row['1_open'], axis=1))
    df = df.assign(X1_3_M1_lower_beard=lambda df: df.apply(lambda row: row['4_close'] - row['3_low'], axis=1))
    df = df.assign(X1_4_M1_trend=lambda df: df.apply(lambda row: row['1_open'] - row['4_close'], axis=1))

    func_range_vectorize = np.vectorize(X_range_vectorize, excluded=[1, 2, 3])
    func_upper_beard_vectorize = np.vectorize(X_upper_beard_vectorize, excluded=[1, 2, 3])
    func_lower_beard_vectorize = np.vectorize(X_lower_beard_vectorize, excluded=[1, 2, 3])
    func_trend_vectorize = np.vectorize(X_trend_vectorize, excluded=[1, 2, 3])
    func_y_vectorize = np.vectorize(y_vectorize, excluded=[1, 2])

    print('processing... X')

    df['X1_11_M2_range'] = func_y_vectorize(df.index, df['2_high'], df['3_low'], 2)
    df['X1_12_M3_range'] = func_y_vectorize(df.index, df['2_high'], df['3_low'], 3)
    df['X1_13_M5_range'] = func_y_vectorize(df.index, df['2_high'], df['3_low'], 5)
    df['X1_14_M15_range'] = func_y_vectorize(df.index, df['2_high'], df['3_low'], 15)
    df['X1_15_M30_range'] = func_y_vectorize(df.index, df['2_high'], df['3_low'], 30)
    df['X1_16_M60_range'] = func_y_vectorize(df.index, df['2_high'], df['3_low'], 60)
    df['X1_17_M240_range'] = func_y_vectorize(df.index, df['2_high'], df['3_low'], 240)

    print('processing... X2')

    df['X2_1_M2_range'] = func_range_vectorize(df.index, df['2_high'], df['3_low'], 2)
    df['X2_2_M2_upper_beard'] = func_upper_beard_vectorize(df.index, df['2_high'], df['1_open'], 2)
    df['X2_3_M2_lower_beard'] = func_lower_beard_vectorize(df.index, df['4_close'], df['3_low'], 2)
    df['X2_4_M2_trend'] = func_trend_vectorize(df.index, df['1_open'], df['4_close'], 2)

    print('processing... X3')

    df['X3_1_M3_range'] = func_range_vectorize(df.index, df['2_high'], df['3_low'], 3)
    df['X3_2_M3_upper_beard'] = func_upper_beard_vectorize(df.index, df['2_high'], df['1_open'], 3)
    df['X3_3_M3_lower_beard'] = func_lower_beard_vectorize(df.index, df['4_close'], df['3_low'], 3)
    df['X3_4_M3_trend'] = func_trend_vectorize(df.index, df['1_open'], df['4_close'], 3)

    print('processing... X5')

    df['X5_1_M5_range'] = func_range_vectorize(df.index, df['2_high'], df['3_low'], 5)
    df['X5_2_M5_upper_beard'] = func_upper_beard_vectorize(df.index, df['2_high'], df['1_open'], 5)
    df['X5_3_M5_lower_beard'] = func_lower_beard_vectorize(df.index, df['4_close'], df['3_low'], 5)
    df['X5_4_M5_trend'] = func_trend_vectorize(df.index, df['1_open'], df['4_close'], 5)

    print('processing... X15')

    df['X15_1_M15_range'] = func_range_vectorize(df.index, df['2_high'], df['3_low'], 15)
    df['X15_2_M15_upper_beard'] = func_upper_beard_vectorize(df.index, df['2_high'], df['1_open'], 15)
    df['X15_3_M15_lower_beard'] = func_lower_beard_vectorize(df.index, df['4_close'], df['3_low'], 15)
    df['X15_4_M15_trend'] = func_trend_vectorize(df.index, df['1_open'], df['4_close'], 15)

    print('processing... X30')

    df['X30_1_M30_range'] = func_range_vectorize(df.index, df['2_high'], df['3_low'], 30)
    df['X30_2_M30_upper_beard'] = func_upper_beard_vectorize(df.index, df['2_high'], df['1_open'], 30)
    df['X30_3_M30_lower_beard'] = func_lower_beard_vectorize(df.index, df['4_close'], df['3_low'], 30)
    df['X30_4_M30_trend'] = func_trend_vectorize(df.index, df['1_open'], df['4_close'], 30)

    print('processing... X60')

    df['X60_1_M60_range'] = func_range_vectorize(df.index, df['2_high'], df['3_low'], 60)
    df['X60_2_M60_upper_beard'] = func_upper_beard_vectorize(df.index, df['2_high'], df['1_open'], 60)
    df['X60_3_M60_lower_beard'] = func_lower_beard_vectorize(df.index, df['4_close'], df['3_low'], 60)
    df['X60_4_M60_trend'] = func_trend_vectorize(df.index, df['1_open'], df['4_close'], 60)

    print('processing... X240')

    df['X240_1_M240_range'] = func_range_vectorize(df.index, df['2_high'], df['3_low'], 240)
    df['X240_2_M240_upper_beard'] = func_upper_beard_vectorize(df.index, df['2_high'], df['1_open'], 240)
    df['X240_3_M240_lower_beard'] = func_lower_beard_vectorize(df.index, df['4_close'], df['3_low'], 240)
    df['X240_4_M240_trend'] = func_trend_vectorize(df.index, df['1_open'], df['4_close'], 240)

    return df


def X_range_vectorize(index, x, y, m_size):
    # high low
    if index - m_size + 1 < 0:
        return 0
    if index < 0:
        return 0

    a = x.ix[index - m_size + 1:index]
    b = y.ix[index - m_size + 1:index]

    return a.max() - b.min()


def X_upper_beard_vectorize(index, x, y, m_size):
    # high open
    if index - m_size + 1 < 0:
        return 0
    if index < 0:
        return 0

    a = x.ix[index - m_size + 1:index]
    b = y.ix[index - m_size + 1:index - m_size + 1]

    return a.max() - b.min()


def X_lower_beard_vectorize(index, x, y, m_size):
    # close low
    if index - m_size + 1 < 0:
        return 0
    if index < 0:
        return 0

    a = x.ix[index:index]
    b = y.ix[index - m_size + 1:index]

    return a.min() - b.min()


def X_trend_vectorize(index, x, y, m_size):
    # open close
    if index - m_size + 1 < 0:
        return 0
    if index < 0:
        return 0

    a = x.ix[index - m_size + 1:index - m_size + 1]
    b = y.ix[index:index]

    return a.min() - b.min()


def y_vectorize(index, x, y, m_size):
    if index - m_size + 1 < 0:
        return 0
    if index < 0:
        return 0

    a = x.ix[index:index + m_size - 1].dropna()
    b = y.ix[index:index + m_size - 1].dropna()

    return a.mean() - b.mean()
