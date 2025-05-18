"""
https://leetcode.com/problems/mice-and-cheese/description/
"""


class Solution:
    """
    Solution
    """

    def mice_and_cheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        """
        mice and cheese
        """
        points = sum(reward2)
        sorted_diffs = sorted(
            [r1 - r2 for r1, r2 in zip(reward1, reward2)],
            reverse=True
        )
        return points + sum(sorted_diffs[:k])


print(Solution().mice_and_cheese([1, 4, 4, 6, 4], [6, 5, 3, 6, 1], 1))
