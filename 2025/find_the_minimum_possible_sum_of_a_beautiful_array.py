"""
https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_possible_sum(self, n: int, target: int) -> int:
        """
        minimum possible sum
        """
        k = target // 2
        m = 10 ** 9 + 7
        if n <= k:
            return (n * (n + 1) // 2) % m

        return (
            k * (k + 1) // 2 +
            (target + target + n - k - 1) * (n - k) // 2
        ) % m
