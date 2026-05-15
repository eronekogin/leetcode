"""
https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/
"""


class Solution:
    """
    Solution
    """

    def result_array(self, nums: list[int]) -> list[int]:
        """
        result array
        """
        a1: list[int] = [nums[0]]
        a2: list[int] = [nums[1]]
        for i in range(2, len(nums)):
            x = nums[i]
            if a1[-1] > a2[-1]:
                a1.append(x)
            else:
                a2.append(x)

        return a1 + a2
