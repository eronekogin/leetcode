"""
https://leetcode.com/problems/count-total-number-of-colored-cells/description/
"""


class Solution:
    """
    Solution
    """

    def colored_cells(self, n: int) -> int:
        """
        sk = 1 + 4 * (1 + 2 + ... + k - 1)
            = 1 + 2 * k * (k - 1)
        """
        return 1 + 2 * n * (n - 1)
