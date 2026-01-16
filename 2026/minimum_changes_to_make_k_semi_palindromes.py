"""
https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/description/
"""


from collections import defaultdict
from functools import cache


class Solution:
    """
    Docstring for Solution
    """

    def minimum_changes(self, s: str, k: int) -> int:
        """
        Docstring for minimum_changes

        :param self: Description
        :param s: Description
        :type s: str
        :param k: Description
        :type k: int
        :return: Description
        :rtype: int
        """
        @cache
        def semi(i: int, j: int, d: int):
            """
            The cost to change s[i: j] to a semi palindrom with
            divsor d
            """
            if i >= j:
                return 0

            return (
                semi(i + d, j - d, d) +
                sum(
                    s[i + m] != s[j - d + m]
                    for m in range(d)
                )
            )

        def change(i: int, j: int):
            """
            The cost to change s[i: j] to a semi palindrome
            """
            return min(semi(i, j, d) for d in divisors[j - i])

        @cache
        def dp(j: int, k: int):
            """
            dp[j, k] stands for the cost to split s[:j] into k
            semi palindromes
            """
            if k == 1:
                return change(0, j)

            return min(
                dp(i, k - 1) + change(i, j)
                for i in range((k - 1) * 2, j - 1)
            )

        divisors = defaultdict(lambda: [1])
        n = len(s)
        for d in range(2, n):
            for v in range(d + d, n + 1, d):
                divisors[v].append(d)

        return dp(n, k)
