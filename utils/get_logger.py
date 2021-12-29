# -*- coding: utf-8 -*-
# @Author  : Yingying
# @Time    : 2021/12/20 3:31 下午
# @Function:
import logging
import logging.handlers
from Config.config import ALL_LOG_PATH, ERROR_LOG_PATH


def get_logger(name=__name__,filename=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    rf_handler =logging.FileHandler(ALL_LOG_PATH)
    # rf_handler = logging.handlers.TimedRotatingFileHandler(ALL_LOG_PATH, when='midnight', interval=1, backupCount=7,
    #                                                        atTime=datetime.time)
    rf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))

    f_handler = logging.FileHandler(ERROR_LOG_PATH)
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)

    return logger