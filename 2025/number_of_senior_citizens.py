"""
https://leetcode.com/problems/number-of-senior-citizens/description/
"""


class Solution:
    """
    Solution
    """

    def count_seniors(self, details: list[str]) -> int:
        """
        count seniors
        """
        return sum(
            int(s[11: 13]) > 60
            for s in details
        )
