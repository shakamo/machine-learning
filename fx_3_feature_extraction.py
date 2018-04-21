import argparse
from datetime import datetime
import pandas as pd

import talib as ta

from lib import get_module_logger
from lib.datasets import csv
from lib.prepare import feature_extraction
from lib.prepare import talib

logger = get_module_logger(__name__)


def main():
    print(datetime.now())
    print(ta.get_function_groups())

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', default='0')
    args = parser.parse_args()

    ohlc = get_ohlc_data(args.time)

    ohlc = feature_extraction.extract_for_fx_by_m1_vectorize(ohlc)

    ohlc = ohlc.sort_index(axis=0, ascending=True)

    ohlc = talib.extract_for_fx_by_m1(ohlc)

    ohlc = ohlc.dropna(how='any')
    csv.save_csv_file('USDJPY.new.csv', ohlc)

    print(datetime.now())


def get_ohlc_data(time_span):
    dtype = {
        '0_openTime': 'object', '1_open': 'float16', '2_high': 'float16', '3_low': 'float16', '4_close': 'float16',
        '5_volume': 'int16'
    }

    ohlc = csv.load_csv_file('USDJPY.hst_.csv', dtype=dtype, parse_dates=['0_openTime'])
    print(ohlc.dtypes)
    # print(ohlc.describe())

    ohlc = ohlc.sort_index(axis=0, ascending=False)
    if time_span == '0':
        ohlc = ohlc.iloc[0:400]
    else:
        a = float(time_span) * 372000
        ohlc = ohlc.iloc[0:int(a)]

    return ohlc


if __name__ == '__main__':
    main()
