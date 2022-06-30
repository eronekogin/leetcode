"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""


from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in connections:
            graph[src].append((dest, True))
            graph[dest].append((src, False))

        currNodes = [0]
        cnt = 0
        visited = set()
        while currNodes:
            nextNodes = []
            for currNode in currNodes:
                visited.add(currNode)
                for nextNode, isReachable in graph[currNode]:
                    if nextNode not in visited:
                        if isReachable:
                            cnt += 1

                        nextNodes.append(nextNode)

            currNodes = nextNodes

        return cnt


print(Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
