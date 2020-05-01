from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        If those rectangles could form a perfect rectangle:

        1. The summary of the area of the rectangles in the input list should
        be the same as the final rectangle.

        2. The corner points of each sub rectangle should occur even times
        except the four corner points in the final rectangle.
        """
        corners = set()
        fx1 = fy1 = float('inf')
        fx2 = fy2 = float('-inf')
        areaSum = 0
        for x1, y1, x2, y2 in rectangles:
            fx1 = min(fx1, x1)
            fx2 = max(fx2, x2)
            fy1 = min(fy1, y1)
            fy2 = max(fy2, y2)
            areaSum += (x2 - x1) * (y2 - y1)
            corners ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}

        rslt = corners == {(fx1, fy1), (fx1, fy2), (fx2, fy1), (fx2, fy2)}
        return rslt and areaSum == (fx2 - fx1) * (fy2 - fy1)


print(Solution().isRectangleCover(
    [[0, 0, 1, 1], [0, 0, 2, 1], [1, 0, 2, 1], [0, 2, 2, 3]]
))
