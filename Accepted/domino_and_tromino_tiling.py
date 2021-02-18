"""
https://leetcode.com/problems/domino-and-tromino-tiling/
"""


class Solution:
    def numTilings(self, N: int) -> int:
        """
        1. We have 6 types of tiles as follows:
            xx  x  x    x  xx  xx 
                x  xx  xx  x    x
        2. Suppose we are going to tile a board with 2 columns and n rows, the
            number of tiling it is T(n). Then the tiles on the last row could
            be type 1 to 4. Type 5 to 6 could not complete the board.
            2.1 If it is type 1, the tiling ways should be T(n - 1) as all the
                above rows should be already tiled.
            2.2 If it is type 2, the tiling ways should be T(n - 2) as except
                the last two rows, all the above rows should be already tiled.
            2.3 If it is type 3, it fills the left of row n - 1 and the last
                row, and we need to fill the right of row n - 1 and all the
                above rows in order to combine with tile type 3 to complete
                the board. Suppose the ways to fill the board until the
                right of row n is T_right(n), then in our case,
                it is T_right(n - 1).
            2.4 If it is type 4, similar as 2.3, suppose the ways to fill the
                board till the left of row n is T_left(n), then in our case,
                it is T_left(n - 1).
        3. Now let's consider T_right(n):
            3.1 If it is type 2, it is T_left(n - 1).
            3.2 If it is type 6, it is T(n - 2).
        4. Similar as T_left(n), which will be T_right(n - 1) + T(n - 2).
        5. Now T(n) = T(n - 1) + T(n - 2) + T_left(n - 1) + T_right(n - 1)
            = T(n - 1) + T(n - 2) + T_left(n - 2) + T(n - 3) + T_right(n - 2)
                + T(n - 3)
            = T(n - 1) + T(n - 3) + [T(n - 2) + T(n - 3) + T_left(n - 2)
                + T_right(n - 2)]
            = T(n - 1) + T(n - 3) + T(n - 1)
            = 2 * T(n - 1) + T(n - 3)
        """
        BASE = [1, 2, 5]
        if N < 4:
            return BASE[N - 1]

        t3, t2, t1 = BASE  # Stands for T(n - 3), T(n - 2), T(n - 1).
        MOD = 10 ** 9 + 7
        for _ in range(4, N + 1):
            tn = ((t1 << 1) + t3) % MOD
            t1, t2, t3 = tn, t1, t2

        return tn
