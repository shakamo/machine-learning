from lib.datasets import toy
from lib.learning.fit import bayesian_executor


def main():
    digits = toy.load_digits()

    n_samples = len(digits.images)
    X = digits.images.reshape(n_samples, -1)
    y = digits.target

    bayesian_executor.tune(X, y)


if __name__ == '__main__':
    main()
