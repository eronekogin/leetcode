"""
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
"""


class Solution:
    """
    Solution
    """

    def minimized_maximum(self, n: int, quantities: list[int]) -> int:
        """
        minimized_maximum
        """
        l, r = 1, max(quantities)
        while l < r:
            m = l + ((r - l) >> 1)
            if sum((x + m - 1) // m for x in quantities) > n:
                l = m + 1
            else:
                r = m

        return l
