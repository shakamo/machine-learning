# python fx_1_historical_data_downloader.py
# python fx_1_historical_data_downloader.py -f USDJPY -u http://tools.fxdd.com/tools/M1Data/USDJPY.zip

import argparse
import urllib.request as req
import zipfile

import fxlib

logger = fxlib.get_module_logger(__name__)


def download():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', default='USDJPY')
    parser.add_argument(
        '-u', '--url', default='http://tools.fxdd.com/tools/M1Data/USDJPY.zip')
    args = parser.parse_args()

    filepath = fxlib.get_input_path().joinpath(args.filename + ".zip")

    req.urlretrieve(args.url, filepath)

    with zipfile.ZipFile(filepath, 'r') as inputFile:
        inputFile.extractall(fxlib.get_input_path())


if __name__ == "__main__":
    download()
