"""
https://leetcode.com/problems/maximize-greatness-of-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def maximize_greatness(self, nums: list[int]) -> int:
        """
        maximize greatness
        """
        nums.sort()
        cnt = 0
        prev = 0
        for x in nums:
            if x > nums[prev]:
                cnt += 1
                prev += 1

        return cnt
