"""
https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/
"""


from collections import defaultdict
from math import comb


class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        def dfs(parent: int):
            """
            Suppose dfs(parent) stands for the number of ways to build rooms starting from parent node:
                1. If the parent node contains just two branches, each branch is a chain, and suppose left length is l
                    and right length is r, then we are simply picking l from l + r positions, the remaining r positions
                    are fixed, so the total ways are comb(l + r, l)
                
                2. Then if the two branches are not chain, suppose dfs(left) is x and dfs(right) is y, then the total
                    ways are x * y * comb(l + r, l)

                3. Then if there are more than two branches, we can combine result with two adjacent branches from
                    leftmost until we reached the end. 
            """
            if not parents[parent]:  # leaf node.
                return (1, 1)
            
            rslt, l = 1, 0
            for child in parents[parent]:
                tmp, r = dfs(child)
                rslt = (rslt * tmp * comb(l + r, r)) % MOD
                l += r
            
            return rslt, l + 1

        parents = defaultdict(list)
        for child, parent in enumerate(prevRoom):
            parents[parent].append(child)
        
        MOD = 10 ** 9 + 7

        return dfs(0)[0]
