"""
https://leetcode.com/problems/maximum-running-time-of-n-computers/description/
"""


class Solution:
    """
    Solution
    """

    def max_run_time(self, n: int, batteries: list[int]) -> int:
        """
        max_run_time
        """
        l, r = 1, sum(batteries) // n
        while l < r:
            target = r - ((r - l) >> 1)
            extra = 0
            for p in batteries:
                extra += min(p, target)

            if extra >= target * n:
                l = target
            else:
                r = target - 1

        return l
