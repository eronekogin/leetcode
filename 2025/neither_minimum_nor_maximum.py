"""
https://leetcode.com/problems/neither-minimum-nor-maximum/description/
"""


class Solution:
    """
    Solution
    """

    def find_non_min_or_max(self, nums: list[int]) -> int:
        """
        find non min or max
        """
        if len(nums) < 3:
            return -1

        return sorted(nums[:3])[1]
