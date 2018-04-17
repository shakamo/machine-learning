from lib.datasets import csv
from lib.learning.fit import bayesian_executor


def main():
    dtype = {
        '1_1_M1_range': 'float16', '1_2_M1_upper_beard': 'float16', '1_3_M1_lower_beard': 'float16',
        '1_4_M1_trend': 'float16', '2_1_M2_range': 'float16',
        '2_2_M2_upper_beard': 'float16', '2_3_M2_lower_beard': 'float16', '2_4_M2_trend': 'float16',
        '3_1_M3_range': 'float16',
        '3_2_M3_upper_beard': 'float16', '3_3_M3_lower_beard': 'float16', '3_4_M3_trend': 'float16',
        '5_1_M5_range': 'float16',
        '5_2_M5_upper_beard': 'float16', '5_3_M5_lower_beard': 'float16', '5_4_M5_trend': 'float16',
        '15_1_M15_range': 'float16',
        '15_2_M15_upper_beard': 'float16', '15_3_M15_lower_beard': 'float16', '15_4_M15_trend': 'float16',
        '30_1_M30_range': 'float16',
        '30_2_M30_upper_beard': 'float16', '30_3_M30_lower_beard': 'float16', '30_4_M30_trend': 'float16',
        '60_1_M60_range': 'float16',
        '60_2_M60_upper_beard': 'float16', '60_3_M60_lower_beard': 'float16', '60_4_M60_trend': 'float16',
        '240_1_M240_range': 'float16',
        '240_2_M240_upper_beard': 'float16', '240_3_M240_lower_beard': 'float16', '240_4_M240_trend': 'float16'
        , '1_11_M2_range': 'float16'
        , '1_12_M3_range': 'float16'
        , '1_13_M5_range': 'float16'
        , '1_14_M15_range': 'float16'
        , '1_15_M30_range': 'float16'
        , '1_16_M60_range': 'float16'
        , '1_17_M240_range': 'float16'
    }

    df = csv.load_csv_file('USDJPY.new.csv', True, dtype)
    print(df.head())

    X = df.loc[:, ['1_1_M1_range', '1_2_M1_upper_beard', '1_3_M1_lower_beard', '1_4_M1_trend', '2_1_M2_range',
                   '2_2_M2_upper_beard', '2_3_M2_lower_beard', '2_4_M2_trend', '3_1_M3_range',
                   '3_2_M3_upper_beard', '3_3_M3_lower_beard', '3_4_M3_trend', '5_1_M5_range',
                   '5_2_M5_upper_beard', '5_3_M5_lower_beard', '5_4_M5_trend', '15_1_M15_range',
                   '15_2_M15_upper_beard', '15_3_M15_lower_beard', '15_4_M15_trend', '30_1_M30_range',
                   '30_2_M30_upper_beard', '30_3_M30_lower_beard', '30_4_M30_trend', '60_1_M60_range',
                   '60_2_M60_upper_beard', '60_3_M60_lower_beard', '60_4_M60_trend', '240_1_M240_range',
                   '240_2_M240_upper_beard', '240_3_M240_lower_beard', '240_4_M240_trend']]
    y = df.loc[:, ['1_14_M15_range']]

    print(X.head())

    bayesian_executor.tune(X, y)

    # y = df[
    #     '1_11_M2_range'
    #     , '1_12_M3_range'
    #     , '1_13_M5_range'
    #     , '1_14_M15_range'
    #     , '1_15_M30_range'
    #     , '1_16_M60_range'
    #     , '1_17_M240_range']


if __name__ == '__main__':
    main()
