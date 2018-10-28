import numpy as np
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def XG_BOOSTING1():
    return Pipeline([('scl', StandardScaler()), ('est', xgb.XGBRegressor())])


def XG_BOOSTING2():
    max_depth = 9
    min_child_weight = 10
    subsample = 1.0
    colsample_bytree = 0.5
    num_estimators = 3000
    learning_rate = 0.009

    model = xgb.XGBRegressor(max_depth=max_depth,
                             min_child_weight=min_child_weight,
                             subsample=subsample,
                             colsample_bytree=colsample_bytree,
                             n_estimators=num_estimators,
                             learning_rate=learning_rate,
                             gamma=0.2,
                             scale_pos_weight=1
                             )

    return Pipeline([('scl', StandardScaler()), ('est', model)])


def XG_BOOSTING3():
    max_depth = 7
    min_child_weight = 9
    subsample = 0.5
    colsample_bytree = 0.6
    objective = 'reg:linear'
    num_estimators = 800
    learning_rate = 0.005

    model = xgb.XGBRegressor(max_depth=max_depth,
                             min_child_weight=min_child_weight,
                             subsample=subsample,
                             colsample_bytree=colsample_bytree,
                             objective=objective,
                             n_estimators=num_estimators,
                             learning_rate=learning_rate)

    return Pipeline([('scl', StandardScaler()), ('est', model)])


def XG_BOOSTING4():
    max_depth = 10
    num_estimators = 3000
    learning_rate = 0.01

    model = xgb.XGBRegressor(max_depth=max_depth,
                             n_estimators=num_estimators,
                             learning_rate=learning_rate
                             )

    return Pipeline([('scl', StandardScaler()), ('est', model)])


def TUNE_XG_BOOSTING():
    model = GridSearchCV(xgb.XGBRegressor(),
                         {
                             'eta': np.arange(0.01, 0.21, 0.01),
                             'learning_rate': np.arange(0.001, 0.01, 0.001),
                             'max_depth': np.arange(6, 8, 1),
                             'min_child_weight': np.arange(6, 11, 1),
                             'gamma': [2],
                             'subsample': [1],
                             'colsample_bytree': np.arange(0.4, 0.71, 0.1),
                             'scale_pos_weight': [1],
                             'objective': ['reg:linear'],
                             'nthread': [4]
    }, scoring='r2', cv=10
    )

    return Pipeline([('scl', StandardScaler()), ('est', model)])


kernel2domains = {
    'full': [
        {'name': 'eta', 'type': 'continuous', 'domain': (0.01, 0.3)},
        {'name': 'min_child_weigh', 'type': 'continuous', 'domain': (1, 10)},
        {'name': 'max_depth', 'type': 'continuous', 'domain': (3, 10)},
        {'name': 'gamma', 'type': 'continuous', 'domain': (0, 0.5)},
        {'name': 'subsample', 'type': 'continuous', 'domain': (0, 1)},
        {'name': 'colsample_bytree', 'type': 'continuous', 'domain': (0.5, 1)},
        {'name': 'n_estimators', 'type': 'continuous', 'domain': (100, 5000)},
        {'name': 'learning_rate', 'type': 'continuous', 'domain': (0.001, 0.3)}
    ],
    'middle': [
        {'name': 'learning_rate', 'type': 'continuous',
            'domain': (0.00005, 0.1)},
        {'name': 'gamma', 'type': 'continuous', 'domain': (0.00005, 0.0015)}
    ],
    'low': [
        {'name': 'learning_rate', 'type': 'continuous',
            'domain': (0.00005, 0.1)},
    ]
}


def Bayesian_XG_BOOSTING(params, name):
    print(_refine_param(params, name))

    model = xgb.XGBRegressor(**_refine_param(params, name))

    return Pipeline([('scl', StandardScaler()), ('est', model)])


def _refine_param(param, kernel):
    assert kernel in ['rbf', 'linear',
                      'xgboosting', 'xgboosting2', 'xgboosting3']
    if kernel == 'rbf':
        return {'kernel': kernel, 'learning_rate': param[0], 'eta': param[1]}
    elif kernel == 'xgboosting':
        return {
            'kernel': kernel,
            'eta': round(param[0], 2),
            'min_child_weigh': int(param[1] + 0.5),
            'max_depth': int(param[2] + 0.5),
            'gamma': round(param[3], 1),
            'subsample': int(param[4] + 0.5),
            'colsample_bytree': round(param[5], 1),
            'n_estimators': int(param[6] + 0.5),
            'learning_rate': round(param[7], 3)
        }
    elif kernel == 'xgboosting2':
        return {
            'kernel': kernel,
            'eta': round(param[0], 2),
            'learning_rate': round(param[1], 3)
        }
    elif kernel == 'xgboosting3':
        return {
            'kernel': kernel,
            'eta': round(param[0], 2),
            'learning_rate': round(param[1], 3),
            'max_depth': int(param[2] + 0.5)
        }
    else:
        return {'kernel': kernel, 'learning_rate': param[0]}
