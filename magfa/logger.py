"""
 * magfa client
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2025 - ali sharifi
 * https://github.com/alisharify7/magfa-client
"""

import logging
import sys


def get_logger(
    log_level: int, logger_name: str = "Flask-Captcha"
) -> logging.Logger:
    """create a custom stdout Logger with given level and name

    :param logger_name: name of the logger
    :type logger_name: str

    :param log_level: logging level
    :type log_level: int

    :return: logging.Logger
    :rtype: logging.Logger
    """
    log_level = log_level or logging.DEBUG
    logformat = logging.Formatter(
        f"[{logger_name}" + "- %(levelname)s] [%(asctime)s] - %(message)s"
    )
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    handler.setFormatter(logformat)
    logger.addHandler(handler)
    return logger