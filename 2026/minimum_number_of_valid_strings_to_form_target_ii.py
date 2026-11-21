"""
https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/description/
"""


class Solution:
    """
    Solution
    """

    def min_valid_strings(self, words: list[str], target: str) -> int:
        """
        match target from right to left, then we can simply take the maximum prefix
        in words that match target
        """
        def generate_prefix(s: str):
            n = len(s)
            lps = [0] * n

            for i in range(1, n):
                j = lps[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = lps[j - 1]

                if s[i] == s[j]:
                    j += 1

                lps[i] = j

            return lps

        n = len(target)
        ps = [0] * (n + 1)
        for w in words:
            lps = generate_prefix(w + '#' + target)
            for i in range(1, n + 1):
                ps[i] = max(ps[i], lps[len(w) + i])

        rslt = 0
        while n and ps[n]:
            n -= ps[n]
            rslt += 1

        if n == 0:
            return rslt

        return -1
