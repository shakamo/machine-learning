from joblib import Parallel, delayed

from lib.learning.pipelines import xgboosting_pipelines


def tune(X, y):
    futures = Parallel(n_jobs=-1)([
        delayed(fit)('TUNE_XG_BOOSTING', xgboosting_pipelines.TUNE_XG_BOOSTING(), X, y)
    ])


def fit(name, pipeline, X, y):
    # 学習モデル作成
    pipeline.fit(X, y)

    if pipeline.steps[1][1].__class__.__name__ == 'GridSearchCV':
        pipeline.steps[1][1].fit(X, y)
        print(pipeline.steps[1][1].best_params_)
