"""
https://leetcode.com/problems/range-addition-ii/
"""


from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        maxRow, maxCol = m, n
        for r, c in ops:
            maxRow = min(maxRow, r)
            maxCol = min(maxCol, c)

        return maxRow * maxCol
