"""
https://leetcode.com/problems/is-graph-bipartite/
"""


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        For each node, if it does not have a color, try to put a color on it
        and put another color on all its neighbor nodes. If the graph is
        bipartite, there should be no conflicts when doing the above action.
        Otherwise, it is not bipartite.
        """
        def could_be_painted(node: int, color: int) -> bool:
            if colors[node]:  # If the current node is already painted.
                return colors[node] == color  # Check if it is the same color.

            colors[node] = color  # Paint the current node.

            # Then check if all its neighbors could be painted with the other
            # color.
            return all(
                could_be_painted(neighbor, -color)
                for neighbor in graph[node])

        N = len(graph)
        colors = [0] * N
        return all(
            could_be_painted(node, 1)
            for node in range(N)
            if not colors[node])


print(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
