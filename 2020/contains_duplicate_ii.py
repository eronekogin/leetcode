"""
https://leetcode.com/problems/contains-duplicate-ii/
"""


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}  # number:index.
        for i, num in enumerate(nums):
            if num in memo and i <= k + memo[num]:
                return True

            # Update with the current index for later comparison.
            memo[num] = i

        return False
