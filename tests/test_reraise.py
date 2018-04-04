from pytest import raises
from tests.utils import fraise
from examples.reraise import reraise


class ErrorA(Exception): pass
class ErrorB(Exception): pass
class ErrorC(Exception): pass


def test_raised_and_caught():
    with raises(ErrorB):
        reraise(catch=ErrorA, throw=ErrorB)(
            lambda: fraise(ErrorA)
        )()


def test_raised_but_not_caught():
    with raises(ErrorC):
        reraise(catch=ErrorA, throw=ErrorB)(
            lambda: fraise(ErrorC)
        )()


def test_not_raised():
    assert reraise(catch=ErrorA, throw=ErrorB)(
        lambda: 42
    )() == 42
