import logging
import os
import shutil
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

from src.utilities.constants import LOGGING, LOGGING_LOG_FILE_PATH, LOGGING_MAX_FILE_SIZE, LOGGING_BACKUP_COUNT, \
    LOGGING_FILE_LOG_LEVEL, LOGGING_CONSOLE_LOG_LEVEL
from src.utilities.properties import Properties


def setup_logger():
    log_console_format = '%(levelname)s:%(message)s'
    log_file_format = '%(levelname)s:%(asctime)s %(message)s'

    logger = logging.getLogger(__name__)
    logger.setLevel(level=0)

    file_name = Properties.get(LOGGING).get(LOGGING_LOG_FILE_PATH)
    directory = "".join(file_name.split("/")[:-1])
    if not os.path.exists(directory):
        os.makedirs(directory)
    clean_directory(directory)
    rf_handler = RotatingFileHandler(file_name, maxBytes=Properties.get(LOGGING).get(LOGGING_MAX_FILE_SIZE),
                                     backupCount=Properties.get(LOGGING).get(LOGGING_BACKUP_COUNT))
    rf_handler.setLevel(level=Properties.get(LOGGING).get(LOGGING_FILE_LOG_LEVEL))
    rf_handler.setFormatter(logging.Formatter(log_file_format))
    logger.addHandler(rf_handler)

    console_handler = StreamHandler()
    console_handler.setLevel(level=Properties.get(LOGGING).get(LOGGING_CONSOLE_LOG_LEVEL))
    console_handler.setFormatter(logging.Formatter(log_console_format))
    logger.addHandler(console_handler)

    logging.basicConfig(level=0, handlers=[rf_handler, console_handler])


def clean_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
