"""
https://leetcode.com/problems/brick-wall/
"""


from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # {edge index on the row: total number of edges}.
        # (0, 0) stands for the corner case when there is no edge between
        # the leftmost and rightmost boarders in which each brick
        # has to be crossed once.
        edges = {0: 0}
        for row in wall:
            widthSum = 0
            for currWidth in row[:-1]:
                widthSum += currWidth
                edges[widthSum] = edges.get(widthSum, 0) + 1

        return len(wall) - max(edges.values())


print(Solution().leastBricks(
    [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
