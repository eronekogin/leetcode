"""
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
"""


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        def find(x: int) -> int:
            if parents[x] != x:
                parents[x] = find(parents[x])

            return parents[x]

        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False

            parents[px] = py
            return True

        removedEdges = aliceEdges = bobEdges = 0

        # Edges for both alice and bob.
        parents = list(range(n + 1))
        for t, x, y in edges:
            if t == 3:
                if union(x, y):
                    aliceEdges += 1
                    bobEdges += 1
                else:  # already unioned.
                    removedEdges += 1

        backup = parents[:]

        # Edges for alice.
        for t, x, y in edges:
            if t == 1:
                if union(x, y):
                    aliceEdges += 1
                else:
                    removedEdges += 1

        # Edges for bob.
        parents = backup
        for t, x, y in edges:
            if t == 2:
                if union(x, y):
                    bobEdges += 1
                else:
                    removedEdges += 1

        if aliceEdges == bobEdges == n - 1:
            return removedEdges

        return -1  # Not possible.
