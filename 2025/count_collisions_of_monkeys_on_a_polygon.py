"""
https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description/
"""


class Solution:
    """
    Solution
    """

    def monkey_move(self, n: int) -> int:
        """
        Each monkey has two directions to move, so the total
        number of moves is 2^n. Now count the case when no collision
        will happen:
            1. All monkey goes to the same direction, which can be
                clockwise or anti-clockwise.
            2. When n is even, half monkeys can go adjancent direction
                who exchange the positions with the other half of monkeys.

        So when n is even, the answer will be 2^n - 4 instead. 
        """
        m = 10 ** 9 + 7
        return (pow(2, n, m) - 2) % m
