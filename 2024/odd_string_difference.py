"""
https://leetcode.com/problems/odd-string-difference/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def odd_string(self, words: list[str]) -> str:
        """
        odd string
        """
        def convert(w: str):
            return ' '.join(
                str(ord(y) - ord(x))
                for x, y in zip(w, w[1:])
            )

        memo: defaultdict[str, list[str]] = defaultdict(list)
        for w in words:
            memo[convert(w)].append(w)

        for v in memo.values():
            if len(v) == 1:
                return v[0]

        return ''


print(Solution().odd_string(["abm", "bcn", "alm"]))
