"""
https://leetcode.com/problems/stone-game/
"""


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        """
        The first player could eithe take the 1th, the 3rd, the 5th, ... or
        take the 2nd, the 4th, the 6th, ...
        Since the total stones are odd, the sum of odd piles either greater
        or less than the sum of even piles. In the end, the first player could
        always win. 
        """
        return True
