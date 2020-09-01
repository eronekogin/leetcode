"""
https://leetcode.com/problems/remove-boxes/
"""


from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        Let T(start, end, k) be the maximum points gained by removing boxes
        among boxes[start:end + 1], which has k boxes having the same color
        as boxes[start] to its left side, then we have:

        1. T(start, start - 1, k) = 0, no existing box at all.
        2. T(start, start, k) = (k + 1) ** 2, only 1 box to be removed.
        3. T(start, end, k):
            3.1 If we simply remove box[start]:
                T(start, end, k) = (k + 1) ** 2 + T(start + 1, j, 0)
            3.2 If we keep box[start], then we have:
                T(start, j, k) = max(
                    T(start + 1, m - 1, 0) + T(m, end, k)
                    for m in range(start + 1, end + 1)
                    if box[m] == box[start])

        An optimization is that we always want to remove contiguous boxes with
        the same color together instead of removing them separately. As this
        will give us more points because (a + b) ** 2 > a**2 + b**2.
        """
        def get_max_points(start: int, end: int, k: int) -> int:
            if end < start:
                return 0

            if T[start][end][k]:  # Already calculated.
                return T[start][end][k]

            # Check if any contiguous boxes with the
            # same color as boxes[start].
            actualStart = start + 1
            while actualStart <= end and\
                    boxes[actualStart] == boxes[start]:
                actualStart += 1

            actualK = k + actualStart - start

            # Case 1: Simply remove boxes[i].
            rslt = actualK ** 2 + get_max_points(actualStart, end, 0)

            # Case 2: Keep boxes[i] for later removal.
            for m in range(actualStart, end + 1):
                if boxes[m] == boxes[start]:
                    rslt = max(
                        rslt,
                        get_max_points(actualStart, m - 1, 0) +
                        get_max_points(m, end, actualK))

            T[actualStart - 1][end][actualK - 1] = rslt
            return rslt

        N = len(boxes)
        T = [[[0] * N for _ in range(N)] for _ in range(N)]
        return get_max_points(0, N - 1, 0)  # Left side has no box initially.


print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
