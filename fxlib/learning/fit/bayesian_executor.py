import GPyOpt
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from fxlib.learning.kernel import kernels
from fxlib.learning.pipelines import xgboosting_pipelines
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def tune(X, y, chart=False, test_size=0.2, random_state=42):
    # name = 'xgboosting2'
    # d = kernels.domains[name]
    #
    # opt = GPyOpt.methods.BayesianOptimization(f=lambda x: _optimize(x, name, X, y), domain=d)
    # opt.run_optimization(max_iter=15)
    # a1, a2 = np.split(opt.X, 2, axis=1)
    # matplotlib.show_2d(a1, a2, -opt.Y, 'eta', 'learning_rate')
    # https://pythondatascience.plavox.info/matplotlib/%E6%95%A3%E5%B8%83%E5%9B%B3

    name = 'xgboosting3'
    d = kernels.domains[name]

    opt = GPyOpt.methods.BayesianOptimization(
        f=lambda x: _optimize(x, name, X, y), domain=d)
    opt.run_optimization(max_iter=5)
    a1, a2, a3 = np.split(opt.X, 3, axis=1)
    # matplotlib.show_3d(a1, a2, a3, np.squeeze(-opt.Y), 'eta', 'learning_rate', 'max_depth')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter(a1, a2, a3, c=np.squeeze(-opt.Y))
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    plt.show()


def _optimize(params, name, X, y):
    model = xgboosting_pipelines.Bayesian_XG_BOOSTING(np.ravel(params), name)
    kfold = KFold(n_splits=2, random_state=42)

    return -cross_val_score(model, X, y, cv=kfold, scoring='r2').mean()
