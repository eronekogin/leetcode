"""
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_sum(i: int, v: int):
            total = 0
            if v > i:
                total += (v + v - i) * (i + 1) // 2
            else:
                total += (v + 1) * v // 2 + i - v + 1

            if v >= n - i:
                total += (v + v - n + 1 + i) * (n - i) // 2
            else:
                total += (v + 1) * v // 2 + n - i - v

            return total - v

        l, r = 1, maxSum
        while l < r:
            m = (l + r + 1) // 2
            if get_sum(index, m) <= maxSum:
                l = m
            else:
                r = m - 1

        return l
