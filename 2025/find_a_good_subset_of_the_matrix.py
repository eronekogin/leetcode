"""
https://leetcode.com/problems/find-a-good-subset-of-the-matrix/description/
"""


class Solution:
    """
    Solution
    """

    def good_subset_of_binary_matrix(self, grid: list[list[int]]) -> list[int]:
        """
        good subset of binary matrix
        """
        if len(grid) == 1:
            return [0] if all(x == 0 for x in grid[0]) else []

        memo: dict[int, int] = {}
        for i, row in enumerate(grid):
            curr = sum(d << j for j, d in enumerate(row))
            for key, value in memo.items():
                if key & curr == 0:
                    return [value, i]

            memo[curr] = i

        return []
