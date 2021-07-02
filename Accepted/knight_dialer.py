"""
https://leetcode.com/problems/knight-dialer/
"""


class Solution:
    def knightDialer(self, n: int) -> int:
        """
        Simply generating the current counters from previous results. For
        example, when n = 3, first the knight was placed at 0, then for the
        first jump, knight could move to 4 and 6, and the next jump the knight
        could move to 0, 3, 9 or 0, 1, 7.
        """
        MOD = 10 ** 9 + 7
        JUMP_TO = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: tuple(),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }

        currCnts = [1] * 10
        for _ in range(n - 1):
            nextCnts = [0] * 10
            for src in range(10):
                for dest in JUMP_TO[src]:
                    nextCnts[dest] = (nextCnts[dest] + currCnts[src]) % MOD

            currCnts = nextCnts

        return sum(currCnts) % MOD


print(Solution().knightDialer(4))
