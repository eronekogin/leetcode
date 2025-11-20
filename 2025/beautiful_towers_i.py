"""
https://leetcode.com/problems/beautiful-towers-i/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_sum_of_heights(self, heights: list[int]) -> int:
        """
        maximum sum of heights
        """
        n = len(heights)
        left_sums = [0] * n
        stack = [-1]
        curr_sum = 0

        # Scan from left to right
        for i, h in enumerate(heights):
            while len(stack) > 1 and heights[stack[-1]] > h:
                j = stack.pop()
                curr_sum -= (j - stack[-1]) * heights[j]

            curr_sum += (i - stack[-1]) * h
            stack.append(i)
            left_sums[i] = curr_sum

        # Scan from right to left and calculate the maximum result
        stack = [n]
        rslt = 0
        right_sum = 0
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while len(stack) > 1 and heights[stack[-1]] > h:
                j = stack.pop()
                right_sum -= (stack[-1] - j) * heights[j]

            right_sum += (stack[-1] - i) * h
            stack.append(i)

            # h is calculated twice in left and right sums, so
            # we need to subtract one from them
            rslt = max(rslt, left_sums[i] + right_sum - h)

        return rslt
