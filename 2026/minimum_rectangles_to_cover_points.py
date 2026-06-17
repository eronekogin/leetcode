"""
https://leetcode.com/problems/minimum-rectangles-to-cover-points/description/
"""


class Solution:
    """
    Solution
    """

    def min_rectangles_to_cover_points(self, points: list[list[int]], w: int) -> int:
        """
        min rectangles to cover points
        """
        sorted_x = sorted(x for x, _ in points)
        start = 0
        cnt = 0
        for end, x in enumerate(sorted_x):
            if x - sorted_x[start] > w:
                cnt += 1
                start = end

        return cnt + 1
