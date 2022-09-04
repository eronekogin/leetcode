"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
"""


class Solution:
    def findSmallestSetOfVertices(
        self,
        n: int,
        edges: list[list[int]]
    ) -> list[int]:
        """
        Since the graph is acyclic, a node with no incoming edge can only be
        reached by itself. So we can just return all the nodes with no
        incoming edge. All the other nodes could be reached from those nodes.
        """
        srcSet: set[int] = set()
        destSet: set[int] = set()
        for src, dest in edges:
            srcSet.add(src)
            destSet.add(dest)

        return list(srcSet - destSet)


print(Solution().findSmallestSetOfVertices(6,
                                           [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
