"""
Contains the core of $package: ... , etc.

NOTE: this module is private. All functions and objects are available in the main
`$package` namespace - use that instead.

"""

import logging
import sys
import traceback
from logging import CRITICAL, DEBUG, ERROR, FATAL, INFO, NOTSET, WARN, WARNING
from typing import TYPE_CHECKING, Mapping

if TYPE_CHECKING:
    from logging import _ExcInfoType, _Level


_ANSI_RESET = "\x1b[0m"
_ANSI_LEVEL_COLORS = {
    DEBUG: "\x1b[36m",
    INFO: "\x1b[32m",
    WARNING: "\x1b[33m",
    ERROR: "\x1b[31m",
    CRITICAL: "\x1b[35m",
}


__all__ = [
    "get_logger",
    "CRITICAL",
    "DEBUG",
    "ERROR",
    "FATAL",
    "INFO",
    "NOTSET",
    "WARN",
    "WARNING",
    "critical",
    "debug",
    "error",
    "fatal",
    "info",
    "warn",
    "warning",
    "log",
]


def get_logger(
    name: str | None = None, level: "_Level | None" = None
) -> logging.Logger:
    """
    Return a logger with the specified name, creating it and adding a
    default handler if necessary.

    Parameters
    ----------
    name : str | None, optional
        Logger name, by default None. If not specified, use `__name__`
        of the calling function's module.
    level : _Level | None, optional
        Specifies logging level of the logger.

    Returns
    -------
    logging.Logger
        Logger with the specified name.

    """

    if name is None:
        name = __get_module_name()
    if name == "__main__":
        name = None
    logger = logging.getLogger(name)
    logger.propagate = False
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = __get_formatter(handler)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    if level is not None:
        logger.setLevel(level)
    return logger


class _AnsiColorFormatter(logging.Formatter):
    """Format log output with ANSI colors by level."""

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        color = _ANSI_LEVEL_COLORS.get(record.levelno)
        if color is None:
            return message
        return f"{color}{message}{_ANSI_RESET}"


def __get_formatter(handler: logging.StreamHandler) -> logging.Formatter:
    fmt = "%(levelname)s:%(name)s:%(message)s"
    stream = getattr(handler, "stream", None)
    if stream is not None and hasattr(stream, "isatty") and stream.isatty():
        return _AnsiColorFormatter(fmt)
    return logging.Formatter(fmt)


def critical(
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with severity 'CRITICAL' on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).critical(
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def debug(
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with severity 'DEBUG' on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).debug(
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def error(
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with severity 'ERROR' on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).error(
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def fatal(
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with severity 'CRITICAL' on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).critical(
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def info(
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with severity 'INFO' on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).info(
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def warn(
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with severity 'WARNING' on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).warning(
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def warning(
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with severity 'WARNING' on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).warning(
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def log(
    level: int,
    msg: object,
    *args: object,
    exc_info: "_ExcInfoType" = None,
    line_info: bool = False,
    stack_info: bool = False,
    stacklevel: int = 1,
    extra: Mapping[str, object] | None = None,
) -> None:
    """Log 'msg % args' with the integer severity `level` on the module logger."""
    if line_info:
        msg = __add_line_info(msg, stacklevel)
        stack_info = False
    get_logger(__get_module_name()).log(
        level,
        msg,
        *args,
        exc_info=exc_info,
        stack_info=stack_info,
        stacklevel=stacklevel,
        extra=extra,
    )


def __get_module_name() -> str:
    frame = sys._getframe(2)  # pylint: disable=protected-access
    return frame.f_globals["__name__"]


def __add_line_info(msg: str, stacklevel: int) -> str:
    stack = traceback.extract_stack()[-max(stacklevel + 2, 1)]
    msg = (
        f"{msg}\n  file {stack.filename}, line {stack.lineno}, in {stack.name}"
        f"\n    {stack.line}"
    )
    return msg
