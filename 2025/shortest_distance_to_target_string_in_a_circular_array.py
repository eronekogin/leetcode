"""
https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/
"""


class Solution:
    """
    Solution
    """

    def closet_target(self, words: list[str], target: str, start_index: int) -> int:
        """
        closet target
        """
        min_dis = n = len(words)
        for i, c in enumerate(words):
            if c == target:
                d = abs(i - start_index)
                min_dis = min(min_dis, d, n - d)

        if min_dis == n:
            return -1

        return min_dis
