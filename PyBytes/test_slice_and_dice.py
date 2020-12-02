import pytest
from slice_dice import slice_and_dice






### parametrized tests
input1 = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""
expected1 =  ['objects', 'y', 'too', ':)', 'bites']

input2 = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""
expected2 = ['word', 'list', 'list']

input3 = """
  this has some whitespace
This does not start lower
that is all!
"""

expected3 = ['whitespace', 'all']

params = [
    (
        input1, expected1
    ),
    (
        input2, expected2
    ),
    (
        input3, expected3
    ),
           ]

@pytest.mark.parametrize("input, expected", params)
def test_slice_and_dice(input, expected):
    result = slice_and_dice(input)
    assert result == expected
