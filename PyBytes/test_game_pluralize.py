import pytest

from game_pluralize import print_game_stats, games_won


def test_print_game_states(capsys):
    print_game_stats(games_won)
    out,err = capsys.readouterr()
    result = out.split('\n')
    assert result[0] == "sara has won 0 games"
    assert result[1] == "bob has won 1 game"
    assert result[2] == "tim has won 5 games"
    assert result[3] == "julian has won 3 games"
    assert result[4] == "jim has won 1 game"

def test_zero(capsys):
    print_game_stats({'dave' : 0})
    out,err = capsys.readouterr()
    results = out.strip('\n')
    assert results == 'dave has won 0 games'

def test_one(capsys):
    print_game_stats({'mike' : 1})
    out,err = capsys.readouterr()
    results = out.strip('\n')
    assert results == 'mike has won 1 game'



