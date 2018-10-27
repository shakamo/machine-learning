from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def STANDARD_LINER_REGRESSION():
    return Pipeline([('scl', StandardScaler()), ('est', LinearRegression())])


def STANDARD_RIDGE():
    return Pipeline([('scl', StandardScaler()), ('est', Ridge(random_state=1))])


def RANDOM_FOREST():
    return Pipeline([('scl', StandardScaler()), ('est', RandomForestRegressor(random_state=42))])


def GRADIENT_BOOSTING():
    return Pipeline([('scl', StandardScaler()), ('est', GradientBoostingRegressor(random_state=42))])
