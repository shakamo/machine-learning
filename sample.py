from lib.datasets import csv
from lib.ml import executor
from lib.pd import utils


def main():
    # PD_DataFrame取得
    X, y = csv.load_boston_data()
    utils.info(X, y)

    # X, y = csv.load_csv_file_with_split_Xy("USDJPY.hst_.csv")
    # utils.info(X, y)

    # X = csv.load_csv_file("USDJPY.hst_.csv")
    # utils.info(X)

    executor.executor(X, y, chart=False, test_size=0.1)


if __name__ == '__main__':
    main()
