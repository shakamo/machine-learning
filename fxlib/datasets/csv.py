import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).parent.parent.parent.joinpath('input')


def load_csv_file(file_name, without_header=True, dtype={}, parse_dates={}):
    """CSVファイルを読み込む

    Keyword arguments:
        file_name -- ファイル名
        without_header -- CSVのヘッダーを除くかどうか

    """
    if without_header is True:
        def parser(date): return pd.to_datetime(
            date, format='%Y-%m-%d %H:%M:%S')
        df = pd.read_csv(ROOT.joinpath(file_name), header=0,
                         parse_dates=['0_openTime'], date_parser=parser)
        return df.iloc[:]
    else:
        df = pd.read_csv(ROOT.joinpath(file_name), header=None,
                         dtype=dtype, parse_dates=parse_dates)
        return df.iloc[:]


def save_csv_file(file_name, df):
    """CSVファイルを書き出す

    Keyword arguments:
        file_name -- ファイル名

    """
    df.to_csv(ROOT.joinpath(file_name))


def load_csv_file_with_split_Xy(file_name, without_header=True):
    """CSVファイルを読み込む

    Keyword arguments:
        file_name -- ファイル名
        without_header -- CSVのヘッダーを除くかどうか

    """
    if without_header is True:
        df = pd.read_csv(ROOT.joinpath(file_name), header=0)
        # 全行対象,最終カラム以外をXとする
        X = df.iloc[:, :-1]
        # 全行対象,最終カラムをyとする
        y = df.iloc[:, [-1]]
    else:
        df = pd.read_csv(ROOT.joinpath(file_name), header=None)
        # 全行対象,最終カラム以外をXとする
        X = df.iloc[:, :-1]
        # 全行対象,最終カラムをyとする
        y = df.iloc[:, [-1]]

    return X, y
