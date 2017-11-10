from pytest import raises
from examples.typecheck import accepts, returns


@accepts(types=(int, int))
@returns(type_=int)
def multiply_ints(a, b):
    if a == 6 and b == 9:
        return 42.0
    else:
        return a * b


def test_typecheck_all_types_are_correct():
    assert multiply_ints(2, 2) == 4


def test_typecheck_incorrect_first_arg_type():
    with raises(TypeError):
        multiply_ints(2.0, 2)


def test_typecheck_incorrect_second_arg_type():
    with raises(TypeError):
        multiply_ints(2, 2.0)


def test_typecheck_both_args_types_are_incorrect():
    with raises(TypeError):
        multiply_ints(2.0, 2.0)


def test_typecheck_incorrect_return_type():
    with raises(TypeError):
        multiply_ints(6, 9)
