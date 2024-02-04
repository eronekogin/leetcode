"""
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/
"""


class Solution:
    """
    Solution
    """

    def check_valid(self, matrix: list[list[int]]) -> bool:
        """
        check_valid
        """
        n = len(matrix)

        return (
            all(len(set(row)) == n for row in matrix) and
            all(len(set(col)) == n for col in zip(*matrix))
        )
