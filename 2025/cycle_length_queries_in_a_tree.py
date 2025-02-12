"""
https://leetcode.com/problems/cycle-length-queries-in-a-tree/description/
"""


class Solution:
    """
    Solution
    """

    def cycle_length_queries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        Add an edge between node a and b, which means the cycle will end at the
        lowest common ancestor of node a and b. We could let the node with bigger
        value to go up, until they meet at the lowest common ancestor.
        """
        rslt: list[int] = []
        for a, b in queries:
            d = 1

            while a != b:
                a, b = min(a, b), max(a, b) >> 1
                d += 1

            rslt.append(d)

        return rslt
