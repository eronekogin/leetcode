"""
https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description/
"""


from collections import defaultdict, deque


class DSU:
    """
    Disjoint Set Union
    """

    def __init__(self, size: int):
        self.nodes = list(range(size + 1))

    def find(self, x: int) -> int:
        """
        find
        """
        if self.nodes[x] != x:
            self.nodes[x] = self.find(self.nodes[x])

        return self.nodes[x]

    def union(self, x: int, y: int) -> None:
        """
        union
        """
        px, py = self.find(x), self.find(y)
        self.nodes[px] = py


class Solution:
    """
    Solution
    """

    def magnificent_sets(self, n: int, edges: list[list[int]]) -> int:
        """
        magnificent sets
        """
        def divide_groups(node: int) -> int:
            queue = deque([(node, 1)])
            visited = {node: 1}
            level = 1

            while queue:
                curr_node, level = queue.popleft()
                for next_node in graph[curr_node]:
                    if next_node not in visited:
                        visited[next_node] = level + 1
                        queue.append((next_node, level + 1))
                    elif visited[next_node] == level:  # Found cycle.
                        return -1

            return level

        dsu = DSU(n)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            dsu.union(u, v)

        max_groups = defaultdict(int)
        for node in range(1, n + 1):
            groups = divide_groups(node)
            if groups == -1:
                return -1

            p = dsu.find(node)
            max_groups[p] = max(max_groups[p], groups)

        return sum(max_groups.values())
