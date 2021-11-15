"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/
"""


class Solution:
    def shortestAlternatingPaths(
        self,
        n: int,
        red_edges: list[list[int]],
        blue_edges: list[list[int]]
    ) -> list[int]:
        # Build graph.
        graph = [[[], []] for _ in range(n)]  # [red, blue]
        for src, dst in red_edges:
            graph[src][0].append(dst)

        for src, dst in blue_edges:
            graph[src][1].append(dst)

        # The maximum case happen when there is a red path from 0 to n - 1,
        # while each node except the first and the last have a self blue edge,
        # so the total edges could be 2 * (n - 2) + 1 = 2n - 3, and we simply
        # set the max limit to 2n instead.
        MAX_LIMIT = n << 1

        # paths[i][0] contains the length of the path to node i when the
        # previous edge is red, while paths[i][1] is when the previous edge
        # is blue.
        paths = [[0, 0]] + [[MAX_LIMIT, MAX_LIMIT] for _ in range(n - 1)]

        # Then use bfs to calculate the path to each node.
        bfs = [[0, 0], [0, 1]]  # [[node 0, red color], [node 0, blue color]]
        for src, color in bfs:
            for dst in graph[src][color]:
                if paths[dst][color] == MAX_LIMIT:  # Reached the current node.
                    paths[dst][color] = paths[src][1 - color] + 1
                    bfs.append([dst, 1 - color])

        # Then get the shortest path based on paths.
        return [
            x
            if x < MAX_LIMIT else -1
            for x in map(min, paths)
        ]
