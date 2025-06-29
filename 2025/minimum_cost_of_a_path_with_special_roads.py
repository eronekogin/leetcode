"""
https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def minimum_cost(
        self,
        start: list[int],
        target: list[int],
        special_roads: list[list[int]]
    ) -> int:
        """
        minimum cost
        """
        short_cuts = [
            [a, b, c, d, cost]
            for a, b, c, d, cost in special_roads
            if abs(c - a) + abs(d - b) > cost
        ]

        distances = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        max_distance = (
            abs(target[0] - start[0]) +
            abs(target[1] - start[1])
        )

        min_distance = max_distance
        while heap:
            curr_distance, x, y = heappop(heap)
            for a, b, c, d, cost in short_cuts:
                next_distance = (
                    curr_distance +
                    abs(x - a) +
                    abs(y - b) +
                    cost
                )

                if distances.get((c, d), max_distance) > next_distance:
                    distances[(c, d)] = next_distance
                    heappush(heap, (next_distance, c, d))

        for a, b, c, d, cost in short_cuts:
            min_distance = min(
                min_distance,
                abs(target[0] - c) +
                abs(target[1] - d) +
                distances.get((c, d), max_distance)
            )

        return min_distance
