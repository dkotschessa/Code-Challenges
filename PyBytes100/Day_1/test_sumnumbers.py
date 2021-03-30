from sumnumbers import sum_numbers


def test_sum_numbers():
    result = sum_numbers([1, 1, 1, 1, 1])
    assert result == 5


def test_no_entry():
    result = sum_numbers()
    assert result == 5050
