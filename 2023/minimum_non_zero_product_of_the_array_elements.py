"""
https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/
"""


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        """
        1. We have 2^p - 1 numbers.
        2. For each pair a <= b, (a - 1) * (b + 1) < ab.
        3. So for each swap, we are actually decrease a while increase b, so eventually we can make all pairs (a, b)
            to become (1, 2^p - 2)
        4. For 2^p - 1 itself, it does not have a pair, as its pair is 0, so this 2^p - 1 should be multiplied in
            the final product.
        """
        MOD = 10 ** 9 + 7
        MAX_VALUE = 1 << p
        return (pow(MAX_VALUE - 2, (MAX_VALUE >> 1) - 1, MOD) * (MAX_VALUE - 1)) % MOD