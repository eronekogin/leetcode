"""
https://leetcode.com/problems/count-number-of-ways-to-place-houses/description/
"""


class Solution:
    """
    Solution
    """

    def count_house_placements(self, n: int) -> int:
        """
        count house placements
        """
        pp, p, m = 1, 1, 10 ** 9 + 7
        for _ in range(n):
            pp, p = p, (p + pp) % m

        return (p * p) % m
