import os

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).parent.resolve().parent.resolve().parent.resolve().joinpath('input')


def load_csv_file(file_name, without_header=True, dtype = {}):
    """CSVファイルを読み込む

    Keyword arguments:
        file_name -- ファイル名
        without_header -- CSVのヘッダーを除くかどうか

    """
    if without_header is True:
        df = pd.read_csv(ROOT.joinpath(file_name), header=0, dtype = dtype)
        return df.iloc[:]
    else:
        df = pd.read_csv(ROOT.joinpath(file_name), header=None, dtype = dtype)
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
