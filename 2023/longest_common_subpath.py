"""
https://leetcode.com/problems/longest-common-subpath/
"""


class Solution:
    def longestCommonSubpath(self, n: int, paths: list[list[int]]) -> int:
        def rabinKarp(path: list[int], l): # modified Rabin-Karp
            mod = 2**63 - 1 
            power = 100007
            n = len(path)
            
            seen = set()
            pow_k = pow(power, l, mod)
            currHash = 0
            for i in range(n - 1, -1, -1):
                currHash = (currHash * power + path[i]) % mod
                if i < n - l :                 
                    currHash = (mod + currHash - path[i + l] * pow_k % mod) % mod

                if i <= n - l :
                    seen.add(currHash)
            return seen
        
        
        def isValid(paths: list[list[int]], l: int):
            sets = rabinKarp(paths[0], l)
            for i in range(1,len(paths)):
                sets &= rabinKarp(paths[i], l)  # take intersection
            
            return len(sets) >= 1
        
        # Binary Search
        res = 0
        l, r = 0, len(min(paths, key=len))
        while l <= r :
            mid = (l + r ) // 2
            if isValid(paths, mid) :
                res = mid
                l = mid + 1
            else:
                r = mid - 1
            
        return res