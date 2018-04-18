import os
import sys

sys.path.append(os.path.abspath(os.pardir))

from datetime import datetime


def main():
    print(os.path.abspath(os.pardir))
    print(datetime.now())
    print(datetime.now())


if __name__ == '__main__':
    main()
