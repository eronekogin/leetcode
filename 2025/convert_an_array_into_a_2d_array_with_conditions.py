"""
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
"""


class Solution:
    """
    Solution
    """

    def find_matrix(self, nums: list[int]) -> list[list[int]]:
        """
        find matrix
        """
        memo: dict[int, int] = {}
        for x in nums:
            memo[x] = memo.get(x, 0) + 1

        rows: list[list[int]] = []
        while memo:
            row: list[int] = []
            for k in list(memo.keys()):
                row.append(k)
                memo[k] -= 1
                if memo[k] == 0:
                    del memo[k]

            rows.append(row)

        return rows
