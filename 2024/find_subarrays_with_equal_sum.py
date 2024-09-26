"""
https://leetcode.com/problems/find-subarrays-with-equal-sum/description/
"""


class Solution:
    """
    Solution
    """

    def find_subarrays(self, nums: list[int]) -> bool:
        """
        find subarrays
        """
        seen: set[int] = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s in seen:
                return True

            seen.add(s)

        return False
