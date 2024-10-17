"""
https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
"""


class Solution:
    """
    Solution
    """

    def match_players_and_trainers(self, players: list[int], trainers: list[int]) -> int:
        """
        match player and trainers
        """
        sorted_players, sorted_trainers = sorted(players), sorted(trainers)
        i, j = len(players) - 1, len(trainers) - 1
        matched = 0
        while i >= 0 and j >= 0:
            while i >= 0 and sorted_players[i] > sorted_trainers[j]:
                i -= 1

            if i >= 0:
                matched += 1
                j -= 1
                i -= 1

        return matched
