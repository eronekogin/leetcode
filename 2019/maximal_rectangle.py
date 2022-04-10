"""
https://leetcode.com/problems/maximal-rectangle/
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Using the same idea from the largest_rectangle_in_histogram.
        For each row, the height for each column is the total consecutive
        1s from the current row to the top row. Then we scan the current row
        to find the largest rectangle.
        """
        if not matrix or not matrix[0]:
            return 0

        n, rslt = len(matrix[0]), 0
        heights = [0] * (n + 1)
        for row in matrix:
            # Calculate heights for each column in the current row.
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Search for the largest rectangle in the current row.
            workStack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[workStack[-1]]:
                    h = heights[workStack.pop()]
                    w = i - workStack[-1] - 1
                    rslt = max(rslt, h * w)

                workStack.append(i)

        return rslt
