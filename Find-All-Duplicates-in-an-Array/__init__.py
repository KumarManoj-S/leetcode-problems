class Solution:
    def findDuplicates(self, nums):
        n = len(nums) + 1

        for i in range(len(nums)):
            index = nums[i] % n
            nums[index-1] += n

        return [
            idx + 1
            for idx, i in enumerate(nums)
            if i // n > 1
        ]



s = Solution()

assert s.findDuplicates([4,3,2,7,8,2,3,1]) == [2, 3]
assert s.findDuplicates([1, 1]) == [1]
assert s.findDuplicates([1]) == []