"""
https://leetcode.com/problems/minimize-length-of-array-using-operations/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_array_length(self, nums: list[int]) -> int:
        """
        minimum array length
        """
        min_num = min(nums)
        for x in nums:
            if x % min_num > 0:
                # x % min_num is less than min_num,
                # so x % min_num will be the only number
                # in the result array
                return 1

        return (nums.count(min_num) + 1) >> 1


print(Solution().minimum_array_length([1, 4, 3, 1]))
