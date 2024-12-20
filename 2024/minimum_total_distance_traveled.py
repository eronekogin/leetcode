"""
https://leetcode.com/problems/minimum-total-distance-traveled/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_total_distance(self, robot: list[int], factory: list[list[int]]) -> int:
        """
        minimum total distance
        """
        robot.sort()
        factory.sort(key=lambda x: x[0])
        factory_positions: list[int] = []

        for p, occur in factory:
            factory_positions.extend([p] * occur)

        robot_count = len(robot)
        factory_count = len(factory_positions)
        dp = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]

        for i in range(robot_count):
            dp[i][factory_count] = 10 ** 12  # No more factory.

        for i in range(robot_count - 1, -1, -1):
            for j in range(factory_count - 1, -1, -1):
                assign = (
                    abs(robot[i] - factory_positions[j]) +
                    dp[i + 1][j + 1]
                )

                skip = dp[i][j + 1]
                dp[i][j] = min(assign, skip)

        return dp[0][0]
