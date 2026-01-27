"""
https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def maximum_score_after_operations(self, edges: list[list[int]], values: list[int]) -> int:
        """
        Docstring for maximum_score_after_operations

        :param self: Description
        :param edges: Description
        :type edges: list[list[int]]
        :param values: Description
        :type values: list[int]
        :return: Description
        :rtype: int
        """
        def dfs(curr: int, parent=-1):
            if curr and g[curr] == [parent]:  # leaf node
                return values[curr]

            return min(
                values[curr],
                sum(dfs(child, curr) for child in g[curr] if child != parent)
            )

        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            # The edges does not strictly follow parent to child
            # so we still need graph
            g[u].append(v)
            g[v].append(u)

        return sum(values) - dfs(0)


print(Solution().maximum_score_after_operations(
    [[7, 0], [3, 1], [6, 2], [4, 3], [4, 5], [4, 6], [4, 7]],
    [2, 16, 23, 17, 22, 21, 8, 6]
))
