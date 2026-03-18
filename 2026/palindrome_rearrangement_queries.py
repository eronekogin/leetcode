"""
https://leetcode.com/problems/palindrome-rearrangement-queries/description/
"""


import numpy as np


class Solution:
    """
    Solution
    """

    def can_make_palindrome_queries(self, s: str, queries: list[list[int]]) -> list[bool]:
        """
        can make palindrome queries
        """
        n = len(s)
        pdiff = [0]
        for i in range(n >> 1):
            pdiff.append(pdiff[-1] + (s[i] != s[n - 1 - i]))

        prefix = [np.zeros(26)]

        for i in range(n):
            freq = np.copy(prefix[-1])
            freq[ord(s[i])-97] += 1
            prefix.append(freq)

        ans: list[bool] = []

        for a, b, c, d in queries:
            aa = n-1-a
            bb = n-1-b
            cc = n-1-c
            dd = n-1-d
            if (
                min(a, dd) and
                pdiff[min(a, dd)] or
                max(b, cc) < n//2 and
                pdiff[n//2] - pdiff[max(b, cc)+1] or
                b < dd and
                pdiff[dd] - pdiff[b+1] or
                cc < a
                and pdiff[a] - pdiff[cc+1]
            ):
                ans.append(False)
            else:
                upper = prefix[d+1] - prefix[c]
                lower = prefix[b+1] - prefix[a]
                if dd < a:
                    upper -= prefix[min(a, cc+1)] - prefix[dd]
                if b < cc:
                    upper -= prefix[cc+1] - prefix[max(b+1, dd)]
                if bb < c:
                    lower -= prefix[min(c, aa+1)] - prefix[bb]
                if d < aa:
                    lower -= prefix[aa+1] - prefix[max(d+1, bb)]
                cand = np.all((lower == upper) & (lower >= 0) & (upper >= 0))
                ans.append(bool(cand))

        return ans
