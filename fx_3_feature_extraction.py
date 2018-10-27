# 2 month(60000)
#  python fx_3_feature_extraction.py
# 1 Year
#  python fx_3_feature_extraction.py -t 1
# 2 Year
#  python fx_3_feature_extraction.py -t 2

import argparse
from datetime import datetime

import fxlib
import fxlib.datasets as datasets
from fxlib.prepare import features, talib
from fxlib.utils import ohlc

logger = fxlib.get_module_logger(__name__)


def main():
    print(datetime.now())

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', default='0')
    args = parser.parse_args()

    df = ohlc.get_data(args.time)

    df = features.extract(df)

    df = talib.extract(df)

    datasets.csv.save_csv_file('USDJPY.extracted.csv', df)

    print(datetime.now())


if __name__ == '__main__':
    main()
