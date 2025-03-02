"""
https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/
"""


from heapq import heapify, heappop, heappush
from math import ceil


class Solution:
    """
    Solution
    """

    def max_k_elements(self, nums: list[int], k: int) -> int:
        """
        max k elements
        """
        candidates = [-x for x in nums]
        heapify(candidates)
        score = 0
        for _ in range(k):
            x = heappop(candidates)
            score -= x
            heappush(candidates, -ceil(-x / 3))

        return score
