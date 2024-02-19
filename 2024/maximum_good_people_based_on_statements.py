"""
https://leetcode.com/problems/maximum-good-people-based-on-statements/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_good(self, statements: list[list[int]]) -> int:
        """
        maximum_good
        """
        def is_valid(curr: int):
            for i in range(n):
                if curr & 1 << (n - 1 - i):
                    for j in range(n):
                        if (
                            statements[i][j] != 2 and
                            statements[i][j] != bool(curr & 1 << (n - 1 - j))
                        ):
                            return False

            return True

        n = len(statements)
        return max(
            bin(i).count('1') if is_valid(i) else 0
            for i in range(1 << n)
        )
