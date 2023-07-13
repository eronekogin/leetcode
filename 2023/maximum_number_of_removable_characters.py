"""
https://leetcode.com/problems/maximum-number-of-removable-characters/
"""


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def check(m: int):
            i = j = 0
            while i < len(s) and j < len(p):
                if i in memo and memo[i] <= m:  # Skip removable.
                    pass
                elif s[i] == p[j]:
                    j += 1
                
                i += 1
            
            return j == len(p)

        l, r = 0, len(removable) + 1
        memo = {r: i for i, r in enumerate(removable)}
        while l < r:
            m = l + ((r - l) >> 1)
            if check(m):
                l = m + 1
            else:
                r = m
        
        if l < len(removable):
            return l
        
        return l - 1