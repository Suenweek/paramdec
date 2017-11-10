from pytest import raises
from .utils import raise_runtime_error_when_called
from examples.stringwrap import stringwrap, START_DEFAULT, END_DEFAULT


START_CUSTOM, END_CUSTOM = "<custom>", "</custom>"
FOO, BAR = "foo", "bar"


def test_paramdec_called_as_decorator():
    @stringwrap
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_no_args():
    @stringwrap()
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_first_kwarg():
    @stringwrap(start=START_CUSTOM)
    def foo(): return FOO
    assert foo() == START_CUSTOM + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_second_kwarg():
    @stringwrap(end=END_CUSTOM)
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_CUSTOM


def test_paramdec_called_as_factory_with_both_kwargs():
    @stringwrap(start=START_CUSTOM, end=END_CUSTOM)
    def foo(): return FOO
    assert foo() == START_CUSTOM + FOO + END_CUSTOM


def test_paramdec_called_as_factory_with_single_callable_pos_arg():
    with raises(RuntimeError):
        @stringwrap(raise_runtime_error_when_called)
        def foo(): return FOO


def test_paramdec_called_as_factory_with_single_callable_pos_arg_and_one_kwarg():
    @stringwrap(raise_runtime_error_when_called, start=START_DEFAULT)
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_as_factory_with_single_non_callable_pos_arg():
    @stringwrap(BAR)
    def foo(): return FOO
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_paramdec_called_with_unexpected_kwargs():
    with raises(TypeError):
        @stringwrap(unexpected_kwarg=BAR)
        def foo(): return FOO


def test_paramdec_called_twice():
    @stringwrap(start=START_CUSTOM, end=END_CUSTOM)
    @stringwrap
    def foo(): return FOO
    assert foo() == START_CUSTOM + START_DEFAULT + FOO + END_DEFAULT + END_CUSTOM
