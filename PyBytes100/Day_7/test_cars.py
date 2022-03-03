from cars import (get_all_jeeps, get_all_matching_models,
                  get_first_model_each_manufacturer, sort_car_models)
from cars import cars


def test_get_all_jeeps():
    expected = "Grand Cherokee, Cherokee, Trailhawk, Trackhawk"
    result = get_all_jeeps()
    assert result == expected


def test_get_first_model_each_manufacturer():
    expected = ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    result = get_first_model_each_manufacturer()
    assert result == expected


def test_get_all_matching_models():
    expected = ['Trailblazer', 'Trailhawk']
    result = get_all_matching_models()
    assert result == expected

def tes_get_all_matching_another_grep():
    expeced

def test_sort_car_models():
    expected = {'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
                'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
                'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
                'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
                'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk']}
    result = sort_car_models()
    assert result == expected

