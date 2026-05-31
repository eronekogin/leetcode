"""
https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, k: int) -> int:
        """
        strict order is to increase the first element to a optimized value x,
        then duplicate x until the sum is >= k.

        For such x, total ops = (x - 1) + ceil(k / x) - 1

        the reason the decrease 1 at the end is because we have an x in the
        first place.

        Now for the total ops to be minimized, we need a minimum x + ceil(k / x),
        and the sum is minimized only when x == k / x, which is x * x == k
        x = sqrt(k)
        """
        v = int(k ** 0.5)
        return v + (k - 1) // v - 1
