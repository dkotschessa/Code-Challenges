import pytest
from type_and_exceptions import divide_numbers


def test_raise_value_error():
    with pytest.raises(ValueError) as excinfo:
        divide_numbers('a', 'b')
    assert "invalid literal for int()" in str(excinfo.value)


def test_does_not_raise_zero_division_error():
    result = divide_numbers(1, 0)
    assert result == 0


params = [
    (
        '1', '2', 0.5
    ),
    (
        4.3, 5.6, .8
    ),
    (
        '5', 4, 1.25
    )

]


@pytest.mark.parametrize("numerator, denominator, expected", params)
def test_division(numerator, denominator, expected):
    result = divide_numbers(numerator, denominator)
    assert result == expected

