import os
import sys

sys.path.append(os.path.abspath(os.pardir))

from datetime import datetime

from lib.datasets import toy
from lib.learning.fit import tuning_executor
from lib.utils import log


def main():
    print(datetime.now())
    X, y = toy.load_boston_data()
    log.info(X, y)
    tuning_executor.tune(X, y.as_matrix().ravel(), chart=False)

    print(datetime.now())


if __name__ == '__main__':
    main()
