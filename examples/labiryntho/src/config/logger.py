import os
import enum
import logging
import logging.config
import atexit

from functools import wraps
from typing import override

from .consts import *

logger = logging.getLogger(LOGGER_NAME)
os.makedirs(LOGS_DIR, exist_ok=True)


class StdoutLogFilter(logging.Filter):
    @override
    def filter(self, record: logging.LogRecord) -> bool | logging.LogRecord:
        return record.levelno < logging.INFO


class FileLogFilter(logging.Filter):
    @override
    def filter(self, record: logging.LogRecord) -> bool | logging.LogRecord:
        return record.levelno > logging.DEBUG


stdout_log_filter = StdoutLogFilter()
file_log_filter = FileLogFilter()

config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filters": [stdout_log_filter],
            "stream": "ext://sys.stdout",
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filters": [file_log_filter],
            "filename": f"{LOGS_DIR}/{APP_NAME}.log",
            "maxBytes": 4_194_304,
            "backupCount": 64,
        },
        "queue_handler": {
            "class": "logging.handlers.QueueHandler",
            "handlers": ["stdout", "stderr", "file"],
            "respect_handler_level": True
        },
    },
    "loggers": {
        LOGGER_NAME: {
            "level": "DEBUG",
            "handlers": ["queue_handler"],
        }
    }
}

logging.config.dictConfig(config)
queue_handler = logging.getHandlerByName("queue_handler")
if queue_handler is not None:
    queue_handler.listener.start()
    atexit.register(queue_handler.listener.stop)


class LogLevel(enum.IntEnum):
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def log(msg, level: LogLevel = LogLevel.DEBUG):
    logger.log(level, msg)


def log_func(level: LogLevel = LogLevel.DEBUG, msg=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            real_msg = f" with message: {msg}" if msg else ""
            log_msg = f"function ({func.__name__}) called{real_msg}"
            log(log_msg, level)
            return func(*args, **kwargs)

        return wrapper

    return decorator
