"""
* magfa client
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/magfa-client
"""

import logging

from magfa.logger import get_logger


class LoggerMixin:
    """
    A mixin class that provides a reusable logging interface using Python's logging module.

    This mixin sets up a logger for any class that inherits from it. The logger can be used
    to print debug messages and helps in consistent logging throughout the application.

    Example usage:
        class MyClass(LoggerMixin):
            def __init__(self):
                super().__init__(logger_name="MyClassLogger")
                self.log("Logger initialized.")

    :param log_level: Logging level (e.g., logging.DEBUG, logging.INFO).
    :param logger_name: Name of the logger instance.
    """

    def __init__(
        self,
        log_level: int = logging.DEBUG,
        logger_name: str = "MagfaClient",
        debug: bool = False,
    ):
        """
        Initialize the LoggerMixin with a given log level and logger name.

        :param log_level: Logging level to use (default is logging.DEBUG).
        :param logger_name: Name of the logger (default is "MagfaClient").
        """
        self._logger_name = logger_name
        self._log_level = log_level
        self._logger = None
        self.debug = debug
        self.setup_logger()

    @property
    def logger(self) -> logging.Logger:
        """
        Get the logger instance, initializing it if necessary.

        :return: Configured logger instance.
        """

        if self._logger is None:
            self.setup_logger()
        return self._logger

    def setup_logger(self) -> None:
        """
        Set up the logger using the get_logger utility function.
        Ensures that the logger is only initialized once.
        """
        if self._logger is None:
            self._logger = get_logger(
                log_level=self._log_level, logger_name=self._logger_name
            )

    def log(self, message: str) -> None:
        """
        Log a debug-level message using the configured logger.

        :param message: Message to log.
        """
        if self.debug:
            self.logger.debug(message)
