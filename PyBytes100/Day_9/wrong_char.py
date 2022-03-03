"""
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given 
characters differs from the others. He observed that one char usually differs 
from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the 
different one (the alphanumeric among non-alphanumerics or vice versa) 
among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars 
list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
See the TESTS tab for more details
"""

def get_index_different_char(chars):
    """
    >>> get_index_different_char(['A', 'f', '.', 'Q', 2])
    2
    >> get_index_different_char(['.', '{', ' ^', '%', 'a'])
    4
    """
    index_of_truth_values = [str(x).isalnum() for x in chars]
    it_is_mostly_alphanumeric = index_of_truth_values.count(True) > 1
    if it_is_mostly_alphanumeric:
        which_one_is_false = index_of_truth_values.index(False)
        return which_one_is_false
    else:
        which_one_is_true = index_of_truth_values.index(True)
        return which_one_is_true


    
