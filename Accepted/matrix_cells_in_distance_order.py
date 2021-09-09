"""
https://leetcode.com/problems/matrix-cells-in-distance-order/
"""


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        rslt = [[r, c] for r in range(rows) for c in range(cols)]
        rslt.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return rslt
