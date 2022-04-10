"""
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
"""


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """
        1. xx, yy takes 1 swap to make them equal to yx, yx.
        2. xy, yx takes 2 swaps to make them equal to yx, yx.
        3. So in order to achieve the minimum swaps, we should apply step 1
            as much as possible and check if the last pair is a step 2 case.
        """
        xy = yx = 0
        for c1, c2 in zip(s1, s2):
            if c1 == 'x' and c2 == 'y':
                xy += 1
            elif c1 == 'y' and c2 == 'x':
                yx += 1

        if (xy + yx) & 1:  # Not possible.
            return -1

        cnt = (xy >> 1) + (yx >> 1)
        if xy & 1:  # Remaining pari is xy, yx.
            cnt += 2

        return cnt
