"""
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        sortedPositions = sorted(x for x, _ in points)
        return max(y - x for x, y in zip(sortedPositions, sortedPositions[1:]))
