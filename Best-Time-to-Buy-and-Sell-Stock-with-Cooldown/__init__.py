class Solution:
    def maxProfit(self, prices):
        res = self.calculate_max_profit_1(prices)
        return res

    # Recursive solution
    def calculate_max_profit(self, prices, last_bought_price=0, i=0, last_bought=False):
        if i >= len(prices):
            return 0

        results = [
            self.calculate_max_profit(prices, prices[j], j + 1, True)
            if not last_bought
            else (prices[j] - last_bought_price) + self.calculate_max_profit(prices, prices[j], j + 2, False)
            for j in range(i, len(prices))
        ]
        return max(results, default=0)

    # Optimal solution
    def calculate_max_profit_1(self, prices):
        if len(prices) == 0:
            return 0

        A, B, C = 0, -prices[0], 0

        for i in prices[1:]:
            A, B, C = max(A, C), max(A-i, B), B+i

        return max([A, B, C])


# s = Solution()
# assert s.maxProfit(
#     [48, 12, 60, 93, 97, 42, 25, 64, 17, 56, 85, 93, 9, 48, 52, 42, 58, 85, 81, 84, 69, 36, 1, 54, 23, 15, 72, 15, 11,
#      94]) == 428
# assert s.maxProfit([1, 2, 4]) == 3
# assert s.maxProfit([1, 2, 3, 10, 4, 6, 2, 12]) == 19
