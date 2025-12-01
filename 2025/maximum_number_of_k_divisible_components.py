"""
https://leetcode.com/problems/maximum-number-of-k-divisible-components/description/
"""


class Solution:
    """
    Solution
    """

    def max_k_divisible_components(
        self,
        n: int,
        edges: list[list[int]],
        values: list[int],
        k: int
    ) -> int:
        """
        max k divisible components
        """
        def dfs(curr: int, parent: int) -> int:
            nonlocal components

            curr_sum = 0
            for node in graph[curr]:
                if node != parent:
                    curr_sum += dfs(node, curr)
                    curr_sum %= k

            curr_sum += values[curr]
            curr_sum %= k

            if curr_sum == 0:
                components += 1

            return curr_sum

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        components = 0
        dfs(0, -1)
        return components
