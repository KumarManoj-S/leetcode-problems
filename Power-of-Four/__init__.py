import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        result = math.log(num) / math.log(4)
        return result.is_integer()

    def isPowerOfFour2(self, num: int) -> bool:
        if num <= 0:
            return False
        if num & (num-1) != 0:
            return False
        return len(bin(num)) % 2 == 1

s = Solution()

assert s.isPowerOfFour(16) is True
assert s.isPowerOfFour(4) is True
assert s.isPowerOfFour(1) is True
assert s.isPowerOfFour(0) is False
assert s.isPowerOfFour(64) is True
assert s.isPowerOfFour(5) is False
