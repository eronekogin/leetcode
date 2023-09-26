"""
https://leetcode.com/problems/maximum-matrix-sum/
"""


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        """
        1. If there are even number of negative numbers, we can always swap them to all positive.
        2. Otherwise, we will choose to leave the negative number having the minimum absolute value.
        """
        totalSum = 0
        negativeNumbers = 0
        minAbsNum = 10 ** 6
        for row in matrix:
            for num in row:
                totalSum += abs(num)
                negativeNumbers += num < 0
                minAbsNum = min(minAbsNum, abs(num))
        
        if negativeNumbers & 1:
            return totalSum - 2 * minAbsNum
        
        return totalSum
        