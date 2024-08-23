"""
https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_groups(self, grades: list[int]) -> int:
        """
        maximum groups
        """
        curr_group_required = 1
        remain = len(grades)
        groups = 0
        while remain >= curr_group_required:
            groups += 1
            remain -= curr_group_required
            curr_group_required += 1

        return groups
