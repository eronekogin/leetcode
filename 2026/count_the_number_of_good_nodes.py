"""
https://leetcode.com/problems/count-the-number-of-good-nodes/description/
"""


class Solution:
    """
    Solution
    """

    def count_good_nodes(self, edges: list[list[int]]) -> int:
        """
        count good nodes
        """
        def get_size(curr_node: int, parent: int):
            nonlocal rslt
            curr_size = 1
            prev_size = -1
            is_good = 1

            for next_node in g[curr_node]:
                if next_node != parent:
                    next_size = get_size(next_node, curr_node)

                    if prev_size == -1:
                        prev_size = next_size
                    elif prev_size != next_size:
                        is_good = 0

                    curr_size += next_size

            rslt += is_good
            return curr_size

        n = len(edges) + 1
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        rslt = 0
        get_size(0, -1)
        return rslt


print(Solution().count_good_nodes(
    [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]))
