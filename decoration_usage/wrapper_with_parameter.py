import logging
from functools import wraps


def logged(level, name=None, message=None):
    """
    Add logging to function. if name and message aren't specified, they default to the funcion's module and name.
    :param level: level is the logging level
    :param name: name is the logger name
    :param message: message is the log message.
    :return:
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

add(1, 2)

spam()