"""
https://leetcode.com/problems/minimize-manhattan-distances/description/
"""


from math import inf


class Solution:
    """
    Solution
    """

    def minimum_distance(self, points: list[list[int]]) -> int:
        """
        minimum distance
        """
        def get_distance(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        def get_points_pair_with_max_distance(remove: int):
            max_sum, min_sum, max_diff, min_diff = -inf, inf, -inf, inf
            max_sum_index = min_sum_index = max_diff_index = min_diff_index = 0
            for i, (x, y) in enumerate(points):
                if i == remove:
                    continue

                s = x + y
                d = x - y

                if s > max_sum:
                    max_sum = s
                    max_sum_index = i

                if s < min_sum:
                    min_sum = s
                    min_sum_index = i

                if d > max_diff:
                    max_diff = d
                    max_diff_index = i

                if d < min_diff:
                    min_diff = d
                    min_diff_index = i

            if max_sum - min_sum > max_diff - min_diff:
                return (max_sum_index, min_sum_index)

            return (max_diff_index, min_diff_index)

        # get pair with max distance without removing any point
        mi, mj = get_points_pair_with_max_distance(-1)

        # Then we can either remove mi or mj to get the minimum distance
        return min(
            get_distance(*get_points_pair_with_max_distance(mi)),
            get_distance(*get_points_pair_with_max_distance(mj))
        )
