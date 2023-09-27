"""
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
"""


from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        def dijkstra(src: int):
            dist = [float('inf')] * n
            ways = [0] * n
            heap = [(0, src)]
            ways[src] = 1
            
            while heap:
                d, u = heappop(heap)
                if dist[u] < d:
                    continue

                for v, t in graph[u]:
                    if dist[v] > d + t:
                        dist[v] = d + t
                        ways[v] = ways[u]
                        heappush(heap, (dist[v], v))
                    elif dist[v] == d + t:
                        ways[v] = (ways[u] + ways[v]) % MOD
            
            return ways[-1]

        MOD = 10 ** 9 + 7

        # Build graph.
        graph: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        return dijkstra(0)


print(Solution().countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))