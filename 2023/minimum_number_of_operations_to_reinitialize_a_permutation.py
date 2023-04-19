"""
https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        """
        In each step, suppose index x will get index i's value:
            1. if x is odd: (n + x - 1) / 2 = i, which means x = 2i - (n - 1)
            2. if x is even: x / 2 = i, which means x = 2i

        So if we check x % (n - 1), we can get rid of the above checking and
        then make sure if after the current step, the index i is back to its
        original place.
        """
        step = 0
        i = 1
        while step == 0 or i > 1:
            i = (i << 1) % (n - 1)
            step += 1

        return step
