"""
https://leetcode.com/problems/elimination-game/
"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        l, r = 1, n
        step = 1
        l2r = True  # Initially deleting number from left to right.
        while l < r:
            if ((r - l) // step + 1) % 2:  # total integers is an odd number.
                r -= step
                l += step
            else:  # Total integers is an even number.
                if l2r:
                    l += step
                else:
                    r -= step

            l2r = not l2r
            step <<= 1

        return l


print(Solution().lastRemaining(9))
