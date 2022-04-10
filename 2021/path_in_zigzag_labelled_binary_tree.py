"""
https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
"""

from math import log2


class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        currRow, currVal = int(log2(label)) + 1, label
        path = [label]
        while currRow > 1:
            offset = (currVal - (1 << (currRow - 1))) >> 1
            currRow -= 1
            currVal = ((1 << currRow) - 1) - offset
            path.append(currVal)

        return path[::-1]


print(Solution().pathInZigZagTree(13))
