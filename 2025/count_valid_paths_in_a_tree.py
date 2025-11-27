"""
https://leetcode.com/problems/count-valid-paths-in-a-tree/description/
"""

SIZE = 10 ** 5 + 1
SIEVE = [True] * SIZE
SIEVE[1] = False
for i in range(2, int(SIZE ** 0.5) + 1):
    if SIEVE[i]:
        for j in range(i * i, SIZE, i):
            SIEVE[j] = False


class Solution:
    """
    Solution
    """

    def count_paths(self, n: int, edges: list[list[int]]) -> int:
        """
        count paths
        """
        def dfs(curr_node: int, parent_node: int) -> list[int]:
            nonlocal rslt
            v = [1 - SIEVE[curr_node], SIEVE[curr_node]]

            for next_node in graph[curr_node]:
                if next_node == parent_node:
                    continue

                p = dfs(next_node, curr_node)
                rslt += (
                    p[0] * v[1] + p[1] * v[0]
                )

                if SIEVE[curr_node]:
                    v[1] += p[0]
                else:
                    v[0] += p[0]
                    v[1] += p[1]

            return v

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        rslt = 0
        dfs(1, 0)
        return rslt
