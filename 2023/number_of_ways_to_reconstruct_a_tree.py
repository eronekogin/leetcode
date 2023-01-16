"""
https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/
"""

from collections import defaultdict


class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        def helper(nodes: list[int]):
            def dfs(node: int, i: int):
                comps[i].add(node)
                seen.add(node)
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        dfs(neighbor, i)

            degree = defaultdict(list)
            maxDegree = len(nodes) - 1
            for node in nodes:
                degree[len(graph[node])].append(node)

            if len(degree[maxDegree]) == 0:
                # Found no node that connects to all the other nodes.
                return 0

            root = degree[maxDegree][0]  # Just pick the first root candidate.
            for node in graph[root]:
                graph[node].remove(root)

            i = 0
            comps = defaultdict(set)
            seen = set()
            for node in nodes:
                if node != root and node not in seen:
                    dfs(node, i)
                    i += 1

            candidates = [helper(comps[i]) for i in comps]
            if 0 in candidates:
                return 0

            if 2 in candidates:
                # More than 2 solutions found for the current root.
                return 2

            if len(degree[maxDegree]) > 1:
                # More than 1 candidate root.
                return 2

            return 1

        graph = defaultdict(set)
        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)

        return helper(set(graph.keys()))
