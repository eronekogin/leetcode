"""
https://leetcode.com/problems/count-tested-devices-after-test-operations/description/
"""


class Solution:
    """
    Solution
    """

    def count_tested_devices(self, battery_percentages: list[int]) -> int:
        """
        count tested devices
        """
        cost = 0
        cnt = 0

        for p in battery_percentages:
            if p + cost > 0:
                cnt += 1
                cost -= 1

        return cnt
