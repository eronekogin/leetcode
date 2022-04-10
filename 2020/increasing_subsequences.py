"""
https://leetcode.com/problems/increasing-subsequences/
"""


from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}

        return [list(sub) for sub in subs if len(sub) >= 2]


print(Solution().findSubsequences([4, 6, 7, 7]))
