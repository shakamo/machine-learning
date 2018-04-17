# python 1_historical_data_downloader.py -f USDJPY.hst -u http://tools.fxdd.com/tools/M1Data/USDJPY.zip

import argparse
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent.resolve().parent.resolve()
sys.path.append(str(ROOT))


def download():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', default='USDJPY')
    parser.add_argument('-u', '--url', default='http://tools.fxdd.com/tools/M1Data/USDJPY.zip')
    args = parser.parse_args()

    filename = args.filename
    url = args.url

    urllib.request.urlretrieve(url, ROOT.joinpath('input').joinpath("{0}".format(filename) + ".zip"))

    with zipfile.ZipFile(ROOT.joinpath('input').joinpath("{0}".format(filename) + ".zip"), 'r') as inputFile:
        inputFile.extractall(ROOT.joinpath('input'))


if __name__ == "__main__":
    download()
