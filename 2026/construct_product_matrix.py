"""
https://leetcode.com/problems/construct-product-matrix/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def construct_product_matrix(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Docstring for construct_product_matrix

        :param self: Description
        :param grid: Description
        :type grid: list[list[int]]
        :return: Description
        :rtype: list[list[int]]
        """
        m, n = len(grid), len(grid[0])
        mod = 12345
        prefix = [1]
        suffix = [1]

        for r in range(m):
            for c in range(n):
                prefix.append((prefix[-1] * grid[r][c]) % mod)

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                suffix.append((suffix[-1] * grid[r][c]) % mod)

        rslt = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                k = r * n + c
                rslt[r][c] = (prefix[k] * suffix[-k - 2]) % mod

        return rslt
