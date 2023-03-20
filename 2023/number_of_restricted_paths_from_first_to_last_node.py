"""
https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
"""


from collections import defaultdict
from heapq import heappush, heappop
from functools import cache


class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        def get_distances():
            """
            Use Dijkstra algorithm to calculate the shortest distance from
            the last node n to any other nodes.
            """
            h = [(0, n)]
            distances = [float('inf')] * n + [0]
            while h:
                d, u = heappop(h)
                if d != distances[u]:
                    continue

                for w, v in g[u]:
                    if distances[v] > distances[u] + w:
                        distances[v] = distances[u] + w
                        heappush(h, (distances[v], v))

            return distances

        @cache
        def check_path(currNode: int):
            """
            Use dfs algorithm to check restricted path.
            """
            if currNode == n:  # Reach the last node.
                return 1

            cnt = 0
            for _, nextNode in g[currNode]:
                if d[currNode] > d[nextNode]:
                    cnt = (cnt + check_path(nextNode)) % M

            return cnt

        if n == 1:
            return 0

        M = 10 ** 9 + 7
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((w, v))
            g[v].append((w, u))

        d = get_distances()
        return check_path(1) % M


print(Solution().countRestrictedPaths(5, [[1, 2, 3], [1, 3, 3], [
      2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]))
