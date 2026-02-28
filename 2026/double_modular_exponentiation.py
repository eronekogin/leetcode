"""
https://leetcode.com/problems/double-modular-exponentiation/description/
"""


class Solution:
    """
    Solution
    """

    def get_good_indices(self, variables: list[list[int]], target: int) -> list[int]:
        """
        get good indices
        """
        return [
            i
            for i, (a, b, c, m) in enumerate(variables)
            if pow(pow(a, b, 10), c, m) == target
        ]
