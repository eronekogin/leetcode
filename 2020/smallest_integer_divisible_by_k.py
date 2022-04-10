"""
https://leetcode.com/problems/smallest-integer-divisible-by-k/
"""


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        """
        1. The target number is always like 1, 11, 111, ..., where
            curr = prev * 10 + 1.
        2. Suppose prev = aK + r, then curr = (ak + r) * 10 + 1 =
            10aK + 10r + 1. Then curr % K = (10r + 1) % K. So we could simply
            use the remainder to check each time to prevent overflow.
        3. Since the unique remainders could only range from 0 to K - 1, if
            we run the loop K times and it doesn't stop, we could determine
            that such kind of number is never divisable by K.
        """
        r = 0
        for minLen in range(1, K + 1):
            r = (r * 10 + 1) % K
            if not r:
                return minLen

        return -1
