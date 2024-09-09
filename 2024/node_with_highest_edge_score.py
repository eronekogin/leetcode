"""
https://leetcode.com/problems/node-with-highest-edge-score/description/
"""


class Solution:
    """
    Solution
    """

    def edge_score(self, edges: list[int]) -> int:
        """
        edge score
        """
        n = len(edges)
        scores = [0] * n
        for u, v in enumerate(edges):
            scores[v] += u

        return scores.index(max(scores))
