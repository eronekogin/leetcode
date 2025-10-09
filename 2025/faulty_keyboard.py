"""
https://leetcode.com/problems/faulty-keyboard/description/
"""


class Solution:
    """
    Solution
    """

    def final_string(self, s: str) -> str:
        """
        final string
        """
        as_is: list[str] = []
        as_reversed: list[str] = []

        for c in s:
            if c == 'i':
                as_is, as_reversed = as_reversed, as_is
            else:
                as_is.append(c)

        return ''.join(as_reversed[::-1] + as_is)


print(Solution().final_string("abcidefighi"))
