Paramdec
========

Paramdec is a convenient way to create parametrized decorators.

Installation
------------

``pip install paramdec``

Usage
-----

Create your parametrized decorator:

>>> from paramdec import paramdec
>>>
>>> @paramdec
... def dec(func, foo=42, bar=None):
...     def wrapper(*func_args, **func_kwargs):
...         # Process foo and bar
...         return func(*func_args, **func_kwargs)
...     return wrapper

Use it with parameters:

>>> @dec(bar="bar")
... def func():
...     pass

Or without parameters:

>>> @dec()
... def func():
...     pass

Or even without parentheses:

>>> @dec
... def func():
...     pass

Also, consider using ``functools.wraps`` for your decorators.

Limitations
-----------

- No positional args supported.

The rationale behind this is the fact that there was not found any pythonic way
to make a decorator differentiate between a function to be decorated and a
callback. So if you pass a single callable positional argument to a
parametrized decorator, it will mistakenly decide that it was called not as a
factory but as a casual decorator.
