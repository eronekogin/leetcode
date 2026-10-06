"""
https://leetcode.com/problems/time-taken-to-mark-all-nodes/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def time_taken(self, edges: list[list[int]]) -> list[int]:
        """
        time taken
        """
        def dfs1(node=0, parent=-1):
            for next_node in g[node]:
                if next_node == parent:
                    continue

                add = 2 - (next_node & 1)
                v = dfs1(next_node, node)

                if v + add >= dp[node][0]:
                    dp[node][0], dp[node][1] = v + add, dp[node][0]
                elif v + add > dp[node][1]:
                    dp[node][1] = v + add

            return dp[node][0]

        def dfs2(node=0, parent=-1):
            if parent != -1:
                parent_to_node_add = 2 - (node & 1)
                node_to_parent_add = 2 - (parent & 1)

                if dp[parent][0] == dp[node][0] + parent_to_node_add:
                    # if the parent longest path contains the current node,
                    # we must use the parent's second longest path length so
                    # that the path won't go back to node to form a circular
                    parent_max_time = dp[parent][1]
                else:
                    # otherwise we can safely use the parent's longest path length
                    parent_max_time = dp[parent][0]

                parent_max_time += node_to_parent_add

                if parent_max_time >= dp[node][0]:
                    dp[node][0], dp[node][1] = parent_max_time, dp[node][0]
                elif parent_max_time > dp[node][1]:
                    dp[node][1] = parent_max_time

            for next_node in g[node]:
                if next_node == parent:
                    continue

                dfs2(next_node, node)

        n = len(edges)

        # dp[i][0] is the longest path starting from node i to the other nodes
        # dp[i][1] is the second longest path starting from node i to the other nodes
        dp = [[0, 0] for _ in range(n + 1)]
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        dfs1()
        dfs2()

        return [x[0] for x in dp]
