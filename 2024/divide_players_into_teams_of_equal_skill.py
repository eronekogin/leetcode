"""
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def divide_players(self, skill: list[int]) -> int:
        """
        divide players
        """
        teams = len(skill) >> 1
        target, r = divmod(sum(skill), teams)

        if r > 0:  # Not dividible.
            return -1

        cnt = Counter(skill)
        chemistry = 0
        for s, freq in cnt.items():
            other_skill = target - s
            other_freq = cnt[other_skill]
            if other_freq != freq:
                return -1

            chemistry += s * other_skill * freq

        return chemistry >> 1


print(Solution().divide_players([5, 3, 7, 1]))
