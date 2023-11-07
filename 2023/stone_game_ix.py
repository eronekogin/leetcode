"""
https://leetcode.com/problems/stone-game-ix/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def stone_game_ix(self, stones: list[int]) -> bool:
        """
        * if alice starts with mod3 == 1, then the pick order is 1, 1, 2, 1, 2, 1, 2, ..., which
            means alice needs mod3 == 2 in the next picks.
        * if alice starts with mod3 == 2, then the pick order is 2, 2, 1, 2, 1, 2, 1, ..., which
            means alice needs mod3 == 1 in the next picks.

        So we have:
            * if cnt[1] == 0, alice needs to start with 2
            * if cnt[2] == 0, alice needs to start with 1
            * alice can win if max(cnt[1], cnt[2]) > 2 and cnt[0] is odd.
            * if cnt[0] is even, alice can choose the less one from 1 and 2.
        """
        cnt = Counter(s % 3 for s in stones)
        if cnt[0] & 1 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        return abs(cnt[1] - cnt[2]) > 2
