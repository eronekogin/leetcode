"""
https://leetcode.com/problems/exclusive-time-of-functions/
"""


from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []  # Holds the function ids.
        rslt = [0] * n
        preTime = 0
        for log in logs:
            fid, action, time = log.split(':')
            fid, time = int(fid), int(time)
            if action == 'start':  # New function.
                if stack:
                    rslt[stack[-1]] += time - preTime

                stack.append(fid)
                preTime = time
            else:
                rslt[stack[-1]] += time - preTime + 1
                stack.pop()
                preTime = time + 1

        return rslt


print(Solution().exclusiveTime(
    1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
