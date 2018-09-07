from functools import wraps


def paramdec(dec):
    """
    Create parametrized decorator.

    >>> from paramdec import paramdec
    >>>
    >>> @paramdec
    ... def dec(func, foo=42, bar=None):
    ...     def wrapper(*func_args, **func_kwargs):
    ...         # Process foo and bar
    ...         return func(*func_args, **func_kwargs)
    ...     return wrapper
    """
    @wraps(dec)
    def wrapper(func=None, **dec_kwargs):
        if callable(func) and not dec_kwargs:
            return dec(func)
        return lambda real_func: dec(real_func, **dec_kwargs)
    return wrapper


__all__ = ("paramdec",)
