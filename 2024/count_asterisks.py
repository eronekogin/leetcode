"""
https://leetcode.com/problems/count-asterisks/description/
"""


class Solution:
    """
    Solution
    """

    def count_asterisks(self, s: str) -> int:
        """
        count asterisks
        """
        not_between_bars = True
        cnt = 0
        for c in s:
            if c == '|':
                not_between_bars = not not_between_bars
            elif c == '*':
                cnt += not_between_bars

        return cnt
