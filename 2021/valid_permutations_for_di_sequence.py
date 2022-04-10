"""
https://leetcode.com/problems/valid-permutations-for-di-sequence/
"""


from itertools import accumulate


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        """
        1. Suppose dp[i][j] stands for the number of permutation of the first
            i + 1 numbers while the i + 1 th number is the j + 1 th smallest
            number in the remaining unused numbers.
        2. Then when s[i] == I, we calculate the prefix from the previous dp;
            when s[i] == D, we calcuate the suffix from the previous dp.
        """
        dp = [1] * (len(s) + 1)
        for a, b in zip('I' + s, s):
            dp = list(accumulate(dp[:-1] if a == b else dp[-1:0:-1]))

        return dp[0] % (10 ** 9 + 7)
