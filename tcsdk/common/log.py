
import logging

from tcsdk.common import default

logger = logging.getLogger(__name__)


def init_logger(name=default.NAME, level=default.LOGGER_LEVEL):
    global logger
    format_string = "%(asctime)s %(name)s [%(levelname)s] %(thread)d : %(message)s"
    logger = logging.getLogger(name)
    logger.setLevel(level)
    fh = logging.StreamHandler()
    fh.setLevel(level)
    formatter = logging.Formatter(format_string)
    fh.setFormatter(formatter)
    logger.addHandler(fh)