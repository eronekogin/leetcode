"""
https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/description/
"""


class KMP:
    """
    KMP
    """

    def __init__(self, p: str):
        m = len(p)
        dp = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and p[i] != p[j]:
                j = dp[j - 1]

            if p[i] == p[j]:
                j += 1

            dp[i] = j

        self.dp = dp
        self.p = p

    def search(self, s: str):
        """
        search the next pattern in s starting at start
        """
        j = 0
        m = len(self.p)
        rslt: list[int] = []
        for i, c in enumerate(s):
            while j > 0 and c != self.p[j]:
                j = self.dp[j - 1]

            if c == self.p[j]:
                j += 1

            if j == m:
                rslt.append(i - m + 1)
                j = self.dp[j - 1]

        return rslt


class Solution:
    """
    Solution
    """

    def beautiful_indices(self, s: str, a: str, b: str, k: int) -> list[int]:
        """
        beautiful indices
        """
        ka = KMP(a)
        kb = KMP(b)

        ia, ib = ka.search(s), kb.search(s)
        rslt: list[int] = []
        i = j = 0

        while i < len(ia) and j < len(ib):
            if abs(ia[i] - ib[j]) <= k:
                rslt.append(ia[i])
                i += 1
            elif ib[j] > ia[i] + k:
                i += 1
            else:
                j += 1

        return rslt
