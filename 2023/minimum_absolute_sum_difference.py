"""
https://leetcode.com/problems/minimum-absolute-sum-difference/
"""


from bisect import bisect_left


class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        sortedNums1 = sorted(nums1)
        maxChange = -1
        diffSum = 0
        for x1, x2 in zip(nums1, nums2):
            diff = abs(x1 - x2)
            diffSum += diff

            i = bisect_left(sortedNums1, x2)
            if i < len(sortedNums1):
                maxChange = max(maxChange, diff - (sortedNums1[i] - x2))

            if i > 0:
                maxChange = max(maxChange, diff - (x2 - sortedNums1[i - 1]))

        return (diffSum - maxChange) % (10 ** 9 + 7)


nums1 = [38, 48, 73, 55, 25, 47, 45, 62, 15, 34, 51, 20, 76, 78, 38, 91, 69, 69, 73, 38, 74, 75, 86, 63, 73, 12, 100, 59, 29, 28, 94, 43, 100, 2, 53, 31, 73, 82, 70, 94, 2, 38, 50, 67, 8, 40, 88, 87, 62, 90,
         86, 33, 86, 26, 84, 52, 63, 80, 56, 56, 56, 47, 12, 50, 12, 59, 52, 7, 40, 16, 53, 61, 76, 22, 87, 75, 14, 63, 96, 56, 65, 16, 70, 83, 51, 44, 13, 14, 80, 28, 82, 2, 5, 57, 77, 64, 58, 85, 33, 24]

nums2 = [90, 62, 8, 56, 33, 22, 9, 58, 29, 88, 10, 66, 48, 79, 44, 50, 71, 2, 3, 100, 88, 16, 24, 28, 50, 41, 65, 59, 83, 79, 80, 91, 1, 62, 13, 37, 86, 53, 43, 49, 17, 82, 27, 17, 10, 89, 40, 82, 41, 2,
         48, 98, 16, 43, 62, 33, 72, 35, 10, 24, 80, 29, 49, 5, 14, 38, 30, 48, 93, 86, 62, 23, 17, 39, 40, 96, 10, 75, 6, 38, 1, 5, 54, 91, 29, 36, 62, 73, 51, 92, 89, 88, 74, 91, 87, 34, 49, 56, 33, 67]

print(Solution().minAbsoluteSumDiff(nums1, nums2))
