"""
https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/
"""

from collections import defaultdict, deque


class Solution:
    def countSubgraphsForEachDiameter(
        self,
        n: int,
        edges: list[list[int]]
    ) -> list[int]:
        def bfs(src: int, cities: set[int]):
            visited = {src}
            q: deque[tuple[int, int]] = deque([(src, 0)])
            farthestNode, farthestDistance = -1, 0
            while q:
                farthestNode, farthestDistance = u, d = q.popleft()
                for v in graph[u]:
                    if v not in visited and v in cities:
                        visited.add(v)
                        q.append((v, d + 1))

            return farthestNode, farthestDistance, visited

        def get_diameter(cities: set[int]):
            randomNode = cities.pop()
            cities.add(randomNode)
            farthestNode, _, visited = bfs(randomNode, cities)
            if len(visited) < len(cities):  # Cannot visit all cities.
                return 0

            _, farthestDist, _ = bfs(farthestNode, cities)
            return farthestDist

        def get_max_distance(state: int):
            cities: set[int] = set()
            for i in range(n):
                if (state >> i) & 1:
                    cities.add(i)

            return get_diameter(cities)

        graph: defaultdict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        rslt = [0] * (n - 1)
        for state in range(1, 1 << n):
            d = get_max_distance(state)
            if d:
                rslt[d - 1] += 1

        return rslt
