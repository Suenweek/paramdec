from functools import wraps
from paramdec import paramdec


def test_paramdec():
    @paramdec
    def test_dec(func, *dec_args, **dec_kwargs):
        @wraps(func)
        def wrapper(*func_args, **func_kwargs):
            return func(*func_args, **func_kwargs)
        return wrapper

    @test_dec
    def to_nth_power(n, p):
        return n ** p

    to_nth_power(2, 16)
