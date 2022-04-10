"""
https://leetcode.com/problems/permutation-in-string/
"""


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s2) < len(s1):
            return False

        c1 = Counter(s1)
        start, end = len(s1) - 1, len(s2)
        c2 = Counter(s2[:start])
        for i in range(start, end):
            c2[s2[i]] += 1
            if c2 == c1:
                return True

            removeChar = s2[i - start]
            c2[removeChar] -= 1
            if not c2[removeChar]:
                c2.pop(removeChar)

        return False
