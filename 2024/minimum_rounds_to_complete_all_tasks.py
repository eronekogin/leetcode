"""
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_tounds(self, tasks: list[int]) -> int:
        """
        minimum rounds
        """
        cnt = Counter(tasks)
        rounds = 0
        for v in cnt.values():
            if v < 2:
                return -1

            q, r = divmod(v, 3)
            rounds += q + (r > 0)

        return rounds
