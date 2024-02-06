import enum
import logging
import logging.config

from functools import wraps
from inspect import ismethod

import config.consts as consts


logger = logging.getLogger(consts.LOGGER_NAME)


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
            "filename": f"../logs/{consts.APP_NAME}.log",
            "maxBytes": 1, # 16384,
            "backupCount": 16,
        }
    },
    "loggers": {
        consts.LOGGER_NAME: {
            "level": "DEBUG",
            "handlers": ["stdout", "stderr", "file"],
        }
    }
}

logging.config.dictConfig(config)


class LogLevel(enum.IntEnum):  # Values from logging module into enum
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0


def log(level: LogLevel = LogLevel.INFO, message=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            real_message = f" with message: {message}" if message else ""
            logger.log(level, f"function ({func.__name__}) called{real_message}")
            return func(*args, **kwargs)

        return wrapper

    return decorator
