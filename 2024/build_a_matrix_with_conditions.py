"""
https://leetcode.com/problems/build-a-matrix-with-conditions/description/
"""


from collections import defaultdict, deque


class Solution:
    """
    Solution
    """

    def build_matrix(
        self,
        k: int,
        row_conditions: list[list[int]],
        col_conditions: list[list[int]]
    ) -> list[list[int]]:
        """
        build matrix
        """
        def topo_sort(g: defaultdict[int, list[int]]):
            in_degrees = {i: 0 for i in range(1, k + 1)}
            for v in g.values():
                for node in v:
                    in_degrees[node] += 1

            queue = deque(k for k, v in in_degrees.items() if v == 0)
            order: list[int] = []

            while queue:
                node = queue.popleft()
                order.append(node)
                for v in g[node]:
                    in_degrees[v] -= 1
                    if in_degrees[v] == 0:
                        queue.append(v)

            if len(order) == k:
                return order

            return []

        row_graph: defaultdict[int, list[int]] = defaultdict(list)
        col_graph: defaultdict[int, list[int]] = defaultdict(list)

        for u, v in row_conditions:
            row_graph[u].append(v)

        for u, v in col_conditions:
            col_graph[u].append(v)

        row_order = topo_sort(row_graph)
        col_order = topo_sort(col_graph)

        if not row_order or not col_order:
            return []

        row_map = {x: i for i, x in enumerate(row_order)}
        col_map = {x: i for i, x in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            matrix[row_map[i]][col_map[i]] = i

        return matrix
