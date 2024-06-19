"""
https://leetcode.com/problems/count-integers-in-intervals/description/
"""

from bisect import bisect_left, bisect_right


class CountIntervals:
    """
    Count intervals
    """

    def __init__(self):
        self.intervals: list[tuple[int, int]] = [(0, 0), (10**10, 10**10)]
        self.covered_numbers = 0

    def add(self, left: int, right: int) -> None:
        """
        add
        """
        intervals = self.intervals

        l = bisect_left(intervals, left - 1, key=lambda x: x[1])
        left_bound = min(intervals[l][0], left)

        r = bisect_right(intervals, right + 1, key=lambda x: x[0])
        right_bound = max(intervals[r - 1][1], right)

        deleted_numbers = sum(
            intervals[i][1] - intervals[i][0] + 1
            for i in range(l, r)
        )

        self.covered_numbers += right_bound - left_bound + 1 - deleted_numbers
        self.intervals[l: r] = [(left_bound, right_bound)]

    def count(self) -> int:
        """
        count
        """
        return self.covered_numbers
