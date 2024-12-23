"""
https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
"""


class Solution:
    """
    Solution
    """

    def most_profitable_path(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        """
        most profitable path
        """
        def dfs(curr_node: int, d0: int):
            visited[curr_node] = 1
            rslt = float('-inf')

            db = 0 if curr_node == bob else n

            for next_node in graph[curr_node]:
                if visited[next_node]:
                    continue

                next_income, next_db = dfs(next_node, d0 + 1)
                rslt = max(rslt, next_income)
                db = min(db, next_db)

            if rslt == float('-inf'):
                rslt = 0

            if d0 == db:  # Bob and Alice reach node i at the same time.
                rslt += amount[curr_node] // 2

            if d0 < db:  # Alice reach node i earlier.
                rslt += amount[curr_node]

            return (rslt, db + 1)

        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [0] * n

        return dfs(0, 0)[0]
