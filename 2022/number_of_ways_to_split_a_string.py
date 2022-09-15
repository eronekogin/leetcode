"""
https://leetcode.com/problems/number-of-ways-to-split-a-string/
"""


class Solution:
    def numWays(self, s: str) -> int:
        N, MOD = len(s), 10 ** 9 + 7
        ones = [i for i, c in enumerate(s) if c == '1']
        if len(ones) == 0:
            # combination of picking 2 places out of N - 1 places, which is
            # (N - 1)! / (2!) * (N - 3)!
            return ((N - 1) * (N - 2) // 2) % MOD

        offset, r = divmod(len(ones), 3)
        if r > 0:
            return 0

        return (
            (ones[offset] - ones[offset - 1]) *
            (ones[offset * 2] - ones[offset * 2 - 1])
        ) % MOD
