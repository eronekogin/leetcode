"""
https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/
"""


class Solution:
    """
    Solution
    """

    def valid_strings(self, n: int) -> list[str]:
        """
        valid strings
        """
        curr_strings = ['0', '1']

        for _ in range(2, n + 1):
            next_strings: list[str] = []
            for s in curr_strings:
                if s[-1] == '1':
                    next_strings.append(s + '0')

                next_strings.append(s + '1')

            curr_strings = next_strings

        return curr_strings
