"""
https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
"""


from heapq import heapify, heappop, heappush
from math import floor


class Solution:
    """
    Solution
    """

    def pick_gifts(self, gifts: list[int], k: int) -> int:
        """
        pick gifts
        """
        h = [-x for x in gifts]
        heapify(h)

        for _ in range(k):
            curr = heappop(h)
            heappush(h, -floor((-curr) ** 0.5))

        return -sum(h)


print(Solution().pick_gifts([25, 64, 9, 4, 100], 4))
