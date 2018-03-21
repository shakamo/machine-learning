from concurrent.futures import ProcessPoolExecutor, as_completed

import plotly.offline as py
from plotly.graph_objs import *
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from lib.pd import pipelines


def executor(X, y, chart=False, test_size=0.2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    with ProcessPoolExecutor(max_workers=1) as executor:
        futures = [
            (executor.submit(standard_liner_regression, X_train, X_test, y_train, y_test))
            , executor.submit(standard_ridge, X_train, X_test, y_train, y_test)
            , executor.submit(standard_random_forest, X_train, X_test, y_train, y_test)
            , executor.submit(standard_gradient_boosting, X_train, X_test, y_train, y_test)]

        if chart is True:
            aa = list(map(lambda future: future.result(), as_completed(futures)))
            py.offline.plot(
                list(map(lambda a: Scatter(x=a[1], y=y_test.as_matrix().ravel(), mode='markers', name=a[0]), aa)))


def standard_liner_regression(X_train, X_test, y_train, y_test):
    # Pipeline
    pipeline = pipelines.STANDARD_LINER_REGRESSION()

    # 学習モデル作成
    pipeline.fit(X_train, y_train.as_matrix().ravel())

    # 推定
    y_predicted = pipeline.predict(X_test)

    print('R2 score:STANDARD LINER: %.6f' % r2_score(y_test, y_predicted))

    return 'OLS', y_predicted


def standard_ridge(X_train, X_test, y_train, y_test):
    # Pipeline
    pipeline = pipelines.STANDARD_RIDGE()

    # 学習モデル作成
    pipeline.fit(X_train, y_train.as_matrix().ravel())

    # 推定
    y_predicted = pipeline.predict(X_test)

    print('R2 score:STANDARD RIDGE: %.6f' % r2_score(y_test, y_predicted))

    return 'RIDGE', y_predicted


def standard_random_forest(X_train, X_test, y_train, y_test):
    # Pipeline
    pipeline = pipelines.RANDOM_FOREST()

    # 学習モデル作成
    pipeline.fit(X_train, y_train.as_matrix().ravel())

    # 推定
    y_predicted = pipeline.predict(X_test)

    print('R2 score:STANDARD RANDOM FOREST: %.6f' % r2_score(y_test, y_predicted))

    return 'random forest', y_predicted


def standard_gradient_boosting(X_train, X_test, y_train, y_test):
    # Pipeline
    pipeline = pipelines.GRADIENT_BOOSTING()

    # 学習モデル作成
    pipeline.fit(X_train, y_train.as_matrix().ravel())

    # 推定
    y_predicted = pipeline.predict(X_test)

    print('R2 score:STANDARD GRADIENT BOOSTING: %.6f' % r2_score(y_test, y_predicted))

    return 'gradient', y_predicted


def xg_boosting(X_train, X_test, y_train, y_test):
    # Pipeline
    pipeline = pipelines.XG_BOOSTING()

    # 学習モデル作成
    pipeline.fit(X_train, y_train.as_matrix().ravel())

    # 推定
    y_predicted = pipeline.predict(X_test)

    print('R2 score:XG BOOSTING: %.6f' % r2_score(y_test, y_predicted))

    return 'xg', y_predicted
