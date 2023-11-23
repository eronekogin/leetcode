"""
https://leetcode.com/problems/count-nodes-with-the-highest-score/
"""


from collections import Counter, defaultdict


class Solution:
    """
    Solution
    """

    def count_highest_score_nodes(self, parents: list[int]) -> int:
        """
        count_highest_score_nodes
        """
        def count_node(node: int):
            score, total_sub_nodes = 1, 0

            for child in graph[node]:
                sub_nodes = count_node(child)
                score *= sub_nodes
                total_sub_nodes += sub_nodes

            score *= max(1, n - 1 - total_sub_nodes)
            scores[score] += 1
            return total_sub_nodes + 1  # Include node itself.

        graph = defaultdict(list)
        for node, parent in enumerate(parents):
            graph[parent].append(node)

        n = len(parents)
        scores = Counter()
        count_node(0)

        return scores[max(scores.keys())]
