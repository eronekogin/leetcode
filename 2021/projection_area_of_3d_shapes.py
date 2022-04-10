"""
https://leetcode.com/problems/projection-area-of-3d-shapes/
"""


class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        area = sum(v > 0 for row in grid for v in row)  # Projection on Z-axis
        area += sum(max(row) for row in grid)  # Projection on X-axis
        area += sum(max(col) for col in zip(*grid))  # Projection on Y-axis
        return area
