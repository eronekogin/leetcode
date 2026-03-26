"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_operations_to_make_equal(self, x: int, y: int) -> int:
        """
        minimum operations to make equal
        """
        if x <= y:
            return y - x

        ops = x - y

        for v in (5, 11):
            ops = min(
                ops,
                (
                    self.minimum_operations_to_make_equal(x // v, y) +
                    1 + x % v
                ),
                (
                    self.minimum_operations_to_make_equal(x // v + 1, y) +
                    1 + v - x % v
                )
            )

        return ops
