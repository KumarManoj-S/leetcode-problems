class Solution:
    def getWinner(self, arr, k: int) -> int:
        winner = arr[0]
        winner_count = 0

        for i in arr[1:]:
            if winner < i:
                winner = i
                winner_count = 1
            else:
                winner_count += 1

            if winner_count == k:
                break

        return winner


s = Solution()

print(s.getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000))
