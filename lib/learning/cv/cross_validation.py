from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from lib.utils import matplotlib

from xgboost import plot_importance
from matplotlib import pyplot

def fit_and_predict(name, pipeline, X, y, test_size=0.1, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # 学習モデル作成
    pipeline.fit(X_train, y_train)

    # 推定
    y_predicted = pipeline.predict(X_test)

    print('HoldOut %25s R2 score: %.5f' % (name, r2_score(y_test, y_predicted)))

    return name, y_predicted


def fit_and_importance(name, pipeline, X, y, test_size=0.1, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # 学習モデル作成
    pipeline.fit(X_train, y_train)

    return pipeline


def kFold(name, pipeline, X, y, n_splits=10, random_state=42, debug_log=False):
    # 学習モデル作成(fit)＆推定(fit)
    kfold = KFold(n_splits=n_splits, random_state=random_state)
    scores = cross_val_score(pipeline, X, y, cv=kfold, scoring='r2')

    if pipeline.steps[1][1].__class__.__name__ == 'GridSearchCV':
        pipeline.steps[1][1].fit(X, y)
        print(pipeline.steps[1][1].best_params_)

    if debug_log:
        # 各分割におけるスコア
        print('Cross-Validation scores: {}'.format(scores))

    # スコアの平均値
    print('kFold %27s R2 score: %.5f' % (name, scores.mean()))

    return name, scores.mean()
