"""
https://leetcode.com/problems/match-substring-after-replacement/description/
"""


class Solution:
    """
    Solution
    """

    def match_replacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        """
        match replacement
        """
        if sub in s:
            return True

        memo: dict[str, set[str]] = {c: {c} for c in sub}
        for u, v in mappings:
            memo[u] = memo.get(u, set()) | {v}

        n = len(sub)
        for i in range(len(s) - n + 1):
            if all(s[i + j] in memo[sub[j]] for j in range(n)):
                return True

        return False
