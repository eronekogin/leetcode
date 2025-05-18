"""
https://leetcode.com/problems/minimum-reverse-operations/description/

https://leetcode.com/problems/minimum-reverse-operations/solutions/3368533/python3-solution/
"""


class Solution:
    """
    Solution
    """

    def min_reverse_operations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:
        """
        min reverse operations
        """
        rslt = [-1] * n
        for curr_node in banned:
            rslt[curr_node] = -2

        curr_nodes = [p]
        depth = 0
        step = k - 1
        rslt[p] = 0
        next_nodes_to_see = [i + 2 for i in range(n)]

        while curr_nodes:
            depth += 1
            next_nodes: list[int] = []
            for curr_node in curr_nodes:
                l_reverse_start = max(curr_node - step, 0)
                r_reverse_start = min(curr_node, n - k)

                l_node = 2 * l_reverse_start + k - 1 - curr_node
                r_node = 2 * r_reverse_start + k - 1 - curr_node

                post_node = r_node + 2
                next_node = l_node

                while next_node <= r_node:
                    next_node_to_see = next_nodes_to_see[next_node]
                    next_nodes_to_see[next_node] = post_node

                    if 0 <= next_node < n and rslt[next_node] == -1:
                        next_nodes.append(next_node)
                        rslt[next_node] = depth

                    next_node = next_node_to_see

            curr_nodes = next_nodes

        for node in banned:
            rslt[node] = -1

        return rslt
