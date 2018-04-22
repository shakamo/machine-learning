from lib import get_module_logger
from lib.datasets import csv
from lib.prepare import features

logger = get_module_logger(__name__)


def main():
    df = csv.load_csv_file('USDJPY.new.csv', True)

    df = df.drop('0_openTime', axis=1)
    df = df.drop('Unnamed: 0', axis=1)
    df = df.dropna(how='any')

    y = df['Y1_11_M15_range']
    print('y')
    print(y.head())

    X = df.drop('Y1_11_M15_range', axis=1)
    print()
    print('X')
    print(X.head())
    print(X.columns.values)

    for i in range(len(X.columns.values)):
        list_item = X.columns.values[i]
        print('{0}:{1}'.format(i, list_item))

    features.extract(X, y, chart=True)


if __name__ == '__main__':
    main()
