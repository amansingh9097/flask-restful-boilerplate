import logging.handlers
import os

from src.instance.config import config


def __setup_logger(filename):
    dev = True
    if dev:
        LOG_LOCATION = './logs/'
    else:
        try:
            LOG_LOCATION = os.environ['LOG_PATH'] + '/'
        except Exception as ex:
            print ('please setup env variable LOG_PATH')
            exit(1)

    # logfile settings
    LOG_FORMAT = "%(asctime)s [%(levelname)-5.5s] %(message)s"
    LOG_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
    LOG_PATH = LOG_LOCATION

    progressLogger = logging.getLogger(filename)
    progressLogger.setLevel(logging.DEBUG)
    rotatingfileHandler = logging.handlers.RotatingFileHandler(LOG_PATH + filename,
                                                               maxBytes=(1048576 * 5), backupCount=7)
    # log file handler
    logFormatter = logging.Formatter(LOG_FORMAT)
    rotatingfileHandler.setFormatter(logFormatter)
    progressLogger.addHandler(rotatingfileHandler)
    rotatingfileHandler.setLevel(logging.INFO)

    # console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    progressLogger.addHandler(consoleHandler)
    consoleHandler.setLevel(logging.INFO)
    return progressLogger

log_file = config['host_service']['name'] + ".log"
serviceLogger = __setup_logger(log_file)