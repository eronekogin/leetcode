"""
https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
"""


class Solution:
    """
    Solution
    """

    def find_winners(self, matches: list[list[int]]) -> list[list[int]]:
        """
        find winners
        """
        winners = set()
        losers = set()
        one_match_losers = set()
        for w, l in matches:
            winners.add(w)

            if l not in losers:
                losers.add(l)
                one_match_losers.add(l)
            elif l in one_match_losers:
                one_match_losers.remove(l)

        return [
            sorted(winners - losers),
            sorted(one_match_losers)
        ]
