"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        newHeights = heights + [0]  # Append 0 to the end to handle boundary.
        workStack, rslt = [-1], 0
        for i in range(len(newHeights)):
            while newHeights[i] < newHeights[workStack[-1]]:
                h = newHeights[workStack.pop()]
                # For the current popped bar x from workStack, newHeights[i]
                # is its right boundary and the last element in the current
                # workStack is its left boundary. So the width for the current
                # rectangle including bar x will be i - workStack[-1] + 1 - 2
                # as the left and right boundary bars are exclusive.
                w = i - workStack[-1] - 1
                rslt = max(rslt, h * w)

            workStack.append(i)

        return rslt


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
