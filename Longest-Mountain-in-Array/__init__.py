class Solution:
    def longestMountain(self, A) -> int:
        is_increasing = True
        maximum, inc_c, dec_c = 0, 0, 0

        for i, _ in enumerate(A[1:]):
            if A[i] < A[i+1]:
                if not is_increasing:
                    if inc_c and dec_c:
                        maximum = max([maximum, inc_c + dec_c + 1])
                    inc_c, dec_c = 0, 0
                is_increasing = True
                inc_c += 1
            elif A[i] > A[i+1]:
                if is_increasing:
                    is_increasing = False
                dec_c += 1
            else:
                if inc_c and dec_c:
                    maximum = max([maximum, inc_c + dec_c + 1])
                inc_c, dec_c = 0, 0
                is_increasing = True

        if inc_c and dec_c:
            maximum = max([maximum, inc_c + dec_c + 1])

        return maximum


s = Solution()

assert s.longestMountain([2,1,4,7,3,2,5]) == 5
assert s.longestMountain([2,2, 2]) == 0
assert s.longestMountain([3]) == 0
assert s.longestMountain([]) == 0
assert s.longestMountain([1, 2, 3, 4, 3, 2, 1, 9, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1]) == 11