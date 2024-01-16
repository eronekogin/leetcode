"""
https://leetcode.com/problems/adding-spaces-to-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def add_spaces(self, s: str, spaces: list[int]) -> str:
        """
        add_spaces
        """
        rslt: list[str] = []
        j = 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                rslt.append(' ')
                j += 1

            rslt.append(c)

        return ''.join(rslt)
