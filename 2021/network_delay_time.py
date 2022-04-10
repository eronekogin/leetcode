"""
https://leetcode.com/problems/network-delay-time/
"""


from typing import List


from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Use Djikstra algorithm to find the shorted path from the given source
        node to any other nodes in the graph. Here the visited dictionary
        stores the shortest time from the source node to the node specified by
        the key.

        Use heap so that we could always return the nearest node (the node
        having the minimum elapsed time).
        """
        memo = defaultdict(list)
        for s, d, t in times:
            memo[s].append((d, t))

        heap, visited = [(0, k)], {}
        while heap:
            elapsedTime, node = heappop(heap)
            if node not in visited:
                visited[node] = elapsedTime
                for d, t in memo[node]:
                    if d not in visited:
                        heappush(heap, (elapsedTime + t, d))

        if len(visited) < n:  # Not able to reach all nodes.
            return -1

        return max(visited.values())


print(Solution().networkDelayTime(
    [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
))
