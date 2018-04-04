from functools import wraps
from paramdec import paramdec


@paramdec
def reraise(func, catch=Exception, throw=Exception):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except catch as e:
            raise throw(*e.args)
    return wrapper
