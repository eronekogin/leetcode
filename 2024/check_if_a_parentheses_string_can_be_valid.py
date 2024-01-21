"""
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/
"""


class Solution:
    """
    Solution
    """

    def can_be_valid(self, s: str, locked: str) -> bool:
        """
        can_be_valid
        """
        if len(s) & 1:
            return False

        # scan left to right for '('.
        balance = wild = 0
        for i, c in enumerate(s):
            if locked[i] == '1':
                balance += 1 if c == '(' else -1
            else:
                wild += 1

            if balance + wild < 0:  # Not balance any longer.
                return False

        if balance > wild:
            return False

        # Scan right to left for ')'.
        balance = wild = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                balance += 1 if s[i] == ')' else -1
            else:
                wild += 1

            if balance + wild < 0:  # Not balance any longer.
                return False

        return balance <= wild


print(Solution().can_be_valid('))()))', '010100'))
