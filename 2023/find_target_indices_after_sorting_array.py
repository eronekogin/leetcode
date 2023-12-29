"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/
"""


class Solution:
    """
    Solution
    """

    def target_indices(self, nums: list[int], target: int) -> list[int]:
        """
        target_indices
        """
        less_count = equal_count = 0
        for x in nums:
            if x < target:
                less_count += 1
            elif x == target:
                equal_count += 1

        return list(range(less_count, less_count + equal_count))
