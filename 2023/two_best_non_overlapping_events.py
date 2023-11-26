"""
https://leetcode.com/problems/two-best-non-overlapping-events/
"""


class Solution:
    """
    Solution
    """

    def max_two_events(self, events: list[list[int]]) -> int:
        """
        max_two_events
        """
        intervals: list[tuple[int, bool, int]] = []
        max_sum = prev_max_value = 0

        # Build intervals.
        for s, e, v in events:
            intervals.append((s, True, v))
            intervals.append((e + 1, False, v))

        intervals.sort()

        # Get maximum sum.
        for _, is_start, v in intervals:
            if is_start:
                max_sum = max(max_sum, prev_max_value + v)
            else:
                prev_max_value = max(prev_max_value, v)

        return max_sum
