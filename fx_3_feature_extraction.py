import argparse
from datetime import datetime

import talib as ta

from lib import get_module_logger
from lib.datasets import csv
from lib.prepare import features
from lib.prepare import talib
from lib.utils import ohlc

logger = get_module_logger(__name__)


def main():
    print(datetime.now())
    print(ta.get_function_groups())

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', default='0')
    args = parser.parse_args()

    df = ohlc.get_data(args.time)

    df = features.extract(df)

    df = talib.extract(df)

    csv.save_csv_file('USDJPY.M1.csv', df)

    print(datetime.now())


if __name__ == '__main__':
    main()
