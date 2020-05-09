"""
https://leetcode.com/problems/evaluate-division/
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def calcEquation(
            self,
            equations: List[List[str]],
            values: List[float],
            queries: List[List[str]]) -> List[float]:
        """
        Take the equations as slope in the graph.
        """
        graph = defaultdict(dict)
        for (a, b), k in zip(equations, values):
            graph[a][b] = k
            graph[b][a] = 1 / k

        def search(a: str, b: str) -> float:
            if a not in graph or b not in graph:
                return -1.0

            if a == b:
                return 1.0

            used = {a}
            queue = deque([(a, 1.0)])
            while queue:
                currNode, currVal = queue.popleft()
                for nextNode, nextVal in graph[currNode].items():
                    if nextNode in used:  # Skipped pre-used node.
                        continue

                    totalVal = currVal * nextVal
                    if nextNode == b:
                        graph[a][b] = totalVal
                        graph[b][a] = 1 / totalVal
                        return totalVal

                    used.add(nextNode)
                    queue.append((nextNode, totalVal))

            return -1.0  # No match path.

        return [search(a, b) for a, b in queries]


e = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
v = [3.0, 4.0, 5.0, 6.0]
q = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"],
     ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
print(Solution().calcEquation(e, v, q))
