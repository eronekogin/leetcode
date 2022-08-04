"""
https://leetcode.com/problems/path-with-maximum-probability/
"""


from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start: int,
        end: int
    ) -> float:
        probs = [0] * n
        graph = defaultdict(list)
        for i, (src, dest) in enumerate(edges):
            graph[src].append((dest, succProb[i]))
            graph[dest].append((src, succProb[i]))

        probs[start] = 1

        heap = [(-probs[start], start)]
        while heap:
            prob, node = heappop(heap)
            if node == end:
                return -prob

            for nextNode, nextProb in graph[node]:
                newProb = -prob * nextProb
                if newProb > probs[nextNode]:
                    # Only update prob when the prob for the next node could
                    # be higher than before.
                    probs[nextNode] = newProb
                    heappush(heap, (-newProb, nextNode))

        return 0  # Not possible.


print(Solution().maxProbability(3,
                                [[0, 1], [1, 2], [0, 2]],
                                [0.5, 0.5, 0.2],
                                0,
                                2))
