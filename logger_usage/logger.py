import sys

from loguru import logger as _logger
from typing import Optional
import os


class CustomLogger:
    def __init__(self, log_file=sys.stderr, level="DEBUG"):
        self.logger = _logger
        self._log_file = log_file
        self._level = level
        self._format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<blue>[{extra[request_id]}]</blue> |"
            "{process.name} | "
            "{thread.name} | "
            "<cyan>{module}</cyan>.<cyan>{function}</cyan>"
            ":<cyan>{line}</cyan> | "
            "<level>{level}</level> | "
            "<blue><level>{message}</level></blue>"
        )

        self.logger.remove()
        self.logger.add(
            self._log_file, level=self._level, format=self._format, enqueue=True
        )

    def get_logger(self):
        return self.logger

    def set_level(self, log_level):
        self._level = log_level
        self.logger.remove()
        self.logger.add(
            self._log_file, level=self._level, format=self._format, enqueue=True
        )

    def set_output(self, log_file=sys.stderr):
        self._log_file = log_file
        self.logger.remove()
        self.logger.add(
            self._log_file, level=self._level, format=self._format, enqueue=True
        )


CustomLog = CustomLogger()
logger = CustomLog.get_logger()


if __name__ == "__main__":
    import os
    import uuid

    log_level = os.environ.get("LOG_LEVEL", "DEBUG")
    user_id = str(uuid.uuid4())
    with logger.contextualize(request_id=user_id):
        CustomLog.set_level(log_level)
        logger.info("hello world!")
        logger.debug("Nice!")
        logger.info("Nice to meet you!")
