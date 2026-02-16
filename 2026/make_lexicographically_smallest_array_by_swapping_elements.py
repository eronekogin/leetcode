"""
https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/
"""


from collections import deque


class Solution:
    """
    Docstring for Solution
    """

    def lexicographically_smallest_array(self, nums: list[int], limit: int) -> list[int]:
        """
        Docstring for lexicographically_smallest_array

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :param limit: Description
        :type limit: int
        :return: Description
        :rtype: list[int]
        """
        sorted_nums = sorted(nums)

        g = 0
        num_to_group: dict[int, int] = {}
        num_to_group[sorted_nums[0]] = g

        group_to_list: dict[int, deque[int]] = {}
        group_to_list[g] = deque([sorted_nums[0]])

        for i in range(1, len(nums)):
            curr = sorted_nums[i]
            if abs(curr - sorted_nums[i - 1]) > limit:
                g += 1

            num_to_group[curr] = g

            if g not in group_to_list:
                group_to_list[g] = deque()

            group_to_list[g].append(curr)

        rslt: list[int] = []
        for x in nums:
            g = num_to_group[x]
            rslt.append(group_to_list[g].popleft())

        return rslt
