"""
https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/description/
"""


class Solution:
    """
    Solution
    """

    def hardest_worker(self, n: int, logs: list[list[int]]) -> int:
        """
        hardest worker
        """
        hardest_worker, max_work_time = logs[0]
        prev_end = max_work_time

        for i in range(1, len(logs)):
            curr_worker, curr_end = logs[i]
            t = curr_end - prev_end

            if t > max_work_time or (t == max_work_time and curr_worker < hardest_worker):
                hardest_worker, max_work_time = curr_worker, t

            prev_end = curr_end

        return hardest_worker
