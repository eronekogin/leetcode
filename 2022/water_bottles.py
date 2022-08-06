"""
https://leetcode.com/problems/water-bottles/
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            q, r = divmod(emptyBottles, numExchange)
            cnt += q
            emptyBottles = q + r

        return cnt


print(Solution().numWaterBottles(9, 3))
