"""
https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations_queries(
        self,
        n: int,
        edges: list[list[int]],
        queries: list[list[int]]
    ) -> list[int]:
        """
        min operations queries
        """
        def dfs(node: int, parent: int, depth: int):
            parents[0][node] = parent
            depths[node] = depth
            for next_node, w in graph[node]:
                if next_node == parent:
                    continue

                weights[next_node] = weights[node][:]
                weights[next_node][w] += 1
                dfs(next_node, node, depth + 1)

        def lca(start: int, end: int) -> int:
            """
            Get lowest common ancenstor for node start and end
            """
            if depths[start] > depths[end]:
                start, end = end, start

            for p in range(m):
                if (1 << p) & (depths[end] - depths[start]):
                    end = parents[p][end]

            for p in range(m - 1, -1, -1):
                if parents[p][start] != parents[p][end]:
                    start, end = parents[p][start], parents[p][end]

            if start == end:
                return start

            return parents[0][start]

        m = n.bit_length() + 1
        c = 27
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        parents = [[0] * n for _ in range(m)]

        # weights[i][j] stands for the count of weight j
        # on the path from root to node i
        weights = [[] for _ in range(n)]
        weights[0] = [0] * c

        depths = [0] * n

        dfs(0, 0, 0)

        for i in range(1, m):
            for j in range(n):
                parents[i][j] = parents[i - 1][parents[i - 1][j]]

        rslt: list[int] = []
        for start, end in queries:
            middle = lca(start, end)
            total = depths[start] + depths[end] - 2 * depths[middle]

            max_count = max(
                weights[start][w] + weights[end][w] - 2 * weights[middle][w]
                for w in range(1, c)
            )

            rslt.append(total - max_count)

        return rslt
