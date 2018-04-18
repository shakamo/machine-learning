import sys
from datetime import datetime
from pathlib import Path

import talib as ta

ROOT = Path(__file__).parent.resolve().parent.resolve()
sys.path.append(str(ROOT))

from lib.datasets import csv
from lib.prepare import feature_extraction
from lib.prepare import talib


def main():
    print(datetime.now())
    print(ta.get_function_groups())

    dtype = {
        '0_openTime': 'object', '1_open': 'float16', '2_high': 'float16', '3_low': 'float16', '4_close': 'float16',
        '5_volume': 'int16'
    }

    ohlc = csv.load_csv_file('USDJPY.hst_.csv', dtype=dtype)

    print(ohlc.dtypes)

    print(ohlc.describe())

    ohlc = ohlc.sort_index(axis=0, ascending=False)
    print(ohlc.head())

    #ohlc = ohlc.iloc[0:250]

    # 1 Year
    # ohlc = ohlc.iloc[0:372000]

    # 6 Month
    ohlc = ohlc.iloc[0:186000]

    ohlc = feature_extraction.extract_for_fx_by_m1_vectorize(ohlc)

    ohlc = ohlc.sort_index(axis=0, ascending=True)

    ohlc = talib.extract_for_fx_by_m1(ohlc)

    csv.save_csv_file('USDJPY.new.csv', ohlc)

    print(datetime.now())

if __name__ == '__main__':
    main()
