from fxlib import get_module_logger
from fxlib.datasets import csv
from fxlib.learning.fit import bayesian_executor

logger = get_module_logger(__name__)


def main():
    df = csv.load_csv_file('USDJPY.extracted.csv', True)
    df = df.dropna(how='any')
    print(df.head())

    df = df.drop('0_openTime', axis=1)

    X = df.iloc[:, :-1]
    print(X.head())
    y = df.iloc[:, -1:]
    print(y.head())

    bayesian_executor.tune(X, y)

    # y = df[
    #     '1_11_M2_range'
    #     , '1_12_M3_range'
    #     , '1_13_M5_range'
    #     , '1_14_M15_range'
    #     , '1_15_M30_range'
    #     , '1_16_M60_range'
    #     , '1_17_M240_range']


if __name__ == '__main__':
    main()
