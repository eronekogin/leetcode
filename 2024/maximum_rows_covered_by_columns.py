"""
https://leetcode.com/problems/maximum-rows-covered-by-columns/description/
"""


from itertools import combinations


class Solution:
    """
    Solution
    """

    def maximum_rows(self, matrix: list[list[int]], num_select: int) -> int:
        """
        maximum rows
        """
        m, n = len(matrix), len(matrix[0])
        max_covered = -1
        for comb in combinations(range(n), n - num_select):
            not_covered = len({
                r
                for r in range(m)
                for c in comb
                if matrix[r][c] == 1
            })

            max_covered = max(max_covered, m - not_covered)

        return max_covered
