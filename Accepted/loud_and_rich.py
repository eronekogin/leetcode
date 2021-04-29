"""
https://leetcode.com/problems/loud-and-rich/
"""


class Solution:
    def loudAndRich(
            self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        """
        1. Draw an edge from the x to y if y definitely has more money than x.
        2. Since the relationship is logically consistent, which means our
            final graph does not contain any cycles. So our job is to find
            the nodes in the subtree rooted by node x having the minimum quiet
            value.
        3. We could memo the rslt to make the dfs faster.
        """
        def do(currNode: int) -> int:
            if memo[currNode] is None:
                minNode = currNode
                for child in graph[currNode]:
                    candidate = do(child)
                    if quiet[candidate] < quiet[minNode]:
                        minNode = candidate

                memo[currNode] = minNode

            return memo[currNode]

        N = len(quiet)
        graph = [[] for _ in range(N)]
        for x, y in richer:
            graph[y].append(x)

        memo = [None] * N
        return [do(i) for i in range(N)]


print(Solution().loudAndRich(
    [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
    [3, 2, 5, 4, 6, 1, 7, 0]))
