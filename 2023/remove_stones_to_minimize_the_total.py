"""
https://leetcode.com/problems/remove-stones-to-minimize-the-total/
"""


from heapq import heappush, heappop, heapify


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        stones = [-stone for stone in piles]
        heapify(stones)
        for _ in range(k):
            currMaxStone = -heappop(stones)
            heappush(stones, -(currMaxStone - (currMaxStone >> 1)))
        
        return -sum(stones)

        