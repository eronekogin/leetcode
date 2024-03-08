"""
https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/description/
"""


class Solution:
    """
    Solution
    """

    def sum_of_three(self, num: int) -> list[int]:
        """
        sum of three
        """
        total = num - 3
        x, r = divmod(total, 3)
        if r == 0:
            return [x, x + 1, x + 2]

        return []
