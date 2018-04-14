from datetime import datetime

import pandas as pd
import talib as ta

from lib.datasets import csv
from lib.prepare import feature_extraction
from lib.prepare import talib
from lib.utils import matplotlib


def main():
    print(datetime.now())
    print(ta.get_function_groups())

    ohlc = csv.load_csv_file('USDJPY.hst_.csv')

    feature_extraction.extract_for_fx_by_m1_vectorize(ohlc)

    df = pd.DataFrame(index=ohlc.index)
    df['0_openTime'] = ohlc['0_openTime']

    macd = talib.get_macd(ohlc)
    rsi = talib.get_rsi(ohlc)

    df = pd.concat([macd, rsi], axis=1)

    matplotlib.show_line3(df.macd, df.macdsignal, df.macdhist, df['0_openTime'])


if __name__ == '__main__':
    main()
