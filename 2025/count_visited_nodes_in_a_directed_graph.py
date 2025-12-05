"""
https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/description/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def count_visited_nodes(self, edges: list[int]) -> list[int]:
        """
        count visited nodes
        """
        def check_cycle(start: int):
            node = start
            size = 0

            while not visited[node]:
                visited[node] = True
                size += 1
                node = edges[node]

            rslt[start] = size
            node = edges[start]
            while node != start:
                rslt[node] = size
                node = edges[node]

        n = len(edges)
        rslt = [0] * n
        in_degrees = [0] * n
        visited = [False] * n
        stack: list[int] = []

        for v in edges:
            in_degrees[v] += 1

        queue = deque([node for node in range(n) if in_degrees[node] == 0])
        while queue:
            curr_node = queue.popleft()
            stack.append(curr_node)
            visited[curr_node] = True
            next_node = edges[curr_node]
            in_degrees[next_node] -= 1

            if in_degrees[next_node] == 0:
                queue.append(next_node)

        for node in range(n):
            if not visited[node]:
                check_cycle(node)

        while stack:
            node = stack.pop()
            rslt[node] = rslt[edges[node]] + 1

        return rslt


print(Solution().count_visited_nodes([3, 6, 1, 0, 5, 7, 4, 3]))
