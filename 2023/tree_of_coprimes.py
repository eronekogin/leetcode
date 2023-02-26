"""
https://leetcode.com/problems/tree-of-coprimes/
"""


from collections import defaultdict
from math import gcd


class Solution:
    def getCoprimes(
        self,
        nums: list[int],
        edges: list[list[int]]
    ) -> list[int]:
        def dfs(node: int, depth: int):
            if node in visited:
                return

            visited.add(node)
            maxDepth = -1
            for x in range(1, 51):
                if gcd(nums[node], x) == 1:
                    if len(paths[x]) > 0:
                        topNode, topDepth = paths[x][-1]
                        if maxDepth < topDepth:
                            maxDepth = topDepth
                            rslt[node] = topNode

            paths[nums[node]].append((node, depth))

            for neighbor in graph[node]:
                dfs(neighbor, depth + 1)

            paths[nums[node]].pop()

        N = len(nums)
        rslt = [-1] * N
        paths: list[list[tuple[int, int]]] = [[] for _ in range(51)]
        graph = defaultdict(list)
        visited: set[int] = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dfs(0, 0)
        return rslt
