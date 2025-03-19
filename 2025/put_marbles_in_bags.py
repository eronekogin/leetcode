"""
https://leetcode.com/problems/put-marbles-in-bags/description/
"""


class Solution:
    """
    Solution
    """

    def put_marbles(self, weights: list[int], k: int) -> int:
        """
        put marbles
        """
        n = len(weights)
        pair_weights = sorted(
            weights[i] + weights[i + 1] for i in range(n - 1)
        )

        return sum(
            pair_weights[n - 2 - i] - pair_weights[i]
            for i in range(k - 1)
        )
