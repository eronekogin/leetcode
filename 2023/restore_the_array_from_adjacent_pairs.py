"""
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
"""


from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        rslt = []
        N = len(adjacentPairs) + 1
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        prev = None
        for k, v in graph.items():
            if len(v) == 1:  # The start point only has 1 neighbor.
                rslt.append(k)
                break

        while len(rslt) < N:
            for curr in graph[rslt[-1]]:
                if curr != prev:
                    prev = rslt[-1]
                    rslt.append(curr)
                    break

        return rslt
