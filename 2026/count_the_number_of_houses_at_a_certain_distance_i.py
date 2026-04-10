"""
https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/description/
"""


class Solution:
    """
    Solution
    """

    def count_of_pairs(self, n: int, x: int, y: int) -> list[int]:
        """
        count of pairs
        """
        if x > y:
            x, y = y, x

        rslt: list[int] = [0] * n

        for i in range(1, n + 1):
            for j in range(1, i):
                d = min(
                    i - j,
                    abs(j - x) + 1 + abs(i - y)
                )

                if d:
                    rslt[d - 1] += 2

        return rslt
