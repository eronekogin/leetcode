"""
https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description/
"""


class Solution:
    """
    Solution
    """

    def number_pf_pairs(self, points: list[list[int]]) -> int:
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


print(Solution().number_pf_pairs([[0, 1], [0, 2], [0, 4]]))
