"""
https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def minimum_time(self, n: int, edges: list[list[int]], disappear: list[int]) -> list[int]:
        """
        minimum time
        """
        g = [[] for _ in range(n)]
        h = [(0, 0)]
        rslt = [-1] * n

        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))

        while h:
            curr_time, u = heappop(h)
            if rslt[u] != -1:  # Already reached before
                continue

            rslt[u] = curr_time

            for v, t in g[u]:
                next_time = curr_time + t
                if next_time >= disappear[v]:
                    continue  # cannot reach any longer

                heappush(h, (next_time, v))

        return rslt
