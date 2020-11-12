import pytest
import mock
from sys import stdout
import sys
from valid_colors import print_colors

params = [
    (
        "blue", "blue"
    ),
    (
         "yellow", "yellow"
    ),
    (
        "red", "red"
    ),
           ]


def test_valid_colors_blue(capsys):
    with mock.patch('builtins.input', side_effect =["blue", "quit"]):
        print_colors()
        out,err = capsys.readouterr()
        assert out == "blue\nbye\n"

def test_valid_colors_yellow(capsys):
    with mock.patch('builtins.input', side_effect =["yellow", "quit"]):
        print_colors()
        out,err = capsys.readouterr()
        assert out == "yellow\nbye\n"

def test_valid_colors_red(capsys):
    with mock.patch('builtins.input', side_effect =["red", "quit"]):
        print_colors()
        out,err = capsys.readouterr()
        assert out == "red\nbye\n"

def test_valid_colors_bye(capsys):
    with mock.patch('builtins.input', side_effect =["quit"]):
        print_colors()
        out,err = capsys.readouterr()
        assert out == "bye\n"

def test_valid_colors_green(capsys):
    with mock.patch('builtins.input', side_effect =["green", "quit""]):
        print_colors()
        out,err = capsys.readouterr()
        assert out == "bye\n"