"""
https://leetcode.com/problems/sum-of-matrix-after-queries/description/
"""


class Solution:
    """
    Solution
    """

    def matrix_sum_queries(self, n: int, queries: list[list[int]]) -> int:
        """
        matrix sum queries
        """
        rslt = 0
        row_visited = col_visited = 0
        visited_rows = [0] * n
        visited_cols = [0] * n
        for is_set_column, i, v in reversed(queries):
            if (is_set_column and visited_cols[i]) or (not is_set_column and visited_rows[i]):
                continue

            if is_set_column:
                rslt += v * (n - row_visited)
                col_visited += 1
                visited_cols[i] = 1
            else:
                rslt += v * (n - col_visited)
                row_visited += 1
                visited_rows[i] = 1

        return rslt


print(Solution().matrix_sum_queries(
    2, [[1, 1, 1], [1, 0, 7], [0, 0, 0]]))
