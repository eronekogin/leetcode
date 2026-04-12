"""
https://leetcode.com/problems/number-of-changing-keys/description/
"""


class Solution:
    """
    Solution
    """

    def count_key_changes(self, s: str) -> int:
        """
        count key changes
        """
        return sum(
            x.lower() != y.lower()
            for x, y in zip(s, s[1:])
        )
