"""
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
"""


from collections import Counter
from itertools import accumulate


class Solution:
    def numSubmatrixSumTarget(
        self,
        matrix: list[list[int]],
        target: int
    ) -> int:
        """
        1. Calculate the prefix sums of each row.
        2. Then sum of each submatrices become the sum of each subarray.
        3. Then calculate the number of subarrays having sum = target.
        4. The general idea is to calculate the sum of items until index i,
            then for any index j having sum of sumI - target, the sum of
            elements between index i and j are equal to target.
        """
        if not matrix or not matrix[0]:
            return 0

        R, C = len(matrix), len(matrix[0])
        prefixSums = [list(accumulate(row)) for row in matrix]
        total = 0
        for cStart in range(C):
            for cEnd in range(cStart, C):
                cnt = Counter()
                cnt[0] = 1
                currSum = 0
                for r in range(R):
                    currSum += prefixSums[r][cEnd]
                    if cStart:
                        currSum -= prefixSums[r][cStart - 1]

                    total += cnt[currSum - target]
                    cnt[currSum] += 1

        return total
