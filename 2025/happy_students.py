"""
https://leetcode.com/problems/happy-students/description/
"""


class Solution:
    """
    Solution
    """

    def count_ways(self, nums: list[int]) -> int:
        """
        count ways
        """
        nums.sort()
        nums.append(10 ** 5 + 1)
        return (
            (nums[0] > 0) +
            sum(
                nums[i] < i + 1 < nums[i + 1]
                for i in range(len(nums) - 1)
            )
        )
