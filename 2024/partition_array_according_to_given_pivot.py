"""
https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
"""


class Solution:
    """
    Solution
    """

    def pivot_array(self, nums: list[int], pivot: int) -> list[int]:
        """
        pivot_array
        """
        small: list[int] = []
        middle: list[int] = []
        large: list[int] = []
        for num in nums:
            if num < pivot:
                small.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                large.append(num)

        return small + middle + large
