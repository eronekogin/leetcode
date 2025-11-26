"""
https://leetcode.com/problems/beautiful-towers-ii/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_sum_of_heights(self, max_heights: list[int]) -> int:
        """
        maximum sum of heights
        """
        n = len(max_heights)
        left = [0] * n
        stack = [-1]
        curr = 0

        for i, h in enumerate(max_heights):
            while len(stack) > 1 and max_heights[stack[-1]] > h:
                j = stack.pop()
                curr -= (j - stack[-1]) * max_heights[j]

            curr += (i - stack[-1]) * h
            stack.append(i)
            left[i] = curr

        rslt = 0
        stack = [n]
        curr = 0
        for i in range(n - 1, -1, -1):
            h = max_heights[i]
            while len(stack) > 1 and max_heights[stack[-1]] > h:
                j = stack.pop()
                curr -= -(j - stack[-1]) * max_heights[j]

            curr += -(i - stack[-1]) * h
            stack.append(i)
            rslt = max(rslt, left[i] + curr - h)

        return rslt
