"""
https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/
"""


from collections import defaultdict


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        digitIndices = defaultdict(list)
        for i in range(len(s) - 1, -1, -1):
            key = int(s[i])
            digitIndices[key].append(i)

        for c in t:
            key = int(c)
            if key not in digitIndices:
                return False

            leftMostIndex = digitIndices[key][-1]
            for smallerDigit in range(key):
                if (
                    digitIndices[smallerDigit] and
                    digitIndices[smallerDigit][-1] < leftMostIndex
                ):
                    return False

            digitIndices[key].pop()

        return True
