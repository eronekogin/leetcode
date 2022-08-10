"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        totalNumbers = high - low + 1
        if low & 1 and totalNumbers & 1:
            return 1 + (totalNumbers >> 1)
        else:
            return totalNumbers >> 1
