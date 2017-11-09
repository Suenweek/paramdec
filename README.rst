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
... def my_dec(func, *dec_args, **dec_kwargs):
...     def wrapper(*func_args, **func_kwargs):
...         # Process dec_args and dec_kwargs
...         return func(*func_args, **func_kwargs)
...     return wrapper

Use it with parameters:

>>> @my_dec(42, foo="bar")
>>> def func(): pass

Or without parameters:

>>> @my_dec  # Parentheses are optional
>>> def func(): pass

Consider using ``functools.wraps`` for your decorators.
