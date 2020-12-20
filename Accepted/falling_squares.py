"""
https://leetcode.com/problems/falling-squares/
"""


from typing import List


from bisect import bisect_left, bisect_right


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights, points, rslt = [0], [0], []
        maxHeight = 0
        for start, sideLen in positions:
            end = start + sideLen

            # Find the nearest point that is > the start.
            left = bisect_right(points, start)

            # Find the nearest point that is >= the end.
            right = bisect_left(points, end)

            # Get the current maximum height from left - 1 to right - 1. The
            # reason is that for each index i in the heights list, it stands
            # for the height of the square that starts from index i, instead
            # of the height of the square that ends at index i.
            currHeight = max(heights[left - 1: right] or [0]) + sideLen

            # Update the target interval in points.
            points[left: right] = [start, end]

            # Update the target interval in heights.
            heights[left: right] = [currHeight, heights[right - 1]]

            # Update the current maximum height.
            maxHeight = max(maxHeight, currHeight)
            rslt.append(maxHeight)

        return rslt


print(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))
