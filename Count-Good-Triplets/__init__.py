class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        counter = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                        counter += 1

        return counter


s = Solution()
assert s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1) == 0
assert s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3) == 4
