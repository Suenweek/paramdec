from pytest import raises
from tests.utils import fraise
from examples.reraise import reraise


def test_no_exc_raised():
    with raises(RuntimeError):
        reraise(catch=ValueError, throw=RuntimeError)(
            lambda: fraise(ValueError)
        )()
