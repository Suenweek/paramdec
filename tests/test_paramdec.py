from functools import wraps
from pytest import raises
from paramdec import paramdec


START_DEFAULT, END_DEFAULT = "<default>", "</default>"
START_CUSTOM, END_CUSTOM = "<custom>", "</custom>"
FOO, BAR = "foo", "bar"


def raise_runtime_error_when_called(*args, **kwargs):
    raise RuntimeError


@paramdec
def string_wrap(func, start=START_DEFAULT, end=END_DEFAULT):
    @wraps(func)
    def wrapper(*func_args, **func_kwargs):
        return start + func(*func_args, **func_kwargs) + end
    return wrapper


def test_paramdec_called_as_decorator():
    @string_wrap
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_no_args():
    @string_wrap()
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_first_kwarg():
    @string_wrap(start=START_CUSTOM)
    def foo(): return FOO
    assert foo() == START_CUSTOM + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_second_kwarg():
    @string_wrap(end=END_CUSTOM)
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_CUSTOM


def test_paramdec_called_as_factory_with_both_kwargs():
    @string_wrap(start=START_CUSTOM, end=END_CUSTOM)
    def foo(): return FOO
    assert foo() == START_CUSTOM + FOO + END_CUSTOM


def test_paramdec_called_as_factory_with_single_callable_pos_arg():
    with raises(RuntimeError):
        @string_wrap(raise_runtime_error_when_called)
        def foo(): return FOO


def test_paramdec_called_as_factory_with_single_callable_pos_arg_and_one_kwarg():
    @string_wrap(raise_runtime_error_when_called, start=START_DEFAULT)
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_single_non_callable_pos_arg():
    @string_wrap(BAR)
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_with_unexpected_kwargs():
    with raises(TypeError):
        @string_wrap(unexpected_kwarg=BAR)
        def foo(): return FOO


def test_paramdec_called_twice():
    @string_wrap(start=START_CUSTOM, end=END_CUSTOM)
    @string_wrap
    def foo(): return FOO
    assert foo() == START_CUSTOM + START_DEFAULT + FOO + END_DEFAULT + END_CUSTOM
