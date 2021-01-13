"""
https://leetcode.com/problems/daily-temperatures/
"""


from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, i, N = [], 0, len(T)
        rslt = [0] * N
        for i in range(N - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()

            if stack:
                rslt[i] = stack[-1] - i

            stack.append(i)

        return rslt


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
