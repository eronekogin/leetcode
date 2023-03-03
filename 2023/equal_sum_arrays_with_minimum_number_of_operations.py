"""
https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
"""


class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0

        if sum1 > sum2:
            larger, smaller = nums1, nums2
        else:
            larger, smaller = nums2, nums1

        diff = abs(sum1 - sum2)

        maxGainInLarger = [x - 1 for x in larger]
        maxGainInSmaller = [6 - x for x in smaller]

        cnt = 0
        for maxGain in sorted(maxGainInLarger + maxGainInSmaller, reverse=True):
            diff -= maxGain
            cnt += 1

            if diff <= 0:
                return cnt

        return -1  # Cannot do achieve the goal.
