"""
https://leetcode.com/problems/count-good-numbers/
"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        evenCounts = pow(5, n - (n >> 1), MOD)
        oddCounts = pow(4, n >> 1, MOD)
        return (evenCounts * oddCounts) % MOD 