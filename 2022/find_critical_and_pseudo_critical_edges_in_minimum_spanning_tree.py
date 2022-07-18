"""
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
"""


class DST:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, u: int):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])

        return self.parents[u]

    def union(self, u: int, v: int):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:  # Already unioned.
            return False

        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:
            self.ranks[pu] += 1
            self.parents[pv] = pu

        return True  # Newly unioned.


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: list[list[int]]
    ) -> list[list[int]]:
        def kruskal(
            remainEdges: int,
            edges: list[list[int]],
            bannedEdge: int,
            includeEdge: int
        ):
            dst = DST(n)
            totalWeight = 0

            if includeEdge != -1:
                u, v, w, _ = edges[includeEdge]
                dst.union(u, v)
                totalWeight += w
                remainEdges -= 1

            for i, (u, v, w, _) in enumerate(edges):
                if i == bannedEdge:
                    continue

                if dst.union(u, v):
                    totalWeight += w
                    remainEdges -= 1

                if remainEdges == 1:  # Used up all edges.
                    break

            if remainEdges > 1:  # minimum spanning tree not found.
                return float('inf')

            return totalWeight

        sortedEdges = [[u, v, w, i] for i, (u, v, w) in enumerate(edges)]
        sortedEdges.sort(key=lambda x: x[2])  # Sort by weight in ascending.

        mstWeight = kruskal(n, sortedEdges, -1, -1)

        # Find critical edges.
        criticalEdges: set[int] = set()
        for i in range(len(sortedEdges)):
            newMstWeight = kruskal(n, sortedEdges, i, -1)
            if newMstWeight > mstWeight:
                # Banning the current edge provides a larger mst weight, so
                # it means the current edge is critical for the original mst.
                criticalEdges.add(sortedEdges[i][-1])

        # Find pseudo critical edges.
        pseudoCriticalEdges: list[int] = []
        for i in range(len(sortedEdges)):
            if sortedEdges[i][-1] in criticalEdges:
                # Skip critical edges.
                continue

            newMstWeight = kruskal(n, sortedEdges, -1, i)
            if newMstWeight == mstWeight:
                # Including the current edge provides no change to the original
                # mst weight, which means it is pseudo critical.
                pseudoCriticalEdges.append(sortedEdges[i][-1])

        return [list(criticalEdges), pseudoCriticalEdges]
