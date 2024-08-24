"""
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
"""


class Solution:
    """
    Solution
    """

    def closest_meeting_node(self, edges: list[int], node1: int, node2: int) -> int:
        """
        closest meeting node
        """
        def walk(start: int):
            memo: dict[int, int] = {start: 0}
            d = 0
            curr = edges[start]
            while curr != -1 and curr not in memo:
                d += 1
                memo[curr] = d
                curr = edges[curr]

            return memo

        m1 = walk(node1)
        m2 = walk(node2)
        min_d = len(edges) + 1
        rslt = -1
        for node, v in m1.items():
            if node in m2:
                curr_d = max(v, m2[node])
                if curr_d < min_d:
                    min_d = curr_d
                    rslt = node
                elif curr_d == min_d and node < rslt:
                    rslt = node

        return rslt
