"""
https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def string_count(self, n: int) -> int:
        """
        see https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/solutions/4276710/c-java-python-inclusion-exclusion-math-o-vyo4/
        for more details
        """
        mod = 10 ** 9 + 7
        return (
            + pow(26, n, mod)
            - (n + 75) * pow(25, n - 1, mod)
            + (2 * n + 72) * pow(24, n - 1, mod)
            - (n + 23) * pow(23, n - 1, mod)
        ) % mod
