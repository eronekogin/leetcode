"""
https://leetcode.com/problems/minimum-levels-to-gain-more-points/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_levels(self, possible: list[int]) -> int:
        """
        minimum levels
        """
        if len(possible) < 3:
            if possible[0] > possible[1]:
                return 1

            return -1

        score = [-1 if x == 0 else 1 for x in possible]
        total = sum(score)
        sa = 0
        for i in range(len(score) - 1):
            sa += score[i]
            total -= score[i]
            if sa > total:
                return i + 1

        return -1


print(Solution().minimum_levels([1, 0, 1, 0]))
