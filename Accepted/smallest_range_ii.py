"""
https://leetcode.com/problems/smallest-range-ii/
"""


from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        """
        1. Sort A in ascending order first.
        2. Suppose from [:i + 1], we increasing each number by K while from
            [i + 1:], we decrease each number by K, then the difference between
            the maximum value and the minimum value is
            max(A[n] - K, A[i] + K) - min(A[0] + K, A[i + 1] - K).
        3. Find the minimum difference by scanning A from left to right.
        """
        sortedA = sorted(A)
        minNum, maxNum = sortedA[0] + K, sortedA[-1] - K
        rslt = maxNum - minNum + (K << 1)
        for a, b in zip(sortedA, sortedA[1:]):
            rslt = min(rslt, max(maxNum, a + K) - min(minNum, b - K))

        return rslt
