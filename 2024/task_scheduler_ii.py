"""
https://leetcode.com/problems/task-scheduler-ii/description/
"""


class Solution:
    """
    Solution
    """

    def task_scheduler_ii(self, tasks: list[int], space: int) -> int:
        """
        tasks scheduler ii
        """
        next_start_day: dict[int, int] = {}
        curr_day = 0
        for t in tasks:
            curr_day = max(curr_day + 1, next_start_day.get(t, 0))
            next_start_day[t] = curr_day + space + 1

        return curr_day


print(Solution().task_scheduler_ii([5, 8, 8, 5], 2))
