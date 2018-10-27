import pandas as pd
from sklearn.datasets import *


def load_boston_data():
    """データセットを取得する
    米国ボストン市郊外における地域別の住宅価格
    regression
    """
    dataset = load_boston()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y


def load_iris_data():
    """データセットを取得する
    3 種類の品種のアヤメのがく片、花弁の幅および長さ　
    classification"""
    dataset = load_iris()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y


def load_diabetes_data():
    """データセットを取得する
    糖尿病患者の検査数値と1年後の疾患進行状況　
    regression"""
    dataset = load_diabetes()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y


def load_digits_data():
    """データセットを取得する
    0~9の手書き文字の8×8画像
    classification"""
    dataset = load_digits()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y


def load_linnerud_data():
    """データセットを取得する
    成人男性の生理学的特徴と運動能力
    multivariate regression"""
    dataset = load_linnerud()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y


def load_wine_data():
    """データセットを取得する
    3種類のワインの科学的特徴
    classification"""
    dataset = load_iris()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y


def load_breast_cancer_data():
    """データセットを取得する
    乳がんの診断結果
    classification"""
    dataset = load_breast_cancer()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = pd.DataFrame(dataset.target, columns=['y'])
    return X, y
