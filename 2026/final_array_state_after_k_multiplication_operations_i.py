"""
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def get_final_state(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        """
        get final state
        """
        heap = [(x, i) for i, x in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            x, i = heappop(heap)
            x *= multiplier
            heappush(heap, (x, i))
            nums[i] = x

        return nums
