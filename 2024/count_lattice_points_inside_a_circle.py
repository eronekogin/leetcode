"""
https://leetcode.com/problems/count-lattice-points-inside-a-circle/description/
"""


class Solution:
    """
    Solution
    """

    def count_lattice_points(self, circles: list[list[int]]) -> int:
        """
        count lattice points
        """
        points: set[tuple[int, int]] = set()
        for x0, y0, r in circles:
            bound = r * r
            for x in range(x0 - r, x0 + r + 1):
                for y in range(y0 - r, y0 + r + 1):
                    if (x - x0) * (x - x0) + (y - y0) * (y - y0) <= bound:
                        points.add((x, y))

        return len(points)

    def count_lattice_points2(self, circles: list[list[int]]) -> int:
        """
        count lattice points
        """
        cnt = 0
        for x in range(201):
            for y in range(201):
                cnt += any(
                    (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2
                    for x0, y0, r in circles
                )

        return cnt


print(Solution().count_lattice_points([[2, 2, 1]]))
