"""
https://leetcode.com/problems/string-transformation/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_ways(self, s: str, t: str, k: int) -> int:
        """
        number of ways
        """
        def kmp(s: str, t: str):
            pi = [0 for _ in range(len(t))]
            res = []
            for i in range(1, len(t)):
                j = pi[i - 1]

                while j > 0 and t[j] != t[i]:
                    j = pi[j - 1]

                pi[i] = 0 if j == 0 and t[0] != t[i] else j + 1

            m, n, j = len(s), len(t), 0

            for i in range(m):
                while j >= n or j > 0 and s[i] != t[j]:
                    j = pi[j - 1]

                if s[i] == t[j]:
                    j += 1

                if j == n:
                    res.append(i - n + 1)

            return res

        n, m = len(s), 10**9 + 7
        pos = kmp((s + s)[:-1], t)
        fk = [0, 0]
        fk[1] = (pow(n - 1, k, m) - (-1)**k + m) * pow(n, m - 2, m) % m
        fk[0] = (fk[1] + (-1)**k + m) % m

        return sum(fk[not not p] for p in pos) % m
