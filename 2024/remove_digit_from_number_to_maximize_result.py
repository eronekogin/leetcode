"""
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
"""


class Solution:
    """
    Solution
    """

    def remove_digit(self, number: str, digit: str) -> str:
        """
        remove digit
        """
        return str(
            max(
                int(number[:i] + number[i + 1:])
                for i, c in enumerate(number)
                if c == digit
            )
        )
