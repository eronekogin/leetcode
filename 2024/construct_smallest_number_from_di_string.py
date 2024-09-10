"""
https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_number(self, pattern: str) -> str:
        """
        Every time we met a 'I', we reverse any number between
        the previous 'I' and the current 'I'
        """
        rslt: list[str] = []
        stack: list[str] = []

        for i, c in enumerate(pattern + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                rslt += stack[::-1]
                stack = []

        return ''.join(rslt)


print(Solution().smallest_number('IIIDIDDD'))
