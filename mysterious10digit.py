"""
Start from the bottom
abcdefghij is divisible by 10 
--> j = 0
abcdefghi is divisible by 9 
--> 
a + b + c + d + e + f + g + h + i % 9 = 0
abcdefgh is divisible by 8
--> fgh % 8 == 0
abcdefg is divisible by 7
--> 
abcdef is divisible by 6 -->
abcdef is divisible by 2 and 3

abcde is divisible by 5 -->
e is 0 or 5

abcd is divisible by 4 -->
if c is odd, d is 0, 4, or 8
if c is even, d is 2 or 6

OR
2c + d % 4 == 0

abc is divisible by 3 -->
a + b + c % 3 == 0

ab is divisible by 2 -->
b is 0, 2, 4, 6, 8

a is divisible by 1
duh

"""

#range 1000000000 999999990


# if abcdefghij is divisible by 10 then the number must be
# abcdefghi0

# a is divisible by 1
# ab is divisible by 2

ab = [x for x in range(10,100) if x % 2 ==0]
[]


def digitsplit(n):
    string_number = str(n)
    return([int(x) for x in string_number])

def digitappend(n, m):
    string_number = str(n)
    digit_to_append = str(m)
    string_result = string_number + digit_to_append
    return(int(string_result))

    
def find_unique(arr):
    for number in arr:
        if unique_digits(number):
            return number

def unique_digits(n):
    # almost not fair
    stringnum = str(n)
    setnum = set(str(n))
    if len(stringnum) == len(setnum):
        return True
    else:
        return False
    

def two_to_three():
    results = []
    for y in range(0,10):
        for x in ab:
            z = digitappend(x,y)
            if z % 3 == 0:
                results.append(z)
    return(results)

def three_to_four():
    results = []
    previous = two_to_three()
    for y in range(0,10):
        for x in previous:
            z = digitappend(x,y)
            if z % 4 == 0:
                results.append(z)
    return(results)

def four_to_five():
    results = []
    previous = three_to_four()
    for y in range(0,10):
        for x in previous:
            z = digitappend(x,y)
            if z % 5 == 0:
                results.append(z)
    return(results)

def five_to_six():
    results = []
    previous = four_to_five()
    for y in range(0,10):
        for x in previous:
            z = digitappend(x,y)
            if z % 6 == 0:
                results.append(z)
    return(results)

def six_to_seven():
    results = []
    previous = five_to_six()
    for y in range(0,10):
        for x in previous:
            z = digitappend(x,y)
            if z % 7 == 0:
                results.append(z)
    return(results)

def seven_to_eight():
    results = []
    previous = six_to_seven()
    for y in range(0,10):
        for x in previous:
            z = digitappend(x,y)
            if z % 8 == 0:
                results.append(z)
    return(results)

def eight_to_nine():
    results = []
    previous = seven_to_eight()
    for y in range(0,10):
        for x in previous:
            z = digitappend(x,y)
            if z % 9 == 0:
                results.append(z)
    return(results)

def nine_to_ten():
    results = []
    previous = eight_to_nine()
    for y in range(0,10):
        for x in previous:
            z = digitappend(x,y)
            if z % 10 == 0:
                results.append(z)
    return(results)


find_unique(nine_to_ten())