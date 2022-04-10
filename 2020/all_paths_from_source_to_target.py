"""
https://leetcode.com/problems/all-paths-from-source-to-target/
"""


from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        queue = deque([(0, [0])])  # (curr node index, previous path)
        rslt = []
        lastNode = len(graph) - 1
        while queue:
            i, prePath = queue.popleft()
            for node in graph[i]:
                if node != lastNode:
                    queue.append((node, prePath + [node]))
                else:
                    rslt.append(prePath + [node])

        return rslt
