"""
https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/description/
"""


from math import comb


class Solution:
    """
    Solution
    """

    def number_of_ways(self, start_pos: int, end_pos: int, k: int) -> int:
        """
        number of ways
        """
        if (start_pos - end_pos - k) & 1:
            return 0

        return comb(k, (end_pos - start_pos + k) >> 1) % (10 ** 9 + 7)
