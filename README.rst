Paramdec
========

Description:
------------

Paramdec is a convenient way to create parametrized decorators.

Usage:
------

Create your decorator:

>>> from paramdec import paramdec
>>> @paramdec
... def my_dec(func, foo=42, bar=None):
...     def wrapper(*func_args, **func_kwargs):
...         # Process foo and bar
...         return func(*func_args, **func_kwargs)
...     return wrapper

Use it with parameters:

>>> @my_dec(bar="bar")
>>> def func(): pass

Or without parameters:

>>> @my_dec  # Parentheses are optional
>>> def func(): pass

Consider using ``functools.wraps`` for your decorators.
