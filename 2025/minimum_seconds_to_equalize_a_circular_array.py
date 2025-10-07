"""
https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def minimum_seconds(self, nums: list[int]) -> int:
        """
        For any i < j and nums[i] == nums[j], for i < k < j and
        nums[k] != nums[i], for eash second we can only change 2 items,
        so we need (j - i) // 2 seconds to change all numbers between i
        and j to nums[i]
        """
        prev_positions = {}
        gaps = defaultdict(lambda: 0)

        for i, x in enumerate(nums + nums):
            if x in prev_positions:
                gaps[x] = max(gaps[x], (i - prev_positions[x]) >> 1)

            prev_positions[x] = i

        return min(gaps.values())
