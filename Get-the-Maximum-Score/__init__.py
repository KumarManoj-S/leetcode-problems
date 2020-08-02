class Solution:
    def maxSum(self, nums1, nums2) -> int:
        i, j, sum1, sum2 = 0, 0, 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                sum1 = sum2 = nums1[i] + max([sum1, sum2])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            else:
                sum2 += nums2[j]
                j += 1
        sum1 += sum(nums1[i:])
        sum2 += sum(nums2[j:])

        return max([sum1, sum2]) % (pow(10, 9) + 7)


s = Solution()

print(s.maxSum([5,9,11,15,17,25,29]
,[6,12,15]))