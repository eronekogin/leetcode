"""
https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/description/
"""


from functools import cache


class Solution:
    """
    Docstring for Solution
    """

    def min_operations(self, s1: str, s2: str, x: int) -> int:
        """
        Docstring for min_operations

        :param self: Description
        :param s1: Description
        :type s1: str
        :param s2: Description
        :type s2: str
        :param x: Description
        :type x: int
        :return: Description
        :rtype: int
        """
        @cache
        def dfs(start: int, end: int):
            if start == end:
                return 0

            return min(
                (
                    min(x, s[k] - s[start]) +
                    dfs(start + 1, k) +
                    dfs(k + 1, end)
                )
                for k in range(start + 1, end, 2)
            )

        s = [i for i in range(len(s1)) if s1[i] != s2[i]]

        if len(s) & 1:
            return -1  # Not possible to swap in odd difference

        return dfs(0, len(s))
