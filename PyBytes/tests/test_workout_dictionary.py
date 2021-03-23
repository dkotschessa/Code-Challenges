import pytest
from workout_dictionary_lookups import get_workout_motd


params = [
    (
        'Friday', 'Go train Shoulders'
    ),
    (
        'Monday', 'Go train Chest+biceps'
    ),
    (
        'Saturday', 'Chill out!'
    ),
    (
        'Sunday', 'Chill out!'
    ),
    (
        'Thursday', 'Go train Legs'
    ),
    (
        'Tuesday', 'Go train Back+triceps'
    ),
    (
        'Wednesday', 'Go train Core'
    ),
    (
        'Blursday', 'Not a valid day'
    )

]


@pytest.mark.parametrize("input, expected", params)
def test_workout_dictionary(input, expected):
    result = get_workout_motd(input)
    assert result == expected
