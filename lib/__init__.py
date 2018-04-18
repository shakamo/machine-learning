import sys
from logging import getLogger, StreamHandler, DEBUG, Formatter
from pathlib import Path

from . import datasets
from . import learning
from . import prepare
from . import utils

ROOT = Path(__file__).parent.resolve().parent.resolve()
print(str(ROOT))
sys.path.append(str(ROOT))


def get_module_logger(module_name):
    logger = getLogger(module_name)
    handler = StreamHandler()
    formatter = Formatter('my-format')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(DEBUG)
    return logger


def get_input_path():
    return ROOT.joinpath('input')
