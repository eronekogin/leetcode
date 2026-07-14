"""
https://leetcode.com/problems/maximum-points-inside-the-square/description/
"""


class Solution:
    """
    Solution
    """

    def max_points_inside_square(self, points: list[list[int]], s: str) -> int:
        """
        max points inside square
        """
        min_sizes = {}
        target_size = float('inf')
        for (x, y), t in zip(points, s):
            curr_size = max(abs(x), abs(y))

            if t not in min_sizes:
                min_sizes[t] = curr_size
            elif curr_size < min_sizes[t]:
                target_size = min(target_size, min_sizes[t])
                min_sizes[t] = curr_size
            else:
                target_size = min(target_size, curr_size)

        return sum(
            x < target_size
            for x in min_sizes.values()
        )
