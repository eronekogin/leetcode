"""
https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/description/
"""


class Solution:
    """
    Solution
    """

    def can_reach_corner(self, x_corner: int, y_corner: int, circles: list[list[int]]) -> bool:
        """
        can reach corner
        """
        def find(i: int) -> int:
            if parents[i] != i:
                parents[i] = find(parents[i])

            return parents[i]

        def union(i: int, j: int) -> None:
            pi, pj = find(i), find(j)
            if pi != pj:
                parents[pi] = pj

        def is_inside_circle(x: int, y: int, cx: int, cy: int, r: int) -> bool:
            return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

        n = len(circles)
        parents = list(range(n + 2))
        top_left = n
        bottom_right = n + 1

        # Check if corners are inside any circle
        for x, y, r in circles:
            if (
                is_inside_circle(x_corner, y_corner, x, y, r) or
                is_inside_circle(0, 0, x, y, r)
            ):
                return False

        for i, (x1, y1, r1) in enumerate(circles):
            # Check top left
            if (
                (abs(x1) <= r1 and 0 <= y1 <= y_corner) or
                (abs(y1 - y_corner) <= r1 and 0 <= x1 <= x_corner)
            ):
                union(i, top_left)

            # Check bottom right
            if (
                (abs(y1) <= r1 and 0 <= x1 <= x_corner) or
                (abs(x1 - x_corner) <= r1 and 0 <= y1 <= y_corner)
            ):
                union(i, bottom_right)

            # Check circle intersection
            for j in range(i):
                x2, y2, r2 = circles[j]

                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2:
                    # check if they intersect inside the rectangle
                    x_mid = (x1 * r2 + x2 * r1) / (r1 + r2)
                    y_mid = (y1 * r2 + y2 * r1) / (r1 + r2)
                    if 0 <= x_mid <= x_corner and 0 <= y_mid <= y_corner:
                        union(i, j)

            if find(top_left) == find(bottom_right):
                return False

        return True
