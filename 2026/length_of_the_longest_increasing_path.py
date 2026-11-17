"""
https://leetcode.com/problems/length-of-the-longest-increasing-path/description/
"""


from bisect import bisect_left
from math import inf


class Solution:
    """
    Solution
    """

    def max_path_length(self, coordinates: list[list[int]], k: int) -> int:
        """
        max path length
        """
        dp = [inf] * len(coordinates)
        xk, yk = coordinates[k]

        # Sort by x to processing points from left to right
        # For a tie on x, process points with larger y first
        for x, y in sorted(coordinates, key=lambda p: (p[0], -p[1])):
            if (x < xk and y < yk) or (x > xk and y > yk):
                dp[bisect_left(dp, y)] = y

        # + 1 is to add the point k itself
        return bisect_left(dp, inf) + 1
