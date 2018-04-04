from pytest import raises
from .utils import fraise
from examples.stringwrap import stringwrap, START_DEFAULT, END_DEFAULT


START_CUSTOM, END_CUSTOM = "<custom>", "</custom>"
FOO, BAR = "foo", "bar"


def test_call_as_decorator():
    foo = stringwrap(lambda: FOO)
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_call_as_factory_with_no_args():
    foo = stringwrap()(lambda: FOO)
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_call_as_factory_with_first_kwarg():
    foo = stringwrap(start=START_CUSTOM)(lambda: FOO)
    assert foo() == START_CUSTOM + FOO + END_DEFAULT


def test_call_as_factory_with_second_kwarg():
    foo = stringwrap(end=END_CUSTOM)(lambda: FOO)
    assert foo() == START_DEFAULT + FOO + END_CUSTOM


def test_call_as_factory_with_both_kwargs():
    foo = stringwrap(start=START_CUSTOM, end=END_CUSTOM)(lambda: FOO)
    assert foo() == START_CUSTOM + FOO + END_CUSTOM


def test_call_as_factory_with_single_callable_pos_arg():
    with raises(RuntimeError):
        stringwrap(fraise)(RuntimeError)


def test_call_as_factory_with_single_callable_pos_arg_and_one_kwarg():
    foo = stringwrap(fraise, start=START_DEFAULT)(lambda: FOO)
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_call_as_factory_with_single_non_callable_pos_arg():
    foo = stringwrap(BAR)(lambda: FOO)
    assert foo() == START_DEFAULT + FOO + END_DEFAULT


def test_call_with_unexpected_kwargs():
    with raises(TypeError):
        stringwrap(unexpected_kwarg=BAR)(lambda: FOO)


def test_call_twice():
    foo = stringwrap(start=START_CUSTOM, end=END_CUSTOM)(stringwrap(lambda: FOO))
    assert foo() == START_CUSTOM + START_DEFAULT + FOO + END_DEFAULT + END_CUSTOM
