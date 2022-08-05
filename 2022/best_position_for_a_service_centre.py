"""
https://leetcode.com/problems/best-position-for-a-service-centre/
"""


class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        def calc_distance(x0: int, y0: int) -> float:
            return sum(
                ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
                for x, y in positions
            )

        # Find center point of each axis first.
        sx = sy = 0
        for x, y in positions:
            sx += x
            sy += y

        cx = sx / len(positions)
        cy = sy / len(positions)

        rslt = calc_distance(cx, cy)
        delta = 100  # x, y in positions are within 0 to 100.
        while delta > 1e-6:  # Accuracy is acceptable at 1e-5
            zoom = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = cx + delta * dx
                ny = cy + delta * dy
                nextRslt = calc_distance(nx, ny)
                if nextRslt < rslt:
                    rslt = nextRslt
                    cx, cy = nx, ny
                    zoom = False
                    break

            if zoom:
                delta /= 2

        return rslt
