"""
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def get_ancestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        get ancestors
        """
        def dfs(curr_node: int, next_node: int):
            for child in children[next_node]:
                if ancestors[child] and ancestors[child][-1] == curr_node:
                    continue

                ancestors[child].append(curr_node)
                dfs(curr_node, child)

        children: defaultdict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            children[u].append(v)

        ancestors: list[list[int]] = [[] for _ in range(n)]

        for i in range(n):
            dfs(i, i)

        return ancestors


print(Solution().get_ancestors(n=8, edges=[[0, 3], [0, 4], [
      1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
