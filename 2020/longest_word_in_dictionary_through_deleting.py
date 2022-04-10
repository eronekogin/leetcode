"""
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""


from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        for t in sorted(d, key=lambda x: (-len(x), x)):
            iterS = iter(s)
            if all(c in iterS for c in t):
                return t

        return ''  # No solution found.

    def findLongestWord2(self, s: str, d: List[str]) -> str:
        """
        Without sorting.
        """
        rslt = ''
        for t in d:
            iterS = iter(s)
            if all(c in iterS for c in t) and (
                    len(t) > len(rslt) or (len(t) == len(rslt) and t < rslt)):
                rslt = t

        return rslt
