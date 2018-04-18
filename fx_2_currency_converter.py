# python fx_2_currency_converter.py -f USDJPY.hst -ty old

import argparse
import struct
import time

import pandas as pd

from lib import get_input_path
from lib import get_module_logger

logger = get_module_logger(__name__)

HEADER_SIZE = 148
OLD_FILE_STRUCTURE_SIZE = 44
NEW_FILE_STRUCTURE_SIZE = 60


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', default='USDJPY.hst')
    parser.add_argument('-ty', '--filetype', default='old')
    args = parser.parse_args()

    filename = args.filename
    filetype = args.filetype

    if filename is None:
        print("Enter a valid filename (-f)")
        quit()

    if filetype != "new" and filetype != "old":
        print("Enter a valid filetype (valid options are old and new)")
        quit()

    read = 0
    open_time = []
    open_price = []
    low_price = []
    high_price = []
    close_price = []
    volume = []

    with open(get_input_path().joinpath(filename), 'rb') as f:
        while True:

            if read >= HEADER_SIZE:

                if filetype == "old":
                    buf = f.read(OLD_FILE_STRUCTURE_SIZE)
                    read += OLD_FILE_STRUCTURE_SIZE

                if filetype == "new":
                    buf = f.read(NEW_FILE_STRUCTURE_SIZE)
                    read += NEW_FILE_STRUCTURE_SIZE

                if not buf:
                    break

                if filetype == "old":
                    bar = struct.unpack("<iddddd", buf)
                    open_time.append(
                        time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.gmtime(bar[0])))
                    open_price.append(bar[1])
                    high_price.append(bar[3])
                    low_price.append(bar[2])
                    close_price.append(bar[4])
                    volume.append(bar[5])
                if filetype == "new":
                    bar = struct.unpack("<Qddddqiq", buf)
                    print(bar)
                    print(bar[0])
                    open_time.append(
                        time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.gmtime(bar[0])))
                    open_price.append(bar[1])
                    high_price.append(bar[2])
                    low_price.append(bar[3])
                    close_price.append(bar[4])
                    volume.append(bar[5])

            else:
                buf = f.read(HEADER_SIZE)
                read += HEADER_SIZE

    data = {
        '0_openTime': open_time,
        '1_open': open_price,
        '2_high': high_price,
        '3_low': low_price,
        '4_close': close_price,
        '5_volume': volume
    }

    result = pd.DataFrame.from_dict(data)
    result = result.set_index('0_openTime')
    result.columns = ['1_open', '2_high', '3_low', '4_close', '5_volume']
    print(result)

    result.to_csv(get_input_path().joinpath(filename + '_.csv'), header=True)


if __name__ == "__main__":
    main()
