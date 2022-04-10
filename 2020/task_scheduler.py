"""
https://leetcode.com/problems/task-scheduler/
"""


from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        1. First we have to arrange the task with the maximum freqency.
        2. If we have 3A, 2B, 2C with n = 2:
            ABCABCA##, which means we need 2 idle slots.
        3. If we have more than 1 task with the maximum frequency, such as
            3A, 3B, 2C with n = 2, then we have to arrange it like:
            ABCABCAB#, which means we need 1 idle slot.
        4. If we have 3A, 3B, 3C with n = 2:
            ABCABCABC, which means we don't need any idle slot.
        5. If we have negative idle slot like 3A, 3B, 3C, 3D with n = 2, we
            could always add D to the end of each C which make us need no idle
            slot.
        """
        cnts = {}  # {task: total number of the task}
        numberOfTasksWithMaxCnt = maxCnt = 0
        for task in tasks:
            cnts[task] = cnts.get(task, 0) + 1
            if cnts[task] == maxCnt:
                numberOfTasksWithMaxCnt += 1
            elif cnts[task] > maxCnt:
                maxCnt = cnts[task]
                numberOfTasksWithMaxCnt = 1

        emptySlots = maxCnt - 1
        slotLen = n - numberOfTasksWithMaxCnt + 1  # ABC#ABC#ABC#.
        remainTasks = len(tasks) - maxCnt * numberOfTasksWithMaxCnt
        idles = max(0, emptySlots * slotLen - remainTasks)
        return len(tasks) + idles
