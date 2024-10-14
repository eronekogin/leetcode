"""
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
"""


class Solution:
    """
    Solution
    """

    def min_groups(self, intervals: list[list[int]]) -> int:
        """
        min groups
        """
        events: list[tuple[int, int]] = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e + 1, -1))

        events.sort()

        max_groups = groups = 0
        for _, offset in events:
            groups += offset
            max_groups = max(max_groups, groups)

        return max_groups
