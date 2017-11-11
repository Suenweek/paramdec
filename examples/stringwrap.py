from functools import wraps
from paramdec import paramdec


START_DEFAULT = END_DEFAULT = ""


@paramdec
def stringwrap(func, start=START_DEFAULT, end=END_DEFAULT):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "%s%s%s" % (start, func(*args, **kwargs), end)
    return wrapper
