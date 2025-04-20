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
    log_level: int = logging.DEBUG, logger_name: str = "MagfaClient-LOGGER"
) -> logging.Logger:
    """Create a custom stdout logger with the given level and name.

    :param logger_name: Name of the logger.
    :param log_level: Logging level.
    :return: Configured logger.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Prevent adding multiple handlers if logger is already configured
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(log_level)
        formatter = logging.Formatter(
            f"[{logger_name}" + " - %(levelname)s] [%(asctime)s] - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
