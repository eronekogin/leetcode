"""
https://leetcode.com/problems/find-missing-and-repeated-values/description/
"""


class Solution:
    """
    Solution
    """

    def find_missing_and_repeated_values(self, grid: list[list[int]]) -> list[int]:
        """
        find missing and repeated values
        """
        n = len(grid)
        cnt = [0] * (n * n)
        for row in grid:
            for x in row:
                cnt[x - 1] += 1

        a = b = -1
        for i, x in enumerate(cnt):
            if x == 2:
                a = i + 1
            elif x == 0:
                b = i + 1

        return [a, b]
