"""
https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/description/
"""


class Solution:
    """
    Solution
    """

    def find_winning_player(self, skills: list[int], k: int) -> int:
        """
        find winning player
        """
        max_skill_index = skills.index(max(skills))
        if k >= max_skill_index:
            return max_skill_index

        prev_index = 0
        prev_wins = 0
        for i in range(max_skill_index):
            if skills[i] > skills[prev_index]:
                prev_index = i
                prev_wins = 1
            elif skills[i] < skills[prev_index]:
                prev_wins += 1

            if prev_wins == k:
                return prev_index

        return max_skill_index


print(Solution().find_winning_player([11, 9, 12, 2, 20, 1, 8], 3))
