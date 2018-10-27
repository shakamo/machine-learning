import os
import datetime
import pathlib
import joblib

import numpy as np
import xgboost as xgb
from matplotlib import pyplot

from fxlib.learning.pipelines import xgboosting_pipelines

ROOT = pathlib.Path(__file__).parent.parent.parent.parent.joinpath('output')


def extract(df):
    func_datetime_vectorize = np.vectorize(datetime_vectorize, excluded=[1, 2])
    func_range_vectorize = np.vectorize(X_range_vectorize, excluded=[1, 2, 3])
    func_upper_beard_vectorize = np.vectorize(
        X_upper_beard_vectorize, excluded=[1, 2, 3])
    func_lower_beard_vectorize = np.vectorize(
        X_lower_beard_vectorize, excluded=[1, 2, 3])
    func_trend_vectorize = np.vectorize(X_trend_vectorize, excluded=[1, 2, 3])
    func_y_vectorize = np.vectorize(y_vectorize, excluded=[1, 2])

    # 1分足のレンジ、上ヒゲ、下ヒゲ、トレンドを算出
    df = df.assign(X1_1_M1_range=lambda df: df.apply(
        lambda row: row['2_high'] - row['3_low'], axis=1))
    df = df.assign(X1_2_M1_upper_beard=lambda df: df.apply(
        lambda row: row['2_high'] - row['1_open'], axis=1))
    df = df.assign(X1_3_M1_lower_beard=lambda df: df.apply(
        lambda row: row['4_close'] - row['3_low'], axis=1))
    df = df.assign(X1_4_M1_trend=lambda df: df.apply(
        lambda row: row['1_open'] - row['4_close'], axis=1))

    # 各足の平均の差
    labels = ['Y1_11_M2_range', 'Y1_11_M3_range', 'Y1_11_M5_range',
              'Y1_11_M15_range', 'Y1_11_M30_range', 'Y1_11_M60_range',
              'Y1_11_M240_range']
    multijob(df, df['2_high'], df['3_low'], func_y_vectorize, labels)

    labels = ['X2_1_M2_range', 'X2_1_M3_range', 'X2_1_M5_range',
              'X2_1_M15_range', 'X2_1_M30_range', 'X2_1_M60_range',
              'X2_1_M240_range']
    multijob(df, df['2_high'], df['3_low'], func_range_vectorize, labels)

    print('processing... X2')

    labels = ['X2_2_M2_upper_beard', 'X2_3_M3_upper_beard',
              'X2_2_M5_upper_beard',     'X2_2_M15_upper_beard',
              'X2_2_M30_upper_beard', 'X2_2_M60_upper_beard',
              'X2_2_M240_upper_beard']
    multijob(df, df['2_high'], df['3_low'], func_upper_beard_vectorize, labels)

    labels = ['X2_3_M2_lower_beard', 'X2_3_M3_lower_beard',
              'X2_3_M5_lower_beard', 'X2_3_M15_lower_beard',
              'X2_3_M30_lower_beard', 'X2_3_M60_lower_beard',
              'X2_3_M240_lower_beard']
    multijob(df, df['2_high'], df['3_low'], func_lower_beard_vectorize, labels)

    labels = ['X2_4_M2_trend', 'X2_4_M3_trend', 'X2_4_M5_trend',
              'X2_4_M15_trend', 'X2_4_M30_trend', 'X2_4_M60_trend',
              'X2_4_M240_trend']
    multijob(df, df['2_high'], df['3_low'], func_trend_vectorize, labels)

    return df


def multijob(df, seriesA, seriesB, func, labels):
    # 各足の平均の差
    datas = [(df.index, seriesA, seriesB, 2),
             (df.index, seriesA, seriesB, 3),
             (df.index, seriesA, seriesB, 5),
             (df.index, seriesA, seriesB, 15),
             (df.index, seriesA, seriesB, 30),
             (df.index, seriesA, seriesB, 60),
             (df.index, seriesA, seriesB, 240)]

    processed = joblib.Parallel(
        n_jobs=-1, verbose=3)(
            [joblib.delayed(func)(
                data[0], data[1], data[2], data[3]) for data in datas])

    y2 = processed[0]
    y3 = processed[1]
    y5 = processed[2]
    y15 = processed[3]
    y30 = processed[4]
    y60 = processed[5]
    y240 = processed[6]

    # 平均化され、ノーマライズされたレンジ値
    df[labels[0]] = normalize(y2)
    df[labels[1]] = normalize(y3)
    df[labels[2]] = normalize(y5)
    df[labels[3]] = normalize(y15)
    df[labels[4]] = normalize(y30)
    df[labels[5]] = normalize(y60)
    df[labels[6]] = normalize(y240)


def normalize(series):
    return np.where(
        series < 0.015, 0, np.where(
            series < 0.03, 0.015, np.where(
                series < 0.05, 0.03, np.where(
                    series < 0.10, 0.05, np.where(
                        series < 0.2, 0.1, np.where(
                            series < 0.3, 0.2, np.where(
                                series < 0.4, 0.3, np.where(
                                    series < 0.5, 0.4, np.nan))))))))


def datetime_vectorize(index, x):
    a = x.ix[index:index]
    return a.values.astype('datetime64[h]').astype(datetime)[0].strftime('%H')


def y_vectorize(index, x, y, m_size):
    """
    果物の値段を取得する。

    Parameters
    ----------
    index : int
        Pandas Index.
    x : Pandas
    """
    a = x.ix[index - m_size + 1:index]
    b = y.ix[index - m_size + 1:index]

    if len(a) != m_size:
        return np.nan

    return a.mean() - b.mean()


def X_range_vectorize(index, x, y, m_size):
    # high low
    a = x.ix[index - m_size + 1:index]
    b = y.ix[index - m_size + 1:index]

    if len(a) != m_size:
        return np.nan

    return a.max() - b.min()


def X_upper_beard_vectorize(index, x, y, m_size):
    # high open
    a = x.ix[index - m_size + 1:index]
    b = y.ix[index - m_size + 1:index - m_size + 1]

    if len(a) != m_size:
        return np.nan

    return a.max() - b.min()


def X_lower_beard_vectorize(index, x, y, m_size):
    # close low
    a = x.ix[index:index]
    b = x.ix[index - m_size + 1:index]

    if len(b) != m_size:
        return np.nan

    return a.min() - b.min()


def X_trend_vectorize(index, x, y, m_size):
    # open close
    a = x.ix[index - m_size + 1:index - m_size + 1]
    b = y.ix[index:index]

    if len(a) != 1:
        return np.nan

    return b.min() - a.min()


def importance(X, y, chart=False):
    pipeline = xgboosting_pipelines.XG_BOOSTING4()

    print(X.head())
    print(y.head())
    pipeline.fit(X, y)

    if chart is True:
        xgb.plot_importance(pipeline.steps[1][1], color=[
                            'r', 'r', 'b', 'b'], title=None, xlabel=None, ylabel=None)
        pyplot.savefig(str(ROOT) + '/' + str(datetime.now()) + ".png")
        pyplot.show()
