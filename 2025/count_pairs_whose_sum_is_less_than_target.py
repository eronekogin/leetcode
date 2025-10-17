"""
https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
"""


class Solution:
    """
    Solution
    """

    def count_pairs(self, nums: list[int], target: int) -> int:
        """
        count pairs
        """
        nums.sort()
        l, r = 0, len(nums) - 1
        pairs = 0
        while l < r:
            if nums[l] + nums[r] < target:
                pairs += r - l
                l += 1
            else:
                r -= 1

        return pairs
