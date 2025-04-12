"""
https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/description/
"""


class Solution:
    """
    Solution
    """

    def max_num_of_marked_indices(self, nums: list[int]) -> int:
        """
        max num of marked indices
        """
        nums.sort()
        l, r = 0, len(nums) >> 1
        while r < len(nums) and l < (len(nums) >> 1):
            if (nums[l] << 1) <= nums[r]:
                l += 1

            r += 1

        return l << 1


print(Solution().max_num_of_marked_indices([9, 2, 5, 4]))
