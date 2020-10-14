'''
Say you have an array prices for which the ith element
 is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e.,
 buy one and sell one share of the stock multiple times).
'''


        

def sell(a,b):
    if b > a:
        return(b-a)
    else:
        return None


def min_sell_max_buy(array):
    # good first start - only one sell
    # need exception if not possible
    smallest = min(array)
    smallest_location = array.index(smallest)
    rest_of_array = array[smallest_location:]
    largest = max(rest_of_array)
    return largest-smallest

    
def max_profit(array):
    # good first start - only one sell
    # need exception if not possible
    smallest = min(array)
    smallest_location = array.index(smallest)
    # nothing before that point matters
    rest_of_array = array[smallest_location:]
    # sell on the next amount that is higher
    largest = max(rest_of_array)
    return largest-smallest




