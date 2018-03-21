import xgboost as xgb
from sklearn.model_selection import GridSearchCV


def XG_BOOSTING():
    xgb_model = xgb.XGBRegressor()
    return GridSearchCV(xgb_model,
                        {'max_depth': [2, 4, 6],
                         'n_estimators': [50, 100, 200]}, verbose=1)
