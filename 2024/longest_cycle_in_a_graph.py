"""
https://leetcode.com/problems/longest-cycle-in-a-graph/description/
"""


class Solution:
    """
    Solution
    """

    def longest_cycle(self, edges: list[int]) -> int:
        """
        Since each node has only one out-going edge, it cannot be
        the joint point for multiple cycles, so for every node that
        has been visited in one cycle, we can safely skip them
        when picking the next start node of the cycle. 
        """
        def dfs(node: int):
            if seen[node]:
                return

            nonlocal max_cycle
            if node in visiting:
                max_cycle = max(
                    max_cycle,
                    len(visiting) - visiting[node]
                )
            elif edges[node] != -1:  # Go to the next node
                visiting[node] = len(visiting)
                dfs(edges[node])
                visiting.pop(node)

            seen[node] = True

        n = len(edges)
        max_cycle = -1
        seen = [False] * n
        visiting: dict[int, int] = {}

        for node in range(n):
            dfs(node)

        return max_cycle
