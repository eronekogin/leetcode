"""
https://leetcode.com/problems/collect-coins-in-a-tree/description/
"""


from collections import defaultdict, deque


class Solution:
    """
    Solution
    """

    def collect_the_coins(self, coins: list[int], edges: list[list[int]]) -> int:
        """
        collect the coins
        """
        n = len(edges)
        graph: defaultdict[int, set[int]] = defaultdict(set)
        total_edges = 2 * n
        deleted_edges = 0

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Find leaf nodes with no coin and delete them
        q: deque[int] = deque()
        for node in range(n + 1):
            if len(graph[node]) == 1 and coins[node] == 0:
                q.append(node)

        while q:
            node = q.popleft()
            if not graph[node]:
                continue

            parent = graph[node].pop()
            graph[parent].remove(node)

            if len(graph[parent]) == 1 and coins[parent] == 0:
                q.append(parent)

            deleted_edges += 2

        # Recheck for leaves having coin after deletion
        for node in range(n + 1):
            if len(graph[node]) == 1:
                q.append(node)

        # Remove leaf and its direct parent since the coin can be
        # reached by its grand parent.
        for _ in range(2):
            qsize = len(q)
            for _ in range(qsize):
                node = q.popleft()
                if not graph[node]:
                    continue

                parent = graph[node].pop()
                graph[parent].remove(node)

                if len(graph[parent]) == 1:
                    q.append(parent)

                deleted_edges += 2

        return total_edges - deleted_edges
