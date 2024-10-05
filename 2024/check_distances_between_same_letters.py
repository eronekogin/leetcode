"""
https://leetcode.com/problems/check-distances-between-same-letters/description/
"""


class Solution:
    """
    Solution
    """

    def check_distances(self, s: str, distance: list[int]) -> bool:
        """
        check distances
        """
        memo = [-1] * 26
        offset = ord('a')
        for i, c in enumerate(s):
            j = ord(c) - offset
            if memo[j] == -1:
                memo[j] = i
            else:
                memo[j] = i - memo[j] - 1

        for i, d in enumerate(distance):
            if memo[i] >= 0 and memo[i] != d:
                return False

        return True
