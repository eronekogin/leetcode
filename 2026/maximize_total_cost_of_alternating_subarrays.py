"""
https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/description/
"""


from math import inf


class Solution:
    """
    Solution
    """

    def maximum_total_cost(self, nums: list[int]) -> int:
        """
        maximum total cost
        """
        pos = -inf  # previous subarray cost ending at i with positive sign
        neg = 0  # previous subarray cost ending at i with negative sign

        for x in nums:
            pos, neg = max(pos, neg) + x, pos - x

        return int(max(pos, neg))
