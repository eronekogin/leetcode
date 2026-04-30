"""
https://leetcode.com/problems/apply-operations-to-make-string-empty/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def last_non_empty_string(self, s: str) -> str:
        """
        last non empty string
        """
        cnt = Counter(s)
        max_f = max(cnt.values())
        rslt: list[str] = []
        for c in reversed(s):
            if cnt[c] == max_f and c not in rslt:
                rslt.append(c)

        return ''.join(reversed(rslt))
