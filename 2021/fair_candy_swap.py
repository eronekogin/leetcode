"""
https://leetcode.com/problems/fair-candy-swap/
"""


class Solution:
    def fairCandySwap(
            self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        """
        1. Suppose alice exchange size x candy with y size candy from bob,
            then we have sa + y - x = sb + x - y, which means
            y = x + (sb - sa) / 2.
        2. Then we simply check if such x, y size candy exists in alice and
            bob, if so, we just exchange it.
        """
        sa, sb = sum(aliceSizes), sum(bobSizes)
        offset = (sb - sa) >> 1
        cb = set(bobSizes)
        for x in aliceSizes:
            if x + offset in cb:
                return [x, x + offset]
