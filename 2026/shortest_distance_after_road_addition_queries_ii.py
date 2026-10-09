"""
https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/description/
"""


class Solution:
    """
    Solution
    """

    def shortest_distance_after_queries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        shortest distance after queries
        """
        d = list(range(1, n))
        rslt: list[int] = []

        curr = n - 1  # total length of the road
        for i, j in queries:
            while d[i] < j:
                # link the node between i to j to j
                d[i], i = j, d[i]
                curr -= 1

            rslt.append(curr)

        return rslt
