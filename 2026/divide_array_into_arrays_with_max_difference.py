"""
https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/
"""


class Solution:
    """
    Solution
    """

    def divide_array(self, nums: list[int], k: int) -> list[list[int]]:
        """
        divide array
        """
        nums.sort()
        rslt: list[list[int]] = []

        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []

            rslt.append(nums[i: i + 3])

        return rslt


print(Solution().divide_array([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
