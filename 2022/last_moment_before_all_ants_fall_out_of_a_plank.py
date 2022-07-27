"""
https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
"""


class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        """
        When two ants meet, they will turn around and keep walking, then we
        could think the original ant now starts to walking at the path the
        other ant was walking, and vice versa.

        In summary, we don't need to care about which ant is which, but only
        need to calculate the longest time it will take for any ant to fall.
        """
        return max(
            max(left or [0]),
            n - min(right or [n])
        )
