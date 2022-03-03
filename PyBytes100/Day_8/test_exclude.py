from exclude import filter_bites

def test_filter_bites():
    bites = {1: 'bob', 2: 'julian', 3: 'tim'}
    exclude_bites = {2, 3}
    result = filter_bites(bites, exclude_bites)

    assert result == {1: 'bob'}