import datetime
from itertools import islice
from pprint import pprint as pp
from gendates import gen_special_pybites_dates


def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    result = list(islice(gen, 5))
    expected = [datetime.datetime(2017, 3, 29, 0, 0),
                datetime.datetime(2017, 7, 7, 0, 0),
                datetime.datetime(2017, 10, 15, 0, 0),
                datetime.datetime(2018, 1, 23, 0, 0),
                datetime.datetime(2018, 5, 3, 0, 0)]
    assert result == expected





