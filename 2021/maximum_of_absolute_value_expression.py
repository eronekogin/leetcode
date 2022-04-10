"""
https://leetcode.com/problems/maximum-of-absolute-value-expression/
"""


class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        """
        1. Suppose f(i) = p * arr1[i] + q * arr2[j] + i, then we have
            |arr1[i]-arr1[j]|+|arr2[i]-arr2[j]|+|i-j| = f(j) - f(i) for
            any i < j.
        2. Then in order to find the maximum f(j) - f(i), we keep updating
            the smallest and try to find the largest.
        """
        N = len(arr1)
        DIRECTIONS = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        rslt = 0
        for p, q in DIRECTIONS:
            smallest = p * arr1[0] + q * arr2[0] + 0
            for i in range(N):
                current = p * arr1[i] + q * arr2[i] + i
                rslt = max(rslt, current - smallest)
                smallest = min(smallest, current)

        return rslt
