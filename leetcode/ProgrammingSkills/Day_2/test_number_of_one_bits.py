from .number_of_one_bits import Solution


solution = Solution()


def test_one_three_bits():
    input = 0b00000000000000000000000000001011
    result = solution.hammingWeight(input)
    assert result == 3


def test_one_one_bit():
    input = 0b00000000000000000000000010000000
    result = solution.hammingWeight(input)
    assert result == 1


def test_thirty_bits():
    input = 0b11111111111111111111111111111101
    result = solution.hammingWeight(input)
    assert result == 31
