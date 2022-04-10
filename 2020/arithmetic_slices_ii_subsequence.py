"""
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
"""


from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        Suppose:
        1. Weak arithmetic slices are the slices of A composed with at least
            two numbers and each adjancent numbers in the slice contains 
            the same difference.
            1.1 Any pair A[i], A[j] could form a weak arithmetic slice.
            1.2 If we add a qualified number to a weak arithmetic slice,
                we could make it an arithmetic slice.

        2. dp[i][d] is the total number of weak arithmetic slices which ends
            at A[i] with difference d.

        Then we have:

        dp[i][d] += dp[j][d] + 1 for j in range(i)

        Notice the 1 means the new weak arithmetic slice formed by
        A[i] and A[j].

        From 1.2 we know that the new formed arithmetic slices will be dp[j][d].
        """
        memo = defaultdict(lambda: defaultdict(int))
        cnt = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                memo[i][diff] += memo[j][diff] + 1
                cnt += memo[j][diff]

        return cnt
