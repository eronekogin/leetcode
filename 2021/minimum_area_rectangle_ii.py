"""
https://leetcode.com/problems/minimum-area-rectangle-ii/
"""


from collections import defaultdict
from itertools import combinations


class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        # store each point as a complex number
        points = [complex(*z) for z in sorted(points)]
        seen = defaultdict(list)  # store each edges in a dictionary
        for P, Q in combinations(points, 2):
            # Q-P, it is a vector that stores both the direction and
            # the length of the edge
            #
            # (P+Q)/2 is the mid point of the edge
            # save the midpoints as a list for all edges with the
            # same direction and length
            seen[Q - P].append((P + Q) / 2)

        ans = float('inf')
        for A, candidates in seen.items():
            # for each pair of edges P and Q
            for P, Q in combinations(candidates, 2):
                # if the line linking two midpoint (P-Q)
                # is perpendicular to the edge
                if A.real * (P - Q).real + A.imag * (P - Q).imag == 0:
                    # calculate the area of the rectangle
                    ans = min(ans, abs(A) * abs(P - Q))

        return ans if ans < float('inf') else 0  # save the smallest rectangle
