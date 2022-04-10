"""
https://leetcode.com/problems/contiguous-array/
"""


from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = cnt = 0
        memo = {0: -1}  # cnt: first occurred index.
        for i, n in enumerate(nums):
            cnt = cnt + 1 if n else cnt - 1
            if cnt not in memo:
                memo[cnt] = i
            else:
                maxLen = max(maxLen, i - memo[cnt])

        return maxLen
