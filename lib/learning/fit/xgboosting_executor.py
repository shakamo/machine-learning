import plotly.offline as py
from joblib import Parallel, delayed
from plotly.graph_objs import *

from lib.learning.cv.cross_validation import *
from lib.learning.pipelines import xgboosting_pipelines


def learn(X, y, chart=False, test_size=0.2, random_state=42):
    futures = Parallel(n_jobs=-1)([
        delayed(fit_and_predict)('XG_BOOSTING1', xgboosting_pipelines.XG_BOOSTING1(), X, y, test_size)
        , delayed(fit_and_predict)('XG_BOOSTING2', xgboosting_pipelines.XG_BOOSTING2(), X, y, test_size)
        , delayed(fit_and_predict)('XG_BOOSTING3', xgboosting_pipelines.XG_BOOSTING3(), X, y, test_size)
        , delayed(kFold)('XG_BOOSTING1', xgboosting_pipelines.XG_BOOSTING1(), X, y)
        , delayed(kFold)('XG_BOOSTING2', xgboosting_pipelines.XG_BOOSTING2(), X, y)
        , delayed(kFold)('XG_BOOSTING3', xgboosting_pipelines.XG_BOOSTING3(), X, y)
    ])
    if chart is True:
        py.offline.plot(
            list(map(lambda a: Scatter(x=a[1], mode='markers', name=a[0]), futures)))
