from lib.datasets import toy
from lib.learning.fit import standard_executor
from lib.utils import log


def main():
    X, y = toy.load_boston_data()
    log.info(X, y)
    standard_executor.learn(X, y.as_matrix().ravel(), chart=False, test_size=0.2)


if __name__ == '__main__':
    main()
