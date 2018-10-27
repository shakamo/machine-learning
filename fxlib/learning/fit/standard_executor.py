import plotly.offline as py
from joblib import Parallel, delayed
from plotly.graph_objs import *

from fxlib.learning.cv.cross_validation import *
from fxlib.learning.pipelines import standard_pipelines


def learn(X, y, chart=False, test_size=0.1, random_state=42):
    futures = Parallel(n_jobs=-1)([
        delayed(fit_and_predict)('LINER', standard_pipelines.STANDARD_LINER_REGRESSION(), X, y, test_size)
        , delayed(fit_and_predict)('RIDGE', standard_pipelines.STANDARD_RIDGE(), X, y, test_size)
        , delayed(fit_and_predict)('RANDOM_FOREST', standard_pipelines.RANDOM_FOREST(), X, y, test_size)
        , delayed(fit_and_predict)('GRADIENT_BOOSTING', standard_pipelines.GRADIENT_BOOSTING(), X, y, test_size)
        , delayed(kFold)('LINER', standard_pipelines.STANDARD_LINER_REGRESSION(), X, y)
        , delayed(kFold)('RIDGE', standard_pipelines.STANDARD_RIDGE(), X, y)
        , delayed(kFold)('RANDOM_FOREST', standard_pipelines.RANDOM_FOREST(), X, y)
        , delayed(kFold)('GRADIENT_BOOSTING', standard_pipelines.GRADIENT_BOOSTING(), X, y)
    ])
    if chart is True:
        py.offline.plot(
            list(map(lambda a: Scatter(x=a[1], mode='markers', name=a[0]), futures)))
