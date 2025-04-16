"""
https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/description/
"""


class Solution:
    """
    Solution
    """

    def count_ways(self, ranges: list[list[int]]) -> int:
        """
        count ways
        """
        non_overlaps = 0
        prev_end = -1
        for start, end in sorted(ranges):
            non_overlaps += prev_end < start
            prev_end = max(prev_end, end)

        return pow(2, non_overlaps, 10 ** 9 + 7)


print(Solution().count_ways([[6, 10], [5, 15]]))
