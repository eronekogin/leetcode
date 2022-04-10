"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
"""


class Solution:
    def findTheCity(
        self,
        n: int,
        edges: list[list[int]],
        distanceThreshold: int
    ) -> int:
        """
        Use Floyd-Washall algorithm to simply calculate the minimum distance
        between each pair of nodes: choose any point k other than point i and
        j, check if there exist such k which connects i and j, and find such
        minimum distance.
        """
        minDistances = [[float('inf')] * n for _ in range(n)]
        for start, end, w in edges:
            minDistances[start][end] = w
            minDistances[end][start] = w

        for i in range(n):
            minDistances[i][i] = 0

        for m in range(n):
            for start in range(n):
                for end in range(n):
                    minDistances[start][end] = min(
                        minDistances[start][end],
                        minDistances[start][m] + minDistances[m][end]
                    )

        res = {
            sum(d <= distanceThreshold for d in minDistances[i]): i
            for i in range(n)
        }

        return res[min(res)]
