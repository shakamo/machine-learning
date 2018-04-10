import sys,pth

from lib.datasets import toy, csv
from lib.utils import log
from lib.prepare import feature_extraction

from datetime import datetime

def main():
    print(datetime.now())

    digits = toy.load_digits()
    data = csv.load_csv_file('USDJPY.hst_.csv')

    # data.reset_index().set_index('0_openTime', inplace=True)
    # log.info(data)
    # data = data.iloc[-1000:]

    # feature_extraction.extract_for_fx_by_m1(data)

    # n_samples = len(digits.images)
    # X = digits.images.reshape(n_samples, -1)
    # y = digits.target
    #
    # bayesian_executor.tune(X, y)

    print(datetime.now())
    feature_extraction.extract_for_fx_by_m1_vectorize(data)
    print(datetime.now())

    csv.save_csv_file('USDJPY.new.csv', data)


if __name__ == '__main__':
    main()
