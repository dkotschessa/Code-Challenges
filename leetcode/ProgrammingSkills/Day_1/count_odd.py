from math import ceil, floor


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = (high + 1) - low
        if length % 2 == 0:  # even lengthed arrays
            return length / 2
        else:
            if low % 2 == 0:  # starts even
                return floor(length / 2)
            else:  # starts oddd
                return ceil(length / 2)
