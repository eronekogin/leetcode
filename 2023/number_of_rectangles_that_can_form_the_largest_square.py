"""
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
"""


class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        maxSquareLen = float('-inf')
        cnt = 0
        for l, w in rectangles:
            currSquareLen = min(l, w)
            if currSquareLen > maxSquareLen:
                maxSquareLen = currSquareLen
                cnt = 1
            elif currSquareLen == maxSquareLen:
                cnt += 1

        return cnt
