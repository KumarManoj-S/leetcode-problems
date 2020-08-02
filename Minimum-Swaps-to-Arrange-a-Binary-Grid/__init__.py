import re

class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        counter = 0
        for i in range(len(grid)):
            zeros = n - (i + 1)
            present = False
            for j in range(i, len(grid)):
                if re.match("[01]*0{" + str(zeros) + "}$", "".join([str(s) for s in grid[j]])):
                    grid = grid[:i] + [grid[j]] + grid[i:j] + grid[j+1:]
                    counter += j - i
                    present = True
                    break
            if not present:
                return -1

        return counter

s = Solution()

# print(s.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))
assert s.minSwaps([[0,0,1],[1,1,0],[1,0,0]]) == 3
assert s.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]) == -1
assert s.minSwaps([[1,0,0],[1,1,0],[1,1,1]]) == 0
# print(s.minSwaps([[1,0,0],[1,1,0],[1,1,1]]))
