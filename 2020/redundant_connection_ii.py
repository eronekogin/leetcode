"""
https://leetcode.com/problems/redundant-connection-ii/
"""


from typing import List


class Solution:
    def findRedundantDirectedConnection(
            self, edges: List[List[int]]) -> List[int]:
        """
        1. The invalid graph could be divided into 3 cases:
            a. When there is no cycle in the graph.
            b. When there is a cycle in the middle of the graph.
            c. When the whole graph is a cycle, which means all the nodes have
                just one parent, and there will be an extra edge pointed to
                the root node.
        2. We could use disjoint set to help us track the ancestor of each
            node. And for each edge, if the parent's ancestor is the same as
            its child, we have discovered that there is a cycle in the graph.
        3. If there is no cycle in the graph, we simply remove the extra edge
            found.
        4. If there is a cycle in the graph, we have to remove the last edge
            in the cycle.
        """
        def find_ancestor(x: int) -> int:
            if ds[x] != x:
                ds[x] = find_ancestor(ds[x])

            return ds[x]

        n = len(edges)
        parents = [None] * (n + 1)
        ds = list(range(n + 1))
        firstEdgeIdx = secondEdgeIdx = lastEdgeIdx = None
        for i, (p, c) in enumerate(edges):
            if parents[c] is not None:
                firstEdgeIdx = parents[c]
                secondEdgeIdx = i
            else:
                parents[c] = i
                pp = find_ancestor(p)
                if pp == c:
                    lastEdgeIdx = i
                else:
                    ds[c] = pp

        if lastEdgeIdx is None:  # No cycle is detected.
            return edges[secondEdgeIdx]

        if secondEdgeIdx is None:  # Every node only has one parent.
            return edges[lastEdgeIdx]

        return edges[firstEdgeIdx]  # Other cases.


print(Solution().findRedundantDirectedConnection([
    [1, 2], [2, 3], [3, 4], [4, 2]
]))
