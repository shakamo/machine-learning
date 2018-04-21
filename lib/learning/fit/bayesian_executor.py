import GPyOpt
import numpy as np
from matplotlib import pyplot
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from xgboost import plot_importance

from lib.learning.kernel import kernels
from lib.learning.pipelines import xgboosting_pipelines
from lib.utils import matplotlib


def tune(X, y, chart=False, test_size=0.2, random_state=42):
    # name = 'xgboosting2'
    # d = kernels.domains[name]
    #
    # opt = GPyOpt.methods.BayesianOptimization(f=lambda x: _optimize(x, name, X, y), domain=d)
    # opt.run_optimization(max_iter=15)
    # a1, a2 = np.split(opt.X, 2, axis=1)
    # matplotlib.show_2d(a1, a2, -opt.Y, 'eta', 'learning_rate')

    name = 'xgboosting3'
    d = kernels.domains[name]

    opt = GPyOpt.methods.BayesianOptimization(f=lambda x: _optimize(x, name, X, y), domain=d)
    opt.run_optimization(max_iter=5)
    a1, a2, a3 = np.split(opt.X, 3, axis=1)
    # matplotlib.show_3d(a1, a2, a3, np.squeeze(-opt.Y), 'eta', 'learning_rate', 'max_depth')


def _optimize(params, name, X, y):
    model = xgboosting_pipelines.Bayesian_XG_BOOSTING(np.ravel(params), name)
    kfold = KFold(n_splits=2, random_state=42)


    return -cross_val_score(model, X, y, cv=kfold, scoring='r2').mean()
