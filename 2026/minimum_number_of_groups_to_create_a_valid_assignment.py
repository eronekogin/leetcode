"""
https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/description/
"""


from collections import Counter
from math import ceil


class Solution:
    """
    Docstring for Solution
    """

    def min_groups_for_valid_assignment(self, balls: list[int]) -> int:
        """
        Docstring for min_groups_for_valid_assignment

        :param self: Description
        :param balls: Description
        :type balls: list[int]
        :return: Description
        :rtype: int
        """
        def check(box: int) -> int:
            total = 0
            for f in freqs:
                if (f % box) > f // box:
                    # ax + b(x + 1) = f
                    # so (a + b) x + b = f
                    # f % x = b
                    # f // x = a + b
                    # and a, b are non-negative
                    return 0

                total += ceil(f / (box + 1))

            return total

        if len(balls) == 1:
            return 1

        freqs = list(Counter(balls).values())
        max_box = min(freqs)
        for box in range(max_box, 0, -1):
            total = check(box)
            if total > 0:
                return total

        return -1
