"""
https://leetcode.com/problems/minimum-time-to-complete-all-tasks/description/
"""


class Solution:
    """
    Solution
    """

    def find_minimum_time(self, tasks: list[list[int]]) -> int:
        """
        find minimum time
        """
        lines = [0] * 2001
        tasks.sort(key=lambda x: x[1])

        for start, end, duration in tasks:
            duration -= sum(lines[start: end + 1])
            t = end
            while duration > 0:
                if not lines[t]:
                    lines[t] = 1
                    duration -= 1

                t -= 1

        return sum(lines)
