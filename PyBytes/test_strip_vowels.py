import pytest
from strip_vowels_count import strip_vowels

zen = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

params = [
    (
        'hello world', ('h*ll* w*rld', 3)
    ),
    (
        'aaaaaaagh!', ('*******gh!', 7)
    ),
    (
    'slyly spryly tryst by my crypt', ('slyly spryly tryst by my crypt', 0)
    ),
    (
        'I MAY HAVE NEGLECTED CAPITAL VOWELS', ('* M*Y H*V* N*GL*CT*D C*P*T*L V*W*LS', 12)
    ),
    (    
        'aaaaaaagh!\naaaaaaagh!\naaaaaaagh!', ('*******gh!\n*******gh!\n*******gh!', 21)

    )
    ]

@pytest.mark.parametrize("input, expected", params)
def test_strip_vowels(input, expected):
    result = strip_vowels(input)
    assert result == expected

