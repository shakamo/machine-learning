from logging import getLogger, StreamHandler, DEBUG, Formatter

def get_module_logger(module_name):
    logger = getLogger(module_name)
    handler = StreamHandler()
    formatter = Formatter('my-format')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(DEBUG)
    return logger
