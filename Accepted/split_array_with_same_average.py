"""
https://leetcode.com/problems/split-array-with-same-average/
"""


class Solution:
    def splitArraySameAverage(self, A: list[int]) -> bool:
        """
        The problem could be converted to a n-sum problem as follows:
        1. To find if 1 element sum to avg(A).
        2. To find if 2 elements sum to 2 * avg(A).
        3. To find if k elements sum to k * avg(A).

        The smaller list between B and C has a length k < N / 2 + 1.
        """
        def find(targetSum: int, remainings: int, startIdx: int) -> bool:
            if not remainings:  # No more element to search.
                return targetSum == 0  # Check if target sum is satisfied.

            if startIdx + remainings > N:  # No more element to use.
                return False

            if (targetSum, remainings, startIdx) not in memo:
                # Either taking the element at startIdx or ignore it.
                take = find(
                    targetSum - A[startIdx], remainings - 1, startIdx + 1)
                ignore = find(
                    targetSum, remainings, startIdx + 1)
                memo[(targetSum, remainings, startIdx)] = take or ignore

            return memo[(targetSum, remainings, startIdx)]

        memo = {}
        N, S = len(A), sum(A)
        return any(
            find(S * remainings // N, remainings, 0)
            for remainings in range(1, (N >> 1) + 1)
            if not (S * remainings) % N)
