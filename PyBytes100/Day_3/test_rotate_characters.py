from rotate import rotate


def test_rotate_positive():
    result = rotate('hello', 2)
    expected = 'llohe'
    assert result == expected


def test_rotate_negative():
    result = rotate('hello', -2)
    expected = 'lohel'
    assert result == expected
