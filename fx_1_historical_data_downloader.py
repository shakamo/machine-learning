# python fx_1_historical_data_downloader.py -f USDJPY.hst -u http://tools.fxdd.com/tools/M1Data/USDJPY.zip

import argparse
import urllib.request
import zipfile

from lib import get_input_path
from lib import get_module_logger

logger = get_module_logger(__name__)


def download():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', default='USDJPY')
    parser.add_argument('-u', '--url', default='http://tools.fxdd.com/tools/M1Data/USDJPY.zip')
    args = parser.parse_args()

    filename = args.filename
    url = args.url

    urllib.request.urlretrieve(url, get_input_path().joinpath("{0}".format(filename) + ".zip"))

    with zipfile.ZipFile(get_input_path().joinpath("{0}".format(filename) + ".zip"), 'r') as inputFile:
        inputFile.extractall(get_input_path())


if __name__ == "__main__":
    download()
