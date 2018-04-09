import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve().parent.resolve()
sys.path.append(ROOT)


from lib.datasets import toy, csv
from lib.utils import log
from lib.prepare import feature_extraction

from datetime import datetime


def main():
    print(Path(__file__).parent.resolve() + 'is run?')
    print(ROOT + 'is root')
    print(datetime.now())

    digits = toy.load_digits()
    data = csv.load_csv_file('USDJPY.hst_.csv')

    # data.reset_index().set_index('0_openTime', inplace=True)
    # log.info(data)
    # data = data.iloc[-100:]

    feature_extraction.extract_for_fx_by_m1(data)

    log.info(data)

    csv.save_csv_file('USDJPY.new.csv', data)

    # n_samples = len(digits.images)
    # X = digits.images.reshape(n_samples, -1)
    # y = digits.target
    #
    # bayesian_executor.tune(X, y)

    print(datetime.now())


if __name__ == '__main__':
    main()
