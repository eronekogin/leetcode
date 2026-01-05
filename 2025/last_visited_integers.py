"""
https://leetcode.com/problems/last-visited-integers/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def last_visited_integers(self, nums: list[int]) -> list[int]:
        """
        Docstring for last_visited_integers

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :return: Description
        :rtype: list[int]
        """
        k = 0
        rslt: list[int] = []
        seen: list[int] = []
        for x in nums:
            if x > 0:
                k = 0
                seen.append(x)
                continue

            k += 1
            if k > len(seen):
                rslt.append(-1)
            else:
                rslt.append(seen[-k])

        return rslt
