"""
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
"""


class Solution:
    def numSubarrayBoundedMax(self, A: list[int], L: int, R: int) -> int:
        start = totalCnt = prevCnt = 0
        for end in range(len(A)):
            if L <= A[end] <= R:
                prevCnt = end - start + 1
                totalCnt += prevCnt
            elif A[end] < L:
                totalCnt += prevCnt
            else:
                start = end + 1
                prevCnt = 0

        return totalCnt
