"""
https://leetcode.com/problems/frog-position-after-t-seconds/
"""


class Solution:
    def frogPosition(
        self,
        n: int,
        edges: list[list[int]],
        t: int,
        target: int
    ) -> float:
        def dfs(currNode: int, currTime: int) -> bool:
            if currNode != 1 and len(graph[currNode]) == 1 or currTime == 0:
                return currNode == target

            visited[currNode] = 1
            cnt = sum(
                dfs(nextNode, currTime - 1)
                for nextNode in graph[currNode]
                if not visited[nextNode]
            )

            return cnt / (len(graph[currNode]) - (currNode != 1))

        if n == 1:
            return 1.0

        graph = [[] for _ in range(n + 1)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = [0] * (n + 1)
        return dfs(1, t)
