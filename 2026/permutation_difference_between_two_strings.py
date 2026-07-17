"""
https://leetcode.com/problems/permutation-difference-between-two-strings/description/
"""


class Solution:
    """
    Solution
    """

    def find_permutation_difference(self, s: str, t: str) -> int:
        """
        find permutation difference
        """
        ms = {c: i for i, c in enumerate(s)}
        mt = {c: i for i, c in enumerate(t)}
        return sum(
            abs(ms[c] - mt[c])
            for c in ms
        )
