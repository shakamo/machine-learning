from lib import get_module_logger
from lib.datasets import csv
from lib.prepare import features
from lib.utils import *

logger = get_module_logger(__name__)


def main():
    df = csv.load_csv_file('USDJPY.M1.csv', True, parse_dates=['0_openTime'])

    print(df.info())
    print(df.describe())
    a = df['0_openTime']
    a = a.to_frame()
    a['macd_1440'] = df['macd_1440']
    a = a.set_index('0_openTime')
    print(a.info())
    print()
    print(a.head())
    print()

    b = a.resample('D').first()

    print(df['macd_1440'].head())

    print(a.info())
    print()
    print(b.info())
    print()
    print()
    print(a.head())
    print()
    print(b.head())

    matplotlib.show_line1(b['macd_1440'], b.index)


    df = df.drop('0_openTime', axis=1)
    df = df.drop('Unnamed: 0', axis=1)
    df = df.dropna(how='any')

    y = df['Y1_11_M15_range']

    X = df.drop('Y1_11_M15_range', axis=1)
    X = X.drop('X15_1_M15_range', axis=1)
    print(X.columns.values)

    for i in range(len(X.columns.values)):
        list_item = X.columns.values[i]
        print('{0}:{1}'.format(i, list_item))

    features.importance(X, y, chart=True)


if __name__ == '__main__':
    main()
