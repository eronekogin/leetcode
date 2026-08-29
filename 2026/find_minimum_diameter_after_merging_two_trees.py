"""
https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
"""


from collections import defaultdict
from math import ceil


class Solution:
    """
    Solution
    """

    def minimum_diameter_after_merge1(
        self,
        edges1: list[list[int]],
        edges2: list[list[int]]
    ) -> int:
        """
        BFS
        """
        def find_farthest_node(memo: defaultdict[int, list[int]], start: int):
            visited = {start}
            curr_nodes = [start]

            max_distance = 0
            farthest_node = start

            while curr_nodes:
                next_nodes: list[int] = []
                for node in curr_nodes:
                    for next_node in memo[node]:
                        if next_node not in visited:
                            visited.add(next_node)
                            next_nodes.append(next_node)

                if next_nodes:
                    max_distance += 1
                    farthest_node = next_nodes[-1]

                curr_nodes = next_nodes

            return (farthest_node, max_distance)

        def find_diameter(memo: defaultdict[int, list[int]]):
            # Find the farthest node from node 0, this ensure us that the
            # farthest node it can reach is one of the end point on
            # the diameter
            farthest_node, _ = find_farthest_node(memo, 0)
            _, diameter = find_farthest_node(memo, farthest_node)
            return diameter

        def get_memo(edges: list[list[int]]):
            memo: defaultdict[int, list[int]] = defaultdict(list)
            for u, v in edges:
                memo[u].append(v)
                memo[v].append(u)

            return memo

        m1 = get_memo(edges1)
        m2 = get_memo(edges2)
        d1 = find_diameter(m1)
        d2 = find_diameter(m2)

        return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)

    def minimum_diameter_after_merge2(
        self,
        edges1: list[list[int]],
        edges2: list[list[int]]
    ) -> int:
        """
        Topological sorting
        """
        def find_diameter(memo: defaultdict[int, list[int]]):
            curr_leaves: list[int] = []
            n = len(memo)
            degrees = [0] * n

            for node, v in memo.items():
                degrees[node] = len(v)
                if degrees[node] == 1:
                    curr_leaves.append(node)

            remaining_nodes = n
            layers = 0
            while remaining_nodes > 2:
                remaining_nodes -= len(curr_leaves)
                layers += 1
                next_leaves: list[int] = []

                for leaf in curr_leaves:
                    for node in memo[leaf]:
                        degrees[node] -= 1
                        if degrees[node] == 1:
                            next_leaves.append(node)

                curr_leaves = next_leaves

            return 2 * layers + (remaining_nodes == 2)

        def get_memo(edges: list[list[int]]):
            memo: defaultdict[int, list[int]] = defaultdict(list)
            for u, v in edges:
                memo[u].append(v)
                memo[v].append(u)

            return memo

        m1 = get_memo(edges1)
        m2 = get_memo(edges2)
        d1 = find_diameter(m1)
        d2 = find_diameter(m2)

        return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)
