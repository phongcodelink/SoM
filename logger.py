import logging
import sys


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\x1b[0m'

    def __init__(self, log_prefix):
        super().__init__()
        self.FORMATS = {
            logging.DEBUG: log_prefix + self.grey + '\n%(message)s' + self.reset,
            logging.INFO: log_prefix + self.blue + '\n%(message)s' + self.reset,
            logging.WARNING: log_prefix + self.yellow + '\n%(message)s' + self.reset,
            logging.ERROR: log_prefix + self.red + '\n%(message)s' + self.reset,
            logging.CRITICAL: log_prefix +
                              self.bold_red + '\n%(message)s' + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%m-%d %H:%M")
        return formatter.format(record)


def get_logger():
    logger = logging.getLogger('uvicorn')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    handler.setFormatter(CustomFormatter(log_prefix='[%(asctime)s] [%(levelname)s] %(funcName)s()::%(lineno)d'))

    if (logger.hasHandlers()):
        logger.handlers.clear()

    logger.addHandler(handler)
    logger.propagate = False

    return logger
