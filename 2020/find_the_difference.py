"""
https://leetcode.com/problems/find-the-difference/
"""


from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        rslt = 0
        for c in s:
            rslt ^= ord(c)

        for c in t:
            rslt ^= ord(c)

        return chr(rslt)

    def findTheDifference2(self, s: str, t: str) -> str:
        diff = Counter(t) - Counter(s)
        return list(diff.keys())[0]
