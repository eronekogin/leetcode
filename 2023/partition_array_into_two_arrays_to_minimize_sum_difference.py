"""
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
"""


from itertools import combinations
from bisect import bisect_left


class Solution:
    """
    Solution
    """

    def minimum_difference(self, nums: list[int]) -> int:
        """
        minimum_difference
        """
        n = len(nums) >> 1
        original_left = nums[:n]
        original_right = nums[n:]
        total = sum(nums)

        # Sum of first n half - sum of second n half.
        min_diff = abs((sum(original_left) << 1) - total)
        half = total >> 1

        for pivot in range(1, n):
            left = [sum(comb) for comb in combinations(original_left, pivot)]
            right = [sum(comb)
                     for comb in combinations(original_right, n - pivot)]
            right.sort()
            for l in left:
                r = half - l
                i = bisect_left(right, r)
                if 0 <= i < len(right):
                    left_sum = l + right[i]
                    right_sum = total - left_sum
                    min_diff = min(min_diff, abs(left_sum - right_sum))

        return min_diff
