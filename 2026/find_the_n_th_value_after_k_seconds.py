"""
https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/description/
"""


from itertools import accumulate
from math import comb


class Solution:
    """
    Solution
    """

    def value_after_k_seconds(self, n: int, k: int) -> int:
        """
        value after k seconds
        """
        rslt = [1] * n
        for _ in range(k):
            rslt = list(accumulate(rslt))

        return rslt[-1] % (10 ** 9 + 7)

    def value_after_k_seconds2(self, n: int, k: int) -> int:
        """
        pascal triangle:

        k = 0:  1   1   1   1
        k = 1:  1   2   3   4
        k = 2:  1   3   6  10
        k = 3:  1   4  10  20

        So in order to go to the n - 1 th column at the kth row,
        in total we have k + n - 1 steps, and the unique path
        is to pick n - 1 right moves from k + n - 1 steps, or
        to pick k down moves from k + n - 1 steps, both works.
        """
        return comb(k + n - 1, k) % (10 ** 9 + 7)
