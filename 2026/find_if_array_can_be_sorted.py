"""
https://leetcode.com/problems/find-if-array-can-be-sorted/description/
"""


class Solution:
    """
    Solution
    """

    def can_sort_array(self, nums: list[int]) -> bool:
        """
        can sort array
        """
        prev_max = 0
        curr_count, curr_min, curr_max = nums[0].bit_count(), nums[0], nums[0]
        for x in nums:
            if x.bit_count() == curr_count:
                curr_min = min(curr_min, x)
                curr_max = max(curr_max, x)
            else:
                if curr_min < prev_max:
                    return False

                prev_max = curr_max
                curr_count, curr_min, curr_max = x.bit_count(), x, x

        # last group
        return prev_max < curr_min


print(Solution().can_sort_array([20, 16]))
