from names import dedup_and_title_case_names, sort_by_surname_desc, shortest_first_name
from names import NAMES


def test_dedup_and_title_case():
    expected = ['Arnold Schwarzenegger',
                'Alec Baldwin',
                'Bob Belderbos',
                'Julian Sequeira',
                'Sandra Bullock',
                'Keanu Reeves',
                'Julbob Pybites',
                'Al Pacino',
                'Brad Pitt',
                'Matt Damon',
                ]
    result = dedup_and_title_case_names(NAMES)
    assert expected == result


def test_sort_by_surname():
    expected = [
                'Julian Sequeira',
                'Arnold Schwarzenegger',
                'Keanu Reeves',
                'Julbob Pybites',
                'Brad Pitt',
                'Al Pacino',
                'Matt Damon',
                'Sandra Bullock',
                'Bob Belderbos',
                'Alec Baldwin'
                ]
    result = sort_by_surname_desc(NAMES)
    assert expected == result


def test_shortest_first_name():
    expected = 'Al'
    result = shortest_first_name(NAMES)
    assert expected == result
    
