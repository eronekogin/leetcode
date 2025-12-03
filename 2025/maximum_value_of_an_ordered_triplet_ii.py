"""
https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_triplet_value(self, nums: list[int]) -> int:
        """
        maximum triplet value
        """
        rslt = 0
        max_first = max_diff = 0
        for v in nums:
            rslt = max(rslt, max_diff * v)
            max_diff = max(max_diff, max_first - v)
            max_first = max(max_first, v)

        return rslt
