"""
https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description/
"""


class Solution:
    """
    Solution
    """

    def is_reachable_at_time(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        """
        is reachable at time
        """
        w = abs(sx - fx)
        h = abs(sy - fy)

        if w == 0 or h == 0 and t == 1:
            # start and end are the same point, and
            # time = 1 is not possible
            return False

        return t >= max(w, h)
