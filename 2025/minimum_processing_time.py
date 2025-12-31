"""
https://leetcode.com/problems/minimum-processing-time/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def min_processing_time(self, processor_time: list[int], tasks: list[int]) -> int:
        """
        Docstring for min_processing_time

        :param self: Description
        :param processor_time: Description
        :type processor_time: list[int]
        :param tasks: Description
        :type tasks: list[int]
        :return: Description
        :rtype: int
        """
        processor_time.sort()
        tasks.sort()
        max_time = 0
        curr_task = len(tasks)
        for curr_time in processor_time:
            max_time = max(
                max_time,
                curr_time + max(tasks[curr_task - 4:curr_task])
            )
            curr_task -= 4

        return max_time


print(Solution().min_processing_time([8, 10], [2, 2, 3, 1, 8, 7, 4, 5]))
