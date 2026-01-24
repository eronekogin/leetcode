"""
https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/description/
"""


from functools import cache


class Solution:
    """
    Docstring for Solution
    """

    def maximum_points(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        """
        Docstring for maximum_points

        :param self: Description
        :param edges: Description
        :type edges: list[list[int]]
        :param coins: Description
        :type coins: list[int]
        :param k: Description
        :type k: int
        :return: Description
        :rtype: int
        """
        @cache
        def dp(curr: int, prev: int, shifted_bits: int) -> int:
            if shifted_bits > 13:
                return 0

            remain_coins = coins[curr] >> shifted_bits

            option1 = (
                remain_coins -
                k +
                sum(
                    dp(next_node, curr, shifted_bits)
                    for next_node in g[curr]
                    if next_node != prev
                )
            )

            if remain_coins >= k + k:
                return option1

            option2 = (
                (remain_coins >> 1) +
                sum(
                    dp(next_node, curr, shifted_bits + 1)
                    for next_node in g[curr]
                    if next_node != prev
                )
            )

            return max(option1, option2)

        n = len(edges) + 1
        g = [set() for _ in range(n)]
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        return dp(0, -1, 0)
