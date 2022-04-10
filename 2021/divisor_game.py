"""
https://leetcode.com/problems/divisor-game/
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        1. Base case is when the player has a current number 2, which leads to
            the next player lose the game.
        2. So at first the number is odd, as odd numbers only have odd factors,
            which means after the first player's move, the next player will
            always get an even number.
        3. Then if at the first the number is even, the player could always
            subtract 1 from it to make it an odd number, which leads the next
            player to give back an even number after his turn. Eventually the
            number will become 2, which makes the first winner win.
        4. So if both players play the game optimally, if the first player has
            odd number, he will always lose; otherwise he will always win.
        """
        return not n & 1
