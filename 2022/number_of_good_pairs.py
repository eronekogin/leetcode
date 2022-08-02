"""
https://leetcode.com/problems/number-of-good-pairs/
"""


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        memo: dict[int, list[int]] = {}
        cnt = 0
        for i, num in enumerate(nums):
            if num in memo:
                cnt += len(memo[num])
                memo[num].append(i)
            else:
                memo[num] = [i]

        return cnt
