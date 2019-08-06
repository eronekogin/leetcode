"""
https://leetcode.com/problems/group-anagrams/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rslt = {}
        for s in strs:
            key = tuple(sorted(s))
            rslt[key] = rslt.get(key, []) + [s]

        return list(rslt.values())


strs = ['huh', 'tit']
print(Solution().groupAnagrams(strs))
