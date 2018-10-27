from fxlib import get_module_logger
from fxlib.datasets import csv
from fxlib.prepare import features
from fxlib.utils import *

logger = get_module_logger(__name__)


def main():
    df = csv.load_csv_file('USDJPY.extracted.csv', True, parse_dates=['0_openTime'])
    df = df.set_index('0_openTime')
    df = df.resample('15T').interpolate()

    df = df.drop('Unnamed: 0', axis=1)
    df = df.dropna(how='any')

    y = df['Y1_11_M15_range']
    X = df.drop('Y1_11_M15_range', axis=1)

    # X = X.drop('X15_1_M15_range', axis=1)

    for i in range(len(X.columns.values)):
        list_item = X.columns.values[i]
        print('{0}:{1}'.format(i, list_item))

    features.importance(X, y, chart=True)


if __name__ == '__main__':
    main()
