from lib.datasets import toy
from lib.learning.fit import xgboosting_executor
from lib.utils import log


def main():
    X, y = toy.load_boston_data()
    log.info(X, y)
    xgboosting_executor.learn(X, y.as_matrix().ravel(), chart=False)


if __name__ == '__main__':
    main()
