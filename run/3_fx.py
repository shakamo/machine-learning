from datetime import datetime
from pathlib import Path
import os,sys

import talib as ta

ROOT = Path(__file__).parent.resolve().parent.resolve()
sys.path.append(str(ROOT))

from lib.datasets import csv
from lib.prepare import feature_extraction
from lib.prepare import talib


def main():
    print(datetime.now())
    print(ta.get_function_groups())

    ohlc = csv.load_csv_file('USDJPY.hst_.csv')

    ohlc = feature_extraction.extract_for_fx_by_m1_vectorize(ohlc)
    ohlc = talib.extract_for_fx_by_m1(ohlc)

    # matplotlib.show_line3(df.macd, df.macdsignal, df.macdhist, df['0_openTime'])


if __name__ == '__main__':
    main()
