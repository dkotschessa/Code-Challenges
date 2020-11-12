import pytest
from defang_ip import Defang


params = [
    (
        "1.1.1.1", "1[.]1[.]1[.]1"
    ),
    (
        "255.100.50.0", "255[.]100[.]50[.]0"
    ),
    (
        "266.266.266.266", "Not a valid IP address"
    ),
    (
        "1.2.3.4.5", "Not a valid IP address"
    ),
           ]

@pytest.mark.parametrize("input, expected", params)
def test_defang(input, expected):
    assert Defang(input) == expected
