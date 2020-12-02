import re


"""
In this Bite we'd like you to loop over the characters in the large block of text (the most important text for any Python programmer: The Zen of Python!)

Within this loop you'll perform the following actions:

Replace all vowels (aeiou) with stars (*), do this case insensitively.
Count the number of replacements you do (= vowels in the text).
Return the new block of text post replacements and the count of vowels you replaced.
Hint: Try converting the block of text to a list first to make working with the characters simpler.

Tip: If you're struggling, work on one step at a time and expand on your code slowly. Don't try and tackle every requirement right away.

Bonus: if you already have some Python under your belt, try to use re and try to solve it without a for loop :)
"""

vowels = 'aeiou'

def strip_vowels(text: str):
    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int types in the function defintion above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    for stuff in text:
        count = 0
        for vowel in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            count += text.count(vowel)
    text = re.sub('[aAeEiIoOuU]', '*', text)
    return (text, count)

