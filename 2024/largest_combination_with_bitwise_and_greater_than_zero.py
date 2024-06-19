"""
https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/
"""


class Solution:
    """
    Solution
    """

    def largest_combination(self, candidates: list[int]) -> int:
        """
        largest combination
        """
        return max(
            sum(x & (1 << i) > 0 for x in candidates)
            for i in range(25)
        )
