def fit(name, pipeline, X, y, n_splits=10, random_state=42, debug_log=False):
    # 学習モデル作成
    pipeline.fit(X, y)

    if pipeline.steps[1][1].__class__.__name__ == 'GridSearchCV':
        pipeline.steps[1][1].fit(X, y)
        print(pipeline.steps[1][1].best_params_)
