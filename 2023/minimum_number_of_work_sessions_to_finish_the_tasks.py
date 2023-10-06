"""
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
"""


from functools import cache


class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        def clear_bit(x: int, i: int):
            # Mark the ith bit in x as zero.
            return x - (1 << i)

        @cache
        def dp(mask: int):
            # dp(mask, remainTiem) stands for the mininum session needed to finish mask tasks with remainTime.
            if mask == 0:
                return (0, 0)
            
            minSessions = N  # There will be no more than N session.
            minRemainTime = 0
            for i in range(N):
                if mask & (1 << i):  # If task i is already done.
                    newMask = clear_bit(mask, i)
                    
                    currSessions, currRemainTime = dp(newMask)

                    if tasks[i] <= currRemainTime:
                        currRemainTime -= tasks[i]
                    else:
                        currSessions += 1
                        currRemainTime = sessionTime - tasks[i]
                    
                    if currSessions < minSessions or (currSessions == minSessions and currRemainTime > minRemainTime):
                        minSessions, minRemainTime = currSessions, currRemainTime
            
            return (minSessions, minRemainTime)

        N = len(tasks)

        return dp((1 << N) - 1)[0]