class Solution:
    def find_count(self, n, i=0):
        if n == i:
            return 1
        if n < i:
            return 0

        return self.find_count(n, i+1) + self.find_count(n, i+2)

    def find_count_dp(self, n):
        if n == 0:
            return 0

        dp = ([0] * n) + [1, 0]

        for i in reversed(range(n)):
            dp[i] = dp[i+1] + dp[i+2]

        return dp[0]

    def climbStairs(self, n: int) -> int:
        return self.find_count_dp(n)


s = Solution()

assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
assert s.climbStairs(4) == 5
assert s.climbStairs(12) == 233
assert s.climbStairs(34) == 9227465
assert s.climbStairs(43) == 701408733
