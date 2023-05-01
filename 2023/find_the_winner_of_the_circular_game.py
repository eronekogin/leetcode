"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        rslt = 0
        for x in range(2, n + 1):
            rslt = (rslt + k) % x

        return rslt + 1
