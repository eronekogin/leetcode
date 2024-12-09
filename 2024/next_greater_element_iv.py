"""
https://leetcode.com/problems/next-greater-element-iv/description/
"""


class Solution:
    """
    Solution
    """

    def second_greater_element(self, nums: list[int]) -> list[int]:
        """
        second greater element
        """
        rslt = [-1] * len(nums)
        not_found_first: list[int] = []
        not_found_second: list[int] = []

        for i, x in enumerate(nums):
            while not_found_second and nums[not_found_second[-1]] < x:
                rslt[not_found_second.pop()] = x

            tmp: list[int] = []
            while not_found_first and nums[not_found_first[-1]] < x:
                tmp.append(not_found_first.pop())

            not_found_second.extend(reversed(tmp))
            not_found_first.append(i)

        return rslt
