"""
https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0

        maxSum = minSum = totalSum = currMin = currMax = A[0]
        n = len(A)
        for i in range(1, n):
            currMax = A[i] + max(currMax, 0)
            currMin = A[i] + min(currMin, 0)
            totalSum += A[i]
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)

        if maxSum > 0:
            return max(maxSum, totalSum - minSum)

        return maxSum
