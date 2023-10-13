"""
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
"""


class Solution:
    """
    Solution.
    """

    def number_of_weak_characters(self, properties: list[list[int]]) -> int:
        """
        number of weak characters.
        """
        cnt = 0
        max_defense = 0
        for _, defense in sorted(properties, key=lambda x: (-x[0], x[1])):
            if defense < max_defense:
                cnt += 1
            else:
                max_defense = defense

        return cnt


print(Solution().number_of_weak_characters([[1, 5], [10, 4], [4, 3]]))
