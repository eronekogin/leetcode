"""
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        pairs = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                pairs.append((c1, c2))
                if len(pairs) > 2:
                    return False

        if not pairs:
            return True

        if len(pairs) == 1:
            return False

        if pairs[0][0] != pairs[1][1] or pairs[0][1] != pairs[1][0]:
            return False

        return True
