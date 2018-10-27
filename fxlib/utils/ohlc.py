import fxlib.datasets


def get_data(time_span):
    dtype = {
        '0_openTime': 'object', '1_open': 'float16', '2_high': 'float16', '3_low': 'float16', '4_close': 'float16',
        '5_volume': 'int16'
    }

    ohlc = fxlib.datasets.csv.load_csv_file('USDJPY.csv', dtype=dtype, parse_dates=['0_openTime'])
    print(ohlc.dtypes)
    # print(ohlc.describe())

    ohlc = ohlc.sort_index(axis=0, ascending=False)
    if time_span == '0':
        a = 60000
    else:
        a = float(time_span) * 372000

    print('time_span : ' + str(a))
    ohlc = ohlc.iloc[0:int(a)]

    ohlc = ohlc.sort_index(axis=0, ascending=True)
    return ohlc
