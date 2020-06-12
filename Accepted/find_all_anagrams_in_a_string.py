"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""


from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(s) < len(p):
            return []

        start = end = 0
        maxLen, step = len(s), len(p)
        rslt, cs, cp = [], {}, Counter(p)
        while end < maxLen:
            cs[s[end]] = cs.get(s[end], 0) + 1
            if end - start + 1 == step:
                if cs == cp:
                    rslt.append(start)

                cs[s[start]] -= 1
                if not cs[s[start]]:
                    del cs[s[start]]

                start += 1

            end += 1

        return rslt
