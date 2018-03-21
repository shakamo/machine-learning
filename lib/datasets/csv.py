import os

import pandas as pd
from sklearn.datasets import load_boston

ROOT = os.path.dirname(os.path.abspath(os.pardir)) + "/"


def load_boston_data():
    """ボストンデータセットを取得する"""
    dataset = load_boston()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y


def load_csv_file(file_name, without_header=True):
    """CSVファイルを読み込む

    Keyword arguments:
        file_name -- ファイル名
        without_header -- CSVのヘッダーを除くかどうか

    """
    if without_header is True:
        df = pd.read_csv(ROOT + file_name, header=0)
        return df.iloc[:]
    else:
        df = pd.read_csv(ROOT + file_name, header=None)
        return df.iloc[:]


def load_csv_file_with_split_Xy(file_name, without_header=True):
    """CSVファイルを読み込む

    Keyword arguments:
        file_name -- ファイル名
        without_header -- CSVのヘッダーを除くかどうか

    """
    if without_header is True:
        df = pd.read_csv(ROOT + file_name, header=0)
        # 全行対象,最終カラム以外をXとする
        X = df.iloc[:, :-1]
        # 全行対象,最終カラムをyとする
        y = df.iloc[:, [-1]]
    else:
        df = pd.read_csv(ROOT + file_name, header=None)
        # 全行対象,最終カラム以外をXとする
        X = df.iloc[:, :-1]
        # 全行対象,最終カラムをyとする
        y = df.iloc[:, [-1]]

    return X, y
