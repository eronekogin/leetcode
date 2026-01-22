"""
https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def min_sum(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Docstring for min_sum

        :param self: Description
        :param nums1: Description
        :type nums1: list[int]
        :param nums2: Description
        :type nums2: list[int]
        :return: Description
        :rtype: int
        """
        def count(nums: list[int]):
            total = zeros = 0
            for x in nums:
                total += x
                if x == 0:
                    total += 1  # Replace zero with minimum 1
                    zeros += 1

            return (total, zeros)

        t1, z1 = count(nums1)
        t2, z2 = count(nums2)

        if (
            (z1 == 0 and t2 > t1) or
            (z2 == 0 and t1 > t2)
        ):
            return -1

        return max(t1, t2)
