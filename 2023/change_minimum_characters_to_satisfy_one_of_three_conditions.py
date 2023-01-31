"""
https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/
"""


from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        base = ord('a')
        c1 = Counter(ord(c) - base for c in a)
        c2 = Counter(ord(c) - base for c in b)
        rslt = m + n - max((c1 + c2).values())  # Condition 3
        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            rslt = min(rslt, m - c1[i] + c2[i])  # Condition 1
            rslt = min(rslt, n - c2[i] + c1[i])  # Condition 2

        return rslt
