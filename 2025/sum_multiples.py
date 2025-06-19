"""
https://leetcode.com/problems/sum-multiples/description/
"""


class Solution:
    """
    Solution
    """

    def sum_of_multiples(self, n: int) -> int:
        """
        sum of multiples
        """
        return sum(
            x
            for x in range(1, n + 1)
            if x % 3 == 0 or x % 5 == 0 or x % 7 == 0
        )
