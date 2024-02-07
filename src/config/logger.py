import enum
import logging
import logging.config

from functools import wraps

from .consts import *


logger = logging.getLogger(LOGGER_NAME)


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z"
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": f"{LOGS_DIR}/{APP_NAME}.log",
            "maxBytes": 16384,
            "backupCount": 16,
        }
    },
    "loggers": {
        LOGGER_NAME: {
            "level": "DEBUG",
            "handlers": ["stdout", "stderr", "file"],
        }
    }
}

logging.config.dictConfig(config)


class LogLevel(enum.IntEnum):  # Values from logging module into enum
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def log(msg, level: LogLevel = LogLevel.INFO):
    logger.log(level, msg)


def log_func(level: LogLevel = LogLevel.INFO, msg=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            real_msg = f" with message: {msg}" if msg else ""
            log_msg = f"function ({func.__name__}) called{real_msg}"
            log(log_msg, level)
            return func(*args, **kwargs)

        return wrapper

    return decorator
