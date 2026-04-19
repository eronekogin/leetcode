"""
https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_pairs(self, points: list[list[int]]) -> int:
        """
        number of pairs
        """
        rslt = 0
        n = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))

        for i in range(n - 1):
            y2 = points[i][1]
            min_height = float('-inf')

            for j in range(i + 1, n):
                if points[j][1] > min_height and points[j][1] <= y2:
                    rslt += 1
                    min_height = points[j][1]

        return rslt
