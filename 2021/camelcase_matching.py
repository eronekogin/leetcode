"""
https://leetcode.com/problems/camelcase-matching/
"""


class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def match(query: str) -> bool:
            idxP = 0
            for c in query:
                if idxP < LP and c == pattern[idxP]:
                    idxP += 1
                elif c.isupper():
                    return False

            return idxP == LP

        LP = len(pattern)
        return map(match, queries)
