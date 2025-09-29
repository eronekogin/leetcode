"""
https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/description/
"""


class Solution:
    """
    Solution
    """

    def max_increasing_groups(self, usage_limits: list[int]) -> int:
        """
        max increasing groups
        """
        usage_limits.sort()
        total = groups = 0
        for x in usage_limits:
            total += x

            if total >= (groups + 1) * (groups + 2) // 2:
                groups += 1

        return groups
