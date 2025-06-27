"""
https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/
"""


class Solution:
    """
    Solution
    """

    def is_winner(self, player1: list[int], player2: list[int]) -> int:
        """
        is winner
        """
        def count_score(pins: list[int]):
            score = 0
            for i, x in enumerate(pins):
                if (
                    (i > 0 and pins[i - 1] == 10) or
                    (i > 1 and pins[i - 2] == 10)
                ):
                    score += x

                score += x

            return score

        s1, s2 = count_score(player1), count_score(player2)
        if s1 > s2:
            return 1

        if s1 == s2:
            return 0

        return 2
