"""
https://leetcode.com/problems/cat-and-mouse/
"""


from typing import Iterator
from collections import defaultdict, deque


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        def parents(m: int, c: int, t: int) -> Iterator[tuple[int]]:
            if t == 2:
                for m2 in graph[m]:
                    yield (m2, c, 3 - t)
            else:
                for c2 in graph[c]:
                    if c2:
                        yield (m, c2, 3 - t)

        DRAW, MOUSE, CAT, N = 0, 1, 2, len(graph)
        color = defaultdict(int)

        # Initialize the number of neutral children of the current node.
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[(m, c, MOUSE)] = len(graph[m])
                degree[(m, c, CAT)] = len(graph[c]) - (0 in graph[c])

        queue = deque([])
        for c in range(N):
            for t in range(1, 3):
                color[(0, c, t)] = MOUSE  # Mouse reaches node 0.
                queue.append((0, c, t, MOUSE))
                if c > 0:  # Cat cannot enter node 0.
                    color[(c, c, t)] = CAT  # Cat caught mouse.
                    queue.append((c, c, t, CAT))

        while queue:
            m, c, t, player = queue.popleft()
            for m2, c2, t2 in parents(m, c, t):
                if color[(m2, c2, t2)] == DRAW:  # Not colored yet.
                    if t2 == player:
                        color[(m2, c2, t2)] = player
                        queue.append((m2, c2, t2, player))
                    else:
                        degree[(m2, c2, t2)] -= 1
                        if degree[(m2, c2, t2)] == 0:
                            color[(m2, c2, t2)] = 3 - t2
                            queue.append((m2, c2, t2, 3 - t2))

        # Initially mouse starts at 1 and cat starts at 2
        # and mouse moves first.
        return color[(1, 2, 1)]
